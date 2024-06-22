# from __future__ import annotations  # This doesn't work because we're annotating with local types. So this code won't work on Python 4. OK.
from typing import Annotated, Type
from urllib.parse import urlencode
import unittest

from fastapi import APIRouter, Depends, HTTPException, Query, Response
from fastapi.responses import JSONResponse
from starlette import status
import humps

from .annotations import Annotations
from .dependencies_extraction import extract_dependencies
from .utils import Urls
from .models import Decider, make_create_input_model, make_filters_dependable, make_output_models, make_update_input_model


# @todo Check consistency of "type" attributes in input 'ObjectId's
# @todo Check consistency of "id" attributes in input 'ObjectId's
# @todo Check Content-Type header in requests (vnd.api+json for requests with payloads, not set for requests without payloads)
# @todo Check Accept header in requests (vnd.api+json)


class JSONAPIResponse(JSONResponse):
    media_type = "application/vnd.api+json"


def make_jsonapi_router(resources, polymorphism: dict[Type, str]):
    decider = Decider({
        resource.Model: humps.camelize(resource.singular_name) for resource in resources
    })
    polymorphism = {
        key: humps.camelize(value)
        for (key, value) in polymorphism.items()
    }
    resources = {
        humps.camelize(resource.singular_name): CompiledResource(decider, polymorphism, resource)
        for resource in resources
    }

    router = APIRouter(
        default_response_class=JSONAPIResponse,
    )

    for resource in resources.values():
        add_resource_routes(resources, resource, router)

    add_batch_route(resources, router)

    return router


