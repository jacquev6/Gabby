from typing import Literal

import pydantic

from . import parsing


class BaseModel(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")


class _PlainText(BaseModel):
    type: Literal["plainText"]
    text: str

    def to_generic(self):
        return self.text

def PlainText(text: str):
    return _PlainText(type="plainText", text=text)


class _SelectableText(BaseModel):
    type: Literal["selectableText"]
    text: str
    colors: int

    def to_generic(self):
        return f"{{selectable-text|{self.colors}|{self.text}}}"

def SelectableText(text: str, colors: int):
    return _SelectableText(type="selectableText", text=text, colors=colors)


class _SelectedText(BaseModel):
    type: Literal["selectedText"]
    text: str
    color: int
    colors: int

    def to_generic(self):
        return f"{{selected-text|{self.color}|{self.colors}|{self.text}}}"

def SelectedText(text: str, color: int, colors: int):
    return _SelectedText(type="selectedText", text=text, color=color, colors=colors)


class _SelectedClicks(BaseModel):
    type: Literal["selectedClicks"]
    color: int
    colors: int

    def to_generic(self):
        return f"{{selected-clicks|{self.color}|{self.colors}}}"

def SelectedClicks(color: int, colors: int):
    return _SelectedClicks(type="selectedClicks", color=color, colors=colors)


class _FreeTextInput(BaseModel):
    type: Literal["freeTextInput"]

    def to_generic(self):
        return "{free-text-input}"

def FreeTextInput():
    return _FreeTextInput(type="freeTextInput")


class _MultipleChoicesInput(BaseModel):
    type: Literal["multipleChoicesInput"]
    choices: list[str]

    def to_generic(self):
        return "{multiple-choices-input|" + "|".join(self.choices) + "}"

def MultipleChoicesInput(choices: list[str]):
    return _MultipleChoicesInput(type="multipleChoicesInput", choices=choices)


class _Whitespace(BaseModel):
    type: Literal["whitespace"]

    def to_generic(self):
        return " "

def Whitespace():
    return _Whitespace(type="whitespace")


SentenceToken = _PlainText | _SelectableText | _SelectedText | _SelectedClicks | _FreeTextInput | _MultipleChoicesInput | _Whitespace


class Sentence(BaseModel):
    tokens: list[SentenceToken]

    def to_generic(self):
        return "".join(token.to_generic() for token in self.tokens)


class Paragraph(BaseModel):
    sentences: list[Sentence]

    def to_generic(self):
        return " ".join(sentence.to_generic() for sentence in self.sentences)


class Section(BaseModel):
    paragraphs: list[Paragraph]

    def to_generic(self):
        generic = "\n\n".join(p.to_generic() for p in self.paragraphs)
        assert parsing.parse_generic_section(generic) == self
        return generic


class AdaptedExercise(BaseModel):
    number: str
    textbook_page: int | None
    instructions: Section
    wording: Section
