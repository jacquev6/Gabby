from __future__ import annotations

from typing import Any, Iterable
import itertools
import json
import re
import traceback
import typing
import unittest

from mydantic import PydanticBase

from .. import api_models
from .. import deltas
from .. import exercises
from .. import renderable


# We use the 're.*' functions without worrying about re-compiling the same regexes again and again. The 're' module
# does some caching (see https://docs.python.org/3/library/re.html#re.compile) so this does not impact performances.


def adapt(exercise: exercises.Exercise) -> renderable.Exercise:
    return _Adapter(exercise).adapted


class McqDefinition(PydanticBase):
    start: str | None
    separator1: str | None
    separator2: str | None
    stop: str | None
    placeholder: str | None = None
    mcq_field_uid: str | None = None
    deltas: list[deltas.TextInsertOp]


class Interval(PydanticBase):
    begin: int  # Included
    end: int  # Excluded


class AnnotatedSection(PydanticBase):
    class Point(PydanticBase):
        position: int

    class Format(PydanticBase):
        bold: bool
        italic: bool
        sel: int | None

    text: str
    choices: list[tuple[Interval, deltas.Choices2]]
    mcq_placeholders: list[Interval]
    manual_items: list[Interval]
    mcq_fields: list[tuple[Interval, str]]
    formats: list[tuple[Interval, Format]]