class CompiledResource:
    def __init__(self, decider, polymorphism, resource):
        self.polymorphism = polymorphism
        self._resource = resource

        assert humps.is_snakecase(resource.singular_name)
        self.singular_name = resource.singular_name
        self.singularName = humps.camelize(resource.singular_name)
        assert humps.is_snakecase(resource.plural_name)
        self.plural_name = resource.plural_name
        self.pluralName = humps.camelize(resource.plural_name)

        self.Model = resource.Model

        # @todo remove these 'else' branches: they were kept only to ease the transition to the new style
        if hasattr(resource, "create_item"):
            self.ItemCreator = extract_dependencies(resource.create_item)
        else:
            self.ItemCreator = getattr(resource, "ItemCreator", None)
        if hasattr(resource, "get_item"):
            self.ItemGetter = extract_dependencies(resource.get_item)
        else:
            self.ItemGetter = getattr(resource, "ItemGetter", None)
        if hasattr(resource, "get_page"):
            self.PageGetter = extract_dependencies(resource.get_page)
        else:
            self.PageGetter = getattr(resource, "PageGetter", None)
        if hasattr(resource, "save_item"):
            self.ItemSaver = extract_dependencies(resource.save_item)
        else:
            self.ItemSaver = getattr(resource, "ItemSaver", None)
        if hasattr(resource, "delete_item"):
            self.ItemDeleter = extract_dependencies(resource.delete_item)
        else:
            self.ItemDeleter = getattr(resource, "ItemDeleter", None)

        self.default_page_size = resource.default_page_size

        self.output_attributes = []
        self.output_relationships = {}
        for (name, info) in resource.Model.model_fields.items():
            name = humps.camelize(name)
            annotations = Annotations(info.metadata)

            if decider.is_mandatory_relationship(info.annotation):
                if annotations.output:
                    self.output_relationships[name] = (False, decider.get_monomorphic_name(info.annotation))
            elif decider.is_optional_relationship(info.annotation):
                assert info.default is None
                if annotations.output:
                    self.output_relationships[name] = (False, decider.get_monomorphic_name(info.annotation))
            elif decider.is_list_relationship(info.annotation):
                assert info.default == []
                if annotations.output:
                    self.output_relationships[name] = (True, decider.get_monomorphic_name(info.annotation))
            else:
                if annotations.output:
                    self.output_attributes.append(name)

        self.CreateInputModel = make_create_input_model(self.singularName, resource.Model, decider)
        (self.ItemOutputModel, self.PageOutputModel) = make_output_models(self.singularName, resource.Model, decider)
        self.filters = make_filters_dependable(self.singularName, resource.Model, decider)
        self.UpdateInputModel = make_update_input_model(self.singularName, resource.Model, decider)

    def make_item_response(self, resources, *, urls, item, include):
        return_value = {
            "data": self.make_item(resources, urls=urls, item=item),
        }
        if include is not None:
            return_value["included"] = self.make_included(resources, urls, [item], include)
        return return_value

    def make_page_response(self, resources, *, urls, items_count, filters, sort, page_number, page_size, items, raw_include, include):
        pages_count = (items_count + 1) // page_size
        pagination = dict(count=items_count, page=page_number, pages=pages_count)

        base_url = urls.make(f"get_{self.plural_name}")
        def make_url_for_page(number):
            qs = {}
            for (key, value) in sorted(filters.model_dump(exclude_unset=True).items()):
                if value is not None:
                    qs[f"filter[{humps.camelize(key)}]"] = value
            qs["page[number]"] = number
            if page_size != self.default_page_size:
                qs["page[size]"] = page_size
            if raw_include is not None:
                qs["include"] = raw_include
            if sort is not None:
                qs["sort"] = sort
            return base_url + "?" + urlencode(qs)

        if page_number < pages_count:
            next = make_url_for_page(page_number + 1)
        else:
            next = None
        if page_number > 1:
            prev = make_url_for_page(page_number - 1)
        else:
            prev = None
        links = dict(
            first=make_url_for_page(1),
            last=make_url_for_page(pages_count),
            next=next,
            prev=prev,
        )

        return_value = {
            "data": [self.make_item(resources, urls=urls, item=item) for item in items],
            "links": links,
            "meta": dict(pagination=pagination),
        }
        if include is not None:
            return_value["included"] = self.make_included(resources, urls, items, include)
        return return_value

    def make_item(self, resources, *, urls, item):
        r = {
            "type": self.singularName,
            "id": item.id,
            "links": {"self": urls.make(f"get_{self.singular_name}", id=item.id)},
        }
        if self.output_attributes:
            attributes = {}
            for key in self.output_attributes:
                attr = getattr(item, humps.decamelize(key))
                attributes[key] = attr
            r["attributes"] = attributes
        if self.output_relationships:
            relationships = {}
            for (key, (is_list, resource_name)) in self.output_relationships.items():
                attr = getattr(item, humps.decamelize(key))
                if is_list:
                    data = [{"type": resource_name, "id": rel.id} for rel in attr]
                    relationship = {
                        "data": data,
                        "meta": {"count": len(data)},
                    }
                elif attr is None:
                    relationship = {"data": None}
                else:
                    if resource_name is None:
                        resource_name = self.polymorphism[type(attr)]
                    relationship = {"data": {"type": resource_name, "id": attr.id}}
                relationships[key] = relationship
            r["relationships"] = relationships
        return r

    def make_included(self, resources, urls, items, include):
        included = {}

        # @todo Add test showing we don't include the root items even if they appear in included relationships
        # @todo Add test showing we don't include the same item twice

        def recurse(resource, item, include):
            for (name, nested_include) in include.items():
                attr = getattr(item, humps.decamelize(name))
                (is_list, resource_name) = resource.output_relationships[name]
                if is_list:
                    # @todo Add test showing that this variable ('nested_resource') cannot be named 'resource' (bug fixed using tests from Gabby, deserves test in fastjsonapi)
                    nested_resource = resources[resource_name]
                    for incl in attr:
                        included[(resource_name, incl.id)] = nested_resource.make_item(resources, urls=urls, item=incl)
                        recurse(nested_resource, incl, nested_include)
                elif attr is not None:
                    if resource_name is None:
                        resource_name = self.polymorphism[type(attr)]
                    # @todo Add test showing that this variable ('nested_resource') cannot be named 'resource' (bug fixed using tests from Gabby, deserves test in fastjsonapi)
                    nested_resource = resources[resource_name]
                    # @todo Add tests exercising this branch
                    included[(resource_name, attr.id)] = nested_resource.make_item(resources, urls=urls, item=attr)
                    recurse(nested_resource, attr, nested_include)

        for item in items:
            recurse(self, item, include)

        return sorted(included.values(), key=lambda item: (item["type"], item["id"]))


