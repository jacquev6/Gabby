# from __future__ import annotations  # This doesn't work because we're annotating with local types. So this code won't work on Python 4. OK.
from typing import Annotated, Type
import itertools

from fastapi import APIRouter, Body, Depends, HTTPException, Query, Request, Response
from fastapi.responses import JSONResponse
from starlette import status
import humps

from .compilation import compile
from .inclusion import IncludeDependable
from .utils import Urls


# @todo Check consistency of "type" attributes in input 'ObjectId's
# @todo Check consistency of "id" attributes in input 'ObjectId's
# @todo Check Content-Type header in requests (vnd.api+json for requests with payloads, not set for requests without payloads)
# @todo Check Accept header in requests (vnd.api+json)


class JSONAPIResponse(JSONResponse):
    media_type = "application/vnd.api+json"


def make_jsonapi_router(*, resources, polymorphism: dict[Type, str], batching: bool):
    compiled_resources = compile(resources, polymorphism)

    router = APIRouter(
        default_response_class=JSONAPIResponse,
    )

    for resource in compiled_resources.values():
        add_resource_routes(compiled_resources, resource, router)

    if batching:
        add_batch_route(compiled_resources, router)

    return router


def add_resource_routes(resources, resource, router):
    def make_related_getters(relationships):
        related_resources = set(itertools.chain.from_iterable(resource_names for (is_list, resource_names) in relationships.values()))
        # @todo Keep things structured all the way (avoid generating textual code)
        # See... my old answer here: https://stackoverflow.com/a/29927459/905845
        def make_related_getters_code():
            yield "def make_related_getters("
            for name in related_resources:
                yield f'    {name}: Annotated[resources["{name}"].ItemGetter, Depends()],'
            yield "):"
            yield "    return {"
            for name in related_resources:
                yield f'        "{name}": {name},'
            yield "    }"

        globals = {"Annotated": Annotated, "Depends": Depends}
        exec("\n".join(make_related_getters_code()), {"resources": resources}, globals)
        return globals["make_related_getters"]

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
            get_related_item: Annotated[dict, Depends(make_related_getters(resource.create_input_relationships))],
            payload: Annotated[resource.CreateInputModel, Body()],
            include: IncludeDependable,
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
                    relationships[key] = [get_related_item[item.type](id=item.id) for item in value.data]
                elif value.data is None:
                    relationships[key] = None
                else:
                    # @todo Check type against relationship type(s)
                    relationships[key] = get_related_item[value.data.type](id=value.data.id)

            # @todo Pass parsed 'include' to allow pre-fetching
            item = create_item(**attributes, **relationships)

            return resource.make_item_response(resources, urls=urls, item=item, include=include)

    if resource.PageGetter:
        @router.get(
            f"/{resource.pluralName}",
            name=f"get_{resource.plural_name}",
            response_model=resource.PageOutputModel,
            response_model_exclude_unset=True,
        )
        def get_page(
            request: Request,
            urls: Urls,
            get_page: Annotated[resource.PageGetter, Depends()],
            include: IncludeDependable,
            page_size: Annotated[int, Query(alias="page[size]")] = resource.default_page_size,
            page_number: Annotated[int, Query(alias="page[number]")] = 1,
        ):
            # @todo Pass parsed 'include' to allow pre-fetching
            (items_count, items) = get_page(first_index=(page_number - 1) * page_size, page_size=page_size)
            assert len(items) <= page_size
            return resource.make_page_response(
                resources,
                request,
                urls=urls,
                items_count=items_count,
                page_number=page_number,
                page_size=page_size,
                items=items,
                include=include,
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
            include: IncludeDependable,
        ):
            # @todo Pass parsed 'include' to allow pre-fetching
            item = get_item(id=id)
            if item:
                return resource.make_item_response(resources, urls=urls, item=item, include=include)
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
            get_related_item: Annotated[dict, Depends(make_related_getters(resource.update_input_relationships))],
            id: str,
            payload: Annotated[resource.UpdateInputModel, Body()],
            include: IncludeDependable,
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
                                    setattr(item, humps.decamelize(key), [get_related_item[item.type](id=item.id) for item in value.data])
                                elif value.data is None:
                                    setattr(item, humps.decamelize(key), None)
                                else:
                                    setattr(item, humps.decamelize(key), get_related_item[value.data.type](id=value.data.id))
                                needs_save = True
                        if not needs_save:
                            raise NothingToSave()
                except NothingToSave:
                    pass
                return resource.make_item_response(resources, urls=urls, item=item, include=include)
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
                        relationships[key] = [item_getters[item.type](id=item.id) for item in value.data]
                    elif value.data is None:
                        relationships[key] = None
                    else:
                        relationships[key] = item_getters[value.data.type](id=value.data.id)

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