class _Adapter:
    def __init__(self, exercise: exercises.Exercise):
        instructions_section = self.make_annotated_section(exercise.instructions)

        self.single_item_per_paragraph = exercise.adaptation.single_item_per_paragraph
        self.show_mcq_choices_by_default = exercise.adaptation.show_mcq_choices_by_default
        self.show_arrow_before_mcq_fields = exercise.adaptation.show_arrow_before_mcq_fields

        if exercise.adaptation.items is None:
            self.letters_are_items = False
            self.words_are_items = False
            self.punctuation_is_items = False
            self.sentences_are_items = False
            self.manual_items_are_items = False
            self.separated_items_separator = None
        else:
            self.letters_are_items = exercise.adaptation.items.kind == "characters" and exercise.adaptation.items.letters
            self.words_are_items = exercise.adaptation.items.kind == "tokens" and exercise.adaptation.items.words
            self.punctuation_is_items = exercise.adaptation.items.kind == "tokens" and exercise.adaptation.items.punctuation
            self.sentences_are_items = exercise.adaptation.items.kind == "sentences"
            self.manual_items_are_items = exercise.adaptation.items.kind == "manual"
            self.separated_items_separator = exercise.adaptation.items.separator if exercise.adaptation.items.kind == "separated" else None

        if exercise.adaptation.items is not None:
            self.items_are_selectable = exercise.adaptation.items_are_selectable is not None
            if self.items_are_selectable:
                assert exercise.adaptation.items_are_selectable is not None
                self.colors_for_selectable_items = exercise.adaptation.items_are_selectable.colors
            else:
                self.colors_for_selectable_items = []
            self.items_are_boxed = exercise.adaptation.items_are_boxed
        else:
            self.items_are_selectable = False
            self.colors_for_selectable_items = []
            self.items_are_boxed = False

        if exercise.adaptation.items_have_mcq_below:
            self.mcq_below_items = None
            for choices in instructions_section.choices:
                if choices[1].placeholder == "" and choices[1].mcq_field_uid is None:
                    self.mcq_below_items = self.make_multiple_choices_input(instructions_section, choices[0].begin, choices[0].end, choices[1])
                    break
        else:
            self.mcq_below_items = None

        if exercise.adaptation.items_have_mcq_beside:
            self.mcq_beside_items = None
            for choices in instructions_section.choices:
                if choices[1].placeholder == "" and choices[1].mcq_field_uid is None:
                    self.mcq_beside_items = self.make_multiple_choices_input(instructions_section, choices[0].begin, choices[0].end, choices[1])
                    break
        else:
            self.mcq_beside_items = None

        if exercise.adaptation.items_are_repeated_with_mcq:
            assert exercise.adaptation.items is None
            self.sentences_are_items = True
            self.mcq_for_repeated_items = None
            for choices in instructions_section.choices:
                if choices[1].placeholder == "" and choices[1].mcq_field_uid is None:
                    self.mcq_for_repeated_items = self.make_multiple_choices_input(instructions_section, choices[0].begin, choices[0].end, choices[1])
                    break
        else:
            self.mcq_for_repeated_items = None

        self.items_have_gender_mcq_beside = exercise.adaptation.items_have_predefined_mcq.grammatical_gender
        self.items_have_number_mcq_beside = exercise.adaptation.items_have_predefined_mcq.grammatical_number

        adapted_instructions = list(
            self.remove_empty_paragraphs(
                itertools.chain.from_iterable(
                    self.adapt_instructions(section)
                    for section in [instructions_section, self.make_annotated_section(exercise.example), self.make_annotated_section(exercise.clue)]
                )
            )
        )
        self.global_placeholders = dict(self.make_global_placeholders(exercise.adaptation, instructions_section))
        self.mcq_fields = dict(self.make_global_mcq_fields(instructions_section))
        adapted_wording = list(list(w) for w in self.adapt_wording(self.make_annotated_section(exercise.wording)))
        pagelets = list(self.make_pagelets(exercise.adaptation.wording_paragraphs_per_pagelet, adapted_instructions, adapted_wording))

        if exercise.text_reference != deltas.empty:
            pagelets.append(
                self.make_pagelet(
                    list(self.remove_empty_paragraphs(self.adapt_instructions(self.make_annotated_section(exercise.text_reference)))),
                    [],
                )
            )

        self.adapted = renderable.Exercise(number=exercise.number, textbook_page=exercise.textbook_page, pagelets=pagelets)

    def make_annotated_section(self, section_deltas: deltas.Deltas) -> AnnotatedSection:
        begin = 0
        end = 0

        section = AnnotatedSection(
            text="",
            choices=[],
            mcq_placeholders=[],
            manual_items=[],
            mcq_fields=[],
            formats=[],
        )

        for delta in section_deltas:
            if delta.kind == "text":
                section.text += delta.insert
                end += len(delta.insert)

                if delta.attributes.choices2 is not None:
                    if len(section.choices) == 0 or section.choices[-1][1] != delta.attributes.choices2 or section.choices[-1][0].end != begin:
                        section.choices.append((Interval(begin=begin, end=end), delta.attributes.choices2))
                    else:
                        section.choices[-1][0].end = end

                if delta.attributes.mcq_placeholder:
                    if len(section.mcq_placeholders) == 0 or section.mcq_placeholders[-1].end != begin:
                        section.mcq_placeholders.append(Interval(begin=begin, end=end))
                    else:
                        section.mcq_placeholders[-1].end = end

                if delta.attributes.manual_item:
                    if len(section.manual_items) == 0 or section.manual_items[-1].end != begin:
                        section.manual_items.append(Interval(begin=begin, end=end))
                    else:
                        section.manual_items[-1].end = end

                if delta.attributes.bold or delta.attributes.italic or delta.attributes.sel is not None:
                    section.formats.append(
                        (
                            Interval(begin=begin, end=end),
                            AnnotatedSection.Format(bold=delta.attributes.bold, italic=delta.attributes.italic, sel=delta.attributes.sel),
                        )
                    )

                begin += len(delta.insert)
            elif delta.kind == "embed":
                assert delta.insert.kind == "mcq-field"
                section.text += "¤"
                end += 1
                section.mcq_fields.append((Interval(begin=begin, end=end), delta.insert.mcq_field))
                begin += 1
            else:
                assert False, f"Unexpected delta kind: {delta!r}"

        return section

    def adapt_instructions(self, instructions: AnnotatedSection) -> Iterable[renderable.Paragraph]:
        begin, end = self.strip(instructions, 0, len(instructions.text))

        for token_index, token in enumerate(re.split(r"(\s*\n\s*\n\s*)", instructions.text[begin:end])):
            if token_index % 2 == 0 and len(token) > 0:
                for paragraph in self.adapt_instructions_paragraph(instructions, begin, begin + len(token)):
                    yield renderable.Paragraph(contents=list(self.strip_whitespace_renderables(paragraph)))
            begin += len(token)

        assert begin == end

    def adapt_instructions_paragraph(self, instructions: AnnotatedSection, begin: int, end: int) -> Iterable[Iterable[renderable.AnyRenderable]]:
        for b, e in self.fix_instructions_sentence_candidates(instructions, list(self.make_instructions_sentence_candidates(instructions, begin, end))):
            yield self.adapt_instructions_sentence(instructions, b, e)

    def make_instructions_sentence_candidates(self, instructions: AnnotatedSection, begin: int, end: int) -> Iterable[tuple[int, int]]:
        paragraph_begin = begin
        for match in re.finditer(r".*?(:?\.\.\.|[.!?…])\s*", instructions.text[paragraph_begin:end], flags=re.DOTALL):
            assert match.start() == begin - paragraph_begin
            yield (paragraph_begin + match.start(), paragraph_begin + match.end())
            begin = paragraph_begin + match.end()
        if begin < end:
            yield (begin, end)

    def fix_instructions_sentence_candidates(self, instructions: AnnotatedSection, sentence_candidates: list[tuple[int, int]]) -> Iterable[tuple[int, int]]:
        current_begin = None
        for begin, end in sentence_candidates:
            if current_begin is None:
                current_begin = begin
            if not any(choice[0].begin < end <= choice[0].end for choice in instructions.choices):
                yield (current_begin, end)
                current_begin = None
        if current_begin is not None:
            yield (current_begin, end)

    def adapt_instructions_sentence(self, instructions: AnnotatedSection, begin: int, end: int) -> Iterable[renderable.AnyRenderable]:
        assert begin < end, (begin, end)

        while begin < end:
            (next_choices, next_manual_item, next_mcq_field) = self.find_next_disruptions(instructions, begin)
            assert next_manual_item is None
            assert next_mcq_field is None

            next_disruption = min(end, end if next_choices is None else next_choices[0].begin)

            if begin < next_disruption:
                yield from self.adapt_formatted_text(instructions, begin, next_disruption)
                begin = next_disruption
            else:
                assert begin == next_disruption
                if next_choices is not None and next_disruption == next_choices[0].begin:
                    yield from self.adapt_multiple_choices(instructions, next_choices[0].begin, next_choices[0].end, next_choices[1])
                    begin = next_choices[0].end
                else:
                    assert False, "Mishandled disruption"

        assert begin == end, (begin, end)

    def make_global_placeholders(
        self, adaptation: api_models.Adaptation, instructions: AnnotatedSection
    ) -> Iterable[tuple[str, list[renderable.AnyRenderable]]]:
        if adaptation.placeholder_for_fill_with_free_text is not None:
            yield (adaptation.placeholder_for_fill_with_free_text, [renderable.FreeTextInput(kind="freeTextInput")])

        for choices in instructions.choices:
            if choices[1].placeholder != "":
                yield choices[1].placeholder, [self.make_multiple_choices_input(instructions, choices[0].begin, choices[0].end, choices[1])]

    def make_global_mcq_fields(self, instructions: AnnotatedSection) -> Iterable[tuple[str, list[renderable.AnyRenderable]]]:
        for choices in instructions.choices:
            if choices[1].mcq_field_uid is not None:
                yield choices[1].mcq_field_uid, [self.make_multiple_choices_input(instructions, choices[0].begin, choices[0].end, choices[1])]

    def adapt_wording(self, wording: AnnotatedSection) -> Iterable[Iterable[renderable.Paragraph]]:
        begin, end = self.strip(wording, 0, len(wording.text))

        for token_index, token in enumerate(re.split(r"(\s*\n\s*\n\s*\n)", wording.text[begin:end])):
            if token_index % 2 == 0:
                yield self.remove_empty_paragraphs(self.adapt_wording_pagelet(wording, begin, begin + len(token)))
            begin += len(token)

        assert begin == end

    def adapt_wording_pagelet(self, wording: AnnotatedSection, begin: int, end: int) -> Iterable[renderable.Paragraph]:
        assert begin <= end, (begin, end)

        if end != begin:
            for token_index, token in enumerate(re.split(r"(\s*\n\s*)", wording.text[begin:end])):
                if token_index % 2 == 0:
                    for _, group in itertools.groupby(self.adapt_wording_paragraph(wording, begin, begin + len(token)), key=lambda e: e[0]):
                        yield renderable.Paragraph(contents=list(self.strip_whitespace_renderables(e[1] for e in group)))
                begin += len(token)

        assert begin == end, (begin, end)

    def adapt_wording_paragraph(self, wording: AnnotatedSection, begin: int, end: int) -> Iterable[tuple[int, renderable.AnyRenderable]]:
        assert begin <= end, (begin, end)

        placeholders = dict(self.global_placeholders)
        for choices in wording.choices:
            if choices[0].begin >= begin and choices[0].end <= end and choices[1].placeholder != "":
                placeholders[choices[1].placeholder] = [self.make_multiple_choices_input(wording, choices[0].begin, choices[0].end, choices[1])]

        paragraph_index = 0

        r: renderable.AnyRenderable

        if (after_list := self.detect_list_header(wording, begin, end)) is not None:
            for r in self.adapt_formatted_text(wording, begin, after_list):
                yield (paragraph_index, r)
            yield (paragraph_index, renderable.Whitespace(kind="whitespace"))
            begin = after_list

        while begin < end:
            (next_choices, next_manual_item, next_mcq_field) = self.find_next_disruptions(wording, begin)

            next_placeholder: tuple[int, str] | None = None
            for placeholder in placeholders.keys():
                if (index := wording.text.find(placeholder, begin, end)) >= begin and (next_placeholder is None or index < next_placeholder[0]):
                    next_placeholder = (index, placeholder)

            next_disruption = min(
                end,
                end if next_choices is None else next_choices[0].begin,
                end if next_placeholder is None else next_placeholder[0],
                end if next_manual_item is None else next_manual_item.begin,
                end if next_mcq_field is None else next_mcq_field[0].begin,
            )

            if begin < next_disruption:
                if self.letters_are_items:
                    for paragraph_index_2, r in self.adapt_itemized_letters(wording, begin, next_disruption, paragraph_index):
                        paragraph_index = paragraph_index_2
                        yield (paragraph_index, r)
                elif self.words_are_items or self.punctuation_is_items:
                    for paragraph_index_2, r in self.adapt_itemized_words_and_punctuation(wording, begin, next_disruption, paragraph_index):
                        paragraph_index = paragraph_index_2
                        yield (paragraph_index, r)
                elif self.sentences_are_items:
                    for paragraph_index_2, r in self.adapt_itemized_sentences(wording, begin, next_disruption, paragraph_index):
                        paragraph_index = paragraph_index_2
                        yield (paragraph_index, r)
                elif self.separated_items_separator is not None:
                    for paragraph_index_2, r in self.adapt_separated_items(wording, begin, next_disruption, paragraph_index):
                        paragraph_index = paragraph_index_2
                        yield (paragraph_index, r)
                else:
                    for r in self.adapt_formatted_text(wording, begin, next_disruption):
                        yield (paragraph_index, r)
                begin = next_disruption
            else:
                assert begin == next_disruption
                if next_choices is not None and next_disruption == next_choices[0].begin:
                    if next_choices[1].placeholder == "":
                        yield (paragraph_index, self.make_multiple_choices_input(wording, next_choices[0].begin, next_choices[0].end, next_choices[1]))
                    begin = next_choices[0].end
                elif next_placeholder is not None and next_disruption == next_placeholder[0]:
                    for r in placeholders[next_placeholder[1]]:
                        yield (paragraph_index, r)
                    begin += len(next_placeholder[1])
                elif next_manual_item is not None and next_disruption == next_manual_item.begin:
                    assert self.manual_items_are_items
                    for r in self.decorate_item(self.adapt_formatted_text(wording, next_manual_item.begin, next_manual_item.end)):
                        yield (paragraph_index, r)
                    if self.single_item_per_paragraph:
                        paragraph_index += 1
                    begin = next_manual_item.end
                elif next_mcq_field is not None and next_disruption == next_mcq_field[0].begin:
                    mcq_field = self.mcq_fields.get(next_mcq_field[1])
                    if mcq_field is None:
                        yield (
                            paragraph_index,
                            renderable.MultipleChoicesInput(
                                kind="multipleChoicesInput",
                                show_arrow_before=self.show_arrow_before_mcq_fields,
                                choices=[],
                                show_choices_by_default=self.show_mcq_choices_by_default,
                            ),
                        )
                    else:
                        for r in mcq_field:
                            yield (paragraph_index, r)
                    begin = next_mcq_field[0].end
                else:
                    assert False, "Mishandled disruption"

        assert begin == end, (begin, end)

    def find_next_disruptions(
        self, wording: AnnotatedSection, begin: int
    ) -> tuple[tuple[Interval, deltas.Choices2] | None, Interval | None, tuple[Interval, str] | None]:
        next_choices: tuple[Interval, deltas.Choices2] | None = None
        for choices in wording.choices:
            if choices[0].begin >= begin:
                next_choices = choices
                break

        next_manual_item: Interval | None = None
        for manual_item in wording.manual_items:
            if manual_item.begin >= begin:
                next_manual_item = manual_item
                break

        next_mcq_field: tuple[Interval, str] | None = None
        for mcq_field in wording.mcq_fields:
            if mcq_field[0].begin >= begin:
                next_mcq_field = mcq_field
                break

        return (next_choices, next_manual_item, next_mcq_field)

    def detect_list_header(self, wording: AnnotatedSection, begin: int, end: int) -> int | None:
        assert begin <= end, (begin, end)

        (next_choices, next_manual_item, next_mcq_field) = self.find_next_disruptions(wording, begin)
        next_disruption = min(
            end,
            end if next_choices is None else next_choices[0].begin,
            end if next_manual_item is None else next_manual_item.begin,
            end if next_mcq_field is None else next_mcq_field[0].begin,
        )

        # WARNING: keep the list formats supported here consistent with what's supported in 'listFormats' in 'TextPicker.vue'
        text = wording.text[begin:end]

        if (m := re.match(r"^\d+", text)) is None:
            number_prefix = None
        else:
            number_prefix = m.group(0)

        if number_prefix is not None and len(text) > len(number_prefix) and text[len(number_prefix)] in ").":
            # "1. 2. 3.", "1) 2) 3)", etc.
            after_list = begin + len(number_prefix) + 1
        elif len(text) > 1 and text[0] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" and text[1] in ").":
            # "a. b. c.", "A) B) C)", etc.
            after_list = begin + 2
        elif len(text) > 0 and text[0] in "◆■":
            # "◆", "■", etc.
            after_list = begin + 1
        else:
            after_list = None

        if after_list is not None and wording.text[after_list] != " ":  # Space required, but we tolerate if the space is after the next disruption
            after_list = None

        while after_list is not None and after_list < next_disruption and wording.text[after_list] == " ":
            after_list += 1

        return after_list

    def adapt_itemized_letters(self, wording: AnnotatedSection, begin: int, end: int, paragraph_index: int) -> Iterable[tuple[int, renderable.AnyRenderable]]:
        assert self.letters_are_items
        assert begin < end, (begin, end)

        for token_index, token in enumerate(re.split(r"(\.\.\.|\s+|\W)", wording.text[begin:end])):
            if token_index % 2 == 0:
                # Word
                for letter in token:
                    for r in self.decorate_item(self.adapt_formatted_text(wording, begin, begin + len(letter))):
                        yield (paragraph_index, r)
                    if self.single_item_per_paragraph:
                        paragraph_index += 1
                    begin += 1
            else:
                # Separator: whitespace or punctuation
                if token.strip() == "":
                    yield (paragraph_index, renderable.Whitespace(kind="whitespace"))
                else:
                    for r in self.adapt_formatted_text(wording, begin, begin + len(token)):
                        yield (paragraph_index, r)
                begin += len(token)

        assert begin == end, (begin, end)

    def adapt_itemized_words_and_punctuation(
        self, wording: AnnotatedSection, begin: int, end: int, paragraph_index: int
    ) -> Iterable[tuple[int, renderable.AnyRenderable]]:
        assert self.words_are_items or self.punctuation_is_items
        assert begin < end, (begin, end)

        # @todo Clarify spec with client, remove these weird specific cases.
        if self.words_are_items and not self.punctuation_is_items or self.words_are_items and self.punctuation_is_items and self.items_are_boxed:
            # Keep apostrophes near the preceding word, for French elision.
            regex = r"((?:(?=[^\u2019\u0027\u02BC])(?:\.\.\.|\s+|\W|\b)))"
        else:
            regex = r"(\.\.\.|\s+|\W)"

        for token_index, token in enumerate(re.split(regex, wording.text[begin:end])):
            if token_index % 2 == 0:
                if token != "":
                    # Word
                    r = self.adapt_formatted_text(wording, begin, begin + len(token))
                    if self.words_are_items:
                        for r2 in self.decorate_item(r):
                            yield (paragraph_index, r2)
                        if self.single_item_per_paragraph:
                            paragraph_index += 1
                    else:
                        for r2 in r:
                            yield (paragraph_index, r2)
            else:
                # Separator:
                if token.strip() == "":
                    if token != "":
                        # whitespace
                        yield (paragraph_index, renderable.Whitespace(kind="whitespace"))
                else:
                    # or punctuation
                    r = self.adapt_formatted_text(wording, begin, begin + len(token))
                    if self.punctuation_is_items:
                        for r2 in self.decorate_item(r):
                            yield (paragraph_index, r2)
                        if self.single_item_per_paragraph:
                            paragraph_index += 1
                    else:
                        for r2 in r:
                            yield (paragraph_index, r2)
            begin += len(token)

        assert begin == end, (begin, end)

    def adapt_itemized_sentences(self, wording: AnnotatedSection, begin: int, end: int, paragraph_index: int) -> Iterable[tuple[int, renderable.AnyRenderable]]:
        assert self.sentences_are_items
        assert begin < end, (begin, end)

        first = True

        def gen_sentence(b: int, e: int) -> Iterable[tuple[int, renderable.AnyRenderable]]:
            nonlocal paragraph_index
            nonlocal first

            if not first:
                yield (paragraph_index, renderable.Whitespace(kind="whitespace"))
            first = False
            if self.mcq_for_repeated_items is None:
                r = self.adapt_formatted_text(wording, b, e)
                for r2 in self.decorate_item(r):
                    yield (paragraph_index, r2)
            else:
                yield (paragraph_index, self.adapt_sentence_repeated_with_mcq(wording, b, e))
            if self.single_item_per_paragraph:
                paragraph_index += 1

        sentences_begin = begin
        for match in re.finditer(r"(.*?(:?\.\.\.|[.!?…]))\s*", wording.text[sentences_begin:end], flags=re.DOTALL):
            assert match.start() == begin - sentences_begin
            yield from gen_sentence(sentences_begin + match.start(1), sentences_begin + match.end(1))
            begin = sentences_begin + match.end()
        if begin < end:
            yield from gen_sentence(begin, end)

    def adapt_sentence_repeated_with_mcq(self, wording: AnnotatedSection, begin: int, end: int) -> renderable.AnySequence:
        assert begin < end, (begin, end)

        assert self.mcq_for_repeated_items is not None

        original_sentence: list[renderable.AnyRenderable] = []
        repeated_sentence: list[renderable.AnyRenderable] = []

        while begin < end:
            next_mcq_placeholder: Interval | None = None
            for mcq_placeholder in wording.mcq_placeholders:
                if mcq_placeholder.begin >= begin:
                    next_mcq_placeholder = mcq_placeholder
                    break

            next_disruption = min(end, end if next_mcq_placeholder is None else next_mcq_placeholder.begin)

            if begin < next_disruption:
                r = list(self.adapt_formatted_text(wording, begin, next_disruption))
                original_sentence.extend(r)
                repeated_sentence.extend(r)
                begin = next_disruption
            else:
                assert begin == next_disruption
                assert next_mcq_placeholder is not None
                original_sentence.extend(
                    self.adapt_formatted_text(
                        wording, next_mcq_placeholder.begin, next_mcq_placeholder.end, additional_format_parameters={"highlighted": "#ffff00"}
                    )
                )
                repeated_sentence.append(self.mcq_for_repeated_items)
                begin = next_mcq_placeholder.end

        assert begin == end, (begin, end, wording)

        return renderable.AnySequence(
            kind="sequence",
            contents=[
                renderable.AnySequence(kind="sequence", contents=original_sentence),
                renderable.AnySequence(kind="sequence", contents=repeated_sentence),
            ],
            vertical=True,
        )

    def adapt_separated_items(self, wording: AnnotatedSection, begin: int, end: int, paragraph_index: int) -> Iterable[tuple[int, renderable.AnyRenderable]]:
        assert self.separated_items_separator is not None
        assert begin < end, (begin, end)

        for token_index, token in enumerate(re.split(r"(\s*" + re.escape(self.separated_items_separator) + r"\s*)", wording.text[begin:end])):
            if token_index % 2 == 0:
                if token != "":
                    # Item
                    for r2 in self.decorate_item(self.adapt_formatted_text(wording, begin, begin + len(token))):
                        yield (paragraph_index, r2)
                    if self.single_item_per_paragraph:
                        paragraph_index += 1
            else:
                # Separator:
                yield (paragraph_index, renderable.Whitespace(kind="whitespace"))
            begin += len(token)

        assert begin == end, (begin, end)

    def decorate_item(self, r: Iterable[renderable.PassiveRenderable]) -> Iterable[renderable.AnyRenderable]:
        if self.items_are_selectable:
            yield renderable.SelectableInput(kind="selectableInput", contents=list(r), colors=self.colors_for_selectable_items, boxed=self.items_are_boxed)
        elif self.mcq_below_items is not None:
            rr = list(typing.cast(Iterable[renderable.AnyRenderable], r))
            if len(rr) == 1:
                rrr = rr[0]
            else:
                rrr = renderable.AnySequence(kind="sequence", contents=rr, vertical=False)
            yield renderable.AnySequence(kind="sequence", contents=[rrr, self.mcq_below_items], vertical=True)
        elif self.mcq_beside_items is not None:
            yield from r
            yield renderable.Whitespace(kind="whitespace")
            yield self.mcq_beside_items
        elif self.items_are_boxed:
            yield renderable.PassiveSequence(kind="passiveSequence", contents=list(r), boxed=True)
        elif self.items_have_gender_mcq_beside:
            yield from r
            yield renderable.Whitespace(kind="whitespace")
            yield renderable.MultipleChoicesInput(
                kind="multipleChoicesInput",
                show_arrow_before=True,
                choices=[
                    # @todo Support exercises in English?
                    [renderable.Text(kind="text", text="féminin")],
                    [renderable.Text(kind="text", text="masculin")],
                ],
                show_choices_by_default=self.show_mcq_choices_by_default,
            )
            if self.items_have_number_mcq_beside:
                yield renderable.Whitespace(kind="whitespace")
                yield renderable.MultipleChoicesInput(
                    kind="multipleChoicesInput",
                    show_arrow_before=False,
                    choices=[
                        # @todo Support exercises in English?
                        [renderable.Text(kind="text", text="singulier")],
                        [renderable.Text(kind="text", text="pluriel")],
                    ],
                    show_choices_by_default=self.show_mcq_choices_by_default,
                )
        elif self.items_have_number_mcq_beside:
            yield from r
            yield renderable.Whitespace(kind="whitespace")
            yield renderable.MultipleChoicesInput(
                kind="multipleChoicesInput",
                show_arrow_before=True,
                choices=[
                    # @todo Support exercises in English?
                    [renderable.Text(kind="text", text="singulier")],
                    [renderable.Text(kind="text", text="pluriel")],
                ],
                show_choices_by_default=self.show_mcq_choices_by_default,
            )
        else:
            yield from r

    def adapt_formatted_text(
        self, section: AnnotatedSection, begin: int, end: int, additional_format_parameters: dict[str, Any] = {}
    ) -> Iterable[renderable.PassiveLeafRenderable]:
        assert begin < end, (begin, end)

        for token_index, token in enumerate(re.split(r"(\.\.\.|\s+|\W)", section.text[begin:end])):
            token_begin = begin
            token_end = begin + len(token)
            character_formats: list[AnnotatedSection.Format] = [AnnotatedSection.Format(bold=False, italic=False, sel=None) for c in token]
            for interval, format in section.formats:
                if interval.begin < token_end and interval.end > token_begin:
                    for i in range(max(interval.begin, token_begin), min(interval.end, token_end)):
                        character_formats[i - token_begin] = format

            for format, characters in itertools.groupby(zip(character_formats, token, strict=True), lambda c: c[0]):
                format_parameters = dict(additional_format_parameters)
                if format.bold:
                    format_parameters["bold"] = True
                if format.italic:
                    format_parameters["italic"] = True
                if format.sel is not None and len(self.colors_for_selectable_items) > format.sel - 1:
                    format_parameters["highlighted"] = self.colors_for_selectable_items[format.sel - 1]

                text = "".join(c[1] for c in characters)
                if token_index % 2 == 1:
                    if token.strip() == "":
                        yield renderable.Whitespace(kind="whitespace", **format_parameters)
                    else:
                        yield renderable.Text(kind="text", text=text, **format_parameters)
                else:
                    if token.strip() != "":
                        yield renderable.Text(kind="text", text=text, **format_parameters)
                begin += len(text)

        assert begin == end, (begin, end)

    def adapt_multiple_choices(self, instructions: AnnotatedSection, begin: int, end: int, choices: deltas.Choices2) -> Iterable[renderable.PassiveRenderable]:
        choice_locations = self.extract_choice_locations(instructions, begin, end, choices)

        first = True
        for choice in choice_locations[:-1]:
            if not first:
                yield renderable.Text(kind="text", text=",")
                yield renderable.Whitespace(kind="whitespace")
            first = False
            yield renderable.PassiveSequence(
                kind="passiveSequence", contents=list(self.adapt_formatted_text(instructions, choice.begin, choice.end)), boxed=True
            )
        if len(choice_locations) > 1:
            yield renderable.Whitespace(kind="whitespace")
            yield renderable.Text(kind="text", text="ou")  # @todo Fix this if we ever support exercises in English
            yield renderable.Whitespace(kind="whitespace")
        yield renderable.PassiveSequence(
            kind="passiveSequence", contents=list(self.adapt_formatted_text(instructions, choice_locations[-1].begin, choice_locations[-1].end)), boxed=True
        )

    def make_multiple_choices_input(self, section: AnnotatedSection, begin: int, end: int, choices: deltas.Choices2) -> renderable.MultipleChoicesInput:
        choice_locations = self.extract_choice_locations(section, begin, end, choices)

        return renderable.MultipleChoicesInput(
            kind="multipleChoicesInput",
            choices=[list(self.adapt_formatted_text(section, choice.begin, choice.end)) for choice in choice_locations],
            show_arrow_before=self.show_arrow_before_mcq_fields,
            show_choices_by_default=self.show_mcq_choices_by_default,
        )

    def extract_choice_locations(self, section: AnnotatedSection, begin: int, end: int, choices: deltas.Choices2) -> list[Interval]:
        assert begin < end, (begin, end)

        begin, end = self.lstrip(section, begin, end)
        if section.text[begin : begin + len(choices.start)] == choices.start:
            begin += len(choices.start)

        begin, end = self.rstrip(section, begin, end)
        if section.text[end - len(choices.stop) : end] == choices.stop:
            end -= len(choices.stop)

        if choices.separator1 == "":
            choice_locations = [Interval(begin=begin, end=end)]
            begin = end
        else:
            choice_locations = []
            for token_index, token in enumerate(re.split(r"(" + re.escape(choices.separator1) + r")", section.text[begin:end])):
                if token_index % 2 == 0:
                    choice_locations.append(Interval(begin=begin, end=begin + len(token)))
                begin += len(token)

        if choices.separator2 != "" and len(choice_locations) > 0:
            begin = choice_locations[-1].begin
            choice_locations.pop()
            for token_index, token in enumerate(re.split(r"(" + re.escape(choices.separator2) + r")", section.text[begin:end])):
                if token_index % 2 == 0:
                    choice_locations.append(Interval(begin=begin, end=begin + len(token)))
                begin += len(token)

        for choice in choice_locations:
            choice.begin, choice.end = self.strip(section, choice.begin, choice.end)

        assert begin == end, (begin, end)

        return list(filter(lambda c: c.begin < c.end, choice_locations))

    def remove_empty_paragraphs(self, paragraphs: Iterable[renderable.Paragraph]) -> Iterable[renderable.Paragraph]:
        for p in paragraphs:
            if len(p.contents) > 0:
                yield p

    def lstrip(self, section: AnnotatedSection, begin: int, end: int) -> tuple[int, int]:
        while begin < end and section.text[begin].strip() == "":
            begin += 1
        return begin, end

    def rstrip(self, section: AnnotatedSection, begin: int, end: int) -> tuple[int, int]:
        while end > begin and section.text[end - 1].strip() == "":
            end -= 1
        return begin, end

    def strip(self, section: AnnotatedSection, begin: int, end: int) -> tuple[int, int]:
        return self.rstrip(section, *self.lstrip(section, begin, end))

    def strip_whitespace_renderables(self, renderables: Iterable[renderable.AnyRenderable]) -> Iterable[renderable.AnyRenderable]:
        """
        Remove leading and trailing whitespace; replace strides of several whitespace by a single one.
        """
        content_seen = False
        in_stock: list[renderable.AnyRenderable] = []
        for r in renderables:
            if r.kind == "whitespace":
                if content_seen:
                    in_stock.append(r)
            else:
                content_seen = True
                yield from in_stock[0:1]
                in_stock = []
                yield r

    def make_pagelets(
        self, wording_paragraphs_per_pagelet: int | None, instructions: list[renderable.Paragraph], wording: list[list[renderable.Paragraph]]
    ) -> Iterable[renderable.Pagelet]:
        for manual_wording_pagelet in wording:
            has_yielded = False
            current_paragraphs = []
            for paragraph in manual_wording_pagelet:
                current_paragraphs.append(paragraph)
                if len(current_paragraphs) == wording_paragraphs_per_pagelet:
                    has_yielded = True
                    yield self.make_pagelet(instructions, current_paragraphs)
                    current_paragraphs = []
            if len(current_paragraphs) > 0 or not has_yielded:
                yield self.make_pagelet(instructions, current_paragraphs)

    def make_pagelet(self, instructions: list[renderable.Paragraph], wording: list[renderable.Paragraph]) -> renderable.Pagelet:
        return renderable.Pagelet(instructions=renderable.Section(paragraphs=instructions), wording=renderable.Section(paragraphs=wording))


