import abc
import functools
import itertools

import lark

from .testing import TestCase

from . import exercise_delta
from . import renderable


# Might be premature optimization, but we'll have a reasonable number of distinct grammars,
# and current architecture implies recompiling them often without this memo.
@functools.cache
def memoize_parser(grammar, start):
    return lark.Lark(grammar, start=start)


class _SectionDeltaMaker(lark.Transformer):
    def _merge(self, *args):
        for arg in args:
            assert isinstance(arg, list), arg
            for item in arg:
                assert isinstance(item, exercise_delta.InsertOp), item
        return [
            exercise_delta.InsertOp(
                insert="".join(item.insert for item in group),
                attributes=attributes
            )
            for attributes, group in
            itertools.groupby(itertools.chain.from_iterable(args), key=lambda arg: arg.attributes)
        ]

    def paragraph(self, args):
        assert len(args) == 1, args
        return args[0]

    def strict_paragraph(self, args):
        items = []
        for i, arg in enumerate(args):
            if i % 2 == 0:
                for item in arg:
                    assert isinstance(item, exercise_delta.InsertOp), item
                    items.append(item)
            else:
                item = arg
                assert isinstance(item, exercise_delta.InsertOp), item
                items.append(item)
        return items

    def paragraph_separator(self, args):
        assert len(args) == 1, args
        return exercise_delta.InsertOp(insert=args[0].value)

    def strict_sentence(self, args):
        for arg in args:
            assert isinstance(arg, exercise_delta.InsertOp), arg
        return args

    def lenient_paragraph(self, args):
        return args

    def in_sentence_punctuation(self, args):
        assert len(args) == 1
        return exercise_delta.InsertOp(insert=args[0].value)

    def end_of_sentence_punctuation(self, args):
        assert len(args) == 1
        return exercise_delta.InsertOp(insert=args[0].value)

    def word(self, args):
        assert len(args) == 1
        return exercise_delta.InsertOp(insert=args[0].value)

    def whitespace(self, args):
        assert len(args) == 1
        return exercise_delta.InsertOp(insert=args[0].value)

    def punctuation(self, args):
        assert len(args) == 1
        return exercise_delta.InsertOp(insert=args[0].value)

    def INT(self, arg):
        return exercise_delta.InsertOp(insert=arg.value)


class _SectionAdapter(lark.Transformer):
    def paragraph(self, args):
        assert len(args) == 1
        return args[0]

    def strict_paragraph(self, args):
        sentences = args[0::2]
        return renderable.Paragraph(sentences=sentences)

    def strict_sentence(self, args):
        return renderable.Sentence(tokens=args)

    def in_sentence_punctuation(self, args):
        assert len(args) == 1
        return renderable.PlainText(text=args[0].value)

    def end_of_sentence_punctuation(self, args):
        assert len(args) == 1
        return renderable.PlainText(text=args[0].value)

    def lenient_paragraph(self, args):
        return renderable.Paragraph(sentences=[renderable.Sentence(tokens=args)])

    def word(self, args):
        assert len(args) == 1
        return renderable.PlainText(text=args[0].value)

    def whitespace(self, args):
        assert len(args) == 1
        return renderable.Whitespace()

    def punctuation(self, args):
        assert len(args) == 1
        return renderable.PlainText(text=args[0].value)

    def INT(self, arg):
        return int(arg.value)


class InstructionsSectionDeltaMaker(_SectionDeltaMaker):
    def section(self, args):
        items = []
        for i, arg in enumerate(args):
            if i % 2 == 0:
                for item in arg:
                    assert isinstance(item, exercise_delta.InsertOp), item
                    items.append(item)
            else:
                item = arg
                assert isinstance(item, exercise_delta.InsertOp), item
                items.append(item)
        return self._merge(items)


class InstructionsSectionAdapter(_SectionAdapter):
    def section(self, args):
        paragraphs = args[0::2]
        return renderable.Section(paragraphs=list(
            renderable.Paragraph(sentences=[sentence])
            for sentence in
            itertools.chain.from_iterable(paragraph.sentences for paragraph in paragraphs)
        ))


class InstructionsSectionParser:
    def __init__(self, tags, transformer):
        grammar = (
            r"""\
                section: paragraph (paragraph_separator paragraph)*
                paragraph_separator: /\n\n/

                paragraph: strict_paragraph | lenient_paragraph

                strict_paragraph: strict_sentence (whitespace strict_sentence)*
                strict_sentence: (_tag | word | in_sentence_punctuation | whitespace)+ end_of_sentence_punctuation
                in_sentence_punctuation: /[,;:]/
                end_of_sentence_punctuation: /\.\.\.|[.!?…]/

                lenient_paragraph: (_tag | word | punctuation | whitespace)+

                # Keep these three regular expressions mutually exclusive
                word: /[\w]+/
                whitespace: /[ \t]+/
                punctuation: /\.\.\.|[^\w \t\n]/

                # Rules used in tags; do not delete
                STR: /[^}|]+/
                INT: /[0-9]+/
            """
            + f"_tag: {' | '.join(f"{tag}_tag" for tag in tags.keys())}\n"
            + "\n".join(f'{tag}_tag: "{{" "{tag.replace("_", "-")}" {definition} "}}"' for (tag, definition) in tags.items())
        )
        self.parser = memoize_parser(grammar, start="section")
        self.transformer = transformer

    def __call__(self, section: str):
        normalized = self.normalize(section)
        if normalized == "":
            return self.transformer.section([])
        else:
            try:
                return self.transformer.transform(self.parser.parse(normalized))
            except lark.exceptions.ParseError as e:
                raise ValueError(f"Error parsing section {normalized}: {e}")

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


