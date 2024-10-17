import itertools
from typing import ClassVar, Literal
import os

from .. import exercise_delta
from .. import exercise_delta as d
from .. import parsing
from .. import renderable
from .. import renderable as r
from .testing import AdaptationTestCase
from mydantic import PydanticBase

if os.environ.get("GABBY_UNITTESTING", "false") == "true":
    from .. import exercises


class MultipleChoicesInWordingAdaptation(PydanticBase):
    kind: Literal["multiple-choices-in-wording"]

    def make_adapted_instructions(self, exercise):
        return parsing.adapt_plain_instructions_section(exercise.instructions)

    class PlaceholdersGatherer(parsing.Transformer):
        def section(self, args):
            return list(itertools.chain(*args))

        def strict_paragraph(self, args):
            return list(itertools.chain(*args))

        def sentence(self, args):
            return list(itertools.chain(*args))

        def lenient_paragraph(self, args):
            return list(itertools.chain(*args))

        def choices2_tag(self, args):
            assert len(args) == 5
            if args[3] is None:
                return []
            else:
                return [args[3]]

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

    gather_placeholders: ClassVar = parsing.InstructionsSectionParser(
        {
            "choices2": r""" "|" [STR] "|" [STR] "|" [STR] "|" [STR] "|" STR """,
        },
        PlaceholdersGatherer(),
    )

    class WordingAdapter(parsing.WordingSectionAdapter):
        def choices_tag(self, args):
            return renderable.MultipleChoicesInput(choices=[arg for arg in args])

        def sentence(self, args):
            return self._make_sentence(args)

        def lenient_paragraph(self, args):
            return renderable.Paragraph(sentences=[self._make_sentence(args)])

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
                            new_tokens[placeholder_index] = renderable.PlainText(text=new_tokens[placeholder_index][1])
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

        def placeholder2_tag(self, args):
            assert len(args) == 1
            return ("placeholder", args[0])

        def choices2_tag(self, args):
            assert len(args) == 5
            (start, separator, stop, placeholder, text) = args
            text = text.strip()
            if start is not None and stop is not None and text.startswith(start) and text.endswith(stop):
                text = text[len(start) : -len(stop)]
            if separator is None:
                choices = [text]
            else:
                choices = text.split(separator)
            choices = [choice.strip() for choice in choices]
            input = renderable.MultipleChoicesInput(choices=choices)
            if placeholder is None:
                return input
            else:
                return ("input", placeholder, input)

    adapt_wording: ClassVar = parsing.WordingSectionParser(
        {
            "choices": r""" ("|" STR)+ """,
            "choices2": r""" "|" [STR] "|" [STR] "|" [STR] "|" [STR] "|" STR """,
            "placeholder2": r""" "|" STR""",
        },
        WordingAdapter(),
    )

    def make_adapted_wording(self, exercise):
        placeholders = set(self.gather_placeholders(exercise.wording))
        wording = exercise.wording
        for placeholder in placeholders:
            wording = wording.replace(placeholder, f"{{placeholder2|{placeholder}}}").replace(f"|{{placeholder2|{placeholder}}}|", f"|{placeholder}|")
        return self.adapt_wording(wording)

    def make_adapted_example(self, exercise):
        return parsing.adapt_plain_instructions_section(exercise.example)

    def make_adapted_clue(self, exercise):
        return parsing.adapt_plain_instructions_section(exercise.clue)

    def make_instructions_delta(self, exercise):
        return parsing.make_plain_instructions_section_delta(exercise.instructions)

    class WordingDeltaMaker(parsing.WordingSectionDeltaMaker):
        def choices2_tag(self, args):
            assert len(args) == 5
            (start, separator, stop, placeholder, text) = args
            if start is None:
                start = ""
            if separator is None:
                separator = ""
            if stop is None:
                stop = ""
            if placeholder is None:
                placeholder = ""
            return exercise_delta.TextInsertOp(
                insert=text,
                attributes={
                    "choices2": {
                        "start": start,
                        "separator": separator,
                        "stop": stop,
                        "placeholder": placeholder,
                    },
                },
            )

    def make_wording_delta(self, exercise):
        return parsing.WordingSectionParser(
            {
              "choices2": r""" "|" [STR] "|" [STR] "|" [STR] "|" [STR] "|" STR """,
            },
            self.WordingDeltaMaker(),
        )(
            exercise.wording,
        )

    def make_example_delta(self, exercise):
        return parsing.make_plain_instructions_section_delta(exercise.example)

    def make_clue_delta(self, exercise):
        return parsing.make_plain_instructions_section_delta(exercise.clue)


