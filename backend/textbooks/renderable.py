from typing import Literal

import pydantic


class BaseModel(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")


class PlainWord(BaseModel):
    type: Literal["plainWord"]
    text: str

class SelectableWord(BaseModel):
    type: Literal["selectableWord"]
    text: str
    colors: int

class FreeTextInput(BaseModel):
    type: Literal["freeTextInput"]
    pass

class Whitespace(BaseModel):
    type: Literal["whitespace"]
    pass

class Punctuation(BaseModel):
    type: Literal["punctuation"]
    text: str

SentenceToken = PlainWord | SelectableWord | FreeTextInput | Whitespace | Punctuation


class Sentence(BaseModel):
    tokens: list[SentenceToken]


class Paragraph(BaseModel):
    sentences: list[Sentence]


class Section(BaseModel):
    paragraphs: list[Paragraph]


class AdaptedExercise(BaseModel):
    number: str
    textbook_page: int | None
    instructions: str
    wording: Section
