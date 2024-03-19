# from __future__ import annotations  # This doesn't work because we're annotating with local types. So this code won't work on Python 4. OK.
from typing import Annotated
from urllib.parse import urlencode

from fastapi import APIRouter, Depends, HTTPException, Query, Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict, create_model
from pydantic_core import PydanticUndefined
from starlette import status
import humps

from .annotations import Annotations, Annotation
from .utils import Urls


class JSONAPIResponse(JSONResponse):
    media_type = "application/vnd.api+json"


def make_jsonapi_router(resources):
    resource_models = {
        resource.Model: humps.pascalize(resource.singular_name) for resource in resources
    }
    resources = {
        humps.pascalize(resource.singular_name): CompiledResource(resource_models, resource)
        for resource in resources
    }

    router = APIRouter(
        default_response_class=JSONAPIResponse,
    )

    for resource in resources.values():
        add_resource_routes(resources, resource, router)

    return router


class PageMetaModel(BaseModel):
    model_config = ConfigDict(extra="forbid")  # @todo Create a custom model base and use it instead of repeating this line

    class Pagination(BaseModel):
        model_config = ConfigDict(extra="forbid")

        count: int
        page: int
        pages: int

    pagination: Pagination


class PageLinksModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    first: str
    last: str
    next: str | None
    prev: str | None


