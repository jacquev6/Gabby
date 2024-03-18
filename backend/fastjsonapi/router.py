# from __future__ import annotations  # This doesn't work because we're annotating with local types. So this code won't work on Python 4. OK.
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel, create_model
from starlette import status

from .annotations import Annotations, Annotation
from .utils import Urls


class JSONAPIResponse(JSONResponse):
    media_type = "application/vnd.api+json"


def make_jsonapi_router(resource):
    singular_name = resource.singular_name
    plural_name = resource.plural_name
    assert plural_name != singular_name

    (CreateInputModel, ItemOutputModel, PageOutputModel, UpdateInputModel) = make_jsonapi_models(resource)

    router = APIRouter(
        default_response_class=JSONAPIResponse,
    )

    @router.post(
        f"/{plural_name}",
        name=f"create_{singular_name}",
        status_code=status.HTTP_201_CREATED,
        response_model=ItemOutputModel,
        response_model_exclude_unset=True,
    )
    def create_item(
        urls: Urls,
        payload: CreateInputModel,
        include: str = None
    ):
        item = resource.create_item(
            payload.data.attributes,
            payload.data.relationships,
        )

        return make_item_response(urls, item, include)

    @router.get(
        f"/{plural_name}",
        name=f"get_{plural_name}",
        response_model=PageOutputModel,
        response_model_exclude_unset=True,
    )
    def get_page(
        urls: Urls,
        filters: Annotated[dict, Depends(resource.filters)],
        page_number: Annotated[int, Query(alias="page[number]")] = 1,
        include: str = None,
    ):
        page_size = 2
        (items_count, all) = resource.get_page(filters, (page_number - 1) * page_size, page_size)
        assert len(all) <= page_size

        pages_count = (items_count + 1) // 2
        pagination = dict(count=items_count, page=page_number, pages=pages_count)

        # @todo Add original query parameters except page[number] to links
        base_url = urls.make(f"get_{plural_name}")

        if page_number < pages_count:
            next = f"{base_url}?page%5Bnumber%5D={page_number + 1}"
        else:
            next = None
        if page_number > 1:
            prev = f"{base_url}?page%5Bnumber%5D={page_number - 1}"
        else:
            prev = None
        links = dict(
            first=f"{base_url}?page%5Bnumber%5D=1",
            last=f"{base_url}?page%5Bnumber%5D={pages_count}",
            next=next,
            prev=prev,
        )
        return add_included(
            urls,
            dict(
                data=[make_item(urls, item) for item in all],
                links=links,
                meta=dict(pagination=pagination),
            ),
            include,
        )

    @router.get(
        f"/{plural_name}""/{id}",
        name=f"get_{singular_name}",
        response_model=ItemOutputModel,
        response_model_exclude_unset=True,
    )
    def get_item(
        urls: Urls,
        id: str,
        include: str = None,
    ):
        item = resource.get_item(id)
        if item:
            return make_item_response(urls, item, include)
        else:
            raise HTTPException(status_code=404, detail="Item not found")

    @router.patch(
        f"/{plural_name}""/{id}",
        name=f"update_{singular_name}",
        response_model=ItemOutputModel,
        response_model_exclude_unset=True,
    )
    def update_item(
        urls: Urls,
        id: str,
        payload: UpdateInputModel,
        include: str = None,
    ):
        item = resource.get_item(id)
        if item:
            resource.update_item(
                item,
                payload.data.attributes,
                payload.data.relationships,
            )
            return make_item_response(urls, item, include)
        else:
            raise HTTPException(status_code=404, detail="Item not found")

    @router.delete(
        f"/{plural_name}""/{id}",
        name=f"delete_{singular_name}",
        status_code=status.HTTP_204_NO_CONTENT,
        response_class=Response,
    )
    def delete_item(id: str):
        item = resource.get_item(id)
        if item:
            resource.delete_item(item)
        else:
            raise HTTPException(status_code=404, detail="Item not found")

    def make_item_response(urls, item, include):
        return add_included(urls, {"data": make_item(urls, item)}, include)

    def add_included(urls, response, include):
        data = response["data"]
        if isinstance(data, list):
            items = data
        else:
            items = [data]

        to_include = set()
        if include is not None:
            for incl in include.split(","):
                assert "." not in incl  # @todo Lift this restriction
                for item in items:
                    if incl in item["relationships"]:
                        rel = item["relationships"][incl]
                        if isinstance(rel["data"], list):
                            for rel_item in rel["data"]:
                                assert rel_item["type"] == singular_name  # @todo Lift this restriction
                                to_include.add(rel_item["id"])
                        else:
                            rel_item = rel["data"]
                            assert rel_item["type"] == singular_name  # @todo Lift this restriction
                            to_include.add(rel_item["id"])
        if to_include:
            response["included"] = [make_item(urls, resource.get_item(id)) for id in sorted(to_include)]

        return response

    def make_item(urls, item):
        return {
            "type": singular_name,
            "id": str(item.id),
            "links": {"self": urls.make(f"get_{singular_name}", id=str(item.id))},
            "attributes": resource.make_attributes(item),
            "relationships": resource.make_relationships(item),
        }

    return router


