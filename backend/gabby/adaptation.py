import re
import itertools
import unittest

from . import exercise_delta
from . import exercise_delta as d
from . import exercises as e
from . import renderable
from . import renderable as r
from .api_models import AdaptationV2, AdaptationEffect, FillWithFreeTextAdaptationEffect, ItemizedAdaptationEffect


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
        for sentences_deltas in _split_deltas_into_paragraphs_and_sentences(deltas, r"\s*\n\s*\n\s*")
        for deltas in sentences_deltas
    ])

    _strip_section(section)

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

    for (start, separator1, separator2, stop, placeholder, text) in _gather_choices(instructions_deltas):
        if placeholder != "":
            global_placeholders.append((placeholder, renderable.MultipleChoicesInput(choices=_separate_choices(start, separator1, separator2, stop, placeholder, text))))

    for delta in wording_deltas:
        if delta.attributes == {}:
            for index, (placeholder, _token) in enumerate(global_placeholders):
                delta.insert = delta.insert.replace(placeholder, f"ph{index}hp")

    def adapt_sentence(sentence_deltas: list[exercise_delta.TextInsertOp]):
        sentence_specific_placeholders = []

        for (start, separator1, separator2, stop, placeholder, text) in _gather_choices(sentence_deltas):
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
        for sentences_deltas in _split_deltas_into_paragraphs_and_sentences(wording_deltas, r"\s*\n\s*")
    ])

    _strip_section(section)

    return section


def _split_deltas_into_paragraphs_and_sentences(deltas: list[exercise_delta.TextInsertOp], explicit_paragraph_separator_pattern):
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


def _strip_section(section: renderable.Section):
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


def _gather_choices(deltas):
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


class AdaptationTestCase(unittest.TestCase):
    maxDiff = None

    def do_test(self, exercise, expected_adapted, expected_delta):
        actual_adapted, actual_delta = exercise.make_adapted_and_delta()

        if actual_adapted != expected_adapted:
            print("actual_adapted:", [actual_adapted])

        if actual_delta != expected_delta:
            print("actual_delta:", [actual_delta])

        self.assertEqual(actual_adapted, expected_adapted)
        self.assertEqual(actual_delta, expected_delta)


# Tests in this file follow a legacy organization, based on classes that have been deleted.
# There is some duplication because tests have been kept through refactoring.
# A reorganization would be beneficial, future me!


