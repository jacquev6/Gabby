import itertools
import unittest

import lark

from . import deltas


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


instructions_parser = _Parser(
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


example_and_clue_parser = _Parser(
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


wording_parser = _Parser(
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

    def do_test(self, test, expected_ast):
        parse_tree = self.parser.parse(test)
        actual_ast = self.Transformer().transform(parse_tree)
        if actual_ast != expected_ast:
            print("Actual AST:", actual_ast)
        self.assertEqual(actual_ast, expected_ast)


class InstructionsParserTestCase(ParserTestCase):
    parser = instructions_parser

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
    parser = wording_parser

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
                return deltas.InsertOp(
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
        return deltas.InsertOp(insert=arg.value, attributes={})

    def LEADING_WHITESPACE(self, arg):
        return deltas.InsertOp(insert=arg.value, attributes={})

    def TRAILING_WHITESPACE(self, arg):
        return deltas.InsertOp(insert=arg.value, attributes={})

    def PARAGRAPH_SEPARATOR(self, arg):
        return deltas.InsertOp(insert=arg.value, attributes={})

    def SENTENCE_SEPARATOR(self, arg):
        return deltas.InsertOp(insert=arg.value, attributes={})

    def WHITESPACE_IN_SENTENCE(self, arg):
        return deltas.InsertOp(insert=arg.value, attributes={})

    def PUNCTUATION_IN_SENTENCE(self, arg):
        return deltas.InsertOp(insert=arg.value, attributes={})

    def PUNCTUATION_AT_END_OF_SENTENCE(self, arg):
        return deltas.InsertOp(insert=arg.value, attributes={})

    def PUNCTUATION_IN_LENIENT_PARAGRAPH(self, arg):
        return deltas.InsertOp(insert=arg.value, attributes={})

    def INT(self, arg):
        return arg.value

    def STR(self, arg):
        return arg.value.replace(r"\\", "\\").replace(r"\{", "{").replace(r"\}", "}").replace(r"\|", "|")

    def bold_tag(self, args):
        assert len(args) == 1
        return deltas.InsertOp(insert=args[0], attributes={"bold": True})

    def italic_tag(self, args):
        assert len(args) == 1
        return deltas.InsertOp(insert=args[0], attributes={"italic": True})

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
        return deltas.InsertOp(
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
        return deltas.InsertOp(insert=args[0], attributes={"selectable": True})

    def fill_with_free_text_tag(self, args):
        assert len(args) == 1
        return deltas.InsertOp(insert=args[0], attributes={})

    def placeholder2_tag(self, args):
        assert len(args) == 1
        return deltas.InsertOp(insert=args[0], attributes={})

    def sel1_tag(self, args):
        return deltas.InsertOp(insert=args[0], attributes={"sel": 1})

    def sel2_tag(self, args):
        return deltas.InsertOp(insert=args[0], attributes={"sel": 2})

    def sel3_tag(self, args):
        return deltas.InsertOp(insert=args[0], attributes={"sel": 3})

    def sel4_tag(self, args):
        return deltas.InsertOp(insert=args[0], attributes={"sel": 4})

    def sel5_tag(self, args):
        return deltas.InsertOp(insert=args[0], attributes={"sel": 5})
