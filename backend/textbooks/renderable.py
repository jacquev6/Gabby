from typing import Literal

import pydantic


class BaseModel(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")


class PlainText(BaseModel):
    type: Literal["plainText"]
    text: str

class SelectableText(BaseModel):
    type: Literal["selectableText"]
    text: str
    colors: int

class FreeTextInput(BaseModel):
    type: Literal["freeTextInput"]
    pass

class Whitespace(BaseModel):
    type: Literal["whitespace"]
    pass

SentenceToken = PlainText | SelectableText | FreeTextInput | Whitespace


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