parse_plain_instructions_section = InstructionsSectionParser({}, InstructionsSectionDeltaMaker())

adapt_plain_instructions_section = InstructionsSectionParser({}, InstructionsSectionAdapter())


class GenericSectionAdapterMixin:
    def boxed_text_tag(self, args):
        text, = args
        return renderable.BoxedText(text=text.value)

    def selectable_text_tag(self, args):
        colors, text = args
        return renderable.SelectableText(colors=colors, text=text.value)

    def selected_text_tag(self, args):
        color, colors, text = args
        return renderable.SelectedText(color=color, colors=colors, text=text.value)

    def selected_clicks_tag(self, args):
        color, colors = args
        return renderable.SelectedClicks(color=color, colors=colors)

    def multiple_choices_input_tag(self, args):
        choices = args
        return renderable.MultipleChoicesInput(choices=[choice.value for choice in choices])

    def free_text_input_tag(self, args):
        return renderable.FreeTextInput()


class GenericInstructionsSectionAdapter(InstructionsSectionAdapter, GenericSectionAdapterMixin):
    pass


adapt_generic_instructions_section = InstructionsSectionParser(
    {
        "boxed_text": r""" "|" STR """,
        "selectable_text": r""" "|" INT "|" STR """,
        "selected_text": r""" "|" INT "|" INT "|" STR """,
        "selected_clicks": r""" "|" INT "|" INT """,
        "multiple_choices_input": r""" ("|" STR)+ """,
        "free_text_input": "",
    },
    GenericInstructionsSectionAdapter(),
)