class MultipleChoicesInWordingAdaptationTestCase(AdaptationTestCase):
    def test_simple(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose wisely.",
            wording="A {choices|a|b|c} B {choices|d|e}.",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInWordingAdaptation(kind="multiple-choices-in-wording"),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b", "c"]),
                            r.Whitespace(),
                            r.PlainText(text="B"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["d", "e"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
        )

    def test_choices2_without_placeholder(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose wisely.",
            wording="A {choices2|(|/|)||(blah/blih)}.",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInWordingAdaptation(kind="multiple-choices-in-wording"),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blah", "blih"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="(blah/blih)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator": "/",
                                "stop": ")",
                                "placeholder": "",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=".", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_with_spaces(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose wisely.",
            wording="A {choices2|(|/|)||  (  blah  /  blih  )  }.",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInWordingAdaptation(kind="multiple-choices-in-wording"),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blah", "blih"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="  (  blah  /  blih  )  ",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator": "/",
                                "stop": ")",
                                "placeholder": "",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=".", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_with_empty_start_and_stop(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose wisely.",
            wording="A {choices2||/|||blah/blih}.",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInWordingAdaptation(kind="multiple-choices-in-wording"),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blah", "blih"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="blah/blih",
                        attributes={
                            "choices2": {
                                "start": "",
                                "separator": "/",
                                "stop": "",
                                "placeholder": "",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=".", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_with_empty_separator(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose wisely.",
            wording="A {choices2|||||blah / blih}.",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInWordingAdaptation(kind="multiple-choices-in-wording"),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blah / blih"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="blah / blih",
                        attributes={
                            "choices2": {
                                "start": "",
                                "separator": "",
                                "stop": "",
                                "placeholder": "",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=".", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_with_longer_separators(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose wisely.",
            wording="A {choices2|((|//|))||((blah//blih))}.",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInWordingAdaptation(kind="multiple-choices-in-wording"),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blah", "blih"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="((blah//blih))",
                        attributes={
                            "choices2": {
                                "start": "((",
                                "separator": "//",
                                "stop": "))",
                                "placeholder": "",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=".", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_with_escaped_separators(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose wisely.",
            wording=r"A {choices2|\{|\||\}||\{blah\|blih\}}.",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInWordingAdaptation(kind="multiple-choices-in-wording"),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blah", "blih"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="{blah|blih}",
                        attributes={
                            "choices2": {
                                "start": "{",
                                "separator": "|",
                                "stop": "}",
                                "placeholder": "",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=".", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_with_placeholder_before(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose wisely.",
            wording="The sky is @@. {choices2|(|/|)|@@|(blue/red)} ",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInWordingAdaptation(kind="multiple-choices-in-wording"),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="The"),
                            r.Whitespace(),
                            r.PlainText(text="sky"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blue", "red"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="The sky is @@. ", attributes={}),
                    d.TextInsertOp(
                        insert="(blue/red)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator": "/",
                                "stop": ")",
                                "placeholder": "@@",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=" ", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_with_placeholder_after(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose wisely.",
            wording="{choices2|(|/|)|...|(blue/red)} The sky is ....",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInWordingAdaptation(kind="multiple-choices-in-wording"),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="The"),
                            r.Whitespace(),
                            r.PlainText(text="sky"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blue", "red"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(
                        insert="(blue/red)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator": "/",
                                "stop": ")",
                                "placeholder": "...",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=" The sky is ....", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_choices2_with_two_placeholders(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose wisely.",
            wording="{choices2|(|/|)|...|(blue/yellow)} The sky is ..., the sun is ....",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInWordingAdaptation(kind="multiple-choices-in-wording"),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="The"),
                            r.Whitespace(),
                            r.PlainText(text="sky"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blue", "yellow"]),
                            r.PlainText(text=","),
                            r.Whitespace(),
                            r.PlainText(text="the"),
                            r.Whitespace(),
                            r.PlainText(text="sun"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blue", "yellow"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(
                        insert="(blue/yellow)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator": "/",
                                "stop": ")",
                                "placeholder": "...",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=" The sky is ..., the sun is ....", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_two_choices2_with_matching_placeholders(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose wisely.",
            wording="{choices2|(|/|)|@1|(blue/red)} {choices2|[|*|]|@2|[green*yellow]} The sky is @1, the sun is @2.",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInWordingAdaptation(kind="multiple-choices-in-wording"),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="The"),
                            r.Whitespace(),
                            r.PlainText(text="sky"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blue", "red"]),
                            r.PlainText(text=","),
                            r.Whitespace(),
                            r.PlainText(text="the"),
                            r.Whitespace(),
                            r.PlainText(text="sun"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["green", "yellow"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(
                        insert="(blue/red)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator": "/",
                                "stop": ")",
                                "placeholder": "@1",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(
                        insert="[green*yellow]",
                        attributes={
                            "choices2": {
                                "start": "[",
                                "separator": "*",
                                "stop": "]",
                                "placeholder": "@2",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=" The sky is @1, the sun is @2.", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_two_choices2_with_identical_placeholders(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose wisely.",
            wording="The sky is @@. {choices2|(|/|)|@@|(blue/red)}\n\nThe sun is @@. {choices2|(|/|)|@@|(green/yellow)}",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInWordingAdaptation(kind="multiple-choices-in-wording"),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="The"),
                            r.Whitespace(),
                            r.PlainText(text="sky"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blue", "red"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="The"),
                            r.Whitespace(),
                            r.PlainText(text="sun"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["green", "yellow"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="The sky is @@. ", attributes={}),
                    d.TextInsertOp(
                        insert="(blue/red)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator": "/",
                                "stop": ")",
                                "placeholder": "@@",
                            },
                        },
                    ),
                    d.TextInsertOp(insert="\n\nThe sun is @@. ", attributes={}),
                    d.TextInsertOp(
                        insert="(green/yellow)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator": "/",
                                "stop": ")",
                                "placeholder": "@@",
                            },
                        },
                    ),
                ],
                example=[],
                clue=[],
            ),
        )

    def test_two_choices2_with_spaces_between_them(self):
        exercise = exercises.Exercise(
            number="number",
            textbook_page=42,
            instructions="Choose wisely.",
            wording="The sky is @1, {choices2|(|/|)|@1|(blue/red)} {choices2|[|*|]|@2|[green*yellow]} the sun is @2.",
            example="",
            clue="",
            wording_paragraphs_per_pagelet=3,
            adaptation=MultipleChoicesInWordingAdaptation(kind="multiple-choices-in-wording"),
        )

        self.do_test(
            exercise,
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="The"),
                            r.Whitespace(),
                            r.PlainText(text="sky"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["blue", "red"]),
                            r.PlainText(text=","),
                            r.Whitespace(),
                            r.PlainText(text="the"),
                            r.Whitespace(),
                            r.PlainText(text="sun"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["green", "yellow"]),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose wisely.", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="The sky is @1, ", attributes={}),
                    d.TextInsertOp(
                        insert="(blue/red)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator": "/",
                                "stop": ")",
                                "placeholder": "@1",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(
                        insert="[green*yellow]",
                        attributes={
                            "choices2": {
                                "start": "[",
                                "separator": "*",
                                "stop": "]",
                                "placeholder": "@2",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=" the sun is @2.", attributes={}),
                ],
                example=[],
                clue=[],
            ),
        )
