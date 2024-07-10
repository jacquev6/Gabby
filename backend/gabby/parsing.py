import abc
import functools

import lark

from .testing import TestCase

from . import renderable


# Might be premature optimization, but we'll have a reasonable number of distinct grammars,
# and current architecture implies recompiling them often without this memo.
@functools.cache
def memoize_parser(grammar, start):
    return lark.Lark(grammar, start=start)


class SectionTransformer(lark.Transformer):
    def section(self, paragraphs):
        return renderable.Section(paragraphs=paragraphs)

    def paragraph(self, sentences):
        return renderable.Paragraph(sentences=sentences)

    def sentence(self, args):
        return renderable.Sentence(tokens=args)

    def word(self, args):
        return renderable.PlainText(text=args[0])

    def whitespace(self, args):
        return renderable.Whitespace()

    def punctuation(self, args):
        return renderable.PlainText(text=args[0])

    def INT(self, arg):
        return int(arg.value)


class SectionParser(abc.ABC):
    def __init__(self, tags, transformer):
        grammar = (
            r"""\
                section: paragraph ("\n\n" paragraph)*

                paragraph: sentence  # @todo Split paragraph in several sentences

                sentence: (_tag | word | punctuation | whitespace)+

                # Keep these three regular expressions mutually exclusive
                word: /[\w]+/
                whitespace: /[ \t]+/
                punctuation: /[^\w \t\n]/

                STR: /[^}|]+/
                INT: /[0-9]+/
            """
            + f"_tag: {' | '.join(f"{tag}_tag" for tag in tags.keys())}\n"
            + "\n".join(f'{tag}_tag: "{{" "{tag.replace("_", "-")}" {definition} "}}"' for (tag, definition) in tags.items())
        )
        self.parser = memoize_parser(grammar, start="section")
        self.transformer = transformer

    def __call__(self, section: str):
        if section == "":
            return self.transformer.section([])
        else:
            normalized = self.normalize(section)
            try:
                return self.transformer.transform(self.parser.parse(normalized))
            except lark.exceptions.ParseError as e:
                raise ValueError(f"Error parsing section {normalized}: {e}")

    @abc.abstractmethod
    def normalize(self, section: str) -> str:
        raise NotImplementedError()


class InstructionsSectionParser(SectionParser):
    def normalize(self, section):
        # This string manipulation before parsing is fragile but works for now.
        return "\n\n".join(
            p
            for p in (
                p.strip().replace("\n", " ")
                for p in section.strip().replace("\r\n", "\n").replace("\r", "\n").split("\n\n")
            )
            if p != ""
        )


def parse_instructions_section(tags, transformer, section):
    return InstructionsSectionParser(tags, transformer)(section)


parse_plain_instructions_section = InstructionsSectionParser({}, SectionTransformer())


class GenericSectionTransformer(SectionTransformer):
    def boxed_text_tag(self, args):
        text, = args
        return renderable.BoxedText(text=text)

    def selectable_text_tag(self, args):
        colors, text = args
        return renderable.SelectableText(colors=colors, text=text)

    def selected_text_tag(self, args):
        color, colors, text = args
        return renderable.SelectedText(color=color, colors=colors, text=text)

    def selected_clicks_tag(self, args):
        color, colors = args
        return renderable.SelectedClicks(color=color, colors=colors)

    def multiple_choices_input_tag(self, args):
        choices = args
        return renderable.MultipleChoicesInput(choices=[choice.value for choice in choices])

    def free_text_input_tag(self, args):
        return renderable.FreeTextInput()


parse_generic_instructions_section = InstructionsSectionParser(
    {
        "boxed_text": r""" "|" STR """,
        "selectable_text": r""" "|" INT "|" STR """,
        "selected_text": r""" "|" INT "|" INT "|" STR """,
        "selected_clicks": r""" "|" INT "|" INT """,
        "multiple_choices_input": r""" ("|" STR)+ """,
        "free_text_input": "",
    },
    GenericSectionTransformer(),
)