class AdaptationTestCase(unittest.TestCase):
    maxDiff = None
    generate_frontend_tests = True

    @classmethod
    @typing.no_type_check
    def setUpClass(cls):
        cls.tests_to_generate = []
        return super().setUpClass()

    @classmethod
    @typing.no_type_check
    def tearDownClass(cls):
        def generate():
            yield "import TricolorSection from './TricolorSection.vue'"
            yield ""
            yield f"describe('TricolorSection for {cls.__name__}', () => " "{"
            yield "  beforeEach(() => {"
            yield "    cy.viewport(1000, 100)"
            yield "  })"
            seen_paragraphs = set()
            for test_id, adapted in cls.tests_to_generate:
                for pagelet_index, pagelet in enumerate(adapted.pagelets):
                    for section_name in ["instructions", "wording"]:
                        paragraphs = "\n        ".join(
                            line
                            for line in json.dumps(
                                getattr(pagelet, section_name).model_dump(by_alias=True, exclude_defaults=True)["paragraphs"],
                                indent=2,
                            ).splitlines()
                        )
                        if paragraphs in seen_paragraphs:
                            continue
                        seen_paragraphs.add(paragraphs)
                        yield ""
                        yield f"  it('renders {test_id} pagelet {pagelet_index} {section_name}', () => " "{"
                        yield "    cy.mount(TricolorSection, {"
                        yield "      props: {"
                        yield f"        paragraphs: {paragraphs},"
                        yield "        modelValue: {},"
                        yield "      },"
                        yield "    })"
                        yield f"    cy.screenshot('{test_id}.{pagelet_index}.{section_name}')"
                        yield "  })"
            yield "})"

        if cls.generate_frontend_tests:
            with open(f"../frontend/src/adapted/components/TricolorSection.{cls.__name__}.generated.cy.js", "w") as f:
                for line in generate():
                    f.write(line)
                    f.write("\n")

        return super().tearDownClass()

    @typing.no_type_check
    def do_test(self, exercise: exercises.Exercise, expected_adapted: renderable.Exercise):
        self.tests_to_generate.append((self.id(), expected_adapted))

        actual_adapted = exercise.make_adapted()
        if actual_adapted != expected_adapted:
            calling_frame = traceback.extract_stack()[-2]

            print(f"actual_adapted at {calling_frame.filename}:{calling_frame.lineno}:", self.renderable_repr(actual_adapted))
        for pagelet_index, (actual_pagelet, expected_pagelet) in enumerate(itertools.zip_longest(actual_adapted.pagelets, expected_adapted.pagelets)):
            actual_instructions = None if actual_pagelet is None else actual_pagelet.instructions.paragraphs
            expected_instructions = None if expected_pagelet is None else expected_pagelet.instructions.paragraphs
            if actual_instructions != expected_instructions:
                self.fail(
                    f"pagelet {pagelet_index} instructions paragraphs are:\n{self.renderable_repr(actual_instructions)}\ninstead of:\n{self.renderable_repr(expected_instructions)}",
                )
            actual_wording = None if actual_pagelet is None else actual_pagelet.wording.paragraphs
            expected_wording = None if expected_pagelet is None else expected_pagelet.wording.paragraphs
            if actual_wording != expected_wording:
                self.fail(
                    f"pagelet {pagelet_index} wording paragraphs are:\n{self.renderable_repr(actual_wording)}\ninstead of:\n{self.renderable_repr(expected_wording)}",
                )
        if actual_adapted != expected_adapted:
            self.fail(f"adapted is:\n{self.renderable_repr(actual_adapted)}\ninstead of:\n{self.renderable_repr(expected_adapted)}")

    @staticmethod
    @typing.no_type_check
    def renderable_repr(rend):
        r = (
            repr([rend])[1:-1]
            .replace("Exercise(", "r.Exercise(")
            .replace("Pagelet(", "r.Pagelet(")
            .replace("Section(", "r.Section(")
            .replace("Paragraph(", "r.Paragraph(")
            .replace("Text(", "r.Text(")
            .replace("Whitespace(", "r.Whitespace(")
            .replace("FreeTextInput(", "r.FreeTextInput(")
            .replace("MultipleChoicesInput(", "r.MultipleChoicesInput(")
            .replace("SelectableInput(", "r.SelectableInput(")
            .replace("PassiveSequence(", "r.PassiveSequence(")
            .replace("AnySequence(", "r.AnySequence(")
            .replace("bold=False", "")
            .replace("italic=False", "")
            .replace("highlighted=None", "")
            .replace("boxed=False", "")
            .replace("show_arrow_before=False", "")
            .replace("show_choices_by_default=False", "")
            .replace("vertical=False", "")
        )
        while (new_r := r.replace(", , ", ", ").replace(", )", ")")) != r:
            r = new_r
        return r
