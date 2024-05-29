import functools

import lark

from django.test import TestCase

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


class SectionParser:
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
        # This string manipulation before parsing is fragile but works for now.
        normalized = "\n\n".join(
            p.replace("\n", " ")
            for p in section.strip().replace("\r\n", "\n").replace("\r", "\n").split("\n\n")
        )

        return self.transformer.transform(self.parser.parse(normalized))


def parse_section(tags, transformer, section):
    return SectionParser(tags, transformer)(section)


parse_plain_section = SectionParser({}, SectionTransformer())


class GenericSectionTransformer(SectionTransformer):
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


parse_generic_section = SectionParser(
    {
        "selectable_text": r""" "|" INT "|" STR """,
        "selected_text": r""" "|" INT "|" INT "|" STR """,
        "selected_clicks": r""" "|" INT "|" INT """,
        "multiple_choices_input": r""" ("|" STR)+ """,
        "free_text_input": "",
    },
    GenericSectionTransformer(),
)


class ParseGenericSectionTestCase(TestCase):
    def do_test(self, input, expected):
        self.assertEqual(parse_generic_section(input), expected)
        self.assertEqual(parse_generic_section(expected.to_generic()), expected)

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