class AdaptGenericInstructionsSectionTestCase(TestCase):
    def do_test(self, input, expected_section):
        actual_section = adapt_generic_instructions_section(input)
        for paragraph_index, (actual_paragraph, expected_paragraph) in enumerate(zip(actual_section.paragraphs, expected_section.paragraphs, strict=True)):
            for sentence_index, (actual_sentence, expected_sentence) in enumerate(zip(actual_paragraph.sentences, expected_paragraph.sentences, strict=True)):
                self.assertEqual(actual_sentence, expected_sentence, f"Paragraph {paragraph_index}, sentence {sentence_index}")
        if expected_section is not None:
            self.assertEqual(adapt_generic_instructions_section(expected_section.to_generic()), expected_section)

    # In instructions (and example and clue) sections, we want to:
    # - join consecutive lines separated by a single carriage return into a single paragraph
    # - separate paragraphs by at least two carriage returns
    # - split paragraphs made of several sentences into several paragraphs of one sentence each

    def test_empty(self):
        self.do_test("", renderable.Section(paragraphs=[]))

    def test_only_whitespace(self):
        self.do_test("   \t\n    ", renderable.Section(paragraphs=[]))

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
            "This\ris\ta\nparagraph.\n\nThis is\n{boxed-text|another}\nparagraph!\r\n\r\nThird\r\nparagraph.\r\r4th paragraph.",
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
                    renderable.BoxedText(text="another"),
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

    def test_one_paragraph_of_several_sentences(self):
        self.do_test(
            "This\ris\ta\nsentence. This is\n{boxed-text|another}\nsentence! Third\r\nsentence. 4th sentence.",
            renderable.Section(paragraphs=[
                renderable.Paragraph(sentences=[renderable.Sentence(tokens=[
                    renderable.PlainText(text="This"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="is"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="a"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="sentence"),
                    renderable.PlainText(text="."),
                ])]),
                renderable.Paragraph(sentences=[renderable.Sentence(tokens=[
                    renderable.PlainText(text="This"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="is"),
                    renderable.Whitespace(),
                    renderable.BoxedText(text="another"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="sentence"),
                    renderable.PlainText(text="!"),
                ])]),
                renderable.Paragraph(sentences=[renderable.Sentence(tokens=[
                    renderable.PlainText(text="Third"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="sentence"),
                    renderable.PlainText(text="."),
                ])]),
                renderable.Paragraph(sentences=[renderable.Sentence(tokens=[
                    renderable.PlainText(text="4th"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="sentence"),
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


class WordingSectionParser:
    def __init__(self, tags, transformer):
        grammar = (
            r"""\
                section: paragraph ("\n\n" paragraph)*

                paragraph: strict_paragraph | lenient_paragraph

                strict_paragraph: strict_sentence (whitespace strict_sentence)*
                strict_sentence: (_tag | word | in_sentence_punctuation | whitespace)+ end_of_sentence_punctuation
                in_sentence_punctuation: /[,;:]/
                end_of_sentence_punctuation: /\.\.\.|[.!?…]/

                lenient_paragraph: (_tag | word | punctuation | whitespace)+

                # Keep these three regular expressions mutually exclusive
                word: /[\w]+/
                whitespace: /[ \t]+/
                punctuation: /\.\.\.|[^\w \t\n]/

                # Rules used in tags; do not delete
                STR: /[^}|]+/
                INT: /[0-9]+/
            """
            + f"_tag: {' | '.join(f"{tag}_tag" for tag in tags.keys())}\n"
            + "\n".join(f'{tag}_tag: "{{" "{tag.replace("_", "-")}" {definition} "}}"' for (tag, definition) in tags.items())
        )
        self.parser = memoize_parser(grammar, start="section")
        self.transformer = transformer

    def __call__(self, section: str):
        normalized = self.normalize(section)
        if normalized == "":
            return self.transformer.section([])
        else:
            try:
                return self.transformer.transform(self.parser.parse(normalized))
            except lark.exceptions.ParseError as e:
                raise ValueError(f"Error parsing section {normalized}: {e}")

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


class WordingSectionAdapter(_SectionAdapter):
    def section(self, paragraphs):
        return renderable.Section(paragraphs=paragraphs)


def parse_wording_section(tags, transformer, section):
    return WordingSectionParser(tags, transformer)(section)


adapt_plain_wording_section = WordingSectionParser({}, WordingSectionAdapter())


class GenericWordingSectionAdapter(WordingSectionAdapter, GenericSectionAdapterMixin):
    pass


adapt_generic_wording_section = WordingSectionParser(
    {
        "boxed_text": r""" "|" STR """,
        "selectable_text": r""" "|" INT "|" STR """,
        "selected_text": r""" "|" INT "|" INT "|" STR """,
        "selected_clicks": r""" "|" INT "|" INT """,
        "multiple_choices_input": r""" ("|" STR)+ """,
        "free_text_input": "",
    },
    GenericWordingSectionAdapter(),
)


class AdaptGenericWordingSectionTestCase(TestCase):
    def do_test(self, input, expected_section):
        actual_section = adapt_generic_wording_section(input)
        for paragraph_index, (actual_paragraph, expected_paragraph) in enumerate(zip(actual_section.paragraphs, expected_section.paragraphs, strict=True)):
            for sentence_index, (actual_sentence, expected_sentence) in enumerate(zip(actual_paragraph.sentences, expected_paragraph.sentences, strict=True)):
                self.assertEqual(actual_sentence, expected_sentence, f"Paragraph {paragraph_index}, sentence {sentence_index}")
        if expected_section is not None:
            self.assertEqual(adapt_generic_wording_section(expected_section.to_generic()), expected_section)

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

    def test_one_paragraph_with_strict_sentences(self):
        self.do_test(
            "This is: a   sentence.   And, {boxed-text|another}; one. Again... Again… \t Another? Yes! Une autre ? Oui !",
            renderable.Section(paragraphs=[renderable.Paragraph(sentences=[
                renderable.Sentence(tokens=[
                    renderable.PlainText(text="This"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="is"),
                    renderable.PlainText(text=":"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="a"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="sentence"),
                    renderable.PlainText(text="."),
                ]),
                renderable.Sentence(tokens=[
                    renderable.PlainText(text="And"),
                    renderable.PlainText(text=","),
                    renderable.Whitespace(),
                    renderable.BoxedText(text="another"),
                    renderable.PlainText(text=";"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="one"),
                    renderable.PlainText(text="."),
                ]),
                renderable.Sentence(tokens=[
                    renderable.PlainText(text="Again"),
                    renderable.PlainText(text="..."),
                ]),
                renderable.Sentence(tokens=[
                    renderable.PlainText(text="Again"),
                    renderable.PlainText(text="…"),
                ]),
                renderable.Sentence(tokens=[
                    renderable.PlainText(text="Another"),
                    renderable.PlainText(text="?"),
                ]),
                renderable.Sentence(tokens=[
                    renderable.PlainText(text="Yes"),
                    renderable.PlainText(text="!"),
                ]),
                renderable.Sentence(tokens=[
                    renderable.PlainText(text="Une"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="autre"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="?"),
                ]),
                renderable.Sentence(tokens=[
                    renderable.PlainText(text="Oui"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="!"),
                ]),
            ])]),
        )

    def test_one_paragraph_with_almost_two_strict_sentences(self):
        self.do_test(
            "This is a sentence. And another one but without its final dot",
            renderable.Section(paragraphs=[
                renderable.Paragraph(sentences=[renderable.Sentence(tokens=[
                    renderable.PlainText(text="This"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="is"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="a"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="sentence"),
                    renderable.PlainText(text="."),
                    renderable.Whitespace(),
                    renderable.PlainText(text="And"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="another"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="one"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="but"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="without"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="its"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="final"),
                    renderable.Whitespace(),
                    renderable.PlainText(text="dot"),
                ])]),
            ]),
        )
