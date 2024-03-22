from typing import Type
from pydantic_core import PydanticUndefined
import humps
import pydantic

from .annotations import Annotations


class BaseModel(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")


def create_model(name, **fields):
    return pydantic.create_model(name, **fields, __base__=BaseModel)


class PageMetaModel(BaseModel):
    class Pagination(BaseModel):
        count: int
        page: int
        pages: int

    pagination: Pagination


class PageLinksModel(BaseModel):
    first: str
    last: str
    next: str | None
    prev: str | None


class ObjectId(BaseModel):
    type: str
    id: str


class MandatoryRelationship(BaseModel):
    data: ObjectId


class OptionalRelationship(BaseModel):
    data: ObjectId | None = None


class CreateInputListRelationship(BaseModel):
    data: list[ObjectId] = []


class OutputListRelationship(BaseModel):
    class Meta(BaseModel):
        count: int

    data: list[ObjectId]
    meta: Meta


class UpdateInputListRelationship(BaseModel):
    data: list[ObjectId]


def make_create_input_model(resource_name: str, model, resource_models: dict[Type, str]):
    assert humps.is_camelcase(resource_name)

    resource_models = set(resource_models.keys())
    optional_resource_models = {model | None for model in resource_models}
    list_resource_models = {list[model] for model in resource_models}

    attributes = {}
    attributes_can_be_defaulted = True
    relationships = {}
    relationships_can_be_defaulted = True

    for (name, info) in model.model_fields.items():
        name = humps.camelize(name)
        if Annotations(info.metadata).create_input:
            if info.annotation in resource_models:
                assert info.default is PydanticUndefined
                relationships_can_be_defaulted = False
                relationships[name] = (MandatoryRelationship, ...)
            elif info.annotation in optional_resource_models:
                assert info.default is None
                relationships[name] = (OptionalRelationship, OptionalRelationship())
            elif info.annotation in list_resource_models:
                assert info.default == []
                relationships[name] = (CreateInputListRelationship, CreateInputListRelationship())
            else:
                if info.default is PydanticUndefined:
                    attributes_can_be_defaulted = False
                attributes[name] = (info.annotation, info.default)

    Attributes = create_model(f"{resource_name}-CreateInput-Data-Attributes", **attributes)

    Relationships = create_model(f"{resource_name}-CreateInput-Data-Relationships", **relationships)

    return create_model(
        f"{resource_name}-CreateInput",
        data=(
            create_model(
                f"{resource_name}-CreateInput-Data",
                type=(str, ...),
                attributes=(Attributes, Attributes() if attributes_can_be_defaulted else ...),
                relationships=(Relationships, Relationships() if relationships_can_be_defaulted else ...),
            ),
            ...
        ),
    )


def make_output_models(resource_name: str, model, resource_models: dict[Type, str]):
    assert humps.is_camelcase(resource_name)

    resource_models = set(resource_models.keys())
    optional_resource_models = {model | None for model in resource_models}
    list_resource_models = {list[model] for model in resource_models}

    attributes = {}
    relationships = {}

    for (name, info) in model.model_fields.items():
        name = humps.camelize(name)
        if Annotations(info.metadata).output:

            if info.annotation in resource_models:
                relationships[name] = (MandatoryRelationship, ...)
            elif info.annotation in optional_resource_models:
                relationships[name] = (OptionalRelationship, ...)
            elif info.annotation in list_resource_models:
                relationships[name] = (OutputListRelationship, ...)
            else:
                attributes[name] = (info.annotation, ...)

    OutputItemModel = create_model(
        f"{resource_name}-OutputItem",
        type=(str, ...),
        id=(str, ...),
        links=(
            # @todo Make a static model for item links
            create_model(
                f"{resource_name}-OutputItem-Links",
                self=(str, ...),
            ),
            ...
        ),
        **(dict(attributes=(
            create_model(
                f"{resource_name}-OutputItem-Attributes",
                **attributes,
            ),
            ...
        )) if attributes else {}),
        **(dict(relationships=(
            create_model(
                f"{resource_name}-OutputItem-Relationships",
                **relationships,
            ),
            ...
        )) if relationships else {}),
    )

    ItemOutputModel = create_model(
        f"{resource_name}-ItemOutput",
        data=(OutputItemModel, ...),
        included=(list, None),
    )

    PageOutputModel = create_model(
        f"{resource_name}-PageOutput",
        data=(list[OutputItemModel], ...),
        meta=(PageMetaModel, ...),
        links=(PageLinksModel, ...),
        included=(list, None),
    )

    return (ItemOutputModel, PageOutputModel)


def make_update_input_model(resource_name: str, model, resource_models: dict[Type, str]):
    assert humps.is_camelcase(resource_name)

    resource_models = set(resource_models.keys())
    optional_resource_models = {model | None for model in resource_models}
    list_resource_models = {list[model] for model in resource_models}

    attributes = {}
    relationships = {}

    for (name, info) in model.model_fields.items():
        name = humps.camelize(name)
        if Annotations(info.metadata).update_input:
            if info.annotation in resource_models:
                relationships[name] = (MandatoryRelationship, None)
            elif info.annotation in optional_resource_models:
                assert info.default is None
                relationships[name] = (OptionalRelationship, None)
            elif info.annotation in list_resource_models:
                assert info.default == []
                relationships[name] = (UpdateInputListRelationship, None)
            else:
                attributes[name] = (info.annotation, None)

    Attributes = create_model(f"{resource_name}-UpdateInput-Data-Attributes", **attributes)

    Relationships = create_model(f"{resource_name}-UpdateInput-Data-Relationships", **relationships)

    return create_model(
        f"{resource_name}-UpdateInput",
        data=(
            create_model(
                f"{resource_name}-UpdateInput-Data",
                type=(str, ...),
                id=(str, ...),
                attributes=(Attributes, Attributes()),
                relationships=(Relationships, Relationships()),
            ),
            ...
        ),
    )
