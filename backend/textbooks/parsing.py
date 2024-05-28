import dataclasses
import re
import textwrap

import lark

from django.test import TestCase

from . import renderable


class GenericSectionParser:
    grammar = textwrap.dedent(r"""\
        paragraph: sentence  # @todo Split paragraph in several sentences

        sentence: (_tag | word | punctuation | whitespace)+

        _tag: selectable_text_tag | selected_text_tag | selected_clicks_tag | multiple_choices_input_tag | free_text_input_tag

        selectable_text_tag: "{" "selectable-text" "|" INT "|" /[^}]+/ "}"

        selected_text_tag: "{" "selected-text" "|" INT "|" INT "|" /[^}]+/ "}"

        selected_clicks_tag: "{" "selected-clicks" "|" INT "|" INT "}"

        multiple_choices_input_tag: "{" "multiple-choices-input" ("|" /[^}|]+/)+ "}"

        free_text_input_tag: "{" "free-text-input" "}"

        # Keep these three regular expressions mutually exclusive
        word: /[\w]+/
        whitespace: /[ \t]+/
        punctuation: /[^\w \t]/

        %import common.CR
        %import common.LF
        %import common.INT
    """)

    class Transformer(lark.Transformer):
        def paragraph(self, sentences):
            return renderable.Paragraph(sentences=sentences)

        def sentence(self, args):
            return renderable.Sentence(tokens=args)

        def selectable_text_tag(self, args):
            return renderable.SelectableText(colors=args[0], text=args[1].value)

        def selected_text_tag(self, args):
            return renderable.SelectedText(color=args[0], colors=args[1], text=args[2].value)

        def selected_clicks_tag(self, args):
            return renderable.SelectedClicks(color=args[0], colors=args[1])

        def multiple_choices_input_tag(self, args):
            return renderable.MultipleChoicesInput(choices=[arg.value for arg in args])

        def free_text_input_tag(self, args):
            return renderable.FreeTextInput()

        def word(self, args):
            return renderable.PlainText(text=args[0])

        def whitespace(self, args):
            return renderable.Whitespace()

        def punctuation(self, args):
            return renderable.PlainText(text=args[0])

        def INT(self, arg):
            return int(arg.value)

    def __init__(self):
        self.parser = lark.Lark(self.grammar, start="paragraph")
        self.transformer = self.Transformer()

    def __call__(self, section: str) -> renderable.Section:
        paragraphs = []
        for p in section.split("\n\n"):
            p = " ".join(p.splitlines())
            try:
                tree = self.parser.parse(p)
            except lark.exceptions.LarkError as e:
                print("= PARSING ERROR IN ===========")
                print(p)
                print("= ERROR ======================")
                print(e)
                print("==============================")
                raise
            try:
                transformed = self.transformer.transform(tree)
                paragraphs.append(transformed)
            except lark.exceptions.LarkError as e:
                print("= TRANSFORM ERROR IN =========")
                print(p)
                print("= PARSED AS ==================")
                print(tree.pretty(), end="")
                print("= ERROR ======================")
                print(e)
                print("==============================")
                raise

        return renderable.Section(paragraphs=paragraphs)


parse_generic_section = GenericSectionParser()


