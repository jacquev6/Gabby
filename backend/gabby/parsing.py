import abc
import functools
import itertools
import unittest

import lark

from . import exercise_delta
from . import renderable


# Might be premature optimization, but we'll have a reasonable number of distinct grammars,
# and current architecture implies recompiling them often without this memo.
@functools.cache
def memoize_parser(grammar, start):
    return lark.Lark(grammar, start=start)


def make_grammar(tags, whitespace):
    grammar = (
        r"""\
            _separated{x, sep}: x (sep x)*

            section: LEADING_WHITESPACE? [_separated{_paragraph, PARAGRAPH_SEPARATOR}] TRAILING_WHITESPACE?

            _paragraph: strict_paragraph | lenient_paragraph

            strict_paragraph.3: _separated{sentence, SENTENCE_SEPARATOR}

            sentence.4: (_tag | WORD | PUNCTUATION_IN_SENTENCE | WHITESPACE_IN_SENTENCE)+ PUNCTUATION_AT_END_OF_SENTENCE

            lenient_paragraph.2: (_paragraph_token | WHITESPACE_IN_SENTENCE)* _paragraph_token
            _paragraph_token: _tag | WORD | PUNCTUATION_IN_LENIENT_PARAGRAPH

            WORD: /\w+/

            ANY_WHITESPACE: /[ \t\n\r]+/

            LEADING_WHITESPACE: ANY_WHITESPACE
            TRAILING_WHITESPACE: ANY_WHITESPACE
            PARAGRAPH_SEPARATOR: PARAGRAPH_SEPARATING_WHITESPACE
            SENTENCE_SEPARATOR: NON_PARAGRAPH_SEPARATING_WHITESPACE
            WHITESPACE_IN_SENTENCE: NON_PARAGRAPH_SEPARATING_WHITESPACE

            PUNCTUATION_IN_LENIENT_PARAGRAPH: /\.\.\.|[^\w \t\n\r]/
            PUNCTUATION_IN_SENTENCE: /[-,;:–]/
            PUNCTUATION_AT_END_OF_SENTENCE: /\.\.\.|[.!?…]/

            # Terminals usable in tags
            STR: /[^}|]+/
            INT: /[0-9]+/
        """
        + whitespace
        + f"_tag.1: {' | '.join(f"{tag}_tag" for tag in tags.keys())}\n"
        + "\n".join(f'{tag}_tag: "{{" "{tag.replace("_", "-")}" {definition} "}}"' for (tag, definition) in tags.items())
    )
    if len(tags) == 0:
        return grammar.replace("_tag | ", "")
    else:
        return grammar


def make_instructions_grammar(tags):
    return make_grammar(
        tags,
        r"""
            PARAGRAPH_SEPARATING_WHITESPACE: /([ \t]*(\r\n|\n)){2,}[ \t]*/
            NON_PARAGRAPH_SEPARATING_WHITESPACE: /([ \t]*(\r\n|\r|\n)[ \t]*)|[ \t]+/
        """
    )


def GrammarTestCase(grammar):
    class Transformer(lark.Transformer):
        def __getattr__(self, name):
            if name.isupper():
                def token(arg):
                    return (name, arg.value)
                return token
            else:
                def rule(args):
                    return (name.value, args)
                return rule

    parser = lark.Lark(grammar, start="section")
    transformer = Transformer()

    class GrammarTestCase(unittest.TestCase):
        def do_test(self, test, expected_ast):
            parse_tree = parser.parse(test)
            actual_ast = transformer.transform(parse_tree)
            if actual_ast != expected_ast:
                print(actual_ast)
            self.assertEqual(actual_ast, expected_ast)

    return GrammarTestCase


