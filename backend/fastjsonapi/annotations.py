from typing import Any, Iterable


class Annotations:
    def __init__(self, annotations: Iterable[Any]):
        self.create_input = True
        self.update_input = True
        self.output = True
        self.filter = False

        for annotation in annotations:
            if isinstance(annotation, Annotation):
                annotation.apply(self)


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
