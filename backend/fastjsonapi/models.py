import textwrap
from types import UnionType
from typing import Literal, Type
import humps

from .annotations import Annotations
from mydantic import PydanticBase, create_model, PydanticUndefined


class PageMeta(PydanticBase):
    class Pagination(PydanticBase):
        count: int
        page: int
        pages: int

    pagination: Pagination


class PageLinks(PydanticBase):
    # @todo Consider adding 'self'
    first: str
    last: str
    next: str | None
    prev: str | None


class ItemLinks(PydanticBase):
    self: str


class ObjectId(PydanticBase):
    type: str
    id: str


def create_model_for_mandatory_relationship(resource_name, relationship_name, related_names):
    model_name = f"{resource_name}_{relationship_name}_Relationship"

    code = textwrap.dedent(f"""\
        class {model_name}_ObjectId(PydanticBase):
            type: Literal[{', '.join(repr(name) for name in related_names)}]
            id: str

        class {model_name}(PydanticBase):
            data: {model_name}_ObjectId
    """)

    globals = {"PydanticBase": PydanticBase, "Literal": Literal}
    exec(code, globals)
    return globals[model_name]


def create_model_for_optional_relationship(resource_name, relationship_name, related_names):
    model_name = f"{resource_name}_{relationship_name}_Relationship"

    code = textwrap.dedent(f"""\
        class {model_name}_ObjectId(PydanticBase):
            type: Literal[{', '.join(repr(name) for name in related_names)}]
            id: str

        class {model_name}(PydanticBase):
            data: {model_name}_ObjectId | None
    """)

    globals = {"PydanticBase": PydanticBase, "Literal": Literal}
    exec(code, globals)
    return globals[model_name]


def create_model_for_list_relationship_for_input(resource_name, relationship_name, related_names):
    model_name = f"{resource_name}_{relationship_name}_RelationshipInput"

    code = textwrap.dedent(f"""\
        class {model_name}_ObjectId(PydanticBase):
            type: Literal[{', '.join(repr(name) for name in related_names)}]
            id: str

        class {model_name}(PydanticBase):
            data: list[{model_name}_ObjectId]
    """)

    globals = {"PydanticBase": PydanticBase, "Literal": Literal, "OutputListRelationShipMeta": OutputListRelationShipMeta}
    exec(code, globals)
    return globals[model_name]


class OutputListRelationShipMeta(PydanticBase):
    count: int


def create_model_for_list_relationship_for_output(resource_name, relationship_name, related_names):
    model_name = f"{resource_name}_{relationship_name}_RelationshipOutput"

    code = textwrap.dedent(f"""\
        class {model_name}_ObjectId(PydanticBase):
            type: Literal[{', '.join(repr(name) for name in related_names)}]
            id: str

        class {model_name}(PydanticBase):
            data: list[{model_name}_ObjectId]

            meta: OutputListRelationShipMeta
    """)

    globals = {"PydanticBase": PydanticBase, "Literal": Literal, "OutputListRelationShipMeta": OutputListRelationShipMeta}
    exec(code, globals)
    return globals[model_name]


class Decider:
    def __init__(self, resource_models: dict[Type, str]):
        self.__resource_models = dict(resource_models)
        self.__optional_resource_models = {model | None : name for (model, name) in resource_models.items()}
        self.__list_resource_models = {list[model] : name for (model, name) in resource_models.items()}

    def is_mandatory_relationship(self, annotation):
        return annotation in self.__resource_models

    def is_optional_relationship(self, annotation):
        if isinstance(annotation, UnionType):
            has_none = False
            for arg in annotation.__args__:
                if arg is type(None):
                    has_none = True
                    continue
                if arg not in self.__resource_models:
                    return False
            return has_none
        else:
            return False

    def is_list_relationship(self, annotation):
        return annotation in self.__list_resource_models

    def get_polymorphic_names(self, annotation):
        if self.is_mandatory_relationship(annotation):
            return [self.__resource_models[annotation]]
        elif self.is_optional_relationship(annotation):
            return [self.__resource_models[arg] for arg in annotation.__args__ if arg in self.__resource_models]
        elif self.is_list_relationship(annotation):
            return [self.__list_resource_models[annotation]]
        else:
            return []

    def is_attribute(self, annotation):
        return not (
            self.is_mandatory_relationship(annotation)
            or self.is_optional_relationship(annotation)
            or self.is_list_relationship(annotation)
        )


