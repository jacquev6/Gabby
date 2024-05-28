from typing import Literal

import pydantic


class BaseModel(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")


class _PlainText(BaseModel):
    type: Literal["plainText"]
    text: str

def PlainText(text: str):
    return _PlainText(type="plainText", text=text)


class _SelectableText(BaseModel):
    type: Literal["selectableText"]
    text: str
    colors: int

def SelectableText(text: str, colors: int):
    return _SelectableText(type="selectableText", text=text, colors=colors)


class _SelectedText(BaseModel):
    type: Literal["selectedText"]
    text: str
    color: int
    colors: int

def SelectedText(text: str, color: int, colors: int):
    return _SelectedText(type="selectedText", text=text, color=color, colors=colors)


class _SelectedClicks(BaseModel):
    type: Literal["selectedClicks"]
    color: int
    colors: int

def SelectedClicks(color: int, colors: int):
    return _SelectedClicks(type="selectedClicks", color=color, colors=colors)


class _FreeTextInput(BaseModel):
    type: Literal["freeTextInput"]

def FreeTextInput():
    return _FreeTextInput(type="freeTextInput")


class _MultipleChoicesInput(BaseModel):
    type: Literal["multipleChoicesInput"]
    choices: list[str]

def MultipleChoicesInput(choices: list[str]):
    return _MultipleChoicesInput(type="multipleChoicesInput", choices=choices)


class _Whitespace(BaseModel):
    type: Literal["whitespace"]

def Whitespace():
    return _Whitespace(type="whitespace")


SentenceToken = _PlainText | _SelectableText | _SelectedText | _SelectedClicks | _FreeTextInput | _MultipleChoicesInput | _Whitespace


class Sentence(BaseModel):
    tokens: list[SentenceToken]


class Paragraph(BaseModel):
    sentences: list[Sentence]


class Section(BaseModel):
    paragraphs: list[Paragraph]


class AdaptedExercise(BaseModel):
    number: str
    textbook_page: int | None
    instructions: Section
    wording: Section