class FillWithFreeTextAdaptationTestCase(AdaptationTestCase):
    def test_single_sentence(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="instructions\n",
                wording="The wording of this ... is a ... sentence.\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="fill-with-free-text", effects=[FillWithFreeTextAdaptationEffect(kind="fill-with-free-text", placeholder="...")]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="The"),
                            r.Whitespace(),
                            r.PlainText(text="wording"),
                            r.Whitespace(),
                            r.PlainText(text="of"),
                            r.Whitespace(),
                            r.PlainText(text="this"),
                            r.Whitespace(),
                            r.FreeTextInput(),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.PlainText(text="a"),
                            r.Whitespace(),
                            r.FreeTextInput(),
                            r.Whitespace(),
                            r.PlainText(text="sentence"),
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
                    d.TextInsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="The wording of this ... is a ... sentence.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_start_and_end_with_placeholder(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions="instructions\n",
                wording="@ a @\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="fill-with-free-text", effects=[FillWithFreeTextAdaptationEffect(kind="fill-with-free-text", placeholder="@")]),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.FreeTextInput(),
                            r.Whitespace(),
                            r.PlainText(text="a"),
                            r.Whitespace(),
                            r.FreeTextInput(),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="@ a @\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_multiple_lines_in_instructions(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="instructions\nare\n\non\n\nmultiple\nlines\n",
                wording="wording\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="fill-with-free-text", effects=[FillWithFreeTextAdaptationEffect(kind="fill-with-free-text", placeholder="...")]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="instructions"),
                            r.Whitespace(),
                            r.PlainText(text="are"),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="on"),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="multiple"),
                            r.Whitespace(),
                            r.PlainText(text="lines"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="wording"),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="instructions\nare\n\non\n\nmultiple\nlines\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="wording\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_multiple_lines_in_wording(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="instructions\n",
                wording="foo toto : ...\n\nbar : ...\n\nbaz : ...\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="fill-with-free-text", effects=[FillWithFreeTextAdaptationEffect(kind="fill-with-free-text", placeholder="...")]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="foo"),
                            r.Whitespace(),
                            r.PlainText(text="toto"),
                            r.Whitespace(),
                            r.PlainText(text=":"),
                            r.Whitespace(),
                            r.FreeTextInput(),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="bar"),
                            r.Whitespace(),
                            r.PlainText(text=":"),
                            r.Whitespace(),
                            r.FreeTextInput(),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="baz"),
                            r.Whitespace(),
                            r.PlainText(text=":"),
                            r.Whitespace(),
                            r.FreeTextInput(),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="foo toto : ...\n\nbar : ...\n\nbaz : ...\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_unknown_tags(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="{tag|abc}\n",
                wording="{tag|def}\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="fill-with-free-text", effects=[FillWithFreeTextAdaptationEffect(kind="fill-with-free-text", placeholder="...")]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="{"),
                            r.PlainText(text="tag"),
                            r.PlainText(text="|"),
                            r.PlainText(text="abc"),
                            r.PlainText(text="}"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="{"),
                            r.PlainText(text="tag"),
                            r.PlainText(text="|"),
                            r.PlainText(text="def"),
                            r.PlainText(text="}"),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="{tag|abc}\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="{tag|def}\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_strip_whitespace(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="   abc   \n",
                wording="   def   \n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="fill-with-free-text", effects=[FillWithFreeTextAdaptationEffect(kind="fill-with-free-text", placeholder="...")]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="abc"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="def"),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="   abc   \n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="   def   \n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_example_and_clue(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="instructions\n",
                wording="This @ is the wording.\n",
                example="This @ is the example.\n",
                clue="This @ is the clue.\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="fill-with-free-text", effects=[FillWithFreeTextAdaptationEffect(kind="fill-with-free-text", placeholder="@")]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="This"),
                            r.Whitespace(),
                            r.FreeTextInput(),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.PlainText(text="the"),
                            r.Whitespace(),
                            r.PlainText(text="wording"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="This"),
                            r.Whitespace(),
                            r.PlainText(text="@"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.PlainText(text="the"),
                            r.Whitespace(),
                            r.PlainText(text="example"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                clue=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="This"),
                            r.Whitespace(),
                            r.PlainText(text="@"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.PlainText(text="the"),
                            r.Whitespace(),
                            r.PlainText(text="clue"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="This @ is the wording.\n", attributes={}),
                ],
                example=[
                    d.TextInsertOp(insert="This @ is the example.\n", attributes={}),
                ],
                clue=[
                    d.TextInsertOp(insert="This @ is the clue.\n", attributes={}),
                ],
            ),
        )


class ItemizedAdaptationTestCase(AdaptationTestCase):
    def test_selectable_words__plain(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Instructions\n",
                wording="This is, the wording.\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="generic", effects=[ItemizedAdaptationEffect(
                    kind="itemized",
                    items={"kind": "words", "punctuation": False},
                    effects={"selectable": {"colors": ["red", "blue"]}, "boxed": False},
                )]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[r.Paragraph(sentences=[r.Sentence(tokens=[
                    r.SelectableText(text="This", colors=["red", "blue"], boxed=False),
                    r.Whitespace(),
                    r.SelectableText(text="is", colors=["red", "blue"], boxed=False),
                    r.PlainText(text=","),
                    r.Whitespace(),
                    r.SelectableText(text="the", colors=["red", "blue"], boxed=False),
                    r.Whitespace(),
                    r.SelectableText(text="wording", colors=["red", "blue"], boxed=False),
                    r.PlainText(text="."),
                ])])]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_selectable_words_and_punctuation(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Instructions\n",
                wording="This is, the wording.\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="generic", effects=[ItemizedAdaptationEffect(
                    kind="itemized",
                    items={"kind": "words", "punctuation": True},
                    effects={"selectable": {"colors": ["green", "yellow", "orange"]}, "boxed": False},
                )]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[r.Paragraph(sentences=[r.Sentence(tokens=[
                    r.SelectableText(text="This", colors=["green", "yellow", "orange"], boxed=False),
                    r.Whitespace(),
                    r.SelectableText(text="is", colors=["green", "yellow", "orange"], boxed=False),
                    r.SelectableText(text=",", colors=["green", "yellow", "orange"], boxed=False),
                    r.Whitespace(),
                    r.SelectableText(text="the", colors=["green", "yellow", "orange"], boxed=False),
                    r.Whitespace(),
                    r.SelectableText(text="wording", colors=["green", "yellow", "orange"], boxed=False),
                    r.SelectableText(text=".", colors=["green", "yellow", "orange"], boxed=False),
                ])])]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_selectable_words__boxed(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Instructions\n",
                wording="This is, the wording.\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="generic", effects=[ItemizedAdaptationEffect(
                    kind="itemized",
                    items={"kind": "words", "punctuation": False},
                    effects={"selectable": {"colors": ["red", "blue"]}, "boxed": True},
                )]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[r.Paragraph(sentences=[r.Sentence(tokens=[
                    r.SelectableText(text="This", colors=["red", "blue"], boxed=True),
                    r.Whitespace(),
                    r.SelectableText(text="is", colors=["red", "blue"], boxed=True),
                    r.PlainText(text=","),
                    r.Whitespace(),
                    r.SelectableText(text="the", colors=["red", "blue"], boxed=True),
                    r.Whitespace(),
                    r.SelectableText(text="wording", colors=["red", "blue"], boxed=True),
                    r.PlainText(text="."),
                ])])]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_selectable_manual_items__plain(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Instructions\n",
                wording="This {selectable|is}{selectable|,} {selectable|the} wording.\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="generic", effects=[ItemizedAdaptationEffect(
                    kind="itemized",
                    items={"kind": "manual"},
                    effects={"selectable": {"colors": ["red", "blue"]}, "boxed": False},
                )]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[r.Paragraph(sentences=[r.Sentence(tokens=[
                    r.PlainText(text="This"),
                    r.Whitespace(),
                    r.SelectableText(text="is", colors=["red", "blue"], boxed=False),
                    r.SelectableText(text=",", colors=["red", "blue"], boxed=False),
                    r.Whitespace(),
                    r.SelectableText(text="the", colors=["red", "blue"], boxed=False),
                    r.Whitespace(),
                    r.PlainText(text="wording"),
                    r.PlainText(text="."),
                ])])]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[
                    d.TextInsertOp(insert="This ", attributes={}),
                    d.TextInsertOp(insert="is,", attributes={"selectable": True}),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(insert="the", attributes={"selectable": True}),
                    d.TextInsertOp(insert=" wording.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_selectable_manual_items__boxed(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Instructions\n",
                wording="This {selectable|is}{selectable|,} {selectable|the} wording.\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="generic", effects=[ItemizedAdaptationEffect(
                    kind="itemized",
                    items={"kind": "manual"},
                    effects={"selectable": {"colors": ["red", "blue"]}, "boxed": True},
                )]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[r.Paragraph(sentences=[r.Sentence(tokens=[
                    r.PlainText(text="This"),
                    r.Whitespace(),
                    r.SelectableText(text="is", colors=["red", "blue"], boxed=True),
                    r.SelectableText(text=",", colors=["red", "blue"], boxed=True),
                    r.Whitespace(),
                    r.SelectableText(text="the", colors=["red", "blue"], boxed=True),
                    r.Whitespace(),
                    r.PlainText(text="wording"),
                    r.PlainText(text="."),
                ])])]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[
                    d.TextInsertOp(insert="This ", attributes={}),
                    d.TextInsertOp(insert="is,", attributes={"selectable": True}),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(insert="the", attributes={"selectable": True}),
                    d.TextInsertOp(insert=" wording.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_sel_tags(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions="{sel1|abc} {sel2|def} {sel3|ghi} {sel4|jkl}\n",
                wording="wording\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                    adaptation=AdaptationV2(kind="generic", effects=[ItemizedAdaptationEffect(
                        kind="itemized",
                        items={"kind": "words", "punctuation": False},
                        effects={"selectable": {"colors": ["red", "green", "blue"]}, "boxed": False},
                    )]),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectedText(text="abc", color="red"),
                            r.Whitespace(),
                            r.SelectedText(text="def", color="green"),
                            r.Whitespace(),
                            r.SelectedText(text="ghi", color="blue"),
                            r.Whitespace(),
                            r.PlainText(text="jkl"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="wording", colors=["red", "green", "blue"], boxed=False),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="abc", attributes={"sel": 1}),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(insert="def", attributes={"sel": 2}),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(insert="ghi", attributes={"sel": 3}),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(insert="jkl", attributes={"sel": 4}),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="wording\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )


class MultipleChoicesInInstructionsAdaptationTestCase(AdaptationTestCase):
    def test_simple(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose {choices2||or|||...|a or b}.\n",
                wording="A ... B ...\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.BoxedText(text="a"),
                            r.Whitespace(),
                            r.PlainText(text="or"),
                            r.Whitespace(),
                            r.BoxedText(text="b"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b"]),
                            r.Whitespace(),
                            r.PlainText(text="B"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b"]),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose ", attributes={}),
                    d.TextInsertOp(insert="a or b", attributes={"choices2": {"start": "", "separator1": "or", "separator2": "", "stop": "", "placeholder": "..."}}),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ... B ...\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_example_and_clue(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose {choices2||or|||@|a or b}.\n",
                wording="A @ B @\n",
                example="This {choices2||/||||is} the @ example.\n",
                clue="This is {choices2||/||||the} @ clue.\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.BoxedText(text="a"),
                            r.Whitespace(),
                            r.PlainText(text="or"),
                            r.Whitespace(),
                            r.BoxedText(text="b"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b"]),
                            r.Whitespace(),
                            r.PlainText(text="B"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b"]),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="This"),
                            r.Whitespace(),
                            r.PlainText(text="{"),
                            r.PlainText(text="choices2"),
                            r.PlainText(text="|"),
                            r.PlainText(text="|"),
                            r.PlainText(text="/"),
                            r.PlainText(text="|"),
                            r.PlainText(text="|"),
                            r.PlainText(text="|"),
                            r.PlainText(text="|"),
                            r.PlainText(text="is"),
                            r.PlainText(text="}"),
                            r.Whitespace(),
                            r.PlainText(text="the"),
                            r.Whitespace(),
                            r.PlainText(text="@"),
                            r.Whitespace(),
                            r.PlainText(text="example"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                clue=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="This"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.PlainText(text="{"),
                            r.PlainText(text="choices2"),
                            r.PlainText(text="|"),
                            r.PlainText(text="|"),
                            r.PlainText(text="/"),
                            r.PlainText(text="|"),
                            r.PlainText(text="|"),
                            r.PlainText(text="|"),
                            r.PlainText(text="|"),
                            r.PlainText(text="the"),
                            r.PlainText(text="}"),
                            r.Whitespace(),
                            r.PlainText(text="@"),
                            r.Whitespace(),
                            r.PlainText(text="clue"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose ", attributes={}),
                    d.TextInsertOp(insert="a or b", attributes={"choices2": {"start": "", "separator1": "or", "separator2": "", "stop": "", "placeholder": "@"}}),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A @ B @\n", attributes={}),
                ],
                example=[
                    d.TextInsertOp(insert="This {choices2||/||||is} the @ example.\n", attributes={}),
                ],
                clue=[
                    d.TextInsertOp(insert="This is {choices2||/||||the} @ clue.\n", attributes={}),
                ],
            ),
        )

    def test_choices2(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose {choices2||or|||...|a or b}.\n",
                wording="A ... B ...\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.BoxedText(text="a"),
                            r.Whitespace(),
                            r.PlainText(text="or"),
                            r.Whitespace(),
                            r.BoxedText(text="b"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b"]),
                            r.Whitespace(),
                            r.PlainText(text="B"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b"]),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose ", attributes={}),
                    d.TextInsertOp(insert="a or b", attributes={"choices2": {"start": "", "separator1": "or", "separator2": "", "stop": "", "placeholder": "..."}}),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ... B ...\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_choices2_with_two_separators(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose {choices2||,|or||...|a, b, c or d}.\n",
                wording="A ... B ...\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.BoxedText(text="a"),
                            r.PlainText(text=","),
                            r.Whitespace(),
                            r.BoxedText(text="b"),
                            r.PlainText(text=","),
                            r.Whitespace(),
                            r.BoxedText(text="c"),
                            r.Whitespace(),
                            r.PlainText(text="or"),
                            r.Whitespace(),
                            r.BoxedText(text="d"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b", "c", "d"]),
                            r.Whitespace(),
                            r.PlainText(text="B"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b", "c", "d"]),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose ", attributes={}),
                    d.TextInsertOp(insert="a, b, c or d", attributes={"choices2": {"start": "", "separator1": ",", "separator2": "or", "stop": "", "placeholder": "..."}}),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ... B ...\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_choices2_with_oxford_comma(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose {choices2||,|or||...|a, b, c, or d}.\n",
                wording="A ... B ...\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.BoxedText(text="a"),
                            r.PlainText(text=","),
                            r.Whitespace(),
                            r.BoxedText(text="b"),
                            r.PlainText(text=","),
                            r.Whitespace(),
                            r.BoxedText(text="c"),
                            r.Whitespace(),
                            r.PlainText(text="or"),
                            r.Whitespace(),
                            r.BoxedText(text="d"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b", "c", "d"]),
                            r.Whitespace(),
                            r.PlainText(text="B"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b", "c", "d"]),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose ", attributes={}),
                    d.TextInsertOp(insert="a, b, c, or d", attributes={"choices2": {"start": "", "separator1": ",", "separator2": "or", "stop": "", "placeholder": "..."}}),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ... B ...\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_choices2_with_successive_separators(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose {choices2||/|||...|a / b // c}.\n",
                wording="A ... B ...\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.BoxedText(text="a"),
                            r.Whitespace(),
                            r.PlainText(text="/"),
                            r.Whitespace(),
                            r.BoxedText(text="b"),
                            r.Whitespace(),
                            r.PlainText(text="/"),
                            r.Whitespace(),
                            r.BoxedText(text="c"),
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
                            r.MultipleChoicesInput(choices=["a", "b", "c"]),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose ", attributes={}),
                    d.TextInsertOp(insert="a / b // c", attributes={"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": "..."}}),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ... B ...\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_choices2_with_start_and_stop(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose {choices2|(|or||)|...|(a or b)}.\n",
                wording="A ... B ...\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="("),
                            r.BoxedText(text="a"),
                            r.Whitespace(),
                            r.PlainText(text="or"),
                            r.Whitespace(),
                            r.BoxedText(text="b"),
                            r.PlainText(text=")"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b"]),
                            r.Whitespace(),
                            r.PlainText(text="B"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b"]),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose ", attributes={}),
                    d.TextInsertOp(insert="(a or b)", attributes={"choices2": {"start": "(", "separator1": "or", "separator2": "", "stop": ")", "placeholder": "..."}}),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ... B ...\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_two_choices2(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose {choices2||or|||...|a or b} and {choices2||or|||@@@|c or d}.\n",
                wording="A ... @@@\nB ... @@@\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.BoxedText(text="a"),
                            r.Whitespace(),
                            r.PlainText(text="or"),
                            r.Whitespace(),
                            r.BoxedText(text="b"),
                            r.Whitespace(),
                            r.PlainText(text="and"),
                            r.Whitespace(),
                            r.BoxedText(text="c"),
                            r.Whitespace(),
                            r.PlainText(text="or"),
                            r.Whitespace(),
                            r.BoxedText(text="d"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="A"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b"]),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["c", "d"]),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="B"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["a", "b"]),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["c", "d"]),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose ", attributes={}),
                    d.TextInsertOp(insert="a or b", attributes={"choices2": {"start": "", "separator1": "or", "separator2": "", "stop": "", "placeholder": "..."}}),
                    d.TextInsertOp(insert=" and ", attributes={}),
                    d.TextInsertOp(insert="c or d", attributes={"choices2": {"start": "", "separator1": "or", "separator2": "", "stop": "", "placeholder": "@@@"}}),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ... @@@\nB ... @@@\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )


class MultipleChoicesInWordingAdaptationTestCase(AdaptationTestCase):
    def test_simple(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose wisely.\n",
                wording="A {choices2||/||||a/b/c} B {choices2||#||||d#e}.\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
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
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose wisely.\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(insert="a/b/c", attributes={"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": ""}}),
                    d.TextInsertOp(insert=" B ", attributes={}),
                    d.TextInsertOp(insert="d#e", attributes={"choices2": {"start": "", "separator1": "#", "separator2": "", "stop": "", "placeholder": ""}}),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_choices2_without_placeholder(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose wisely.\n",
                wording="A {choices2|(|/||)||(blah/blih)}.\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
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
                    d.TextInsertOp(insert="Choose wisely.\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="(blah/blih)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator1": "/",
                                "separator2": "",
                                "stop": ")",
                                "placeholder": "",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_choices2_with_spaces(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose wisely.\n",
                wording="A {choices2|(|/||)||  (  blah  /  blih  )  }.\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
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
                    d.TextInsertOp(insert="Choose wisely.\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="  (  blah  /  blih  )  ",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator1": "/",
                                "separator2": "",
                                "stop": ")",
                                "placeholder": "",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_choices2_with_empty_start_and_stop(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose wisely.\n",
                wording="A {choices2||/||||blah/blih}.\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
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
                    d.TextInsertOp(insert="Choose wisely.\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="blah/blih",
                        attributes={
                            "choices2": {
                                "start": "",
                                "separator1": "/",
                                "separator2": "",
                                "stop": "",
                                "placeholder": "",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_choices2_with_empty_separator(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose wisely.\n",
                wording="A {choices2||||||blah / blih}.\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
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
                    d.TextInsertOp(insert="Choose wisely.\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="blah / blih",
                        attributes={
                            "choices2": {
                                "start": "",
                                "separator1": "",
                                "separator2": "",
                                "stop": "",
                                "placeholder": "",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_choices2_with_longer_separators(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose wisely.\n",
                wording="A {choices2|((|//||))||((blah//blih))}.\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
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
                    d.TextInsertOp(insert="Choose wisely.\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="((blah//blih))",
                        attributes={
                            "choices2": {
                                "start": "((",
                                "separator1": "//",
                                "separator2": "",
                                "stop": "))",
                                "placeholder": "",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_choices2_with_escaped_separators(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose wisely.\n",
                wording=r"A {choices2|\{|\|||\}||\{blah\|blih\}}." + "\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
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
                    d.TextInsertOp(insert="Choose wisely.\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(
                        insert="{blah|blih}",
                        attributes={
                            "choices2": {
                                "start": "{",
                                "separator1": "|",
                                "separator2": "",
                                "stop": "}",
                                "placeholder": "",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_choices2_with_placeholder_before(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose wisely.\n",
                wording="The sky is @@. {choices2|(|/||)|@@|(blue/red)} \n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
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
                    d.TextInsertOp(insert="Choose wisely.\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="The sky is @@. ", attributes={}),
                    d.TextInsertOp(
                        insert="(blue/red)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator1": "/",
                                "separator2": "",
                                "stop": ")",
                                "placeholder": "@@",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=" \n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_choices2_with_placeholder_after(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose wisely.\n",
                wording="{choices2|(|/||)|...|(blue/red)} The sky is ....\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
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
                    d.TextInsertOp(insert="Choose wisely.\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(
                        insert="(blue/red)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator1": "/",
                                "separator2": "",
                                "stop": ")",
                                "placeholder": "...",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=" The sky is ....\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_choices2_with_two_placeholders(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose wisely.\n",
                wording="{choices2|(|/||)|...|(blue/yellow)} The sky is ..., the sun is ....\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
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
                    d.TextInsertOp(insert="Choose wisely.\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(
                        insert="(blue/yellow)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator1": "/",
                                "separator2": "",
                                "stop": ")",
                                "placeholder": "...",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=" The sky is ..., the sun is ....\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_two_choices2_with_matching_placeholders(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose wisely.\n",
                wording="{choices2|(|/||)|@1|(blue/red)} {choices2|[|*||]|@2|[green*yellow]} The sky is @1, the sun is @2.\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
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
                    d.TextInsertOp(insert="Choose wisely.\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(
                        insert="(blue/red)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator1": "/",
                                "separator2": "",
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
                                "separator1": "*",
                                "separator2": "",
                                "stop": "]",
                                "placeholder": "@2",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=" The sky is @1, the sun is @2.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_two_choices2_with_identical_placeholders(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose wisely.\n",
                wording="The sky is @@. {choices2|(|/||)|@@|(blue/red)}\n\nThe sun is @@. {choices2|(|/||)|@@|(green/yellow)}\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
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
                    d.TextInsertOp(insert="Choose wisely.\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="The sky is @@. ", attributes={}),
                    d.TextInsertOp(
                        insert="(blue/red)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator1": "/",
                                "separator2": "",
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
                                "separator1": "/",
                                "separator2": "",
                                "stop": ")",
                                "placeholder": "@@",
                            },
                        },
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_two_choices2_with_spaces_between_them(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose wisely.\n",
                wording="The sky is @1, {choices2|(|/||)|@1|(blue/red)} {choices2|[|*||]|@2|[green*yellow]} the sun is @2.\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="multiple-choices", effects=[]),
            ),
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
                    d.TextInsertOp(insert="Choose wisely.\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="The sky is @1, ", attributes={}),
                    d.TextInsertOp(
                        insert="(blue/red)",
                        attributes={
                            "choices2": {
                                "start": "(",
                                "separator1": "/",
                                "separator2": "",
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
                                "separator1": "*",
                                "separator2": "",
                                "stop": "]",
                                "placeholder": "@2",
                            },
                        },
                    ),
                    d.TextInsertOp(insert=" the sun is @2.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )


class SelectThingsAdaptationTestCase(AdaptationTestCase):
    def test_single_sentence(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions="instructions\n",
                wording="The wording of this exercise is a single sentence.\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(
                    kind="generic",
                    effects=[
                        ItemizedAdaptationEffect(
                            kind="itemized",
                            items=ItemizedAdaptationEffect.WordsItems(kind="words", punctuation=False),
                            effects=ItemizedAdaptationEffect.Effects(
                                selectable=ItemizedAdaptationEffect.Effects.Selectable(colors=["red", "blue"]),
                                boxed=False,
                            ),
                        ),
                    ],
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="The", colors=["red", "blue"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="wording", colors=["red", "blue"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="of", colors=["red", "blue"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="this", colors=["red", "blue"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="exercise", colors=["red", "blue"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="is", colors=["red", "blue"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="a", colors=["red", "blue"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="single", colors=["red", "blue"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="sentence", colors=["red", "blue"], boxed=False),
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
                    d.TextInsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="The wording of this exercise is a single sentence.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_sel_tags(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions="{sel1|abc} {sel2|def} {sel3|ghi} {sel4|jkl}\n",
                wording="wording\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(
                    kind="generic",
                    effects=[
                        ItemizedAdaptationEffect(
                            kind="itemized",
                            items=ItemizedAdaptationEffect.WordsItems(kind="words", punctuation=False),
                            effects=ItemizedAdaptationEffect.Effects(
                                selectable=ItemizedAdaptationEffect.Effects.Selectable(colors=["red", "green", "blue"]),
                                boxed=False,
                            ),
                        ),
                    ],
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectedText(text="abc", color="red"),
                            r.Whitespace(),
                            r.SelectedText(text="def", color="green"),
                            r.Whitespace(),
                            r.SelectedText(text="ghi", color="blue"),
                            r.Whitespace(),
                            r.PlainText(text="jkl"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="wording", colors=["red", "green", "blue"], boxed=False),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="abc", attributes={"sel": 1}),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(insert="def", attributes={"sel": 2}),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(insert="ghi", attributes={"sel": 3}),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(insert="jkl", attributes={"sel": 4}),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="wording\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_single_color(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions="{sel1|abc}\n",
                wording="wording\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(
                    kind="generic",
                    effects=[
                        ItemizedAdaptationEffect(
                            kind="itemized",
                            items=ItemizedAdaptationEffect.WordsItems(kind="words", punctuation=False),
                            effects=ItemizedAdaptationEffect.Effects(
                                selectable=ItemizedAdaptationEffect.Effects.Selectable(colors=["red"]),
                                boxed=False,
                            ),
                        ),
                    ],
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectedText(text="abc", color="red"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="wording", colors=["red"], boxed=False),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="abc", attributes={"sel": 1}),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="wording\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_multiple_lines_in_instructions(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="instructions\nare\n\non\n\nmultiple\nlines\n",
                wording="wording\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(
                    kind="generic",
                    effects=[
                        ItemizedAdaptationEffect(
                            kind="itemized",
                            items=ItemizedAdaptationEffect.WordsItems(kind="words", punctuation=False),
                            effects=ItemizedAdaptationEffect.Effects(
                                selectable=ItemizedAdaptationEffect.Effects.Selectable(colors=["red"]),
                                boxed=False,
                            ),
                        ),
                    ],
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="instructions"),
                            r.Whitespace(),
                            r.PlainText(text="are"),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="on"),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="multiple"),
                            r.Whitespace(),
                            r.PlainText(text="lines"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="wording", colors=["red"], boxed=False),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="instructions\nare\n\non\n\nmultiple\nlines\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="wording\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_multiple_lines_in_wording(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="instructions\n",
                wording="wording is\n\non\n\nmultiple lines\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(
                    kind="generic",
                    effects=[
                        ItemizedAdaptationEffect(
                            kind="itemized",
                            items=ItemizedAdaptationEffect.WordsItems(kind="words", punctuation=False),
                            effects=ItemizedAdaptationEffect.Effects(
                                selectable=ItemizedAdaptationEffect.Effects.Selectable(colors=["red"]),
                                boxed=False,
                            ),
                        ),
                    ],
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="wording", colors=["red"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="is", colors=["red"], boxed=False),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="on", colors=["red"], boxed=False),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="multiple", colors=["red"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="lines", colors=["red"], boxed=False),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="wording is\n\non\n\nmultiple lines\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_unknown_tags(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="{tag|abc}\n",
                wording="{tag|def}\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(
                    kind="generic",
                    effects=[
                        ItemizedAdaptationEffect(
                            kind="itemized",
                            items=ItemizedAdaptationEffect.WordsItems(kind="words", punctuation=False),
                            effects=ItemizedAdaptationEffect.Effects(
                                selectable=ItemizedAdaptationEffect.Effects.Selectable(colors=["red"]),
                                boxed=False,
                            ),
                        ),
                    ],
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="{"),
                            r.PlainText(text="tag"),
                            r.PlainText(text="|"),
                            r.PlainText(text="abc"),
                            r.PlainText(text="}"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="{"),
                            r.SelectableText(text="tag", colors=["red"], boxed=False),
                            r.PlainText(text="|"),
                            r.SelectableText(text="def", colors=["red"], boxed=False),
                            r.PlainText(text="}"),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="{tag|abc}\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="{tag|def}\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_strip_whitespace(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="   abc   \n",
                wording="   def   \n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(
                    kind="generic",
                    effects=[
                        ItemizedAdaptationEffect(
                            kind="itemized",
                            items=ItemizedAdaptationEffect.WordsItems(kind="words", punctuation=False),
                            effects=ItemizedAdaptationEffect.Effects(
                                selectable=ItemizedAdaptationEffect.Effects.Selectable(colors=["red"]),
                                boxed=False,
                            ),
                        ),
                    ],
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="abc"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="def", colors=["red"], boxed=False),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="   abc   \n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="   def   \n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_example_and_clue(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions="instructions\n",
                wording="wording\n",
                example="This is the example.\n",
                clue="This is the clue.\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(
                    kind="generic",
                    effects=[
                        ItemizedAdaptationEffect(
                            kind="itemized",
                            items=ItemizedAdaptationEffect.WordsItems(kind="words", punctuation=False),
                            effects=ItemizedAdaptationEffect.Effects(
                                selectable=ItemizedAdaptationEffect.Effects.Selectable(colors=["red"]),
                                boxed=False,
                            ),
                        ),
                    ],
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="wording", colors=["red"], boxed=False),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="This"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.PlainText(text="the"),
                            r.Whitespace(),
                            r.PlainText(text="example"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                clue=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="This"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.PlainText(text="the"),
                            r.Whitespace(),
                            r.PlainText(text="clue"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="wording\n", attributes={}),
                ],
                example=[
                    d.TextInsertOp(insert="This is the example.\n", attributes={}),
                ],
                clue=[
                    d.TextInsertOp(insert="This is the clue.\n", attributes={}),
                ],
            ),
        )

    def test_example_and_clue_with_sel_tags(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions="instructions\n",
                wording="wording\n",
                example="{sel1|abc} {sel2|def}\n",
                clue="{sel3|ghi} {sel4|jkl}\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(
                    kind="generic",
                    effects=[
                        ItemizedAdaptationEffect(
                            kind="itemized",
                            items=ItemizedAdaptationEffect.WordsItems(kind="words", punctuation=False),
                            effects=ItemizedAdaptationEffect.Effects(
                                selectable=ItemizedAdaptationEffect.Effects.Selectable(colors=["red", "green", "blue"]),
                                boxed=False,
                            ),
                        ),
                    ],
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="wording", colors=["red", "green", "blue"], boxed=False),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectedText(text="abc", color="red"),
                            r.Whitespace(),
                            r.SelectedText(text="def", color="green"),
                        ]),
                    ]),
                ]),
                clue=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectedText(text="ghi", color="blue"),
                            r.Whitespace(),
                            r.PlainText(text="jkl"),
                        ]),
                    ]),
                ]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="wording\n", attributes={}),
                ],
                example=[
                    d.TextInsertOp(insert="abc", attributes={"sel": 1}),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(insert="def", attributes={"sel": 2}),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                clue=[
                    d.TextInsertOp(insert="ghi", attributes={"sel": 3}),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(insert="jkl", attributes={"sel": 4}),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
            ),
        )


class LenientParagraphTestCase(AdaptationTestCase):
    def test_bold_and_italic(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions="This is a {bold|strict} instructions {italic|paragraph}.\n\nAnd this is a {bold|lenient} instructions {italic|paragraph}\n",
                wording="This is a {bold|strict} wording {italic|paragraph}.\nAnd this is a {bold|lenient} wording {italic|paragraph}\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="generic", effects=[])
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="This"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.PlainText(text="a"),
                            r.Whitespace(),
                            r.BoldText(text="strict"),
                            r.Whitespace(),
                            r.PlainText(text="instructions"),
                            r.Whitespace(),
                            r.ItalicText(text="paragraph"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="And"),
                            r.Whitespace(),
                            r.PlainText(text="this"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.PlainText(text="a"),
                            r.Whitespace(),
                            r.BoldText(text="lenient"),
                            r.Whitespace(),
                            r.PlainText(text="instructions"),
                            r.Whitespace(),
                            r.ItalicText(text="paragraph"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="This"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.PlainText(text="a"),
                            r.Whitespace(),
                            r.BoldText(text="strict"),
                            r.Whitespace(),
                            r.PlainText(text="wording"),
                            r.Whitespace(),
                            r.ItalicText(text="paragraph"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="And"),
                            r.Whitespace(),
                            r.PlainText(text="this"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.PlainText(text="a"),
                            r.Whitespace(),
                            r.BoldText(text="lenient"),
                            r.Whitespace(),
                            r.PlainText(text="wording"),
                            r.Whitespace(),
                            r.ItalicText(text="paragraph"),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="This is a ", attributes={}),
                    d.TextInsertOp(insert="strict", attributes={"bold": True}),
                    d.TextInsertOp(insert=" instructions ", attributes={}),
                    d.TextInsertOp(insert="paragraph", attributes={"italic": True}),
                    d.TextInsertOp(insert=".\n\nAnd this is a ", attributes={}),
                    d.TextInsertOp(insert="lenient", attributes={"bold": True}),
                    d.TextInsertOp(insert=" instructions ", attributes={}),
                    d.TextInsertOp(insert="paragraph", attributes={"italic": True}),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="This is a ", attributes={}),
                    d.TextInsertOp(insert="strict", attributes={"bold": True}),
                    d.TextInsertOp(insert=" wording ", attributes={}),
                    d.TextInsertOp(insert="paragraph", attributes={"italic": True}),
                    d.TextInsertOp(insert=".\nAnd this is a ", attributes={}),
                    d.TextInsertOp(insert="lenient", attributes={"bold": True}),
                    d.TextInsertOp(insert=" wording ", attributes={}),
                    d.TextInsertOp(insert="paragraph", attributes={"italic": True}),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_select_words_without_punctuation(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions="instructions\n",
                wording="This is a strict paragraph, with... some punctuation.\n\nAnd this, is a... lenient paragraph\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(
                    kind="generic",
                    effects=[
                        ItemizedAdaptationEffect(
                            kind="itemized",
                            items=ItemizedAdaptationEffect.WordsItems(kind="words", punctuation=False),
                            effects=ItemizedAdaptationEffect.Effects(
                                selectable=ItemizedAdaptationEffect.Effects.Selectable(colors=["red"]),
                                boxed=False,
                            ),
                        ),
                    ],
                )
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="This", colors=["red"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="is", colors=["red"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="a", colors=["red"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="strict", colors=["red"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="paragraph", colors=["red"], boxed=False),
                            r.PlainText(text=","),
                            r.Whitespace(),
                            r.SelectableText(text="with", colors=["red"], boxed=False),
                            r.PlainText(text="..."),
                        ]),
                        r.Sentence(tokens=[
                            r.SelectableText(text="some", colors=["red"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="punctuation", colors=["red"], boxed=False),
                            r.PlainText(text="."),
                        ])
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="And", colors=["red"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="this", colors=["red"], boxed=False),
                            r.PlainText(text=","),
                            r.Whitespace(),
                            r.SelectableText(text="is", colors=["red"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="a", colors=["red"], boxed=False),
                            r.PlainText(text="..."),
                            r.Whitespace(),
                            r.SelectableText(text="lenient", colors=["red"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="paragraph", colors=["red"], boxed=False),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="This is a strict paragraph, with... some punctuation.\n\nAnd this, is a... lenient paragraph\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_select_words_with_punctuation(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions="instructions\n",
                wording="This is a strict paragraph, with... some punctuation.\n\nAnd this, is a... lenient paragraph\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(
                    kind="generic",
                    effects=[
                        ItemizedAdaptationEffect(
                            kind="itemized",
                            items=ItemizedAdaptationEffect.WordsItems(kind="words", punctuation=True),
                            effects=ItemizedAdaptationEffect.Effects(
                                selectable=ItemizedAdaptationEffect.Effects.Selectable(colors=["red"]),
                                boxed=False,
                            ),
                        ),
                    ],
                )
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="This", colors=["red"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="is", colors=["red"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="a", colors=["red"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="strict", colors=["red"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="paragraph", colors=["red"], boxed=False),
                            r.SelectableText(text=",", colors=["red"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="with", colors=["red"], boxed=False),
                            r.SelectableText(text="...", colors=["red"], boxed=False),
                        ]),
                        r.Sentence(tokens=[
                            r.SelectableText(text="some", colors=["red"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="punctuation", colors=["red"], boxed=False),
                            r.SelectableText(text=".", colors=["red"], boxed=False),
                        ])
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.SelectableText(text="And", colors=["red"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="this", colors=["red"], boxed=False),
                            r.SelectableText(text=",", colors=["red"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="is", colors=["red"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="a", colors=["red"], boxed=False),
                            r.SelectableText(text="...", colors=["red"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="lenient", colors=["red"], boxed=False),
                            r.Whitespace(),
                            r.SelectableText(text="paragraph", colors=["red"], boxed=False),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="This is a strict paragraph, with... some punctuation.\n\nAnd this, is a... lenient paragraph\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_fill_with_free_text(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions="instructions\n",
                wording="This is a ... strict paragraph. With some punctuation.\n\nAnd this, is a ... lenient paragraph\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(
                    kind="generic",
                    effects=[FillWithFreeTextAdaptationEffect(kind="fill-with-free-text", placeholder="...")],
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="instructions"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="This"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.PlainText(text="a"),
                            r.Whitespace(),
                            r.FreeTextInput(),
                            r.Whitespace(),
                            r.PlainText(text="strict"),
                            r.Whitespace(),
                            r.PlainText(text="paragraph"),
                            r.PlainText(text="."),
                        ]),
                        r.Sentence(tokens=[
                            r.PlainText(text="With"),
                            r.Whitespace(),
                            r.PlainText(text="some"),
                            r.Whitespace(),
                            r.PlainText(text="punctuation"),
                            r.PlainText(text="."),
                        ])
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="And"),
                            r.Whitespace(),
                            r.PlainText(text="this"),
                            r.PlainText(text=","),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.PlainText(text="a"),
                            r.Whitespace(),
                            r.FreeTextInput(),
                            r.Whitespace(),
                            r.PlainText(text="lenient"),
                            r.Whitespace(),
                            r.PlainText(text="paragraph"),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="This is a ... strict paragraph. With some punctuation.\n\nAnd this, is a ... lenient paragraph\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_multiple_choices(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions="Choose {choices2||/|||...|alpha/bravo}.\n",
                wording="This is a ... strict paragraph. With some punctuation.\n\nAnd this, is a ... lenient paragraph\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="generic", effects=[]),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.BoxedText(text="alpha"),
                            r.Whitespace(),
                            r.PlainText(text="/"),
                            r.Whitespace(),
                            r.BoxedText(text="bravo"),
                            r.PlainText(text="."),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="This"),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.PlainText(text="a"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["alpha", "bravo"]),
                            r.Whitespace(),
                            r.PlainText(text="strict"),
                            r.Whitespace(),
                            r.PlainText(text="paragraph"),
                            r.PlainText(text="."),
                        ]),
                        r.Sentence(tokens=[
                            r.PlainText(text="With"),
                            r.Whitespace(),
                            r.PlainText(text="some"),
                            r.Whitespace(),
                            r.PlainText(text="punctuation"),
                            r.PlainText(text="."),
                        ])
                    ]),
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="And"),
                            r.Whitespace(),
                            r.PlainText(text="this"),
                            r.PlainText(text=","),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.PlainText(text="a"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["alpha", "bravo"]),
                            r.Whitespace(),
                            r.PlainText(text="lenient"),
                            r.Whitespace(),
                            r.PlainText(text="paragraph"),
                        ]),
                    ]),
                ]),
                example=r.Section(paragraphs=[]),
                clue=r.Section(paragraphs=[]),
                wording_paragraphs_per_pagelet=3,
            ),
            d.Exercise(
                instructions=[
                    d.TextInsertOp(insert="Choose ", attributes={}),
                    d.TextInsertOp(insert="alpha/bravo", attributes={"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": "..."}}),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="This is a ... strict paragraph. With some punctuation.\n\nAnd this, is a ... lenient paragraph\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )


class MultipleAdaptationEffectsTestCase(AdaptationTestCase):
    def test_fill_with_free_text_and_multiple_choices_in_instructions(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="instructions {choices2||/|||@@@|short/long}\n",
                wording="The wording of this ... is a @@@ sentence.\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="generic", effects=[
                    FillWithFreeTextAdaptationEffect(kind="fill-with-free-text", placeholder="..."),
                ]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="instructions"),
                            r.Whitespace(),
                            r.BoxedText(text="short"),
                            r.Whitespace(),
                            r.PlainText(text="/"),
                            r.Whitespace(),
                            r.BoxedText(text="long"),
                        ]),
                    ]),
                ]),
                wording=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="The"),
                            r.Whitespace(),
                            r.PlainText(text="wording"),
                            r.Whitespace(),
                            r.PlainText(text="of"),
                            r.Whitespace(),
                            r.PlainText(text="this"),
                            r.Whitespace(),
                            r.FreeTextInput(),
                            r.Whitespace(),
                            r.PlainText(text="is"),
                            r.Whitespace(),
                            r.PlainText(text="a"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["short", "long"]),
                            r.Whitespace(),
                            r.PlainText(text="sentence"),
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
                    d.TextInsertOp(insert="instructions ", attributes={}),
                    d.TextInsertOp(insert="short/long", attributes={"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": "@@@"}}),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="The wording of this ... is a @@@ sentence.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )

    def test_multiple_choices_in_instructions_and_wording(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions="Choose wisely {choices2||/|||@@@|alpha/bravo}.\n",
                wording="A {choices2||/||||a/b/c} B {choices2||/||||d/e} C @@@.\n",
                example="\n",
                clue="\n",
                wording_paragraphs_per_pagelet=3,
                adaptation=AdaptationV2(kind="generic", effects=[]),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                instructions=r.Section(paragraphs=[
                    r.Paragraph(sentences=[
                        r.Sentence(tokens=[
                            r.PlainText(text="Choose"),
                            r.Whitespace(),
                            r.PlainText(text="wisely"),
                            r.Whitespace(),
                            r.BoxedText(text="alpha"),
                            r.Whitespace(),
                            r.PlainText(text="/"),
                            r.Whitespace(),
                            r.BoxedText(text="bravo"),
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
                            r.Whitespace(),
                            r.PlainText(text="C"),
                            r.Whitespace(),
                            r.MultipleChoicesInput(choices=["alpha", "bravo"]),
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
                    d.TextInsertOp(insert="Choose wisely ", attributes={}),
                    d.TextInsertOp(insert="alpha/bravo", attributes={"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": "@@@"}}),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ", attributes={}),
                    d.TextInsertOp(insert="a/b/c", attributes={"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": ""}}),
                    d.TextInsertOp(insert=" B ", attributes={}),
                    d.TextInsertOp(insert="d/e", attributes={"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": ""}}),
                    d.TextInsertOp(insert=" C @@@.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
            ),
        )
