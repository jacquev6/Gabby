import re
from typing import Annotated, ClassVar, Literal
import itertools
import unittest

import lark
import pydantic

from . import exercise_delta
from . import renderable
from mydantic import PydanticBase


class FillWithFreeTextAdaptationEffect(PydanticBase):
    kind: Literal["fill-with-free-text"]

    placeholder: str

    def preprocess(self, instructions, wording, example, clue):
        wording = wording.replace(self.placeholder, f"{{fill-with-free-text|{self.placeholder}}}")
        return (instructions, wording, example, clue)

    def make_instructions_adapter_constructor_kwds(self):
        return {}

    def make_wording_adapter_constructor_kwds(self):
        return {}

    def make_example_adapter_constructor_kwds(self):
        return {}

    def make_clue_adapter_constructor_kwds(self):
        return {}


class ItemizedAdaptationEffect(PydanticBase):
    kind: Literal["itemized"]

    class WordsItems(PydanticBase):
        kind: Literal["words"]
        punctuation: bool

    class SentencesItems(PydanticBase):
        kind: Literal["sentences"]

    class ManualItems(PydanticBase):
        kind: Literal["manual"]

    Items: ClassVar = WordsItems | SentencesItems | ManualItems

    class Effects(PydanticBase):
        class Selectable(PydanticBase):
            colors: list[str]

        selectable: Selectable | None
        boxed: bool

    items: Items
    effects: Effects

    def preprocess(self, instructions, wording, example, clue):
        return (instructions, wording, example, clue)

    def make_instructions_adapter_constructor_kwds(self):
        if self.effects.selectable is None:
            return {}
        else:
            return {
                "selection_colors": self.effects.selectable.colors,
            }

    def make_wording_adapter_constructor_kwds(self):
        if self.effects.selectable is None:
            return {}
        else:
            if self.items.kind == "words":
                return {
                    "select_words": True,
                    "select_punctuation": self.items.punctuation,
                    "selection_colors": self.effects.selectable.colors,
                    "selectable_are_boxed": self.effects.boxed,
                }
            elif self.items.kind == "manual":
                return {
                    "selection_colors": self.effects.selectable.colors,
                    "selectable_are_boxed": self.effects.boxed,
                }
            else:
                assert False, f"Unknown items kind: {self.items.kind}"

    def make_example_adapter_constructor_kwds(self):
        if self.effects.selectable is None:
            return {}
        else:
            return {
                "selection_colors": self.effects.selectable.colors,
            }

    def make_clue_adapter_constructor_kwds(self):
        if self.effects.selectable is None:
            return {}
        else:
            return {
                "selection_colors": self.effects.selectable.colors,
            }


AdaptationEffect = Annotated[
    FillWithFreeTextAdaptationEffect | ItemizedAdaptationEffect,
    pydantic.Field(discriminator="kind"),
]


def gather_choices(deltas):
    choices = []
    for delta in deltas:
        if "choices2" in delta.attributes:
            choices_settings = delta.attributes["choices2"]
            if choices_settings["placeholder"] != "":
                choices.append([
                    choices_settings["start"] or None,
                    choices_settings["separator1"] or None,
                    choices_settings["separator2"] or None,
                    choices_settings["stop"] or None,
                    choices_settings["placeholder"],
                    delta.insert,
                ])
    return choices