def create_model_for_input_for_create(resource_name: str, model, decider: Decider):
    assert humps.is_camelcase(resource_name)

    attributes = {}
    attributes_can_be_defaulted = True
    relationships = {}
    relationships_can_be_defaulted = True

    for (name, info) in model.model_fields.items():
        name = humps.camelize(name)
        if Annotations(info.metadata).create_input:
            if decider.is_mandatory_relationship(info.annotation):
                assert info.default is PydanticUndefined
                relationships_can_be_defaulted = False
                relationship_type = create_model_for_mandatory_relationship(resource_name, name, decider.get_polymorphic_names(info.annotation))
                relationships[name] = (relationship_type, ...)
            elif decider.is_optional_relationship(info.annotation):
                assert info.default is None
                relationship_type = create_model_for_optional_relationship(resource_name, name, decider.get_polymorphic_names(info.annotation))
                relationships[name] = (relationship_type, relationship_type(data=None))
            elif decider.is_list_relationship(info.annotation):
                assert info.default == []
                relationship_type = create_model_for_list_relationship_for_input(resource_name, name, decider.get_polymorphic_names(info.annotation))
                relationships[name] = (relationship_type, relationship_type(data=[]))
            elif decider.is_attribute(info.annotation):
                if info.default is PydanticUndefined:
                    attributes_can_be_defaulted = False
                attributes[name] = (info.annotation, info.default)
            else:
                assert False

    Attributes = create_model(f"{resource_name}CreateInputDataAttributes", **attributes)

    Relationships = create_model(f"{resource_name}CreateInputDataRelationships", **relationships)

    return create_model(
        f"{resource_name}CreateInput",
        data=(
            create_model(
                f"{resource_name}CreateInputData",
                type=(str, ...),
                attributes=(Attributes, Attributes() if attributes_can_be_defaulted else ...),
                relationships=(Relationships, Relationships() if relationships_can_be_defaulted else ...),
            ),
            ...
        ),
    )


def create_models_for_output(resource_name: str, model, decider: Decider):
    assert humps.is_camelcase(resource_name)

    attributes = {}
    relationships = {}

    for (name, info) in model.model_fields.items():
        name = humps.camelize(name)
        if Annotations(info.metadata).output:
            if decider.is_mandatory_relationship(info.annotation):
                relationship_type = create_model_for_mandatory_relationship(resource_name, name, decider.get_polymorphic_names(info.annotation))
                relationships[name] = (relationship_type, ...)
            elif decider.is_optional_relationship(info.annotation):
                relationship_type = create_model_for_optional_relationship(resource_name, name, decider.get_polymorphic_names(info.annotation))
                relationships[name] = (relationship_type, ...)
            elif decider.is_list_relationship(info.annotation):
                relationship_type = create_model_for_list_relationship_for_output(resource_name, name, decider.get_polymorphic_names(info.annotation))
                relationships[name] = (relationship_type, ...)
            elif decider.is_attribute(info.annotation):
                attributes[name] = (info.annotation, ...)
            else:
                assert False

    OutputItem = create_model(
        f"{resource_name}OutputItem",
        type=(str, ...),
        id=(str, ...),
        links=(ItemLinks, ...),
        **(dict(attributes=(
            create_model(
                f"{resource_name}OutputItemAttributes",
                **attributes,
            ),
            ...
        )) if attributes else {}),
        **(dict(relationships=(
            create_model(
                f"{resource_name}OutputItemRelationships",
                **relationships,
            ),
            ...
        )) if relationships else {}),
    )

    ItemOutput = create_model(
        f"{resource_name}ItemOutput",
        data=(OutputItem, ...),
        included=(list, None),
    )

    PageOutput = create_model(
        f"{resource_name}PageOutput",
        data=(list[OutputItem], ...),
        meta=(PageMeta, ...),
        links=(PageLinks, ...),
        included=(list, None),
    )

    return (ItemOutput, PageOutput)


def create_model_for_input_for_update(resource_name: str, model, decider: Decider):
    assert humps.is_camelcase(resource_name)

    attributes = {}
    relationships = {}

    for (name, info) in model.model_fields.items():
        name = humps.camelize(name)
        if Annotations(info.metadata).update_input:
            if decider.is_mandatory_relationship(info.annotation):
                relationship_type = create_model_for_mandatory_relationship(resource_name, name, decider.get_polymorphic_names(info.annotation))
                relationships[name] = (relationship_type, None)
            elif decider.is_optional_relationship(info.annotation):
                assert info.default is None
                relationship_type = create_model_for_optional_relationship(resource_name, name, decider.get_polymorphic_names(info.annotation))
                relationships[name] = (relationship_type, None)
            elif decider.is_list_relationship(info.annotation):
                assert info.default == []
                relationship_type = create_model_for_list_relationship_for_input(resource_name, name, decider.get_polymorphic_names(info.annotation))
                relationships[name] = (relationship_type, None)
            elif decider.is_attribute(info.annotation):
                attributes[name] = (info.annotation, None)
            else:
                assert False

    Attributes = create_model(f"{resource_name}UpdateInputDataAttributes", **attributes)

    Relationships = create_model(f"{resource_name}UpdateInputDataRelationships", **relationships)

    return create_model(
        f"{resource_name}UpdateInput",
        data=(
            create_model(
                f"{resource_name}UpdateInputData",
                type=(str, ...),
                id=(str, ...),
                attributes=(Attributes, Attributes()),
                relationships=(Relationships, Relationships()),
            ),
            ...
        ),
    )