def add_resource_routes(resources, resource, router):
    # @todo Keep things structured all they way (avoid generating textual code)
    # See... my old answer here: https://stackoverflow.com/a/29927459/905845
    def make_related_getters_code():
        yield "def make_related_getters("
        for name in resources.keys():
            yield f'    {name}: Annotated[resources["{name}"].ItemGetter, Depends()],'
        yield "):"
        yield "    return {"
        for name in resources.keys():
            yield f'        "{name}": {name},'
        yield "    }"
    exec("\n".join(make_related_getters_code()), {"resources": resources}, make_related_getters_globals := {"Annotated": Annotated, "Depends": Depends})
    make_related_getters = make_related_getters_globals["make_related_getters"]

    if resource.ItemCreator:
        @router.post(
            f"/{resource.pluralName}",
            name=f"create_{resource.singular_name}",
            status_code=status.HTTP_201_CREATED,
            response_model=resource.ItemOutputModel,
            response_model_exclude_unset=True,
        )
        def create_item(
            urls: Urls,
            create_item: Annotated[resource.ItemCreator, Depends()],
            get_related_item: Annotated[dict, Depends(make_related_getters)],
            payload: resource.CreateInputModel,
            include: str = None
        ):
            attributes = {
                humps.decamelize(key) : value
                for (key, value) in dict(payload.data.attributes).items()
            }

            relationships = {}
            for (key, value) in dict(payload.data.relationships).items():
                key = humps.decamelize(key)
                if isinstance(value.data, list):
                    # @todo Check item type against relationship type
                    relationships[key] = [get_related_item[item.type](item.id) for item in value.data]
                elif value.data is None:
                    relationships[key] = None
                else:
                    # @todo Check type against relationship type(s)
                    relationships[key] = get_related_item[value.data.type](value.data.id)

            # @todo Pass parsed 'include' to allow pre-fetching
            item = create_item(**attributes, **relationships)

            return resource.make_item_response(resources, urls=urls, item=item, include=parse_include(include))

    if resource.PageGetter:
        @router.get(
            f"/{resource.pluralName}",
            name=f"get_{resource.plural_name}",
            response_model=resource.PageOutputModel,
            response_model_exclude_unset=True,
        )
        def get_page(
            urls: Urls,
            get_page: Annotated[resource.PageGetter, Depends()],
            filters: Annotated[resource.filters, Depends()],
            page_size: Annotated[int, Query(alias="page[size]")] = resource.default_page_size,
            page_number: Annotated[int, Query(alias="page[number]")] = 1,
            sort: str = None,
            include: str = None,
        ):
            # @todo Work out authorized values for 'sort' from the resources' definition
            # @todo Sort descending when the sort field is prefixed with a minus sign
            # @todo Allow explicit ascending sorting with a prefix plus sign
            parsed_sort = None if sort is None else [humps.decamelize(part) for part in sort.split(",")]
            # @todo Pass parsed 'include' to allow pre-fetching
            (items_count, items) = get_page(sort=parsed_sort, filters=filters, first_index=(page_number - 1) * page_size, page_size=page_size)
            assert len(items) <= page_size
            return resource.make_page_response(
                resources,
                urls=urls,
                items_count=items_count,
                filters=filters,
                sort=sort,
                page_number=page_number,
                page_size=page_size,
                items=items,
                raw_include=include,
                include=parse_include(include),
            )

    # @todo Actually support resources without an ItemGetter (useful e.g. in Gabby for 'RecoveryEmailRequest' and 'AdaptedExercise')
    if resource.ItemGetter:
        @router.get(
            f"/{resource.pluralName}""/{id}",
            name=f"get_{resource.singular_name}",
            response_model=resource.ItemOutputModel,
            response_model_exclude_unset=True,
        )
        def get_item(
            urls: Urls,
            get_item: Annotated[resource.ItemGetter, Depends()],
            id: str,
            include: str = None,
        ):
            # @todo Pass parsed 'include' to allow pre-fetching
            item = get_item(id=id)
            if item:
                return resource.make_item_response(resources, urls=urls, item=item, include=parse_include(include))
            else:
                raise HTTPException(status_code=404, detail="Item not found")

    if resource.ItemSaver:
        @router.patch(
            f"/{resource.pluralName}""/{id}",
            name=f"update_{resource.singular_name}",
            response_model=resource.ItemOutputModel,
            response_model_exclude_unset=True,
        )
        def update_item(
            urls: Urls,
            get_item: Annotated[resource.ItemGetter, Depends()],
            save_item: Annotated[resource.ItemSaver, Depends()],
            get_related_item: Annotated[dict, Depends(make_related_getters)],
            id: str,
            payload: resource.UpdateInputModel,
            include: str = None,
        ):
            # @todo Pass parsed 'include' to allow pre-fetching
            item = get_item(id=id)
            if item:
                class NothingToSave(Exception):
                    pass

                try:
                    with save_item(item=item):
                        needs_save = False
                        for (key, value) in dict(payload.data.attributes).items():
                            if key in payload.data.attributes.model_fields_set:
                                setattr(item, humps.decamelize(key), value)
                                needs_save = True
                        for (key, value) in dict(payload.data.relationships).items():
                            if key in payload.data.relationships.model_fields_set:
                                if isinstance(value.data, list):
                                    # @todo Check item type against relationship type
                                    setattr(item, humps.decamelize(key), [get_related_item[item.type](item.id) for item in value.data])
                                elif value.data is None:
                                    setattr(item, humps.decamelize(key), None)
                                else:
                                    setattr(item, humps.decamelize(key), get_related_item[value.data.type](value.data.id))
                                needs_save = True
                        if not needs_save:
                            raise NothingToSave()
                except NothingToSave:
                    pass
                return resource.make_item_response(resources, urls=urls, item=item, include=parse_include(include))
            else:
                raise HTTPException(status_code=404, detail="Item not found")

    if resource.ItemDeleter:
        @router.delete(
            f"/{resource.pluralName}""/{id}",
            name=f"delete_{resource.singular_name}",
            status_code=status.HTTP_204_NO_CONTENT,
            response_class=Response,
        )
        def delete_item(
            get_item: Annotated[resource.ItemGetter, Depends()],
            delete_item: Annotated[resource.ItemDeleter, Depends()],
            id: str,
        ):
            item = get_item(id=id)
            if item:
                delete_item(item=item)
            else:
                raise HTTPException(status_code=404, detail="Item not found")


