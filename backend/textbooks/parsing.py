import dataclasses
import re

from django.test import TestCase


@dataclasses.dataclass
class WordToken:
    text: str


@dataclasses.dataclass
class WhitespaceToken:
    text: str


@dataclasses.dataclass
class PunctuationToken:
    text: str

TextToken = WordToken | WhitespaceToken | PunctuationToken


tokenize_text_regex = re.compile(r"(\w+)|(\s+)|(.)")

def tokenize_text(s: str) -> list[TextToken]:
    ret = []
    for m in tokenize_text_regex.finditer(s):
        if m.group(1):
            ret.append(WordToken(m.group(1)))
        elif m.group(2):
            ret.append(WhitespaceToken(m.group(2)))
        else:
            ret.append(PunctuationToken(m.group(0)))
    return ret


class TokenizeTextTestCase(TestCase):
    def make_test(self, input, expected):
        self.assertEqual(tokenize_text(input), expected)

    def test_empty_string(self):
        self.make_test("", [])

    def test_simple_word(self):
        self.make_test("hello", [WordToken("hello")])

    def test_accentuated_word(self):
        self.make_test("àéïîöôù", [WordToken("àéïîöôù")])

    def test_german_word(self):
        self.make_test("Straße", [WordToken("Straße")])

    def test_numbers_as_word(self):
        self.make_test("120", [WordToken("120")])

    def test_whitespace(self):
        self.make_test("  \t\n\t  ", [WhitespaceToken("  \t\n\t  ")])

    def test_punctuation(self):
        self.make_test("!", [PunctuationToken("!")])

    def test_successive_punctuation(self):
        self.make_test(
            "Un martien ?!(vert).",
            [
                WordToken("Un"),
                WhitespaceToken(" "),
                WordToken("martien"),
                WhitespaceToken(" "),
                PunctuationToken("?"),
                PunctuationToken("!"),
                PunctuationToken("("),
                WordToken("vert"),
                PunctuationToken(")"),
                PunctuationToken("."),
            ],
        )
