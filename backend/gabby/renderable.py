from __future__ import annotations

from typing import Literal

from mydantic import PydanticBase


class Whitespace(PydanticBase):
    kind: Literal["whitespace"]


class Text(PydanticBase):
    kind: Literal["text"]
    bold: bool = False
    italic: bool = False
    highlighted: str | None = None
    text: str


PassiveLeafRenderable = Whitespace | Text


class PassiveSequence(PydanticBase):
    kind: Literal["passiveSequence"]
    contents: list[PassiveLeafRenderable]
    boxed: bool = False


PassiveRenderable = PassiveLeafRenderable | PassiveSequence


class FreeTextInput(PydanticBase):
    kind: Literal["freeTextInput"]


class MultipleChoicesInput(PydanticBase):
    kind: Literal["multipleChoicesInput"]
    show_arrow_before: bool = False
    choices: list[list[PassiveRenderable]]
    show_choices_by_default: bool = False


class SelectableInput(PydanticBase):
    kind: Literal["selectableInput"]
    colors: list[str]
    boxed: bool = False
    contents: list[PassiveRenderable]


AlmostAnyRenderable = PassiveRenderable | FreeTextInput | MultipleChoicesInput | SelectableInput


class AnySequence(PydanticBase):
    kind: Literal["sequence"]
    contents: list[AlmostAnyRenderable | AnySequence]
    vertical: bool = False


AnyRenderable = AlmostAnyRenderable | AnySequence


class Paragraph(PydanticBase):
    contents: list[AnyRenderable]


class Section(PydanticBase):
    paragraphs: list[Paragraph]


class Pagelet(PydanticBase):
    instructions: Section
    wording: Section


class Exercise(PydanticBase):
    number: str
    textbook_page: int | None
    pagelets: list[Pagelet]
