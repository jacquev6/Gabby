from typing import Literal

from . import settings
from mydantic import PydanticBase


class _PlainText(PydanticBase):
    type: Literal["plainText"]
    text: str

    def to_generic(self):
        return self.text

def PlainText(text: str):
    assert text.__class__ == str, text.__class__
    return _PlainText(type="plainText", text=text)


class _BoxedText(PydanticBase):
    type: Literal["boxedText"]
    text: str

    def to_generic(self):
        return f"{{boxed-text|{self.text}}}"

def BoxedText(text: str):
    assert text.__class__ == str, text.__class__
    return _BoxedText(type="boxedText", text=text)


class _BoldText(PydanticBase):
    type: Literal["boldText"]
    text: str

    def to_generic(self):
        return f"{{bold-text|{self.text}}}"

def BoldText(text: str):
    assert text.__class__ == str, text.__class__
    return _BoldText(type="boldText", text=text)


class _ItalicText(PydanticBase):
    type: Literal["italicText"]
    text: str

    def to_generic(self):
        return f"{{italic-text|{self.text}}}"

def ItalicText(text: str):
    assert text.__class__ == str, text.__class__
    return _ItalicText(type="italicText", text=text)


class _SelectableText(PydanticBase):
    type: Literal["selectableText"]
    text: str
    colors: int

    def to_generic(self):
        return f"{{selectable-text|{self.colors}|{self.text}}}"

def SelectableText(text: str, colors: int):
    assert text.__class__ == str, text.__class__
    return _SelectableText(type="selectableText", text=text, colors=colors)


class _SelectedText(PydanticBase):
    type: Literal["selectedText"]
    text: str
    color: int
    colors: int

    def to_generic(self):
        return f"{{selected-text|{self.color}|{self.colors}|{self.text}}}"

def SelectedText(text: str, color: int, colors: int):
    assert text.__class__ == str, text.__class__
    return _SelectedText(type="selectedText", text=text, color=color, colors=colors)


class _SelectedClicks(PydanticBase):
    type: Literal["selectedClicks"]
    color: int
    colors: int

    def to_generic(self):
        return f"{{selected-clicks|{self.color}|{self.colors}}}"

def SelectedClicks(color: int, colors: int):
    return _SelectedClicks(type="selectedClicks", color=color, colors=colors)


class _FreeTextInput(PydanticBase):
    type: Literal["freeTextInput"]

    def to_generic(self):
        return "{free-text-input}"

def FreeTextInput():
    return _FreeTextInput(type="freeTextInput")


class _MultipleChoicesInput(PydanticBase):
    type: Literal["multipleChoicesInput"]
    choices: list[str]

    def to_generic(self):
        return "{multiple-choices-input|" + "|".join(self.choices) + "}"

def MultipleChoicesInput(choices: list[str]):
    return _MultipleChoicesInput(type="multipleChoicesInput", choices=choices)


class _Whitespace(PydanticBase):
    type: Literal["whitespace"]

    def to_generic(self):
        return " "

def Whitespace():
    return _Whitespace(type="whitespace")


SentenceToken = _PlainText | _BoxedText | _BoldText | _ItalicText | _SelectableText | _SelectedText | _SelectedClicks | _FreeTextInput | _MultipleChoicesInput | _Whitespace


class Sentence(PydanticBase):
    tokens: list[SentenceToken]

    def to_generic(self):
        return "".join(token.to_generic() for token in self.tokens)


class Paragraph(PydanticBase):
    sentences: list[Sentence]

    def to_generic(self):
        return " ".join(sentence.to_generic() for sentence in self.sentences)


class Section(PydanticBase):
    paragraphs: list[Paragraph]

    def to_generic(self):
        generic = "\n\n".join(p.to_generic() for p in self.paragraphs)
        if settings.DEBUG:
            from . import parsing
            adapted_again = parsing.adapt_generic_wording_section(generic)
            if adapted_again != self:
                print("Expected:", generic)
                print("Got:", adapted_again.to_generic())
                assert False
        return generic


class Exercise(PydanticBase):
    number: str
    textbook_page: int | None
    instructions: Section
    wording: Section
    example: Section
    clue: Section
