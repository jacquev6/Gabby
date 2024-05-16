import dataclasses
import re

from django.test import TestCase


@dataclasses.dataclass
class TagToken:
    tag: str
    text: str

@dataclasses.dataclass
class WordToken:
    text: str

@dataclasses.dataclass
class ParagraphEndToken:
    pass

@dataclasses.dataclass
class HorizontalWhitespaceToken:
    text: str

@dataclasses.dataclass
class PunctuationToken:
    text: str

TextToken = TagToken | WordToken | ParagraphEndToken | HorizontalWhitespaceToken | PunctuationToken


tokenize_text_regex = re.compile(r"(?:{(?P<tag>[a-z0-9]+)\|(?P<tag_val>[^}]+)})|(?P<word>\w+)|(?P<paragraph_end>\n\n+)|(?P<space>\s+)|(?P<char>.)")

def tokenize_text(s: str) -> list[TextToken]:
    ret = []
    for m in tokenize_text_regex.finditer(s):
        if m.group("tag"):
            assert m.group("tag_val")
            ret.append(TagToken(m.group("tag"), m.group("tag_val")))
        elif m.group("word"):
            ret.append(WordToken(m.group("word")))
        elif m.group("paragraph_end"):
            ret.append(ParagraphEndToken())
        elif m.group("space"):
            ret.append(HorizontalWhitespaceToken(m.group("space")))
        else:
            assert m.group("char")
            ret.append(PunctuationToken(m.group("char")))
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
        self.make_test("  \t\n\t  ", [HorizontalWhitespaceToken("  \t\n\t  ")])

    def test_punctuation(self):
        self.make_test("!", [PunctuationToken("!")])

    def test_successive_punctuation(self):
        self.make_test(
            "Un martien ?!(vert).",
            [
                WordToken("Un"),
                HorizontalWhitespaceToken(" "),
                WordToken("martien"),
                HorizontalWhitespaceToken(" "),
                PunctuationToken("?"),
                PunctuationToken("!"),
                PunctuationToken("("),
                WordToken("vert"),
                PunctuationToken(")"),
                PunctuationToken("."),
            ],
        )

    def test_tag(self):
        self.make_test("{foo|hello}", [TagToken("foo", "hello")])

    def test_paragraph_end(self):
        self.make_test("\n\n", [ParagraphEndToken()])

    def test_paragraph_end__extra(self):
        self.make_test("\n\n\n\n\n", [ParagraphEndToken()])
