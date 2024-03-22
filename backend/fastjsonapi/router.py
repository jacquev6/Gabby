# from __future__ import annotations  # This doesn't work because we're annotating with local types. So this code won't work on Python 4. OK.
from types import UnionType
from typing import Annotated
from urllib.parse import urlencode

from django.test import TestCase
from fastapi import APIRouter, Depends, HTTPException, Query, Response
from fastapi.responses import JSONResponse
from starlette import status
import humps

from .annotations import Annotations
from .utils import Urls
from .models import create_model, make_create_input_model, make_output_models, make_update_input_model


# @todo Check consistency of "type" attributes in input 'ObjectId's
# @todo Check consistency of "id" attributes in input 'ObjectId's
# @todo Check Content-Type header in requests (vnd.api+json for requests with payloads, not set for requests without payloads)
# @todo Check Accept header in requests (vnd.api+json)


class JSONAPIResponse(JSONResponse):
    media_type = "application/vnd.api+json"


def make_jsonapi_router(resources):
    resource_models = {
        resource.Model: humps.camelize(resource.singular_name) for resource in resources
    }
    resources = {
        humps.camelize(resource.singular_name): CompiledResource(resource_models, resource)
        for resource in resources
    }

    router = APIRouter(
        default_response_class=JSONAPIResponse,
    )

    for resource in resources.values():
        add_resource_routes(resources, resource, router)

    return router


class CompiledResource:
    def __init__(self, resource_models, resource):
        self._resource = resource

        optional_resource_models = {model | None : name for (model, name) in resource_models.items()}
        list_resource_models = {list[model] : name for (model, name) in resource_models.items()}

        assert humps.is_snakecase(resource.singular_name)
        self.singular_name = resource.singular_name
        self.singularName = humps.camelize(resource.singular_name)
        assert humps.is_snakecase(resource.plural_name)
        self.plural_name = resource.plural_name
        self.pluralName = humps.camelize(resource.plural_name)

        self.Model = resource.Model

        self.default_page_size = resource.default_page_size

        filterable_attributes = {}
        self.output_attributes = []
        self.output_relationships = {}
        for (name, info) in resource.Model.model_fields.items():
            name = humps.camelize(name)
            annotations = Annotations(info.metadata)

            if (resource_name := resource_models.get(info.annotation)) is not None:
                if annotations.output:
                    self.output_relationships[name] = (False, resource_name)
                if annotations.filter:
                    filterable_attributes[humps.decamelize(name)] = str
            elif (resource_name := optional_resource_models.get(info.annotation)) is not None:
                assert info.default is None
                if annotations.output:
                    self.output_relationships[name] = (False, resource_name)
                if annotations.filter:
                    filterable_attributes[humps.decamelize(name)] = str
            elif (resource_name := list_resource_models.get(info.annotation)) is not None:
                assert info.default == []
                if annotations.output:
                    self.output_relationships[name] = (True, resource_name)
            else:
                if annotations.output:
                    self.output_attributes.append(name)
                if annotations.filter:
                    filterable_attributes[humps.decamelize(name)] = info.annotation

        Filters = create_model(
            f"{self.singularName}-Filters",
            **{
                key: (value | None, ...)
                for (key, value) in filterable_attributes.items()
            },
        )
        # @todo Keep things structured all they way (avoid generating textual code)
        # See... my old answer here: https://stackoverflow.com/a/29927459/905845
        def filter_code():
            yield "def filters("
            for (name, annotation) in filterable_attributes.items():
                if isinstance(annotation, UnionType):
                    assert len(annotation.__args__) == 2
                    assert annotation.__args__[1] is type(None)
                    annotation = annotation.__args__[0]
                yield f"    {name}: Annotated[{annotation.__name__}, Query(alias='filter[{humps.camelize(name)}]')] = None,"
            yield "):"
            yield "    return Filters("
            for name in filterable_attributes:
                yield f"        {name}={name},"
            yield "    )"
        exec("\n".join(filter_code()), {"Filters": Filters}, filter_globals := {"Query": Query, "Annotated": Annotated})
        self.filters = filter_globals["filters"]

        resource_models = set(resource_models.keys())
        self.CreateInputModel = make_create_input_model(self.singularName, resource.Model, resource_models)
        (self.ItemOutputModel, self.PageOutputModel) = make_output_models(self.singularName, resource.Model, resource_models)
        self.UpdateInputModel = make_update_input_model(self.singularName, resource.Model, resource_models)

    def create_item(self, resources, attributes, relationships):
        attrs = {
            humps.decamelize(key) : value
            for (key, value) in dict(attributes).items()
        }

        rels = {}
        for (key, value) in dict(relationships).items():
            key = humps.decamelize(key)
            if isinstance(value.data, list):
                # @todo Check item type against relationship type
                rels[key] = [resources[item.type].get_item(item.id) for item in value.data]
            elif value.data is None:
                rels[key] = None
            else:
                rels[key] = resources[value.data.type].get_item(value.data.id)

        return self._resource.create_item(**attrs, **rels)

    def get_item(self, id):
        # @todo Pass parsed 'include' to allow pre-fetching
        return self._resource.get_item(id)

    def get_page(self, sort, filters, first_index, page_size):
        return self._resource.get_page(sort, filters, first_index, page_size)

    def update_item(self, resources, item, attributes, relationships):
        needs_save = False
        for (key, value) in attributes.model_dump(exclude_unset=True).items():
            setattr(item, humps.decamelize(key), value)
            needs_save = True
        for (key, value) in dict(relationships).items():
            if key in relationships.model_fields_set:
                if isinstance(value.data, list):
                    # @todo Check item type against relationship type
                    setattr(item, humps.decamelize(key), [resources[item.type].get_item(item.id) for item in value.data])
                elif value.data is None:
                    setattr(item, humps.decamelize(key), None)
                else:
                    setattr(item, humps.decamelize(key), resources[value.data.type].get_item(value.data.id))
                needs_save = True
        if needs_save:
            item.save()

    def delete_item(self, item):
        item.delete()

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
                (is_list, resource_name) = resource.output_relationships[name]
                # @todo Add test showing that this variable ('nested_resource') cannot be named 'resource' (bug fixed using tests from Gabby, deserves test in fastjsonapi)
                nested_resource = resources[resource_name]
                attr = getattr(item, humps.decamelize(name))
                if is_list:
                    for incl in attr:
                        included[(resource_name, incl.id)] = nested_resource.make_item(resources, urls=urls, item=incl)
                        recurse(nested_resource, incl, nested_include)
                elif attr is not None:
                    # @todo Add tests exercising this branch
                    included[(resource_name, attr.id)] = nested_resource.make_item(resources, urls=urls, item=attr)
                    recurse(nested_resource, attr, nested_include)

        for item in items:
            recurse(self, item, include)

        return sorted(included.values(), key=lambda item: (item["type"], item["id"]))