class ParseGenericInstructionsSectionTestCase(TestCase):
    def do_test(self, input, expected):
        self.assertEqual(parse_generic_instructions_section(input), expected)
        if expected is not None:
            self.assertEqual(parse_generic_instructions_section(expected.to_generic()), expected)

    # In instructions (and example and clue) sections, we want to:
    # - join consecutive lines separated by a single carriage return into a single paragraph
    # - separate paragraphs by at least two carriage returns
    # - @todo split paragraphs made of several sentences into several paragraphs of one sentence each

    def test_empty(self):
        self.do_test("", renderable.Section(paragraphs=[]))

    def test_single_paragraph_of_a_single_sentence_of_plain_words(self):
        self.do_test(
            "\n\n  \t   This is a\tsingle  \n  sentence.\n\n\n  \n\t\n",
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

    def test_false_paragraph_with_whitespace_only(self):
        self.do_test(
            "Paragraph 1\n\n  \n  \n\nParagraph 2",
            renderable.Section(paragraphs=[
                renderable.Paragraph(sentences=[renderable.Sentence(tokens=[
                    renderable.PlainText(text="Paragraph"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="1"),
                ])]),
                renderable.Paragraph(sentences=[renderable.Sentence(tokens=[
                    renderable.PlainText(text="Paragraph"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="2"),
                ])]),
            ]),
        )

    def test_several_paragraphs_of_one_sentence_each(self):
        self.do_test(
            "This\ris\ta\nparagraph.\n\nThis is\nanother\nparagraph!\r\n\r\nThird\r\nparagraph.\r\r4th paragraph.",
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
                renderable.Paragraph(sentences=[renderable.Sentence(tokens=[
                    renderable.PlainText(text="Third"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="paragraph"),
                    renderable.PlainText(text="."),
                ])]),
                renderable.Paragraph(sentences=[renderable.Sentence(tokens=[
                    renderable.PlainText(text="4th"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="paragraph"),
                    renderable.PlainText(text="."),
                ])]),
            ]),
        )

    def test_paragraphs_separated_by_more_than_two_newlines(self):
        self.do_test(
            "First paragraph.\n\n\nSecond paragraph.\n\n\n\nThird paragraph.\n\n\n\n\n\n\n\n\nFourth paragraph.\n\n\n\n\n\n\n\n\n\n\n\nFifth paragraph.",
            renderable.Section(paragraphs=[
                renderable.Paragraph(sentences=[renderable.Sentence(tokens=[
                    renderable.PlainText(text="First"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="paragraph"),
                    renderable.PlainText(text="."),
                ])]),
                renderable.Paragraph(sentences=[renderable.Sentence(tokens=[
                    renderable.PlainText(text="Second"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="paragraph"),
                    renderable.PlainText(text="."),
                ])]),
                renderable.Paragraph(sentences=[renderable.Sentence(tokens=[
                    renderable.PlainText(text="Third"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="paragraph"),
                    renderable.PlainText(text="."),
                ])]),
                renderable.Paragraph(sentences=[renderable.Sentence(tokens=[
                    renderable.PlainText(text="Fourth"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="paragraph"),
                    renderable.PlainText(text="."),
                ])]),
                renderable.Paragraph(sentences=[renderable.Sentence(tokens=[
                    renderable.PlainText(text="Fifth"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="paragraph"),
                    renderable.PlainText(text="."),
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


class WordingSectionParser(SectionParser):
    def normalize(self, section):
        # This string manipulation before parsing is fragile but works for now.
        return "\n\n".join(
            p
            for p in (
                p.strip()
                for p in section.strip().replace("\r\n", "\n").replace("\r", "\n").split("\n")
            )
            if p != ""
        )


def parse_wording_section(tags, transformer, section):
    return WordingSectionParser(tags, transformer)(section)


parse_plain_wording_section = WordingSectionParser({}, SectionTransformer())


parse_generic_wording_section = WordingSectionParser(
    {
        "boxed_text": r""" "|" STR """,
        "selectable_text": r""" "|" INT "|" STR """,
        "selected_text": r""" "|" INT "|" INT "|" STR """,
        "selected_clicks": r""" "|" INT "|" INT """,
        "multiple_choices_input": r""" ("|" STR)+ """,
        "free_text_input": "",
    },
    GenericSectionTransformer(),
)


class ParseGenericWordingSectionTestCase(TestCase):
    def do_test(self, input, expected):
        self.assertEqual(parse_generic_wording_section(input), expected)
        if expected is not None:
            self.assertEqual(parse_generic_wording_section(expected.to_generic()), expected)

    # In wording sections, we want to:
    # - make a paragraph for each non-empty line

    def test_empty(self):
        self.do_test("", renderable.Section(paragraphs=[]))

    def test_two_paragraphs(self):
        self.do_test(
            "\n\n  \t   This is a\tparagraph\nAnd another\t\n\n\n \t And yet another   \n\t\n",
            renderable.Section(paragraphs=[
                renderable.Paragraph(sentences=[renderable.Sentence(tokens=[
                    renderable.PlainText(text="This"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="is"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="a"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="paragraph"),
                ])]),
                renderable.Paragraph(sentences=[renderable.Sentence(tokens=[
                    renderable.PlainText(text="And"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="another"),
                ])]),
                renderable.Paragraph(sentences=[renderable.Sentence(tokens=[
                    renderable.PlainText(text="And"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="yet"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="another"),
                ])]),
            ]),
        )
