from typing import Literal

from mydantic import PydanticBase


class _PlainText(PydanticBase):
    type: Literal["plainText"]
    text: str

def PlainText(text: str):
    assert text.__class__ == str, text.__class__
    return _PlainText(type="plainText", text=text)


class _BoxedText(PydanticBase):
    type: Literal["boxedText"]
    text: str

def BoxedText(text: str):
    assert text.__class__ == str, text.__class__
    return _BoxedText(type="boxedText", text=text)


class PassiveFormattedText(PydanticBase):
    type: Literal["passiveFormattedText"]
    text: str
    bold: bool
    italic: bool


class _SelectableText(PydanticBase):
    type: Literal["selectableText"]
    text: str
    colors: list[str]
    boxed: bool

def SelectableText(text: str, colors: list[str], boxed: bool):
    assert text.__class__ == str, text.__class__
    return _SelectableText(type="selectableText", text=text, colors=colors, boxed=boxed)


class _SelectedText(PydanticBase):
    type: Literal["selectedText"]
    text: str
    color: str

def SelectedText(text: str, color: str):
    assert text.__class__ == str, text.__class__
    return _SelectedText(type="selectedText", text=text, color=color)


class _FreeTextInput(PydanticBase):
    type: Literal["freeTextInput"]

def FreeTextInput():
    return _FreeTextInput(type="freeTextInput")


class _MultipleChoicesInput(PydanticBase):
    type: Literal["multipleChoicesInput"]
    show_arrow_before: bool
    choices: list[str]
    show_choices_by_default: bool

def MultipleChoicesInput(show_arrow_before: bool, choices: list[str], show_choices_by_default: bool):
    return _MultipleChoicesInput(type="multipleChoicesInput", show_arrow_before=show_arrow_before, choices=choices, show_choices_by_default=show_choices_by_default)


class _Whitespace(PydanticBase):
    type: Literal["whitespace"]

def Whitespace():
    return _Whitespace(type="whitespace")


LeafToken = _PlainText | _BoxedText | PassiveFormattedText | _SelectedText | _FreeTextInput | _MultipleChoicesInput | _Whitespace


class _Selectable(PydanticBase):
    type: Literal["selectable"]
    contents: list[LeafToken]
    colors: list[str]
    boxed: bool

def Selectable(contents: list[LeafToken], colors: list[str], boxed: bool):
    return _Selectable(type="selectable", contents=contents, colors=colors, boxed=boxed)


class _Boxed(PydanticBase):
    type: Literal["boxed"]
    contents: list[LeafToken]

def Boxed(contents: list[LeafToken]):
    return _Boxed(type="boxed", contents=contents)


SentenceToken = LeafToken | _Selectable | _Boxed | _SelectableText


class Paragraph(PydanticBase):
    tokens: list[SentenceToken]


class Section(PydanticBase):
    paragraphs: list[Paragraph]


class Pagelet(PydanticBase):
    instructions: Section
    wording: Section


class Exercise(PydanticBase):
    number: str
    textbook_page: int | None
    pagelets: list[Pagelet]