class ObjectId(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: str
    id: str

class MandatoryRelationship(BaseModel):
    model_config = ConfigDict(extra="forbid")

    data: ObjectId

class OptionalRelationship(BaseModel):
    model_config = ConfigDict(extra="forbid")

    data: ObjectId | None = None

class CreateInputListRelationship(BaseModel):
    model_config = ConfigDict(extra="forbid")

    data: list[ObjectId] = []

class OutputListRelationship(BaseModel):
    model_config = ConfigDict(extra="forbid")

    class Meta(BaseModel):
        model_config = ConfigDict(extra="forbid")

        count: int

    data: list[ObjectId]
    meta: Meta

class UpdateInputListRelationship(BaseModel):
    model_config = ConfigDict(extra="forbid")

    data: list[ObjectId]


class CompiledResource:
    def __init__(self, resource_models, resource):
        self._resource = resource

        optional_resource_models = {model | None : name for (model, name) in resource_models.items()}
        list_resource_models = {list[model] : name for (model, name) in resource_models.items()}

        assert humps.is_snakecase(resource.singular_name)
        self.singular_name = resource.singular_name
        # self.singularName = humps.camelize(resource.singular_name)
        self.SingularName = humps.pascalize(resource.singular_name)
        assert humps.is_snakecase(resource.plural_name)
        self.plural_name = resource.plural_name
        self.pluralName = humps.camelize(resource.plural_name)
        self.PluralName = humps.pascalize(resource.plural_name)

        self.Model = resource.Model

        self.default_page_size = resource.default_page_size

        filterable_attributes = {}
        create_input_attributes_can_be_defaulted = True
        create_input_attributes = {}
        create_input_relationships_can_be_defaulted = True
        create_input_relationships = {}
        self.output_attributes = []
        output_attributes = {}
        self.output_relationships = []
        output_relationships = {}
        update_input_attributes = {}
        update_input_relationships = {}
        for (name, info) in resource.Model.model_fields.items():
            annotations = Annotations()
            for annotation in info.metadata:
                if isinstance(annotation, Annotation):
                    annotation.apply(annotations)

            if annotations.filter:
                filterable_attributes[name] = info.annotation

            name = humps.camelize(name)

            if (resource_name := resource_models.get(info.annotation)) is not None:
                assert info.default is PydanticUndefined
                create_input_relationships_can_be_defaulted = False
                if annotations.create_input:
                    create_input_relationships[name] = (MandatoryRelationship, ...)
                if annotations.output:
                    self.output_relationships.append((name, False, resource_name))
                    output_relationships[name] = (MandatoryRelationship, ...)
                if annotations.update_input:
                    update_input_relationships[name] = (MandatoryRelationship, None)
            elif (resource_name := optional_resource_models.get(info.annotation)) is not None:
                assert info.default is None
                if annotations.create_input:
                    create_input_relationships[name] = (OptionalRelationship, OptionalRelationship())
                if annotations.output:
                    self.output_relationships.append((name, False, resource_name))
                    output_relationships[name] = (OptionalRelationship, ...)
                if annotations.update_input:
                    update_input_relationships[name] = (OptionalRelationship, None)
            elif (resource_name := list_resource_models.get(info.annotation)) is not None:
                assert info.default is PydanticUndefined
                if annotations.create_input:
                    create_input_relationships[name] = (CreateInputListRelationship, CreateInputListRelationship())
                if annotations.output:
                    self.output_relationships.append((name, True, resource_name))
                    output_relationships[name] = (OutputListRelationship, ...)
                if annotations.update_input:
                    update_input_relationships[name] = (UpdateInputListRelationship, None)
            else:
                if annotations.create_input:
                    if info.default == PydanticUndefined:
                        create_input_attributes_can_be_defaulted = False
                    create_input_attributes[name] = (info.annotation, info.default)
                if annotations.output:
                    self.output_attributes.append(name)
                    output_attributes[name] = (info.annotation, ...)
                if annotations.update_input:
                    update_input_attributes[name] = (info.annotation, None)

        Filters = create_model(
            f"{self.SingularName}-Filters",
            **{
                key: (value | None, ...)
                for (key, value) in filterable_attributes.items()
            },
            __config__ = ConfigDict(extra="forbid"),
        )
        # @todo Keep things structured all they way (avoid generating textual code)
        # See... my old answer here: https://stackoverflow.com/a/29927459/905845
        def filter_code():
            yield "def filters("
            for (name, annotation) in filterable_attributes.items():
                yield f"    {name}: Annotated[{annotation.__name__}, Query(alias='filter[{humps.camelize(name)}]')] = None,"
            yield "):"
            yield "    return Filters("
            for name in filterable_attributes:
                yield f"        {name}={name},"
            yield "    )"
        exec("\n".join(filter_code()), {"Filters": Filters}, filter_globals := {"Query": Query, "Annotated": Annotated})
        self.filters = filter_globals["filters"]

        CreateInputDataAttributes = create_model(
            f"{self.SingularName}-CreateInput-Data-Attributes",
            **create_input_attributes,
            __config__ = ConfigDict(extra="forbid"),
        )

        create_input_attributes_default = CreateInputDataAttributes() if create_input_attributes_can_be_defaulted else ...

        CreateInputDataRelationships = create_model(
            f"{self.SingularName}-CreateInput-Data-Relationships",
            **create_input_relationships,
            __config__ = ConfigDict(extra="forbid"),
        )

        create_input_relationships_default = CreateInputDataRelationships() if create_input_relationships_can_be_defaulted else ...

        self.CreateInputModel = create_model(
            f"{self.SingularName}-CreateInput",
            data=(
                create_model(
                    f"{self.SingularName}-CreateInput-Data",
                    type=(str, ...),
                    attributes=(CreateInputDataAttributes, create_input_attributes_default),
                    relationships=(CreateInputDataRelationships, create_input_relationships_default),
                    __config__ = ConfigDict(extra="forbid"),
                ),
                ...
            ),
            __config__ = ConfigDict(extra="forbid"),
        )

        OutputItemModel = create_model(
            f"{self.SingularName}-OutputItem",
            type=(str, ...),
            id=(str, ...),
            links=(
                create_model(
                    f"{self.SingularName}-OutputItem-Links",
                    self=(str, ...),
                    __config__ = ConfigDict(extra="forbid"),
                ),
                ...
            ),
            **(dict(attributes=(
                create_model(
                    f"{self.SingularName}-OutputItem-Attributes",
                    **output_attributes,
                    __config__ = ConfigDict(extra="forbid"),
                ),
                ...
            )) if output_attributes else {}),
            **(dict(relationships=(
                create_model(
                    f"{self.SingularName}-OutputItem-Relationships",
                    **output_relationships,
                    __config__ = ConfigDict(extra="forbid"),
                ),
                ...
            )) if output_relationships else {}),
            __config__ = ConfigDict(extra="forbid"),
        )

        self.ItemOutputModel = create_model(
            f"{self.SingularName}-ItemOutput",
            data=(OutputItemModel, ...),
            __config__ = ConfigDict(extra="forbid"),
        )

        self.PageOutputModel = create_model(
            f"{self.PluralName}-PageOutput",
            data=(list[OutputItemModel], ...),
            meta=(PageMetaModel, ...),
            links=(PageLinksModel, ...),
            __config__ = ConfigDict(extra="forbid"),
        )

        UpdateInputDataAttributes = create_model(
            f"{self.SingularName}-UpdateInput-Data-Attributes",
            **update_input_attributes,
            __config__ = ConfigDict(extra="forbid"),
        )

        UpdateInputDataRelationships = create_model(
            f"{self.SingularName}-UpdateInput-Data-Relationships",
            **update_input_relationships,
            __config__ = ConfigDict(extra="forbid"),
        )

        self.UpdateInputModel = create_model(
            f"{self.SingularName}-UpdateInput",
            data=(
                create_model(
                    f"{self.SingularName}-UpdateInput-Data",
                    type=(str, ...),
                    id=(str, ...),
                    attributes=(UpdateInputDataAttributes, UpdateInputDataAttributes()),
                    relationships=(UpdateInputDataRelationships, UpdateInputDataRelationships()),
                    __config__ = ConfigDict(extra="forbid"),
                ),
                ...
            ),
            __config__ = ConfigDict(extra="forbid"),
        )

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
        return self._resource.get_item(id)

    def get_page(self, filters, first_index, page_size):
        return self._resource.get_page(filters, first_index, page_size)

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
        return {
            "data": self.make_item(resources, urls=urls, item=item),
        }

    def make_page_response(self, resources, *, urls, items_count, filters, page_number, page_size, items, include):
        pages_count = (items_count + 1) // page_size
        pagination = dict(count=items_count, page=page_number, pages=pages_count)

        base_url = urls.make(f"get_{self.plural_name}")
        def make_url_for_page(number):
            qs = {
                "page[size]": page_size,
                "page[number]": number,
            }
            for (key, value) in sorted(filters.model_dump(exclude_unset=True).items()):
                if value is not None:
                    qs[f"filter[{humps.camelize(key)}]"] = value
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

        return {
            "data": [self.make_item(resources, urls=urls, item=item) for item in items],
            "links": links,
            "meta": dict(pagination=pagination),
        }

    def make_item(self, resources, *, urls, item):
        r = {
            "type": self.SingularName,
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
            for (key, is_list, resource_name) in self.output_relationships:
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

        return resource.make_item_response(resources, urls=urls, item=item, include=include)

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
        include: str = None,
    ):
        (items_count, items) = resource.get_page(filters, (page_number - 1) * page_size, page_size)
        assert len(items) <= page_size
        return resource.make_page_response(
            resources,
            urls=urls,
            items_count=items_count,
            filters=filters,
            page_number=page_number,
            page_size=page_size,
            items=items,
            include=include,
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
            return resource.make_item_response(resources, urls=urls, item=item, include=include)
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
            return resource.make_item_response(resources, urls=urls, item=item, include=include)
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

    # def make_item_response(urls, item, include):
    #     return add_included(urls, {"data": make_item(urls, item)}, include)

    # def add_included(urls, response, include):
    #     data = response["data"]
    #     if isinstance(data, list):
    #         items = data
    #     else:
    #         items = [data]

    #     to_include = set()
    #     if include is not None:
    #         for incl in include.split(","):
    #             assert "." not in incl  # @todo Lift this restriction
    #             for item in items:
    #                 if incl in item["relationships"]:
    #                     rel = item["relationships"][incl]
    #                     if isinstance(rel["data"], list):
    #                         for rel_item in rel["data"]:
    #                             assert rel_item["type"] == singular_name  # @todo Lift this restriction
    #                             to_include.add(rel_item["id"])
    #                     else:
    #                         rel_item = rel["data"]
    #                         assert rel_item["type"] == singular_name  # @todo Lift this restriction
    #                         to_include.add(rel_item["id"])
    #     if to_include:
    #         response["included"] = [make_item(urls, resource.get_item(id)) for id in sorted(to_include)]

    #     return response

    # def make_item(urls, item):
    #     return {
    #         "type": singular_name,
    #         "id": str(item.id),
    #         "links": {"self": urls.make(f"get_{singular_name}", id=str(item.id))},
    #         "attributes": resource.make_attributes(item),
    #         "relationships": resource.make_relationships(item),
    #     }


# def make_jsonapi_models(resource):
#     create_input_attributes = {}
#     create_input_relationships = {}
#     output_attributes = {}
#     output_relationships = {}
#     update_input_attributes = {}
#     update_input_relationships = {}

#     class ObjectId(BaseModel):
#         type: str
#         id: str

#     class ScalarRelationShip(BaseModel):
#         data: ObjectId | None = None

#     class ListRelationShip(BaseModel):
#         class Meta(BaseModel):
#             count: int = 0

#         data: list[ObjectId] = []
#         meta: Meta = Meta()

#     for (name, info) in resource.Model.model_fields.items():
#         annotations = Annotations()
#         for annotation in info.metadata:
#             if isinstance(annotation, Annotation):
#                 annotation.apply(annotations)

#         # @todo Be much more generic
#         is_relationship = name in ["prev", "next"]

#         if is_relationship:
#             # @todo Be much more specific
#             if info.annotation.__class__.__name__ == "GenericAlias":
#                 field = (ListRelationShip, ListRelationShip())
#             else:
#                 field = (ScalarRelationShip, ScalarRelationShip())

#             if annotations.create_input:
#                 create_input_relationships[name] = field
#             if annotations.output:
#                 output_relationships[name] = field
#             if annotations.update_input:
#                 update_input_relationships[name] = field
#         else:
#             field = (info.annotation, info.default)
#             if annotations.create_input:
#                 create_input_attributes[name] = field
#             if annotations.output:
#                 output_attributes[name] = field
#             if annotations.update_input:
#                 update_input_attributes[name] = field

#     # @todo Make sure that schemas in the OpenApi don't name-collide
#     CreateInputAttributes = create_model("CreateInputAttributes", **create_input_attributes)
#     CreateInputRelationships = create_model("CreateInputRelationships", **create_input_relationships)
#     OutputAttributes = create_model("OutputAttributes", **output_attributes)
#     OutputRelationships = create_model("OutputRelationships", **output_relationships)
#     UpdateInputAttributes = create_model("UpdateInputAttributes", **update_input_attributes)
#     UpdateInputRelationships = create_model("UpdateInputRelationships", **update_input_relationships)

#     class CreateInputItemModel(BaseModel):
#         type: str
#         attributes: CreateInputAttributes = CreateInputAttributes()
#         relationships: CreateInputRelationships = CreateInputRelationships()

#     class CreateInputModel(BaseModel):
#         data: CreateInputItemModel

#     class OutputItemModel(BaseModel):
#         class Links(BaseModel):
#             self: str

#         type: str
#         id: str
#         links: Links
#         attributes: OutputAttributes
#         relationships: OutputRelationships

#     class ItemOutputModel(BaseModel):
#         data: OutputItemModel
#         included: list[OutputItemModel] = []

#     class PageOutputModel(BaseModel):
#         class Links(BaseModel):
#             first: str
#             last: str
#             next: str | None
#             prev: str | None

#         class Meta(BaseModel):
#             class Pagination(BaseModel):
#                 count: int
#                 page: int
#                 pages: int

#             pagination: Pagination

#         data: list[OutputItemModel]
#         links: Links
#         meta: Meta
#         included: list[OutputItemModel] = []

#     class UpdateInputItemModel(BaseModel):
#         type: str
#         attributes: UpdateInputAttributes = UpdateInputAttributes()
#         relationships: UpdateInputRelationships = UpdateInputRelationships()

#     class UpdateInputModel(BaseModel):
#         data: UpdateInputItemModel

#     return (CreateInputModel, ItemOutputModel, PageOutputModel, UpdateInputModel)