def add_resource_routes(resources, resource, router):
    @router.post(
        f"/{resource.pluralName}",
        name=f"create_{resource.singular_name}",
        status_code=status.HTTP_201_CREATED,
        response_model=resource.ItemOutputModel,
        response_model_exclude_unset=True,
    )
    def create_item(
        urls: Urls,
        payload: resource.CreateInputModel,
        include: str = None
    ):
        item = resource.create_item(
            resources,
            payload.data.attributes,
            payload.data.relationships,
        )

        return resource.make_item_response(resources, urls=urls, item=item, include=parse_include(include))

    @router.get(
        f"/{resource.pluralName}",
        name=f"get_{resource.plural_name}",
        response_model=resource.PageOutputModel,
        response_model_exclude_unset=True,
    )
    def get_page(
        urls: Urls,
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
        (items_count, items) = resource.get_page(parsed_sort, filters, (page_number - 1) * page_size, page_size)
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

    @router.get(
        f"/{resource.pluralName}""/{id}",
        name=f"get_{resource.singular_name}",
        response_model=resource.ItemOutputModel,
        response_model_exclude_unset=True,
    )
    def get_item(
        urls: Urls,
        id: str,
        include: str = None,
    ):
        item = resource.get_item(id)
        if item:
            return resource.make_item_response(resources, urls=urls, item=item, include=parse_include(include))
        else:
            raise HTTPException(status_code=404, detail="Item not found")

    @router.patch(
        f"/{resource.pluralName}""/{id}",
        name=f"update_{resource.singular_name}",
        response_model=resource.ItemOutputModel,
        response_model_exclude_unset=True,
    )
    def update_item(
        urls: Urls,
        id: str,
        payload: resource.UpdateInputModel,
        include: str = None,
    ):
        item = resource.get_item(id)
        if item:
            resource.update_item(
                resources,
                item,
                payload.data.attributes,
                payload.data.relationships,
            )
            return resource.make_item_response(resources, urls=urls, item=item, include=parse_include(include))
        else:
            raise HTTPException(status_code=404, detail="Item not found")

    @router.delete(
        f"/{resource.pluralName}""/{id}",
        name=f"delete_{resource.singular_name}",
        status_code=status.HTTP_204_NO_CONTENT,
        response_class=Response,
    )
    def delete_item(id: str):
        item = resource.get_item(id)
        if item:
            resource.delete_item(item)
        else:
            raise HTTPException(status_code=404, detail="Item not found")


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


class ParseIncludeTests(TestCase):
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
