from pydantic import BaseModel


class Annotations(BaseModel):
    create_input : bool = True
    update_input : bool = True
    output : bool = True
    filter : bool = False


class Annotation:
    pass


class Constant(Annotation):
    def apply(self, annotations : Annotations):
        annotations.update_input = False


class Computed(Annotation):
    def apply(self, annotations : Annotations):
        annotations.create_input = False
        annotations.update_input = False


class Secret(Annotation):
    def apply(self, annotations : Annotations):
        annotations.output = False


class Filterable(Annotation):
    def apply(self, annotations : Annotations):
        annotations.filter = True