class InstructionsGrammarWithTagsTestCase(GrammarTestCase(make_instructions_grammar({
    "empty": "",
    "single_str": r""" "|" STR """,
    "int_and_str": r""" "|" INT "|" STR """,
    "several_ints": r""" ("|" INT)+ """,
}))):
    def test_empty(self):
        self.do_test("", ("section", []))

    def test_only_whitespace(self):
        self.do_test("    \t\n\n \t  \r\n\n\n    ", ("section", [("LEADING_WHITESPACE", "    \t\n\n \t  \r\n\n\n    ")]))

    def test_simple_strict_paragraphs(self):
        self.do_test(
            "First sentence. Second sentence.\n\nThird sentence.\n\nFourth sentence.",
            ("section", [
                ("strict_paragraph", [
                    ("sentence", [("WORD", "First"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")]),
                    ("SENTENCE_SEPARATOR", " "),
                    ("sentence", [("WORD", "Second"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")]),
                ]),
                ("PARAGRAPH_SEPARATOR", "\n\n"),
                ("strict_paragraph", [
                    ("sentence", [("WORD", "Third"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")]),
                ]),
                ("PARAGRAPH_SEPARATOR", "\n\n"),
                ("strict_paragraph", [
                    ("sentence", [("WORD", "Fourth"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")]),
                ]),
            ]),
        )

    def test_punctuation_at_end_of_sentence(self):
        for punctuation in [".", "!", "?", "…", "..."]:
            with self.subTest(punctuation=punctuation):
                self.do_test(
                    f"Strict sentence{punctuation}",
                    ("section", [("strict_paragraph", [("sentence", [("WORD", "Strict"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", punctuation)])])]),
                )

    def test_punctuation_in_sentence(self):
        for punctuation in [",", ";", ":", "-", "–"]:
            with self.subTest(punctuation=punctuation):
                self.do_test(
                    f"Strict{punctuation} sentence.",
                    ("section", [("strict_paragraph", [("sentence", [
                        ("WORD", "Strict"), ("PUNCTUATION_IN_SENTENCE", punctuation), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", "."),
                    ])])]),
                )

    whitespaces_in_sentence = [
        " ",
        "\t",
        " \t",
        "\t " * 5,
        "\n",
        "\r",
        "\r\n",
        "  \t\n",
        "  \t\n \t ",
        "\r",
        "  \t\r  ",
    ]

    def test_whitespace_in_sentence(self):
        for whitespace in self.whitespaces_in_sentence:
            with self.subTest(whitespace=whitespace):
                self.do_test(
                    f"Strict{whitespace}sentence.",
                    ("section", [("strict_paragraph", [("sentence", [("WORD", "Strict"), ("WHITESPACE_IN_SENTENCE", whitespace), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")])])]),
                )

    def test_leading_and_trailing_space(self):
        self.do_test(
            "    \t\n\n \t  \r\n\n\n    Strict sentence.    \t\n\n \t  \r\n\n\n    ",
            ("section", [
                ("LEADING_WHITESPACE", "    \t\n\n \t  \r\n\n\n    "),
                ("strict_paragraph", [
                    ("sentence", [("WORD", "Strict"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")]),
                ]),
                ("TRAILING_WHITESPACE", "    \t\n\n \t  \r\n\n\n    "),
            ]),
        )

    paragraph_separators = [
        "\n\n",
        "\r\n\n",
        "\r\n\r\n",
        "\n\r\n",
        "\n" * 5,
        "\r\n" * 5,
        "\n    \n",
        "     \n\n",
        "\r\n\t\r\n",
        "    \n    \n",
        "    \n" * 5,
        "    \n    \n    ",
    ]

    def test_strict_paragraph_separator(self):
        for separator in self.paragraph_separators:
            with self.subTest(separator=separator):
                self.do_test(
                    "First sentence." + separator + "Second sentence.",
                    ("section", [
                        ("strict_paragraph", [
                            ("sentence", [("WORD", "First"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")]),
                        ]),
                        ("PARAGRAPH_SEPARATOR", separator),
                        ("strict_paragraph", [
                            ("sentence", [("WORD", "Second"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")]),
                        ]),
                    ]),
                )

    sentence_separators = whitespaces_in_sentence

    def test_sentence_separator(self):
        for separator in self.sentence_separators:
            with self.subTest(separator=separator):
                self.do_test(
                    "First sentence." + separator + "Second sentence.",
                    ("section", [("strict_paragraph", [
                        ("sentence", [("WORD", "First"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")]),
                        ("SENTENCE_SEPARATOR", separator),
                        ("sentence", [("WORD", "Second"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")]),
                    ])]),
                )

    def test_simple_lenient_paragraphs(self):
        self.do_test(
            "First # sentence. Second # sentence.\n\nThird # sentence.\n\nFourth # sentence.",
            ("section", [
                ("lenient_paragraph", [
                    ("WORD", "First"),
                    ("WHITESPACE_IN_SENTENCE", " "),
                    ("PUNCTUATION_IN_LENIENT_PARAGRAPH", "#"),
                    ("WHITESPACE_IN_SENTENCE", " "),
                    ("WORD", "sentence"),
                    ("PUNCTUATION_IN_LENIENT_PARAGRAPH", "."),
                    ("WHITESPACE_IN_SENTENCE", " "),
                    ("WORD", "Second"),
                    ("WHITESPACE_IN_SENTENCE", " "),
                    ("PUNCTUATION_IN_LENIENT_PARAGRAPH", "#"),
                    ("WHITESPACE_IN_SENTENCE", " "),
                    ("WORD", "sentence"),
                    ("PUNCTUATION_IN_LENIENT_PARAGRAPH", "."),
                ]),
                ("PARAGRAPH_SEPARATOR", "\n\n"),
                ("lenient_paragraph", [
                    ("WORD", "Third"),
                    ("WHITESPACE_IN_SENTENCE", " "),
                    ("PUNCTUATION_IN_LENIENT_PARAGRAPH", "#"),
                    ("WHITESPACE_IN_SENTENCE", " "),
                    ("WORD", "sentence"),
                    ("PUNCTUATION_IN_LENIENT_PARAGRAPH", "."),
                ]),
                ("PARAGRAPH_SEPARATOR", "\n\n"),
                ("lenient_paragraph", [
                    ("WORD", "Fourth"),
                    ("WHITESPACE_IN_SENTENCE", " "),
                    ("PUNCTUATION_IN_LENIENT_PARAGRAPH", "#"),
                    ("WHITESPACE_IN_SENTENCE", " "),
                    ("WORD", "sentence"),
                    ("PUNCTUATION_IN_LENIENT_PARAGRAPH", "."),
                ]),
            ]),
        )

    def test_lenient_paragraph_separator(self):
        for separator in self.paragraph_separators:
            with self.subTest(separator=separator):
                self.do_test(
                    "First #." + separator + "Second #.",
                    ("section", [
                        ("lenient_paragraph", [
                            ("WORD", "First"), ("WHITESPACE_IN_SENTENCE", " "), ("PUNCTUATION_IN_LENIENT_PARAGRAPH", "#"), ("PUNCTUATION_IN_LENIENT_PARAGRAPH", "."),
                        ]),
                        ("PARAGRAPH_SEPARATOR", separator),
                        ("lenient_paragraph", [
                            ("WORD", "Second"), ("WHITESPACE_IN_SENTENCE", " "), ("PUNCTUATION_IN_LENIENT_PARAGRAPH", "#"), ("PUNCTUATION_IN_LENIENT_PARAGRAPH", "."),
                        ]),
                    ]),
                )

    def test_exotic_characters(self):
        self.do_test(
            "Straße 120 àéïîöôù",
            ("section", [
                ("lenient_paragraph", [
                    ("WORD", "Straße"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "120"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "àéïîöôù"),
                ]),
            ]),
        )

    def test_empty_tag_in_strict_paragraph(self):
        self.do_test(
            "{empty}.",
            ("section", [("strict_paragraph", [("sentence", [("empty_tag", []), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")])])])
        )

    def test_empty_tag_in_lenient_paragraph(self):
        self.do_test(
            "{empty}",
            ("section", [("lenient_paragraph", [("empty_tag", [])])])
        )

    def test_single_str_tag_in_strict_paragraph(self):
        self.do_test(
            "{single-str|foo}.",
            ("section", [("strict_paragraph", [("sentence", [("single_str_tag", [("STR", "foo")]), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")])])])
        )

    def test_single_str_tag_in_lenient_paragraph(self):
        self.do_test(
            "{single-str|foo}",
            ("section", [("lenient_paragraph", [("single_str_tag", [("STR", "foo")])])])
        )

    def test_int_and_str_tag_in_strict_paragraph(self):
        self.do_test(
            "{int-and-str|12|bar baz}.",
            ("section", [("strict_paragraph", [("sentence", [("int_and_str_tag", [("INT", "12"), ("STR", "bar baz")]), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")])])])
        )

    def test_int_and_str_tag_in_lenient_paragraph(self):
        self.do_test(
            "{int-and-str|12|bar baz}",
            ("section", [("lenient_paragraph", [("int_and_str_tag", [("INT", "12"), ("STR", "bar baz")])])])
        )

    def test_several_ints_tag_in_strict_paragraph(self):
        self.do_test(
            "{several-ints|42|43|45}.",
            ("section", [("strict_paragraph", [("sentence", [("several_ints_tag", [("INT", "42"), ("INT", "43"), ("INT", "45")]), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")])])])
        )

    def test_several_ints_tag_in_lenient_paragraph(self):
        self.do_test(
            "{several-ints|42|43|45}",
            ("section", [("lenient_paragraph", [("several_ints_tag", [("INT", "42"), ("INT", "43"), ("INT", "45")])])])
        )


class InstructionsGrammarWithoutTagsTestCase(GrammarTestCase(make_instructions_grammar({}))):
    def test_empty(self):
        self.do_test("", ("section", []))


class InstructionsSectionParser:
    def __init__(self, tags, transformer):
        tags = dict(
            bold = r""" "|" STR """,
            italic = r""" "|" STR """,
            **tags
        )
        self.parser = memoize_parser(make_instructions_grammar(tags), start="section")
        self.transformer = transformer

    def __call__(self, section: str):
        parsed = self.parser.parse(section)
        return self.transformer.transform(parsed)


class Transformer(lark.Transformer, abc.ABC):
    @abc.abstractmethod
    def section(self, args):
        pass

    @abc.abstractmethod
    def strict_paragraph(self, args):
        pass

    @abc.abstractmethod
    def sentence(self, args):
        pass

    @abc.abstractmethod
    def lenient_paragraph(self, args):
        pass

    @abc.abstractmethod
    def WORD(self, arg):
        pass

    @abc.abstractmethod
    def LEADING_WHITESPACE(self, arg):
        pass

    @abc.abstractmethod
    def TRAILING_WHITESPACE(self, arg):
        pass

    @abc.abstractmethod
    def PARAGRAPH_SEPARATOR(self, arg):
        pass

    @abc.abstractmethod
    def SENTENCE_SEPARATOR(self, arg):
        pass

    @abc.abstractmethod
    def WHITESPACE_IN_SENTENCE(self, arg):
        pass

    @abc.abstractmethod
    def PUNCTUATION_AT_END_OF_SENTENCE(self, arg):
        pass

    @abc.abstractmethod
    def PUNCTUATION_IN_SENTENCE(self, arg):
        pass

    @abc.abstractmethod
    def PUNCTUATION_IN_LENIENT_PARAGRAPH(self, arg):
        pass

    @abc.abstractmethod
    def INT(self, arg):
        pass

    @abc.abstractmethod
    def STR(self, arg):
        pass

    @abc.abstractmethod
    def bold_tag(self, args):
        pass

    @abc.abstractmethod
    def italic_tag(self, args):
        pass


class InstructionsSectionDeltaMaker(Transformer):
    def _merge(self, args):
        def join_group(attributes, items):
            items = list(items)
            if len(items) == 1:
                return items[0]
            else:
                assert attributes is not None
                assert all(isinstance(item.insert, str) for item in items)
                return exercise_delta.TextInsertOp(
                    insert="".join(item.insert for item in items),
                    attributes=attributes,
                )

        def key(arg):
            if isinstance(arg.insert, str):
                return arg.attributes
            else:
                assert isinstance(arg.insert, dict)
                return None

        return [
            join_group(group_key, group_items)
            for group_key, group_items in
            itertools.groupby(args, key=key)
        ]

    def _flatten(self, args):
        items = []
        for arg in args:
            if isinstance(arg, list):
                items.extend(arg)
            else:
                items.append(arg)
        return items

    def section(self, args):
        return self._merge(self._flatten(args))

    def strict_paragraph(self, args):
        return self._flatten(args)

    def sentence(self, args):
        return args

    def lenient_paragraph(self, args):
        return args

    def WORD(self, arg):
        return exercise_delta.TextInsertOp(insert=arg.value, attributes={})

    def LEADING_WHITESPACE(self, arg):
        return exercise_delta.TextInsertOp(insert=arg.value, attributes={})

    def TRAILING_WHITESPACE(self, arg):
        return exercise_delta.TextInsertOp(insert=arg.value, attributes={})

    def PARAGRAPH_SEPARATOR(self, arg):
        return exercise_delta.TextInsertOp(insert=arg.value, attributes={})

    def SENTENCE_SEPARATOR(self, arg):
        return exercise_delta.TextInsertOp(insert=arg.value, attributes={})

    def WHITESPACE_IN_SENTENCE(self, arg):
        return exercise_delta.TextInsertOp(insert=arg.value, attributes={})

    def PUNCTUATION_IN_SENTENCE(self, arg):
        return exercise_delta.TextInsertOp(insert=arg.value, attributes={})

    def PUNCTUATION_AT_END_OF_SENTENCE(self, arg):
        return exercise_delta.TextInsertOp(insert=arg.value, attributes={})

    def PUNCTUATION_IN_LENIENT_PARAGRAPH(self, arg):
        return exercise_delta.TextInsertOp(insert=arg.value, attributes={})

    def INT(self, arg):
        return arg.value

    def STR(self, arg):
        return arg.value

    def bold_tag(self, args):
        assert len(args) == 1
        return exercise_delta.TextInsertOp(insert=args[0], attributes={"bold": True})

    def italic_tag(self, args):
        assert len(args) == 1
        return exercise_delta.TextInsertOp(insert=args[0], attributes={"italic": True})


make_plain_instructions_section_delta = InstructionsSectionParser({}, InstructionsSectionDeltaMaker())


class InstructionsSectionAdapter(Transformer):
    def section(self, args):
        paragraphs = list(filter(None, args))
        return renderable.Section(paragraphs=list(
            renderable.Paragraph(sentences=[sentence])
            for sentence in
            itertools.chain.from_iterable(paragraph.sentences for paragraph in paragraphs)
        ))

    def strict_paragraph(self, args):
        sentences = list(filter(None, args))
        return renderable.Paragraph(sentences=sentences)

    def sentence(self, args):
        return renderable.Sentence(tokens=args)

    def lenient_paragraph(self, args):
        return renderable.Paragraph(sentences=[renderable.Sentence(tokens=args)])

    def WORD(self, arg):
        return renderable.PlainText(text=arg.value)

    def LEADING_WHITESPACE(self, arg):
        return None

    def TRAILING_WHITESPACE(self, arg):
        return None

    def PARAGRAPH_SEPARATOR(self, arg):
        return None

    def SENTENCE_SEPARATOR(self, arg):
        return None

    def WHITESPACE_IN_SENTENCE(self, arg):
        return renderable.Whitespace()

    def PUNCTUATION_IN_SENTENCE(self, arg):
        return renderable.PlainText(text=arg.value)

    def PUNCTUATION_AT_END_OF_SENTENCE(self, arg):
        return renderable.PlainText(text=arg.value)

    def PUNCTUATION_IN_LENIENT_PARAGRAPH(self, arg):
        return renderable.PlainText(text=arg.value)

    def INT(self, arg):
        return int(arg.value)

    def STR(self, arg):
        return arg.value

    def bold_tag(self, args):
        assert len(args) == 1
        return renderable.BoldText(text=args[0])

    def italic_tag(self, args):
        assert len(args) == 1
        return renderable.ItalicText(text=args[0])


adapt_plain_instructions_section = InstructionsSectionParser({}, InstructionsSectionAdapter())


class GenericInstructionsSectionAdapter(InstructionsSectionAdapter):
    def boxed_text_tag(self, args):
        text, = args
        return renderable.BoxedText(text=text)

    def selected_text_tag(self, args):
        text, color = args
        return renderable.SelectedText(text=text, color=color)


adapt_generic_instructions_section = InstructionsSectionParser(
    {
        "boxed_text": r""" "|" STR """,
        "selected_text": r""" "|" STR "|" STR """,
    },
    GenericInstructionsSectionAdapter(),
)


class AdaptGenericInstructionsSectionTestCase(unittest.TestCase):
    def do_test(self, input, expected_section):
        actual_section = adapt_generic_instructions_section(input)
        for paragraph_index, (actual_paragraph, expected_paragraph) in enumerate(zip(actual_section.paragraphs, expected_section.paragraphs, strict=True)):
            for sentence_index, (actual_sentence, expected_sentence) in enumerate(zip(actual_paragraph.sentences, expected_paragraph.sentences, strict=True)):
                self.assertEqual(actual_sentence, expected_sentence, f"Paragraph {paragraph_index}, sentence {sentence_index}")
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
            "This\ris\ta\nparagraph.\n\nThis is\n{boxed-text|another}\nparagraph!\r\n\r\nThird\r\nparagraph.\n\n4th paragraph.",
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
            "This is\ta\nsentence. This is\n{boxed-text|another}\nsentence! Third \nsentence. 4th sentence.",
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

    def test_selected_text_tag(self):
        self.do_test(
            "This is {selected-text|selected|red}.",
            renderable.Section(paragraphs=[renderable.Paragraph(sentences=[renderable.Sentence(tokens=[
                renderable.PlainText(text="This"),
                renderable.Whitespace(),
                renderable.PlainText(text="is"),
                renderable.Whitespace(),
                renderable.SelectedText(text="selected", color="red"),
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


def make_wording_grammar(tags):
    return make_grammar(
        tags,
        r"""
            PARAGRAPH_SEPARATING_WHITESPACE: /([ \t]*(\r\n|\n))+[ \t]*/
            NON_PARAGRAPH_SEPARATING_WHITESPACE: /[ \t]+/
        """
    )


class WordingGrammarTestCase(GrammarTestCase(make_wording_grammar({}))):
    def test_empty(self):
        self.do_test("", ("section", []))

    def test_only_whitespace(self):
        self.do_test("    \t\n\n \t  \r\n\n\n    ", ("section", [("LEADING_WHITESPACE", "    \t\n\n \t  \r\n\n\n    ")]))

    def test_simple_strict_paragraphs(self):
        self.do_test(
            "First sentence. Second sentence.\nThird sentence.\nFourth sentence.",
            ("section", [
                ("strict_paragraph", [
                    ("sentence", [("WORD", "First"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")]),
                    ("SENTENCE_SEPARATOR", " "),
                    ("sentence", [("WORD", "Second"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")]),
                ]),
                ("PARAGRAPH_SEPARATOR", "\n"),
                ("strict_paragraph", [
                    ("sentence", [("WORD", "Third"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")]),
                ]),
                ("PARAGRAPH_SEPARATOR", "\n"),
                ("strict_paragraph", [
                    ("sentence", [("WORD", "Fourth"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")]),
                ]),
            ]),
        )

    whitespaces_in_sentence = [
        " ",
        "\t",
        " \t",
        "\t " * 5,
    ]

    def test_whitespace_in_sentence(self):
        for whitespace in self.whitespaces_in_sentence:
            with self.subTest(whitespace=whitespace):
                self.do_test(
                    f"Strict{whitespace}sentence.",
                    ("section", [("strict_paragraph", [("sentence", [("WORD", "Strict"), ("WHITESPACE_IN_SENTENCE", whitespace), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")])])]),
                )

    def test_leading_and_trailing_space(self):
        self.do_test(
            "    \t\n\n \t  \r\n\n\n    Strict sentence.    \t\n\n \t  \r\n\n\n    ",
            ("section", [
                ("LEADING_WHITESPACE", "    \t\n\n \t  \r\n\n\n    "),
                ("strict_paragraph", [
                    ("sentence", [("WORD", "Strict"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")]),
                ]),
                ("TRAILING_WHITESPACE", "    \t\n\n \t  \r\n\n\n    "),
            ]),
        )

    paragraph_separators = [
        "\n",
        "\r\n",
        "\n\n",
        "\r\n\n",
        "\r\n\r\n",
        "\n\r\n",
        "\n" * 5,
        "\r\n" * 5,
        "\n    \n",
        "     \n\n",
        "\r\n\t\r\n",
        "    \n    \n",
        "    \n" * 5,
        "    \n    \n    ",
    ]

    def test_strict_paragraph_separator(self):
        for separator in self.paragraph_separators:
            with self.subTest(separator=separator):
                self.do_test(
                    "First sentence." + separator + "Second sentence.",
                    ("section", [
                        ("strict_paragraph", [
                            ("sentence", [("WORD", "First"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")]),
                        ]),
                        ("PARAGRAPH_SEPARATOR", separator),
                        ("strict_paragraph", [
                            ("sentence", [("WORD", "Second"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")]),
                        ]),
                    ]),
                )

    sentence_separators = whitespaces_in_sentence

    def test_sentence_separator(self):
        for separator in self.sentence_separators:
            with self.subTest(separator=separator):
                self.do_test(
                    "First sentence." + separator + "Second sentence.",
                    ("section", [("strict_paragraph", [
                        ("sentence", [("WORD", "First"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")]),
                        ("SENTENCE_SEPARATOR", separator),
                        ("sentence", [("WORD", "Second"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")]),
                    ])]),
                )

    def test_lenient_paragraph_separator(self):
        for separator in self.paragraph_separators:
            with self.subTest(separator=separator):
                self.do_test(
                    "First #." + separator + "Second #.",
                    ("section", [
                        ("lenient_paragraph", [
                            ("WORD", "First"), ("WHITESPACE_IN_SENTENCE", " "), ("PUNCTUATION_IN_LENIENT_PARAGRAPH", "#"), ("PUNCTUATION_IN_LENIENT_PARAGRAPH", "."),
                        ]),
                        ("PARAGRAPH_SEPARATOR", separator),
                        ("lenient_paragraph", [
                            ("WORD", "Second"), ("WHITESPACE_IN_SENTENCE", " "), ("PUNCTUATION_IN_LENIENT_PARAGRAPH", "#"), ("PUNCTUATION_IN_LENIENT_PARAGRAPH", "."),
                        ]),
                    ]),
                )


class WordingSectionParser:
    def __init__(self, tags, transformer):
        tags = dict(
            bold = r""" "|" STR """,
            italic = r""" "|" STR """,
            **tags
        )
        self.parser = memoize_parser(make_wording_grammar(tags), start="section")
        self.transformer = transformer

    def __call__(self, section: str):
        parsed = self.parser.parse(section)
        return self.transformer.transform(parsed)


class WordingSectionDeltaMaker(Transformer):
    def _merge(self, args):
        def join_group(attributes, items):
            items = list(items)
            if len(items) == 1:
                return items[0]
            else:
                assert attributes is not None
                assert all(isinstance(item.insert, str) for item in items)
                return exercise_delta.TextInsertOp(
                    insert="".join(item.insert for item in items),
                    attributes=attributes,
                )

        def key(arg):
            if isinstance(arg.insert, str):
                return arg.attributes
            else:
                assert isinstance(arg.insert, dict)
                return None

        return [
            join_group(group_key, group_items)
            for group_key, group_items in
            itertools.groupby(args, key=key)
        ]

    def _flatten(self, args):
        items = []
        for arg in args:
            if isinstance(arg, list):
                items.extend(arg)
            else:
                items.append(arg)
        return items

    def section(self, args):
        return self._merge(self._flatten(args))

    def strict_paragraph(self, args):
        return self._flatten(args)

    def sentence(self, args):
        return args

    def lenient_paragraph(self, args):
        return args

    def WORD(self, arg):
        return exercise_delta.TextInsertOp(insert=arg.value, attributes={})

    def LEADING_WHITESPACE(self, arg):
        return exercise_delta.TextInsertOp(insert=arg.value, attributes={})

    def TRAILING_WHITESPACE(self, arg):
        return exercise_delta.TextInsertOp(insert=arg.value, attributes={})

    def PARAGRAPH_SEPARATOR(self, arg):
        return exercise_delta.TextInsertOp(insert=arg.value, attributes={})

    def SENTENCE_SEPARATOR(self, arg):
        return exercise_delta.TextInsertOp(insert=arg.value, attributes={})

    def WHITESPACE_IN_SENTENCE(self, arg):
        return exercise_delta.TextInsertOp(insert=arg.value, attributes={})

    def PUNCTUATION_IN_SENTENCE(self, arg):
        return exercise_delta.TextInsertOp(insert=arg.value, attributes={})

    def PUNCTUATION_AT_END_OF_SENTENCE(self, arg):
        return exercise_delta.TextInsertOp(insert=arg.value, attributes={})

    def PUNCTUATION_IN_LENIENT_PARAGRAPH(self, arg):
        return exercise_delta.TextInsertOp(insert=arg.value, attributes={})

    def INT(self, arg):
        return arg.value

    def STR(self, arg):
        return arg.value

    def bold_tag(self, args):
        assert len(args) == 1
        return exercise_delta.TextInsertOp(insert=args[0], attributes={"bold": True})

    def italic_tag(self, args):
        assert len(args) == 1
        return exercise_delta.TextInsertOp(insert=args[0], attributes={"italic": True})


make_plain_wording_section_delta = WordingSectionParser({}, WordingSectionDeltaMaker())


class WordingSectionAdapter(Transformer):
    def section(self, args):
        paragraphs = list(filter(None, args))
        return renderable.Section(paragraphs=paragraphs)

    def strict_paragraph(self, args):
        sentences = list(filter(None, args))
        return renderable.Paragraph(sentences=sentences)

    def sentence(self, args):
        return renderable.Sentence(tokens=args)

    def lenient_paragraph(self, args):
        return renderable.Paragraph(sentences=[renderable.Sentence(tokens=args)])

    def WORD(self, arg):
        return renderable.PlainText(text=arg.value)

    def LEADING_WHITESPACE(self, arg):
        return None

    def TRAILING_WHITESPACE(self, arg):
        return None

    def PARAGRAPH_SEPARATOR(self, arg):
        return None

    def SENTENCE_SEPARATOR(self, arg):
        return None

    def WHITESPACE_IN_SENTENCE(self, arg):
        return renderable.Whitespace()

    def PUNCTUATION_IN_SENTENCE(self, arg):
        return renderable.PlainText(text=arg.value)

    def PUNCTUATION_AT_END_OF_SENTENCE(self, arg):
        return renderable.PlainText(text=arg.value)

    def PUNCTUATION_IN_LENIENT_PARAGRAPH(self, arg):
        return renderable.PlainText(text=arg.value)

    def INT(self, arg):
        return int(arg.value)

    def STR(self, arg):
        return arg.value

    def bold_tag(self, args):
        assert len(args) == 1
        return renderable.BoldText(text=args[0])

    def italic_tag(self, args):
        assert len(args) == 1
        return renderable.ItalicText(text=args[0])


def parse_wording_section(tags, transformer, section):
    return WordingSectionParser(tags, transformer)(section)


adapt_plain_wording_section = WordingSectionParser({}, WordingSectionAdapter())


class GenericWordingSectionAdapter(WordingSectionAdapter):
    def selectable_text_tag(self, args):
        text = args[0]
        colors = list(args[1:])
        return renderable.SelectableText(text=text, colors=colors, boxed=False)

    def multiple_choices_input_tag(self, args):
        choices = args
        return renderable.MultipleChoicesInput(choices=[choice for choice in choices])

    def free_text_input_tag(self, args):
        return renderable.FreeTextInput()


adapt_generic_wording_section = WordingSectionParser(
    {
        "selectable_text": r""" ("|" STR)+ """,
        "multiple_choices_input": r""" ("|" STR)+ """,
        "free_text_input": "",
    },
    GenericWordingSectionAdapter(),
)


class AdaptGenericWordingSectionTestCase(unittest.TestCase):
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
            "This is: a   sentence.   And, another; one. Again... Again… \t Another? Yes! Une autre ? Oui !",
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
                    renderable.PlainText(text="another"),
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

    def test_selectable_text_tag(self):
        self.do_test(
            "This is {selectable-text|selectable|red|green|blue}.",
            renderable.Section(paragraphs=[renderable.Paragraph(sentences=[renderable.Sentence(tokens=[
                renderable.PlainText(text="This"),
                renderable.Whitespace(),
                renderable.PlainText(text="is"),
                renderable.Whitespace(),
                renderable.SelectableText(text="selectable", colors=["red", "green", "blue"], boxed=False),
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