def split_deltas_into_paragraphs_and_sentences(deltas: list[exercise_delta.TextInsertOp], explicit_paragraph_separator_pattern):
    assert len(deltas) > 0
    deltas[0].insert = deltas[0].insert.lstrip()
    deltas[-1].insert = deltas[-1].insert.rstrip()

    deltas_by_paragraph = [[]]
    for delta in deltas:
        if "choices2" in delta.attributes:
            deltas_by_paragraph[-1].append(delta)
        else:
            for i, paragraph_part in enumerate(re.split(explicit_paragraph_separator_pattern, delta.insert)):
                if i > 0:
                    deltas_by_paragraph.append([])
                if paragraph_part != "":
                    deltas_by_paragraph[-1].append(exercise_delta.TextInsertOp(insert=paragraph_part, attributes=delta.attributes))

    deltas_by_paragraph_and_sentence = []
    for paragraph_deltas in deltas_by_paragraph:
        can_be_splitted_at_sentence_end = True
        for j, delta in enumerate(paragraph_deltas):
            # Ad-hoc for unit tests and migration with behavior preserved bug-to-bug. @todo Remove to allow more splitting by sentences
            if delta.attributes == {} and any(c in delta.insert for c in "'#«»’()*➞+•/"):
                can_be_splitted_at_sentence_end = False

            sentence_parts = re.split(r"(\.\.\.|[.!?…])", delta.insert)
            # Last sentence doesn't end with a punctuation mark
            if j == len(paragraph_deltas) - 1 and sentence_parts[-1] != "":  # Maybe not as robust as we want, but this is behavior we want removed eventually anyway. @todo Remove to allow more splitting by sentences
                can_be_splitted_at_sentence_end = False

            # Sentence has two consecutive punctuation marks
            for i in range(1, len(sentence_parts) // 2):
                if sentence_parts[2 * i].strip() == "":
                    can_be_splitted_at_sentence_end = False

            if not can_be_splitted_at_sentence_end:
                break

        if can_be_splitted_at_sentence_end:
            # Previously know as "strict paragraph"
            deltas_by_paragraph_and_sentence.append([[]])
            for delta in paragraph_deltas:
                if "choices2" in delta.attributes:
                    deltas_by_paragraph_and_sentence[-1][-1].append(delta)
                else:
                    for i, sentence_part in enumerate(re.split(r"(\.\.\.|[.!?…])", delta.insert)):
                        if sentence_part != "":
                            if i % 2 == 0 and i > 1:
                                deltas_by_paragraph_and_sentence[-1].append([])
                            deltas_by_paragraph_and_sentence[-1][-1].append(exercise_delta.TextInsertOp(insert=sentence_part, attributes=delta.attributes))
        else:
            # Previously know as "lenient paragraph"
            deltas_by_paragraph_and_sentence.append([paragraph_deltas])

    return deltas_by_paragraph_and_sentence


def strip_section(section: renderable.Section):
    for paragraph_part in section.paragraphs:
        for s in paragraph_part.sentences:
            fixed_tokens = []
            for token in s.tokens:
                if token == renderable.Whitespace():
                    if len(fixed_tokens) > 0 and fixed_tokens[-1] != renderable.Whitespace():
                        fixed_tokens.append(token)
                else:
                    fixed_tokens.append(token)
            while len(fixed_tokens) > 0 and fixed_tokens[-1] == renderable.Whitespace():
                fixed_tokens.pop(-1)
            s.tokens = fixed_tokens
        paragraph_part.sentences = list(filter(lambda s: len(s.tokens) > 0, paragraph_part.sentences))
    section.paragraphs = list(filter(lambda p: len(p.sentences) > 0, section.paragraphs))


def adapt_instructions(deltas: list[exercise_delta.TextInsertOp], effects: list[AdaptationEffect]):
    selection_colors = []
    for effect in effects:
        if isinstance(effect, ItemizedAdaptationEffect):
            if effect.effects.selectable is not None:
                assert selection_colors == []
                selection_colors = effect.effects.selectable.colors

    def adapt_sentence(deltas: list[exercise_delta.TextInsertOp]):
        for delta in deltas:
            if delta.attributes == {}:
                for text in re.split(r"(\.\.\.|\s+|\W)", delta.insert):
                    if text != "":
                        if text.strip() == "":
                            yield renderable.Whitespace()
                        else:
                            yield renderable.PlainText(text=text)

            elif "sel" in delta.attributes:
                assert delta.attributes == {"sel": delta.attributes["sel"]}

                if len(selection_colors) > delta.attributes["sel"] - 1:
                    yield renderable.SelectedText(text=delta.insert, color=selection_colors[delta.attributes["sel"] - 1])
                else:
                    yield renderable.PlainText(text=delta.insert)

            elif "choices2" in delta.attributes:
                assert delta.attributes == {"choices2": delta.attributes["choices2"]}

                start = delta.attributes["choices2"]["start"] or None
                separator1 = delta.attributes["choices2"]["separator1"] or None
                separator2 = delta.attributes["choices2"]["separator2"] or None
                stop = delta.attributes["choices2"]["stop"] or None
                placeholder = delta.attributes["choices2"]["placeholder"] or None
                text = delta.insert

                add_start_and_stop = start is not None and stop is not None and text.startswith(start) and text.endswith(stop)
                choices = _separate_choices(start, separator1, separator2, stop, placeholder, text)
                if add_start_and_stop:
                    yield renderable.PlainText(text=start)
                yield renderable.BoxedText(text=choices[0])
                if separator2 is None:
                    for choice in choices[1:]:
                        yield renderable.Whitespace()
                        yield renderable.PlainText(text=separator1)
                        yield renderable.Whitespace()
                        yield renderable.BoxedText(text=choice)
                else:
                    for choice in choices[1:-1]:
                        yield renderable.PlainText(text=separator1)
                        yield renderable.Whitespace()
                        yield renderable.BoxedText(text=choice)
                    yield renderable.Whitespace()
                    yield renderable.PlainText(text=separator2)
                    yield renderable.Whitespace()
                    yield renderable.BoxedText(text=choices[-1])
                if add_start_and_stop:
                    yield renderable.PlainText(text=stop)

            elif "bold" in delta.attributes:
                assert delta.attributes == {"bold": delta.attributes["bold"]}

                yield renderable.BoldText(text=delta.insert)

            elif "italic" in delta.attributes:
                assert delta.attributes == {"italic": delta.attributes["italic"]}

                yield renderable.ItalicText(text=delta.insert)

            else:
                assert False, f"Unknown attributes: {delta.attributes}"

    # Each sentence is on its own paragraph
    section = renderable.Section(paragraphs=[
        renderable.Paragraph(sentences=[renderable.Sentence(tokens=list(adapt_sentence(deltas)))])
        for sentences_deltas in split_deltas_into_paragraphs_and_sentences(deltas, r"\s*\n\s*\n\s*")
        for deltas in sentences_deltas
    ])

    strip_section(section)

    return section


def adapt_wording(instructions_deltas, wording_deltas: list[exercise_delta.TextInsertOp], effects: list[AdaptationEffect]):
    global_placeholders: list[tuple[str, renderable.SentenceToken]] = []
    words_are_selectable = False
    punctuation_is_selectable = False
    selectables_colors = []
    selectables_are_boxed = False

    for effect in effects:
        if isinstance(effect, FillWithFreeTextAdaptationEffect):
            global_placeholders.append((effect.placeholder, renderable.FreeTextInput()))
        if isinstance(effect, ItemizedAdaptationEffect):
            words_are_selectable = effect.items.kind == "words"
            punctuation_is_selectable = words_are_selectable and effect.items.punctuation
            if effect.effects.selectable is not None:
                selectables_colors = effect.effects.selectable.colors
                selectables_are_boxed = effect.effects.boxed

    for (start, separator1, separator2, stop, placeholder, text) in gather_choices(instructions_deltas):
        if placeholder != "":
            global_placeholders.append((placeholder, renderable.MultipleChoicesInput(choices=_separate_choices(start, separator1, separator2, stop, placeholder, text))))

    for delta in wording_deltas:
        if delta.attributes == {}:
            for index, (placeholder, _token) in enumerate(global_placeholders):
                delta.insert = delta.insert.replace(placeholder, f"ph{index}hp")

    def adapt_sentence(sentence_deltas: list[exercise_delta.TextInsertOp]):
        sentence_specific_placeholders = []

        for (start, separator1, separator2, stop, placeholder, text) in gather_choices(sentence_deltas):
            if placeholder != "":
                sentence_specific_placeholders.append((placeholder, renderable.MultipleChoicesInput(choices=_separate_choices(start, separator1, separator2, stop, placeholder, text))))

        for delta in sentence_deltas:
            if delta.attributes == {}:
                for index, (placeholder, _token) in enumerate(sentence_specific_placeholders):
                    delta.insert = delta.insert.replace(placeholder, f"ph{len(global_placeholders) + index}hp")

        sentence_placeholders = list(itertools.chain(global_placeholders, sentence_specific_placeholders))

        for delta in sentence_deltas:
            if delta.attributes == {}:
                for i, text in enumerate(re.split(r"(\.\.\.|\s+|\W|ph\d+hp)", delta.insert)):
                    if text != "":
                        if i % 2 == 1:
                            # Separator: punctuation, spacing, placeholders
                            if text.strip() == "":
                                yield renderable.Whitespace()
                            elif text.startswith("ph") and text.endswith("hp"):
                                index = int(text[2:-2])
                                yield sentence_placeholders[index][1]
                            else:
                                if punctuation_is_selectable:
                                    yield renderable.SelectableText(text=text, colors=selectables_colors, boxed=selectables_are_boxed)
                                else:
                                    yield renderable.PlainText(text=text)
                        else:
                            # Separated: words
                            if words_are_selectable:
                                yield renderable.SelectableText(text=text, colors=selectables_colors, boxed=selectables_are_boxed)
                            else:
                                yield renderable.PlainText(text=text)

            elif "selectable" in delta.attributes:
                assert delta.attributes == {"selectable": delta.attributes["selectable"]}

                for text in re.split(r"(\.\.\.|\s+|\W)", delta.insert):
                    if text != "":
                        if text.strip() == "":
                            yield renderable.Whitespace()
                        else:
                            yield renderable.SelectableText(text=text, colors=selectables_colors, boxed=selectables_are_boxed)

            elif "bold" in delta.attributes:
                assert delta.attributes == {"bold": delta.attributes["bold"]}

                yield renderable.BoldText(text=delta.insert)

            elif "italic" in delta.attributes:
                assert delta.attributes == {"italic": delta.attributes["italic"]}

                yield renderable.ItalicText(text=delta.insert)

            elif "choices2" in delta.attributes:
                assert delta.attributes == {"choices2": delta.attributes["choices2"]}

                choices_settings = delta.attributes["choices2"]
                placeholder = choices_settings["placeholder"] or None
                if placeholder is None:
                    start = choices_settings["start"] or None
                    separator1 = choices_settings["separator1"] or None
                    separator2 = choices_settings["separator2"] or None
                    stop = choices_settings["stop"] or None
                    yield renderable.MultipleChoicesInput(choices=_separate_choices(start, separator1, separator2, stop, placeholder, delta.insert))

            else:
                assert False, f"Unknown attributes: {delta.attributes}"

    # Paragraph are preserved
    section = renderable.Section(paragraphs=[
        renderable.Paragraph(sentences=[
            renderable.Sentence(tokens=list(adapt_sentence(deltas)))
            for deltas in sentences_deltas
        ])
        for sentences_deltas in split_deltas_into_paragraphs_and_sentences(wording_deltas, r"\s*\n\s*")
    ])

    strip_section(section)

    return section


class _Parser:
    def __init__(self, tags, whitespace):
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
                STR: /(\\\\|\\{|\\\||\\}|[^\\{|}])+/
                INT: /[0-9]+/
            """
            + whitespace
            + f"_tag.1: {' | '.join(f"{tag}_tag" for tag in tags.keys())}\n"
            + "\n".join(f'{tag}_tag: "{{" "{tag.replace("_", "-")}" {definition} "}}"' for (tag, definition) in tags.items())
        )
        self.lark = lark.Lark(grammar, start="section")

    def parse(self, text):
        assert text.endswith("\n")
        return self.lark.parse(text)


_instructions_parser = _Parser(
    dict(
        bold = r""" "|" STR """,
        italic = r""" "|" STR """,
        choices2 = r""" "|" [STR] "|" [STR] "|" [STR] "|" [STR] "|" [STR] "|" STR """,
        sel1 = r""" "|" STR """,
        sel2 = r""" "|" STR """,
        sel3 = r""" "|" STR """,
        sel4 = r""" "|" STR """,
        sel5 = r""" "|" STR """,
    ),
    r"""
        PARAGRAPH_SEPARATING_WHITESPACE: /([ \t]*(\r\n|\n)){2,}[ \t]*/
        NON_PARAGRAPH_SEPARATING_WHITESPACE: /([ \t]*(\r\n|\r|\n)[ \t]*)|[ \t]+/
    """,
)


_example_and_clue_parser = _Parser(
    dict(
        bold = r""" "|" STR """,
        italic = r""" "|" STR """,
        sel1 = r""" "|" STR """,
        sel2 = r""" "|" STR """,
        sel3 = r""" "|" STR """,
        sel4 = r""" "|" STR """,
        sel5 = r""" "|" STR """,
    ),
    r"""
        PARAGRAPH_SEPARATING_WHITESPACE: /([ \t]*(\r\n|\n)){2,}[ \t]*/
        NON_PARAGRAPH_SEPARATING_WHITESPACE: /([ \t]*(\r\n|\r|\n)[ \t]*)|[ \t]+/
    """,
)


_wording_parser = _Parser(
    dict(
        bold = r""" "|" STR """,
        italic = r""" "|" STR """,
        fill_with_free_text = r""" "|" STR """,
        choices2 = r""" "|" [STR] "|" [STR] "|" [STR] "|" [STR] "|" [STR] "|" STR """,
        placeholder2 = r""" "|" STR""",
        selectable = r""" "|" STR """,
    ),
    r"""
        PARAGRAPH_SEPARATING_WHITESPACE: /([ \t]*(\r\n|\n))+[ \t]*/
        NON_PARAGRAPH_SEPARATING_WHITESPACE: /[ \t]+/
    """,
)


class ParserTestCase(unittest.TestCase):
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

    def do_base_test(self, test, expected_ast):
        parse_tree = self.parser.parse(test)
        actual_ast = self.Transformer().transform(parse_tree)
        if actual_ast != expected_ast:
            print("Actual AST:", actual_ast)
        self.assertEqual(actual_ast, expected_ast)

        return parse_tree


class InstructionsParserTestCase(ParserTestCase):
    parser = _instructions_parser

    def do_test(self, test, expected_ast):
        self.do_base_test(test, expected_ast)
        parse_tree = self.do_base_test(test, expected_ast)

        deltas = DeltaMaker().transform(parse_tree)
        expected_adapted = InstructionsAdapter().transform(parse_tree)
        actual_adapted = adapt_instructions(deltas, [])
        if actual_adapted != expected_adapted:
            print("\nDeltas:", deltas)
            print("Tree:", parse_tree.pretty())
            print("Expected adapted:", expected_adapted)
            print("Actual adapted  :", actual_adapted)
        self.assertEqual(actual_adapted, expected_adapted)

    def test_empty(self):
        self.do_test("\n", ("section", [("LEADING_WHITESPACE", "\n")]))

    def test_only_whitespace(self):
        self.do_test("    \t\n\n \t  \r\n\n\n    \n", ("section", [("LEADING_WHITESPACE", "    \t\n\n \t  \r\n\n\n    \n")]))

    def test_simple_strict_paragraphs(self):
        self.do_test(
            "First sentence. Second sentence.\n\nThird sentence.\n\nFourth sentence.\n",
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
                ('TRAILING_WHITESPACE', '\n'),
            ]),
        )

    def test_punctuation_at_end_of_sentence(self):
        for punctuation in [".", "!", "?", "…", "..."]:
            with self.subTest(punctuation=punctuation):
                self.do_test(
                    f"Strict sentence{punctuation}\n",
                    ("section", [
                        ("strict_paragraph", [("sentence", [("WORD", "Strict"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", punctuation)])]),
                        ('TRAILING_WHITESPACE', '\n'),
                    ]),
                )

    def test_punctuation_in_sentence(self):
        for punctuation in [",", ";", ":", "-", "–"]:
            with self.subTest(punctuation=punctuation):
                self.do_test(
                    f"Strict{punctuation} sentence.\n",
                    ("section", [
                        ("strict_paragraph", [("sentence", [
                            ("WORD", "Strict"), ("PUNCTUATION_IN_SENTENCE", punctuation), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", "."),
                        ])]),
                        ('TRAILING_WHITESPACE', '\n'),
                    ]),
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
                    f"Strict{whitespace}sentence.\n",
                    ("section", [
                        ("strict_paragraph", [("sentence", [("WORD", "Strict"), ("WHITESPACE_IN_SENTENCE", whitespace), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")])]),
                        ('TRAILING_WHITESPACE', '\n'),
                    ]),
                )

    def test_leading_and_trailing_space(self):
        self.do_test(
            "    \t\n\n \t  \r\n\n\n    Strict sentence.    \t\n\n \t  \r\n\n\n    \n",
            ("section", [
                ("LEADING_WHITESPACE", "    \t\n\n \t  \r\n\n\n    "),
                ("strict_paragraph", [
                    ("sentence", [("WORD", "Strict"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")]),
                ]),
                ("TRAILING_WHITESPACE", "    \t\n\n \t  \r\n\n\n    \n"),
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
                    "First sentence." + separator + "Second sentence.\n",
                    ("section", [
                        ("strict_paragraph", [
                            ("sentence", [("WORD", "First"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")]),
                        ]),
                        ("PARAGRAPH_SEPARATOR", separator),
                        ("strict_paragraph", [
                            ("sentence", [("WORD", "Second"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")]),
                        ]),
                        ('TRAILING_WHITESPACE', '\n'),
                    ]),
                )

    sentence_separators = whitespaces_in_sentence

    def test_sentence_separator(self):
        for separator in self.sentence_separators:
            with self.subTest(separator=separator):
                self.do_test(
                    "First sentence." + separator + "Second sentence.\n",
                    ("section", [
                        ("strict_paragraph", [
                            ("sentence", [("WORD", "First"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")]),
                            ("SENTENCE_SEPARATOR", separator),
                            ("sentence", [("WORD", "Second"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")]),
                        ]),
                        ('TRAILING_WHITESPACE', '\n'),
                    ]),
                )

    def test_simple_lenient_paragraphs(self):
        self.do_test(
            "First # sentence. Second # sentence.\n\nThird # sentence.\n\nFourth # sentence.\n",
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
                ('TRAILING_WHITESPACE', '\n'),
            ]),
        )

    def test_lenient_paragraph_separator(self):
        for separator in self.paragraph_separators:
            with self.subTest(separator=separator):
                self.do_test(
                    "First #." + separator + "Second #.\n",
                    ("section", [
                        ("lenient_paragraph", [
                            ("WORD", "First"), ("WHITESPACE_IN_SENTENCE", " "), ("PUNCTUATION_IN_LENIENT_PARAGRAPH", "#"), ("PUNCTUATION_IN_LENIENT_PARAGRAPH", "."),
                        ]),
                        ("PARAGRAPH_SEPARATOR", separator),
                        ("lenient_paragraph", [
                            ("WORD", "Second"), ("WHITESPACE_IN_SENTENCE", " "), ("PUNCTUATION_IN_LENIENT_PARAGRAPH", "#"), ("PUNCTUATION_IN_LENIENT_PARAGRAPH", "."),
                        ]),
                        ('TRAILING_WHITESPACE', '\n'),
                    ]),
                )

    def test_exotic_characters(self):
        self.do_test(
            "Straße 120 àéïîöôù\n",
            ("section", [
                ("lenient_paragraph", [
                    ("WORD", "Straße"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "120"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "àéïîöôù"),
                ]),
                ('TRAILING_WHITESPACE', '\n'),
            ]),
        )


class WordingParserTestCase(ParserTestCase):
    parser = _wording_parser

    def do_test(self, test, expected_ast):
        self.do_base_test(test, expected_ast)
        parse_tree = self.do_base_test(test, expected_ast)

        deltas = DeltaMaker().transform(parse_tree)
        expected_adapted = WordingAdapter().transform(parse_tree)
        actual_adapted = adapt_wording([], deltas, [])
        if actual_adapted != expected_adapted:
            print("\nDeltas:", deltas)
            print("Tree:", parse_tree.pretty())
            print("Expected adapted:", expected_adapted)
            print("Actual adapted  :", actual_adapted)
        self.assertEqual(actual_adapted, expected_adapted)

    def test_empty(self):
        self.do_test("\n", ("section", [("LEADING_WHITESPACE", "\n")]))

    def test_only_whitespace(self):
        self.do_test("    \t\n\n \t  \r\n\n\n    \n", ("section", [("LEADING_WHITESPACE", "    \t\n\n \t  \r\n\n\n    \n")]))

    def test_simple_strict_paragraphs(self):
        self.do_test(
            "First sentence. Second sentence.\nThird sentence.\nFourth sentence.\n",
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
                ("TRAILING_WHITESPACE", "\n"),
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
                    f"Strict{whitespace}sentence.\n",
                    ("section", [
                        ("strict_paragraph", [("sentence", [("WORD", "Strict"), ("WHITESPACE_IN_SENTENCE", whitespace), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")])]),
                        ("TRAILING_WHITESPACE", "\n"),
                    ]),
                )

    def test_leading_and_trailing_space(self):
        self.do_test(
            "    \t\n\n \t  \r\n\n\n    Strict sentence.    \t\n\n \t  \r\n\n\n    \n",
            ("section", [
                ("LEADING_WHITESPACE", "    \t\n\n \t  \r\n\n\n    "),
                ("strict_paragraph", [
                    ("sentence", [("WORD", "Strict"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")]),
                ]),
                ("TRAILING_WHITESPACE", "    \t\n\n \t  \r\n\n\n    \n"),
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
                    "First sentence." + separator + "Second sentence.\n",
                    ("section", [
                        ("strict_paragraph", [
                            ("sentence", [("WORD", "First"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")]),
                        ]),
                        ("PARAGRAPH_SEPARATOR", separator),
                        ("strict_paragraph", [
                            ("sentence", [("WORD", "Second"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")]),
                        ]),
                        ("TRAILING_WHITESPACE", "\n"),
                    ]),
                )

    sentence_separators = whitespaces_in_sentence

    def test_sentence_separator(self):
        for separator in self.sentence_separators:
            with self.subTest(separator=separator):
                self.do_test(
                    "First sentence." + separator + "Second sentence.\n",
                    ("section", [
                        ("strict_paragraph", [
                            ("sentence", [("WORD", "First"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")]),
                            ("SENTENCE_SEPARATOR", separator),
                            ("sentence", [("WORD", "Second"), ("WHITESPACE_IN_SENTENCE", " "), ("WORD", "sentence"), ("PUNCTUATION_AT_END_OF_SENTENCE", ".")]),
                        ]),
                        ("TRAILING_WHITESPACE", "\n"),
                    ]),
                )

    def test_lenient_paragraph_separator(self):
        for separator in self.paragraph_separators:
            with self.subTest(separator=separator):
                self.do_test(
                    "First #." + separator + "Second #.\n",
                    ("section", [
                        ("lenient_paragraph", [
                            ("WORD", "First"), ("WHITESPACE_IN_SENTENCE", " "), ("PUNCTUATION_IN_LENIENT_PARAGRAPH", "#"), ("PUNCTUATION_IN_LENIENT_PARAGRAPH", "."),
                        ]),
                        ("PARAGRAPH_SEPARATOR", separator),
                        ("lenient_paragraph", [
                            ("WORD", "Second"), ("WHITESPACE_IN_SENTENCE", " "), ("PUNCTUATION_IN_LENIENT_PARAGRAPH", "#"), ("PUNCTUATION_IN_LENIENT_PARAGRAPH", "."),
                        ]),
                        ("TRAILING_WHITESPACE", "\n"),
                    ]),
                )


class DeltaMaker(lark.Transformer):
    def _merge(self, args):
        def join_group(key, items):
            items = list(items)
            if len(items) == 1:
                return items[0]
            else:
                assert key is not None
                assert all(isinstance(item.insert, str) for item in items)
                return exercise_delta.TextInsertOp(
                    insert="".join(item.insert for item in items),
                    attributes=key,
                )

        def key(arg):
            if not hasattr(arg, "insert"):
                print(arg)
            if isinstance(arg.insert, str):
                return arg.attributes
            else:
                assert isinstance(arg.insert, dict)
                return arg.insert

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
        return arg.value.replace(r"\\", "\\").replace(r"\{", "{").replace(r"\}", "}").replace(r"\|", "|")

    def bold_tag(self, args):
        assert len(args) == 1
        return exercise_delta.TextInsertOp(insert=args[0], attributes={"bold": True})

    def italic_tag(self, args):
        assert len(args) == 1
        return exercise_delta.TextInsertOp(insert=args[0], attributes={"italic": True})

    def choices2_tag(self, args):
        assert len(args) == 6
        (start, separator1, separator2, stop, placeholder, text) = args
        if start is None:
            start = ""
        if separator1 is None:
            separator1 = ""
        if separator2 is None:
            separator2 = ""
        if stop is None:
            stop = ""
        if placeholder is None:
            placeholder = ""
        return exercise_delta.TextInsertOp(
            insert=text,
            attributes={
                "choices2": {
                    "start": start,
                    "separator1": separator1,
                    "separator2": separator2,
                    "stop": stop,
                    "placeholder": placeholder,
                },
            },
        )

    def selectable_tag(self, args):
        assert len(args) == 1
        return exercise_delta.TextInsertOp(insert=args[0], attributes={"selectable": True})

    def fill_with_free_text_tag(self, args):
        assert len(args) == 1
        return exercise_delta.TextInsertOp(insert=args[0], attributes={})

    def placeholder2_tag(self, args):
        assert len(args) == 1
        return exercise_delta.TextInsertOp(insert=args[0], attributes={})

    def sel1_tag(self, args):
        return exercise_delta.TextInsertOp(insert=args[0], attributes={"sel": 1})

    def sel2_tag(self, args):
        return exercise_delta.TextInsertOp(insert=args[0], attributes={"sel": 2})

    def sel3_tag(self, args):
        return exercise_delta.TextInsertOp(insert=args[0], attributes={"sel": 3})

    def sel4_tag(self, args):
        return exercise_delta.TextInsertOp(insert=args[0], attributes={"sel": 4})

    def sel5_tag(self, args):
        return exercise_delta.TextInsertOp(insert=args[0], attributes={"sel": 5})


class ChoicesGatherer(lark.Transformer):
    def section(self, args):
        return list(itertools.chain(*args))

    def strict_paragraph(self, args):
        return list(itertools.chain(*args))

    def sentence(self, args):
        return list(itertools.chain(*args))

    def lenient_paragraph(self, args):
        return list(itertools.chain(*args))

    def choices2_tag(self, args):
        assert len(args) == 6
        if args[4] is None:
            return []
        else:
            return [args]

    def sel1_tag(self, args):
        return []

    def sel2_tag(self, args):
        return []

    def sel3_tag(self, args):
        return []

    def sel4_tag(self, args):
        return []

    def sel5_tag(self, args):
        return []

    def WORD(self, arg):
        return []

    def LEADING_WHITESPACE(self, arg):
        return []

    def TRAILING_WHITESPACE(self, arg):
        return []

    def PARAGRAPH_SEPARATOR(self, arg):
        return []

    def SENTENCE_SEPARATOR(self, arg):
        return []

    def WHITESPACE_IN_SENTENCE(self, arg):
        return []

    def PUNCTUATION_IN_SENTENCE(self, arg):
        return []

    def PUNCTUATION_AT_END_OF_SENTENCE(self, arg):
        return []

    def PUNCTUATION_IN_LENIENT_PARAGRAPH(self, arg):
        return []

    def INT(self, arg):
        return None

    def STR(self, arg):
        return arg.value

    def bold_tag(self, args):
        return []

    def italic_tag(self, args):
        return []


class InstructionsAdapter(lark.Transformer):
    def __init__(self, *, selection_colors: list[str]=[]):
        super().__init__()
        self.selection_colors = selection_colors

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
        args = list(itertools.chain.from_iterable(args))
        return renderable.Sentence(tokens=args)

    def lenient_paragraph(self, args):
        args = list(itertools.chain.from_iterable(args))
        return renderable.Paragraph(sentences=[renderable.Sentence(tokens=args)])

    def WORD(self, arg):
        return [renderable.PlainText(text=arg.value)]

    def LEADING_WHITESPACE(self, arg):
        return None

    def TRAILING_WHITESPACE(self, arg):
        return None

    def PARAGRAPH_SEPARATOR(self, arg):
        return None

    def SENTENCE_SEPARATOR(self, arg):
        return None

    def WHITESPACE_IN_SENTENCE(self, arg):
        return [renderable.Whitespace()]

    def PUNCTUATION_IN_SENTENCE(self, arg):
        return [renderable.PlainText(text=arg.value)]

    def PUNCTUATION_AT_END_OF_SENTENCE(self, arg):
        return [renderable.PlainText(text=arg.value)]

    def PUNCTUATION_IN_LENIENT_PARAGRAPH(self, arg):
        return [renderable.PlainText(text=arg.value)]

    def INT(self, arg):
        return int(arg.value)

    def STR(self, arg):
        return arg.value.replace(r"\\", "\\").replace(r"\{", "{").replace(r"\}", "}").replace(r"\|", "|")

    def bold_tag(self, args):
        assert len(args) == 1
        return [renderable.BoldText(text=args[0])]

    def italic_tag(self, args):
        assert len(args) == 1
        return [renderable.ItalicText(text=args[0])]

    def choices2_tag(self, args):
        assert len(args) == 6
        (start, separator1, separator2, stop, placeholder, text) = args
        add_start_and_stop = start is not None and stop is not None and text.startswith(start) and text.endswith(stop)
        choices = _separate_choices(start, separator1, separator2, stop, placeholder, text)
        ret = []
        if add_start_and_stop:
            ret.append(renderable.PlainText(text=start))
        ret.append(renderable.BoxedText(text=choices[0]))
        if separator2 is None:
            for choice in choices[1:]:
                ret.append(renderable.Whitespace())
                ret.append(renderable.PlainText(text=separator1))
                ret.append(renderable.Whitespace())
                ret.append(renderable.BoxedText(text=choice))
        else:
            for choice in choices[1:-1]:
                ret.append(renderable.PlainText(text=separator1))
                ret.append(renderable.Whitespace())
                ret.append(renderable.BoxedText(text=choice))
            ret.append(renderable.Whitespace())
            ret.append(renderable.PlainText(text=separator2))
            ret.append(renderable.Whitespace())
            ret.append(renderable.BoxedText(text=choices[-1]))
        if add_start_and_stop:
            ret.append(renderable.PlainText(text=stop))
        return ret

    def sel1_tag(self, args):
        if len(self.selection_colors) > 0:
            return [renderable.SelectedText(text=args[0], color=self.selection_colors[0])]
        else:
            return [renderable.PlainText(text=args[0])]

    def sel2_tag(self, args):
        if len(self.selection_colors) > 1:
            return [renderable.SelectedText(text=args[0], color=self.selection_colors[1])]
        else:
            return [renderable.PlainText(text=args[0])]

    def sel3_tag(self, args):
        if len(self.selection_colors) > 2:
            return [renderable.SelectedText(text=args[0], color=self.selection_colors[2])]
        else:
            return [renderable.PlainText(text=args[0])]

    def sel4_tag(self, args):
        if len(self.selection_colors) > 3:
            return [renderable.SelectedText(text=args[0], color=self.selection_colors[3])]
        else:
            return [renderable.PlainText(text=args[0])]

    def sel5_tag(self, args):
        if len(self.selection_colors) > 4:
            return [renderable.SelectedText(text=args[0], color=self.selection_colors[4])]
        else:
            return [renderable.PlainText(text=args[0])]


class WordingAdapter(lark.Transformer):
    def __init__(
        self,
        *,
        select_words: bool=False,
        select_punctuation: bool=False,
        selection_colors: list[str]=[],
        selectable_are_boxed: bool=False,
        multiple_choices: dict[str, list[str]]={},
    ):
        super().__init__()
        self.select_words = select_words
        self.select_punctuation = select_punctuation
        self.selection_colors = selection_colors
        self.selectable_are_boxed = selectable_are_boxed
        self.multiple_choices = multiple_choices

    def _make_sentence(self, tokens):
        placeholder_indexes_by_placeholder = {}
        input_index_by_placeholder = {}
        new_tokens = []
        for token in tokens:
            if isinstance(token, tuple):
                if token[0] == "placeholder":
                    placeholder_indexes_by_placeholder.setdefault(token[1], []).append(len(new_tokens))
                else:
                    assert token[0] == "input"
                    input_index_by_placeholder[token[1]] = len(new_tokens)
            new_tokens.append(token)
        for placeholder in set(itertools.chain(placeholder_indexes_by_placeholder.keys(), input_index_by_placeholder.keys())):
            placeholder_indexes = placeholder_indexes_by_placeholder.get(placeholder)
            input_index = input_index_by_placeholder.get(placeholder)
            if placeholder_indexes is None:
                if input_index is None:
                    assert False
                else:
                    new_tokens[input_index] = new_tokens[input_index][2]
            else:
                if input_index is None:
                    for placeholder_index in placeholder_indexes:
                        choices = self.multiple_choices.get(new_tokens[placeholder_index][1])
                        if choices is None:
                            new_tokens[placeholder_index] = renderable.PlainText(text=new_tokens[placeholder_index][1])
                        else:
                            new_tokens[placeholder_index] = renderable.MultipleChoicesInput(choices=choices)
                else:
                    for placeholder_index in placeholder_indexes:
                        new_tokens[placeholder_index] = new_tokens[input_index][2]
                    new_tokens[input_index] = None
        new_tokens = list(filter(None, new_tokens))
        while new_tokens[0].type == "whitespace":
            del new_tokens[0]
        while new_tokens[-1].type == "whitespace":
            del new_tokens[-1]
        for i in range(len(new_tokens) - 1):
            if new_tokens[i].type == "whitespace" and new_tokens[i + 1].type == "whitespace":
                new_tokens[i] = None
        new_tokens = list(filter(None, new_tokens))
        return renderable.Sentence(tokens=new_tokens)

    def section(self, args):
        paragraphs = list(filter(None, args))
        return renderable.Section(paragraphs=paragraphs)

    def strict_paragraph(self, args):
        sentences = list(filter(None, args))
        return renderable.Paragraph(sentences=sentences)

    def sentence(self, args):
        return self._make_sentence(args)

    def lenient_paragraph(self, args):
        return renderable.Paragraph(sentences=[self._make_sentence(args)])

    def WORD(self, arg):
        if self.select_words:
            return renderable.SelectableText(text=arg.value, colors=self.selection_colors, boxed=self.selectable_are_boxed)
        else:
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
        if self.select_punctuation:
            return renderable.SelectableText(text=arg.value, colors=self.selection_colors, boxed=self.selectable_are_boxed)
        else:
            return renderable.PlainText(text=arg.value)

    def PUNCTUATION_AT_END_OF_SENTENCE(self, arg):
        if self.select_punctuation:
            return renderable.SelectableText(text=arg.value, colors=self.selection_colors, boxed=self.selectable_are_boxed)
        else:
            return renderable.PlainText(text=arg.value)

    def PUNCTUATION_IN_LENIENT_PARAGRAPH(self, arg):
        if self.select_punctuation:
            return renderable.SelectableText(text=arg.value, colors=self.selection_colors, boxed=self.selectable_are_boxed)
        else:
            return renderable.PlainText(text=arg.value)

    def INT(self, arg):
        return int(arg.value)

    def STR(self, arg):
        return arg.value.replace(r"\\", "\\").replace(r"\{", "{").replace(r"\}", "}").replace(r"\|", "|")

    def bold_tag(self, args):
        assert len(args) == 1
        return renderable.BoldText(text=args[0])

    def italic_tag(self, args):
        assert len(args) == 1
        return renderable.ItalicText(text=args[0])

    def fill_with_free_text_tag(self, args):
        assert len(args) == 1
        return renderable.FreeTextInput()

    def placeholder2_tag(self, args):
        assert len(args) == 1
        return ("placeholder", args[0])

    def choices2_tag(self, args):
        assert len(args) == 6
        (start, separator1, separator2, stop, placeholder, text) = args
        choices = _separate_choices(start, separator1, separator2, stop, placeholder, text)
        input = renderable.MultipleChoicesInput(choices=choices)
        if placeholder is None:
            return input
        else:
            return ("input", placeholder, input)

    def selectable_tag(self, args):
        assert len(args) == 1
        return renderable.SelectableText(text=args[0], colors=self.selection_colors, boxed=self.selectable_are_boxed)


def _separate_choices(start, separator1, separator2, stop, placeholder, text):
    text = text.strip()
    if start is not None and stop is not None and text.startswith(start) and text.endswith(stop):
        text = text[len(start) : -len(stop)]
    if separator1 is None:
        choices = [text]
    else:
        choices = text.split(separator1)
    if separator2 is not None:
        choices[-1:] = choices[-1].split(separator2)
    return list(filter(lambda c: c != "", [choice.strip() for choice in choices]))


class EffectsBasedAdapterAndDeltaMaker:
    def __init__(
        self,
        global_effects: list[AdaptationEffect],
        instructions_text: str,
        instructions_deltas: list[exercise_delta.TextInsertOp],
        wording_text: str,
        wording_deltas: list[exercise_delta.TextInsertOp],
        example_text: str,
        example_deltas: list[exercise_delta.TextInsertOp],
        clue_text: str,
        clue_deltas: list[exercise_delta.TextInsertOp],
    ):
        assert DeltaMaker().transform(_instructions_parser.parse(instructions_text)) == instructions_deltas
        assert DeltaMaker().transform(_wording_parser.parse(wording_text)) == wording_deltas
        assert DeltaMaker().transform(_example_and_clue_parser.parse(example_text)) == example_deltas
        assert DeltaMaker().transform(_example_and_clue_parser.parse(clue_text)) == clue_deltas

        for effect in global_effects:
            (instructions_text, wording_text, example_text, clue_text) = effect.preprocess(instructions_text, wording_text, example_text, clue_text)
        (instructions_text, wording_text, example_text, clue_text) = self.preprocess(instructions_text, instructions_deltas, wording_text, wording_deltas, example_text, clue_text)

        instructions_adapter_constructor_kwds = {}
        wording_adapter_constructor_kwds = {}
        example_adapter_constructor_kwds = {}
        clue_adapter_constructor_kwds = {}
        for effect in global_effects:
            instructions_adapter_constructor_kwds.update(effect.make_instructions_adapter_constructor_kwds())
            wording_adapter_constructor_kwds.update(effect.make_wording_adapter_constructor_kwds())
            example_adapter_constructor_kwds.update(effect.make_example_adapter_constructor_kwds())
            clue_adapter_constructor_kwds.update(effect.make_clue_adapter_constructor_kwds())
        wording_adapter_constructor_kwds.update(self.make_wording_adapter_constructor_kwds(instructions_text, instructions_deltas))

        instructions_tree = _instructions_parser.parse(instructions_text)
        wording_tree = _wording_parser.parse(wording_text)
        example_tree = _example_and_clue_parser.parse(example_text)
        clue_tree = _example_and_clue_parser.parse(clue_text)

        assert DeltaMaker().transform(instructions_tree) == instructions_deltas
        assert DeltaMaker().transform(wording_tree) == wording_deltas
        assert DeltaMaker().transform(example_tree) == example_deltas
        assert DeltaMaker().transform(clue_tree) == clue_deltas

        self.adapted_instructions = adapt_instructions(instructions_deltas, global_effects)
        expected_adapted_instructions = InstructionsAdapter(**instructions_adapter_constructor_kwds).transform(instructions_tree)
        if self.adapted_instructions != expected_adapted_instructions:
            print("Instructions deltas:", instructions_deltas)
            print("Instructions Tree: ", instructions_tree.pretty())
            print("Global effects:", global_effects)
            print("Instructions adaptation keywords:", instructions_adapter_constructor_kwds)
            print("Expected adapted instructions:", expected_adapted_instructions)
            print("Actual adapted instructions  :", self.adapted_instructions)
            assert False

        self.adapted_wording = adapt_wording(instructions_deltas, wording_deltas, global_effects)
        # self.adapted_wording = WordingAdapter(**wording_adapter_constructor_kwds).transform(wording_tree)
        expected_adapted_wording = WordingAdapter(**wording_adapter_constructor_kwds).transform(wording_tree)
        if self.adapted_wording != expected_adapted_wording:
            print("Instructions deltas:", instructions_deltas)
            print("Wording deltas:", wording_deltas)
            print("Wording tree: ", wording_tree.pretty())
            print("Global effects:", global_effects)
            print("Wording adaptation keywords:", wording_adapter_constructor_kwds)
            print("Expected adapted wording:", expected_adapted_wording)
            print("Actual adapted wording  :", self.adapted_wording)
            assert False

        self.adapted_example = adapt_instructions(example_deltas, global_effects)
        expected_adapted_example = InstructionsAdapter(**example_adapter_constructor_kwds).transform(example_tree)
        if self.adapted_example != expected_adapted_example:
            print("Example deltas:", example_deltas)
            print("Example tree: ", example_tree.pretty())
            print("Global effects:", global_effects)
            print("Example adaptation keywords:", example_adapter_constructor_kwds)
            print("Expected adapted example:", expected_adapted_example)
            print("Actual adapted example  :", self.adapted_example)
            assert False

        self.adapted_clue = adapt_instructions(clue_deltas, global_effects)
        expected_adapted_clue = InstructionsAdapter(**clue_adapter_constructor_kwds).transform(clue_tree)
        if self.adapted_clue != expected_adapted_clue:
            print("Clue deltas:", clue_deltas)
            print("Clue Tree: ", clue_tree.pretty())
            print("Global effects:", global_effects)
            print("Clue adaptation keywords:", clue_adapter_constructor_kwds)
            print("Expected adapted clue:", expected_adapted_clue)
            print("Actual adapted clue  :", self.adapted_clue)
            assert False

    def preprocess(self, instructions_text, instructions_deltas, wording_text, wording_deltas, example_text, clue_text):
        placeholders = set(choice[4] for choice in itertools.chain(gather_choices(instructions_deltas), gather_choices(wording_deltas)))
        for placeholder in placeholders:
            wording_text = wording_text.replace(placeholder, f"{{placeholder2|{placeholder}}}").replace(f"|{{placeholder2|{placeholder}}}|", f"|{placeholder}|")
        return (instructions_text, wording_text, example_text, clue_text)

    def make_wording_adapter_constructor_kwds(self, instructions_text, instructions_deltas):
        multiple_choices = {}
        for (start, separator1, separator2, stop, placeholder, text) in gather_choices(instructions_deltas):
            multiple_choices[placeholder] = _separate_choices(start, separator1, separator2, stop, placeholder, text)
        return {
            "multiple_choices": multiple_choices,
        }