class ParseGenericSectionTestCase(TestCase):
    def do_test(self, input, expected):
        self.assertEqual(parse_generic_section(input), expected)
        self.assertEqual(parse_generic_section(expected.to_generic()), expected)

    def test_single_paragraph_of_a_single_sentence_of_plain_words(self):
        self.do_test(
            "This is a\tsingle  \n  sentence.",
            renderable.Section(paragraphs=[renderable.Paragraph(sentences=[renderable.Sentence(tokens=[
                renderable.PlainText(text="This"),
                renderable.Whitespace(),
                renderable.PlainText(text="is"),
                renderable.Whitespace(),
                renderable.PlainText(text="a"),
                renderable.Whitespace(),
                renderable.PlainText(text="single"),
                renderable.Whitespace(),
                renderable.PlainText(text="sentence"),
                renderable.PlainText(text="."),
            ])])]),
        )

    def test_several_paragraphs_of_one_sentence_each(self):
        self.do_test(
            "This is\ta\nparagraph.\n\nThis is\nanother\nparagraph!",
            renderable.Section(paragraphs=[
                renderable.Paragraph(sentences=[renderable.Sentence(tokens=[
                    renderable.PlainText(text="This"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="is"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="a"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="paragraph"),
                    renderable.PlainText(text="."),
                ])]),
                renderable.Paragraph(sentences=[renderable.Sentence(tokens=[
                    renderable.PlainText(text="This"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="is"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="another"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="paragraph"),
                    renderable.PlainText(text="!"),
                ])]),
            ]),
        )

    def test_weird_characters(self):
        self.do_test(
            "Straße 120 àéïîöôù",
            renderable.Section(paragraphs=[renderable.Paragraph(sentences=[renderable.Sentence(tokens=[
                renderable.PlainText(text="Straße"),
                renderable.Whitespace(),
                renderable.PlainText(text="120"),
                renderable.Whitespace(),
                renderable.PlainText(text="àéïîöôù"),
            ])])]),
        )

    def test_selectable_text_tag(self):
        self.do_test(
            "This is {selectable-text|3|selectable}.",
            renderable.Section(paragraphs=[renderable.Paragraph(sentences=[renderable.Sentence(tokens=[
                renderable.PlainText(text="This"),
                renderable.Whitespace(),
                renderable.PlainText(text="is"),
                renderable.Whitespace(),
                renderable.SelectableText(colors=3, text="selectable"),
                renderable.PlainText(text="."),
            ])])]),
        )

    def test_selected_text_tag(self):
        self.do_test(
            "This is {selected-text|2|5|selected}.",
            renderable.Section(paragraphs=[renderable.Paragraph(sentences=[renderable.Sentence(tokens=[
                renderable.PlainText(text="This"),
                renderable.Whitespace(),
                renderable.PlainText(text="is"),
                renderable.Whitespace(),
                renderable.SelectedText(color=2, colors=5, text="selected"),
                renderable.PlainText(text="."),
            ])])]),
        )

    def test_selected_clicks_tag(self):
        self.do_test(
            "A {selected-clicks|2|5}.",
            renderable.Section(paragraphs=[renderable.Paragraph(sentences=[renderable.Sentence(tokens=[
                renderable.PlainText(text="A"),
                renderable.Whitespace(),
                renderable.SelectedClicks(color=2, colors=5),
                renderable.PlainText(text="."),
            ])])]),
        )

    def test_multiple_choices_input_tag(self):
        self.do_test(
            "A {multiple-choices-input|one|two|three}.",
            renderable.Section(paragraphs=[renderable.Paragraph(sentences=[renderable.Sentence(tokens=[
                renderable.PlainText(text="A"),
                renderable.Whitespace(),
                renderable.MultipleChoicesInput(choices=["one", "two", "three"]),
                renderable.PlainText(text="."),
            ])])]),
        )

    def test_free_text_input_tag(self):
        self.do_test(
            "Input {free-text-input}.",
            renderable.Section(paragraphs=[renderable.Paragraph(sentences=[renderable.Sentence(tokens=[
                renderable.PlainText(text="Input"),
                renderable.Whitespace(),
                renderable.FreeTextInput(),
                renderable.PlainText(text="."),
            ])])]),
        )

    def test_unknown_tag(self):
        self.do_test(
            "This is {unknown}.",
            renderable.Section(paragraphs=[renderable.Paragraph(sentences=[renderable.Sentence(tokens=[
                renderable.PlainText(text="This"),
                renderable.Whitespace(),
                renderable.PlainText(text="is"),
                renderable.Whitespace(),
                renderable.PlainText(text="{"),
                renderable.PlainText(text="unknown"),
                renderable.PlainText(text="}"),
                renderable.PlainText(text="."),
            ])])]),
        )


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