def make_jsonapi_models(resource):
    create_input_attributes = {}
    create_input_relationships = {}
    output_attributes = {}
    output_relationships = {}
    update_input_attributes = {}
    update_input_relationships = {}

    class ObjectId(BaseModel):
        type: str
        id: str

    class ScalarRelationShip(BaseModel):
        data: ObjectId | None = None

    class ListRelationShip(BaseModel):
        class Meta(BaseModel):
            count: int = 0

        data: list[ObjectId] = []
        meta: Meta = Meta()

    for (name, info) in resource.Model.model_fields.items():
        annotations = Annotations()
        for annotation in info.metadata:
            if isinstance(annotation, Annotation):
                annotation.apply(annotations)

        # @todo Be much more generic
        is_relationship = name in ["prev", "next"]

        if is_relationship:
            # @todo Be much more specific
            if info.annotation.__class__.__name__ == "GenericAlias":
                field = (ListRelationShip, ListRelationShip())
            else:
                field = (ScalarRelationShip, ScalarRelationShip())

            if annotations.create_input:
                create_input_relationships[name] = field
            if annotations.output:
                output_relationships[name] = field
            if annotations.update_input:
                update_input_relationships[name] = field
        else:
            field = (info.annotation, info.default)
            if annotations.create_input:
                create_input_attributes[name] = field
            if annotations.output:
                output_attributes[name] = field
            if annotations.update_input:
                update_input_attributes[name] = field

    # @todo Make sure that schemas in the OpenApi don't name-collide
    CreateInputAttributes = create_model("CreateInputAttributes", **create_input_attributes)
    CreateInputRelationships = create_model("CreateInputRelationships", **create_input_relationships)
    OutputAttributes = create_model("OutputAttributes", **output_attributes)
    OutputRelationships = create_model("OutputRelationships", **output_relationships)
    UpdateInputAttributes = create_model("UpdateInputAttributes", **update_input_attributes)
    UpdateInputRelationships = create_model("UpdateInputRelationships", **update_input_relationships)

    class CreateInputItemModel(BaseModel):
        type: str
        attributes: CreateInputAttributes = CreateInputAttributes()
        relationships: CreateInputRelationships = CreateInputRelationships()

    class CreateInputModel(BaseModel):
        data: CreateInputItemModel

    class OutputItemModel(BaseModel):
        class Links(BaseModel):
            self: str

        type: str
        id: str
        links: Links
        attributes: OutputAttributes
        relationships: OutputRelationships

    class ItemOutputModel(BaseModel):
        data: OutputItemModel
        included: list[OutputItemModel] = []

    class PageOutputModel(BaseModel):
        class Links(BaseModel):
            first: str
            last: str
            next: str | None
            prev: str | None

        class Meta(BaseModel):
            class Pagination(BaseModel):
                count: int
                page: int
                pages: int

            pagination: Pagination

        data: list[OutputItemModel]
        links: Links
        meta: Meta
        included: list[OutputItemModel] = []

    class UpdateInputItemModel(BaseModel):
        type: str
        attributes: UpdateInputAttributes = UpdateInputAttributes()
        relationships: UpdateInputRelationships = UpdateInputRelationships()

    class UpdateInputModel(BaseModel):
        data: UpdateInputItemModel

    return (CreateInputModel, ItemOutputModel, PageOutputModel, UpdateInputModel)
