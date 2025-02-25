from __future__ import annotations

from typing import Literal

from mydantic import PydanticBase


class Whitespace(PydanticBase):
    kind: Literal["whitespace"]
    bold: bool = False
    italic: bool = False
    highlighted: str | None = None


class Text(PydanticBase):
    kind: Literal["text"]
    bold: bool = False
    italic: bool = False
    highlighted: str | None = None
    text: str


PassiveLeafRenderable = Whitespace | Text


class PassiveSequence(PydanticBase):
    kind: Literal["passiveSequence"]
    contents: list[PassiveRenderable]
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


class Section_(PydanticBase):
    paragraphs: list[Paragraph]
    centered: bool
    tricolored: bool


# @todo Remove this legacy adapter
def Section(paragraphs: list[Paragraph]) -> Section_:
    return Section_(paragraphs=paragraphs, centered=False, tricolored=False)


class Pagelet_(PydanticBase):
    sections: list[Section_]


# @todo Remove this legacy adapter
def Pagelet(*, instructions: Section_, wording: Section_) -> Pagelet_:
    assert instructions.centered is False
    instructions.centered = True
    assert instructions.tricolored is False
    assert wording.centered is False
    assert wording.tricolored is False
    wording.tricolored = True
    return Pagelet_(sections=[instructions, wording])


class Exercise(PydanticBase):
    number: str
    textbook_page: int | None
    pagelets: list[Pagelet_]