def add_batch_route(resources, router):
    # @todo Keep things structured all they way (avoid generating textual code)
    # See... my old answer here: https://stackoverflow.com/a/29927459/905845
    def make_item_creators_code():
        yield "def make_item_creators("
        for name, resource in resources.items():
            if resource.ItemCreator:
                yield f'    {name}: Annotated[resources["{name}"].ItemCreator, Depends()],'
        yield "):"
        yield "    return {"
        for name, resource in resources.items():
            if resource.ItemCreator:
                yield f'        "{name}": {name},'
        yield "    }"
    exec("\n".join(make_item_creators_code()), {"resources": resources}, make_item_creators_globals := {"Annotated": Annotated, "Depends": Depends})
    make_item_creators = make_item_creators_globals["make_item_creators"]

    def make_item_getters_code():
        yield "def make_item_getters("
        for name, resource in resources.items():
            if resource.ItemGetter:
                yield f'    {name}: Annotated[resources["{name}"].ItemGetter, Depends()],'
        yield "):"
        yield "    return {"
        for name, resource in resources.items():
            if resource.ItemGetter:
                yield f'        "{name}": {name},'
        yield "    }"
    exec("\n".join(make_item_getters_code()), {"resources": resources}, make_item_getters_globals := {"Annotated": Annotated, "Depends": Depends})
    make_item_getters = make_item_getters_globals["make_item_getters"]

    @router.post(
        f"/batch",
        # response_model=,  # @todo Use a proper response model
        # response_model_exclude_unset=True,
    )
    def batch(
        urls: Urls,
        item_creators: Annotated[dict, Depends(make_item_creators)],
        item_getters: Annotated[dict, Depends(make_item_getters)],
        payload: dict,  # @todo Use a proper payload model
    ):
        results = []

        lid_to_id = {}

        for operation in payload["atomic:operations"]:
            op = operation["op"]
            if op == "add":
                data = operation["data"]
                type = data["type"]
                lid = data.pop("lid", None)

                for relationship in data.get("relationships", {}).values():
                    relationship = relationship["data"]
                    if relationship is None:
                        pass
                    elif isinstance(relationship, dict):
                        if "lid" in relationship:
                            relationship["id"] = lid_to_id[relationship.pop("lid")]
                    else:
                        assert isinstance(relationship, list)
                        for rel in relationship:
                            if "lid" in rel:
                                rel["id"] = lid_to_id[rel.pop("lid")]

                create_payload = resources[type].CreateInputModel(data=data)

                # @todo Factorize this code with 'create_item'
                attributes = {
                    humps.decamelize(key) : value
                    for (key, value) in dict(create_payload.data.attributes).items()
                }

                relationships = {}
                for (key, value) in dict(create_payload.data.relationships).items():
                    key = humps.decamelize(key)
                    if isinstance(value.data, list):
                        # @todo Check item type against relationship type
                        relationships[key] = [item_getters[item.type](item.id) for item in value.data]
                    elif value.data is None:
                        relationships[key] = None
                    else:
                        relationships[key] = item_getters[value.data.type](value.data.id)

                item = item_creators[type](**attributes, **relationships)

                if lid is not None:
                    lid_to_id[lid] = item.id

                results.append({"data": resources[type].make_item(resources, urls=urls, item=item)})
            else:
                # @todo Support other operations ('update', 'delete', and operations on relationships)
                assert False
        return {
            "atomic:results": results,
        }


def parse_include(include):
    if include is None:
        return None
    elif include == "":
        return {}
    else:
        paths = [path.split(".") for path in include.split(",")]
        return_value = {}
        for path in paths:
            current = return_value
            for part in path:
                current = current.setdefault(part, {})
        return return_value


class ParseIncludeTestCase(unittest.TestCase):
    def test_none(self):
        self.assertEqual(parse_include(None), None)

    def test_empty_string(self):
        self.assertEqual(parse_include(""), {})

    def test_single_item(self):
        self.assertEqual(parse_include("author"), {"author": {}})

    def test_multiple_items(self):
        self.assertEqual(parse_include("author,comments"), {"author": {}, "comments": {}})

    def test_nested_items(self):
        self.assertEqual(parse_include("comments.author.team.members"), {"comments": {"author": {"team": {"members": {}}}}})

    def test_repeated_prefix(self):
        self.assertEqual(
            parse_include("comments.author.team.members.posts,comments.author.team.leader.comments"),
            {"comments": {"author": {"team": {"members": {"posts": {}}, "leader": {"comments": {}}}}}},
        )
