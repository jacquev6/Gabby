from __future__ import annotations

from typing import Iterable
import copy
import itertools
import json
import os
import re
import traceback
import unittest

from . import deltas
from . import deltas as d
from . import exercises
from . import exercises as e
from . import new_renderable
from . import new_renderable as nr
from . import renderable
from . import renderable as r
from .api_models import Adaptation, TokensItems, Selectable


def old_adapt(exercise: exercises.Exercise) -> renderable.Exercise:
    return _OldAdapter(exercise).adapted


class _OldAdapter:
    def __init__(self, exercise: exercises.Exercise):
        self.show_mcq_choices_by_default = exercise.adaptation.show_mcq_choices_by_default
        self.show_arrow_before_mcq_fields = exercise.adaptation.show_arrow_before_mcq_fields
        self.global_placeholders: list[tuple[str, renderable.SentenceToken]] = []
        self.letters_are_items = False
        self.words_are_items = False
        self.punctuation_is_items = False
        self.sentences_are_items = False
        self.manual_items_are_items = False
        self.items_are_selectable = False
        self.items_are_boxed = False
        self.colors_for_selectable_items = []
        self.items_have_mcq_beside = exercise.adaptation.items_have_mcq_beside
        self.mcq_beside_items = None
        self.items_have_mcq_below = exercise.adaptation.items_have_mcq_below
        self.mcq_below_items = None

        if exercise.adaptation.placeholder_for_fill_with_free_text is not None:
            self.global_placeholders.append((exercise.adaptation.placeholder_for_fill_with_free_text, renderable.FreeTextInput()))

        if exercise.adaptation.items is not None:
            self.letters_are_items = exercise.adaptation.items.kind == "characters" and exercise.adaptation.items.letters
            self.words_are_items = exercise.adaptation.items.kind == "tokens" and exercise.adaptation.items.words
            self.punctuation_is_items = exercise.adaptation.items.kind == "tokens" and exercise.adaptation.items.punctuation
            self.sentences_are_items = exercise.adaptation.items.kind == "sentences"
            self.manual_items_are_items = exercise.adaptation.items.kind == "manual"
            self.items_are_boxed = exercise.adaptation.items_are_boxed
            if exercise.adaptation.items_are_selectable is not None:
                self.items_are_selectable = True
                self.colors_for_selectable_items = exercise.adaptation.items_are_selectable.colors

        for start, separator1, separator2, stop, placeholder, text in self.gather_choices(exercise.instructions):
            if placeholder == "":
                mcq = renderable.MultipleChoicesInput(
                    show_arrow_before=self.show_arrow_before_mcq_fields,
                    choices=self.separate_choices(start, separator1, separator2, stop, placeholder, text),
                    show_choices_by_default=self.show_mcq_choices_by_default,
                )
                if self.items_have_mcq_beside:
                    self.mcq_beside_items = mcq
                elif self.items_have_mcq_below:
                    self.mcq_below_items = mcq
            else:
                self.global_placeholders.append(
                    (
                        placeholder,
                        renderable.MultipleChoicesInput(
                            show_arrow_before=self.show_arrow_before_mcq_fields,
                            choices=self.separate_choices(start, separator1, separator2, stop, placeholder, text),
                            show_choices_by_default=self.show_mcq_choices_by_default,
                        ),
                    ),
                )

        instructions = self.postprocess_section(
            renderable.Section(
                paragraphs=list(
                    itertools.chain.from_iterable(self.adapt_instructions(part) for part in [exercise.instructions, exercise.example, exercise.clue])
                )
            )
        )

        pagelets = list(
            renderable.Pagelet(
                instructions=instructions,
                wording=self.postprocess_section(renderable.Section(paragraphs=wording_paragraphs)),
            )
            for wording_paragraphs in self.adapt_wording(exercise.wording, exercise.wording_paragraphs_per_pagelet)
        )

        if exercise.text_reference != deltas.empty:
            pagelets.append(
                renderable.Pagelet(
                    instructions=self.postprocess_section(renderable.Section(paragraphs=list(self.adapt_instructions(exercise.text_reference)))),
                    wording=renderable.Section(paragraphs=[]),
                )
            )

        self.adapted = renderable.Exercise(number=exercise.number, textbook_page=exercise.textbook_page, pagelets=pagelets)

    def adapt_instructions(self, instructions: deltas.Deltas) -> Iterable[renderable.Paragraph]:
        for paragraph_deltas in self.split_deltas(instructions, r"\s*\n\s*\n\s*"):
            for sentence_deltas in self.split_deltas_into_sentences(paragraph_deltas):
                yield renderable.Paragraph(tokens=list(self.adapt_instructions_sentence(sentence_deltas)))

    def adapt_instructions_sentence(self, sentence_deltas: deltas.Deltas):
        for delta in sentence_deltas:
            if delta.attributes == {}:
                for text in re.split(r"(\.\.\.|\s+|\W)", delta.insert):
                    if text != "":
                        if text.strip() == "":
                            yield renderable.Whitespace()
                        else:
                            yield renderable.PlainText(text=text)

            elif "sel" in delta.attributes:
                assert delta.attributes == {"sel": delta.attributes["sel"]}

                if len(self.colors_for_selectable_items) > delta.attributes["sel"] - 1:
                    yield renderable.SelectedText(text=delta.insert, color=self.colors_for_selectable_items[delta.attributes["sel"] - 1])
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

                choices = self.separate_choices(start, separator1, separator2, stop, placeholder, text)
                # Always format choices the same way in instructions: https://github.com/jacquev6/Gabby/issues/74
                yield renderable.BoxedText(text=choices[0])
                for choice in choices[1:-1]:
                    yield renderable.PlainText(text=",")
                    yield renderable.Whitespace()
                    yield renderable.BoxedText(text=choice)
                if len(choices) > 1:
                    yield renderable.Whitespace()
                    yield renderable.PlainText(text="ou")  # @todo Fix this if we ever support exercises in English
                    yield renderable.Whitespace()
                    yield renderable.BoxedText(text=choices[-1])

            elif "bold" in delta.attributes or "italic" in delta.attributes:
                assert set(delta.attributes.keys()) <= {"bold", "italic"}

                yield renderable.PassiveFormattedText(
                    type="passiveFormattedText", text=delta.insert, bold=delta.attributes.get("bold", False), italic=delta.attributes.get("italic", False)
                )

            else:
                assert False, f"Unknown attributes: {delta.attributes}"

    def adapt_wording(self, wording: deltas.Deltas, wording_paragraphs_per_pagelet: int | None) -> Iterable[list[renderable.Paragraph]]:
        current_pagelet = []
        has_yielded = False
        for pagelet_deltas in self.split_deltas(wording, r"\s*\n\s*\n\s*\n\s*"):
            if len(pagelet_deltas) != 0:
                for paragraph in self.adapt_wording_pagelet(pagelet_deltas):
                    current_pagelet.append(paragraph)
                    if len(current_pagelet) == wording_paragraphs_per_pagelet:
                        yield current_pagelet
                        current_pagelet = []
                        has_yielded = True
            if len(current_pagelet) > 0:
                yield current_pagelet
                current_pagelet = []
                has_yielded = True
        if not has_yielded:
            yield []

    def adapt_wording_pagelet(self, pagelet_deltas: deltas.Deltas) -> Iterable[renderable.Paragraph]:
        for delta in pagelet_deltas:
            if delta.attributes == {}:
                for index, (placeholder, _token) in enumerate(self.global_placeholders):
                    delta.insert = delta.insert.replace(placeholder, f"ph{index}hp")

        return [
            renderable.Paragraph(tokens=list(self.adapt_wording_paragraph(paragraph_deltas)))
            for paragraph_deltas in self.split_deltas(pagelet_deltas, r"\s*\n\s*")
        ]

    def adapt_wording_paragraph(self, paragraph_deltas: deltas.Deltas):
        sentence_specific_placeholders = []

        for start, separator1, separator2, stop, placeholder, text in self.gather_choices(paragraph_deltas):
            if placeholder != "":
                sentence_specific_placeholders.append(
                    (
                        placeholder,
                        renderable.MultipleChoicesInput(
                            show_arrow_before=self.show_arrow_before_mcq_fields,
                            choices=self.separate_choices(start, separator1, separator2, stop, placeholder, text),
                            show_choices_by_default=self.show_mcq_choices_by_default,
                        ),
                    ),
                )

        for delta in paragraph_deltas:
            if delta.attributes == {}:
                for index, (placeholder, _token) in enumerate(sentence_specific_placeholders):
                    delta.insert = delta.insert.replace(placeholder, f"ph{len(self.global_placeholders) + index}hp")

        sentence_placeholders = list(itertools.chain(self.global_placeholders, sentence_specific_placeholders))

        list_header_deltas, paragraph_deltas = self.split_list_header(paragraph_deltas)

        if len(list_header_deltas) > 0:
            for delta in list_header_deltas:
                for text in re.split(r"(\.\.\.|\s+|\W|ph\d+hp)", delta.insert):
                    if text != "":
                        yield renderable.PlainText(text=text)
            yield renderable.Whitespace()

        if self.sentences_are_items:
            assert not self.letters_are_items
            assert not self.words_are_items
            assert not self.punctuation_is_items
            is_first_sentence = True
            for sentence_deltas in self.split_deltas_into_sentences(paragraph_deltas):
                if not is_first_sentence:
                    yield renderable.Whitespace()
                is_first_sentence = False
                contents = list(self.adapt_wording_sentence(sentence_deltas, sentence_placeholders))
                while contents[0].type == "whitespace":
                    contents.pop(0)
                if self.items_are_selectable:
                    contents = [renderable.Selectable(contents=contents, colors=self.colors_for_selectable_items, boxed=self.items_are_boxed)]
                elif self.items_are_boxed:
                    contents = [renderable.Boxed(contents=contents)]
                else:
                    pass
                if self.mcq_below_items is None:
                    yield from contents
                    if self.mcq_beside_items is not None:
                        yield renderable.Whitespace()
                        yield self.mcq_beside_items
                else:
                    yield renderable.Stack(type="stack", contents=[renderable.Line(type="line", contents=contents), self.mcq_below_items])
        else:
            yield from self.adapt_wording_sentence(paragraph_deltas, sentence_placeholders)

    def adapt_wording_sentence(self, sentence_deltas: deltas.Deltas, sentence_placeholders: list[tuple[str, renderable.SentenceToken]]):
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
                                if self.punctuation_is_items:
                                    if self.items_are_selectable:
                                        item = renderable.SelectableText(text=text, colors=self.colors_for_selectable_items, boxed=self.items_are_boxed)
                                    elif self.items_are_boxed:
                                        item = renderable.BoxedText(text=text)
                                    else:
                                        item = renderable.PlainText(text=text)
                                    if self.mcq_below_items is None:
                                        yield item
                                        if self.mcq_beside_items is not None:
                                            yield renderable.Whitespace()
                                            yield self.mcq_beside_items
                                    else:
                                        yield renderable.Stack(type="stack", contents=[item, self.mcq_below_items])
                                else:
                                    yield renderable.PlainText(text=text)
                        else:
                            # Separated: words
                            if self.letters_are_items:
                                for letter in text:
                                    if self.items_are_selectable:
                                        item = renderable.SelectableText(text=letter, colors=self.colors_for_selectable_items, boxed=self.items_are_boxed)
                                    elif self.items_are_boxed:
                                        item = renderable.BoxedText(text=letter)
                                    else:
                                        item = renderable.PlainText(text=letter)
                                    if self.mcq_below_items is None:
                                        yield item
                                        if self.mcq_beside_items is not None:
                                            yield renderable.Whitespace()
                                            yield self.mcq_beside_items
                                    else:
                                        yield renderable.Stack(type="stack", contents=[item, self.mcq_below_items])
                            elif self.words_are_items:
                                if self.items_are_selectable:
                                    item = renderable.SelectableText(text=text, colors=self.colors_for_selectable_items, boxed=self.items_are_boxed)
                                elif self.items_are_boxed:
                                    item = renderable.BoxedText(text=text)
                                else:
                                    item = renderable.PlainText(text=text)
                                if self.mcq_below_items is None:
                                    yield item
                                    if self.mcq_beside_items is not None:
                                        yield renderable.Whitespace()
                                        yield self.mcq_beside_items
                                else:
                                    yield renderable.Stack(type="stack", contents=[item, self.mcq_below_items])
                            else:
                                yield renderable.PlainText(text=text)

            elif "manual-item" in delta.attributes:
                assert delta.attributes == {"manual-item": delta.attributes["manual-item"]}

                for text in re.split(r"(\.\.\.|\s+|\W)", delta.insert):
                    if text != "":
                        if text.strip() == "":
                            yield renderable.Whitespace()
                        else:
                            if self.manual_items_are_items:
                                if self.items_are_selectable:
                                    item = renderable.SelectableText(text=text, colors=self.colors_for_selectable_items, boxed=self.items_are_boxed)
                                elif self.items_are_boxed:
                                    item = renderable.BoxedText(text=text)
                                else:
                                    item = renderable.PlainText(text=text)
                                if self.mcq_below_items is None:
                                    yield item
                                    if self.mcq_beside_items is not None:
                                        yield renderable.Whitespace()
                                        yield self.mcq_beside_items
                                else:
                                    yield renderable.Stack(type="stack", contents=[item, self.mcq_below_items])
                            else:
                                yield renderable.PlainText(text=text)

            elif "bold" in delta.attributes or "italic" in delta.attributes:
                assert set(delta.attributes.keys()) <= {"bold", "italic"}

                yield renderable.PassiveFormattedText(
                    type="passiveFormattedText", text=delta.insert, bold=delta.attributes.get("bold", False), italic=delta.attributes.get("italic", False)
                )

            elif "choices2" in delta.attributes:
                assert delta.attributes == {"choices2": delta.attributes["choices2"]}

                choices_settings = delta.attributes["choices2"]
                placeholder = choices_settings["placeholder"] or None
                if placeholder is None:
                    start = choices_settings["start"] or None
                    separator1 = choices_settings["separator1"] or None
                    separator2 = choices_settings["separator2"] or None
                    stop = choices_settings["stop"] or None
                    yield renderable.MultipleChoicesInput(
                        show_arrow_before=self.show_arrow_before_mcq_fields,
                        choices=self.separate_choices(start, separator1, separator2, stop, placeholder, delta.insert),
                        show_choices_by_default=self.show_mcq_choices_by_default,
                    )

            else:
                assert False, f"Unknown attributes: {delta.attributes}"

    def split_deltas(self, section_deltas: deltas.Deltas, explicit_paragraph_separator_pattern: str) -> Iterable[deltas.Deltas]:
        section_deltas = copy.deepcopy(section_deltas)
        assert len(section_deltas) > 0
        section_deltas[0].insert = section_deltas[0].insert.lstrip()
        section_deltas[-1].insert = section_deltas[-1].insert.rstrip()

        current_paragraph = []
        for delta in section_deltas:
            if "choices2" in delta.attributes:
                current_paragraph.append(delta)
            else:
                for i, paragraph_part in enumerate(re.split(explicit_paragraph_separator_pattern, delta.insert)):
                    if i > 0:
                        yield current_paragraph
                        current_paragraph = []
                    if paragraph_part != "":
                        current_paragraph.append(d.InsertOp(insert=paragraph_part, attributes=delta.attributes))
        yield current_paragraph

    def split_deltas_into_sentences(self, paragraph_deltas: deltas.Deltas) -> Iterable[deltas.Deltas]:
        current_sentence = []
        for delta in paragraph_deltas:
            if "choices2" in delta.attributes:
                current_sentence.append(delta)
            else:
                for i, sentence_part in enumerate(re.split(r"(\.\.\.|[.!?…])", delta.insert)):
                    if sentence_part != "":
                        if i % 2 == 0 and i > 1:
                            yield current_sentence
                            current_sentence = []
                        current_sentence.append(d.InsertOp(insert=sentence_part, attributes=delta.attributes))
        yield current_sentence

    def split_list_header(self, paragraph_deltas: deltas.Deltas) -> tuple[deltas.Deltas, deltas.Deltas]:
        if len(paragraph_deltas) == 0:
            return ([], [])
        else:
            # WARNING: keep the list formats supported here consistent with what's supported in 'listFormats' in 'TextPicker.vue'
            list_header_deltas = []
            paragraph_deltas = copy.deepcopy(paragraph_deltas)

            number_prefix = re.match(r"^\d+", paragraph_deltas[0].insert)
            if number_prefix is not None:
                number_prefix = number_prefix.group(0)

            if number_prefix is not None and len(paragraph_deltas[0].insert) > len(number_prefix) and paragraph_deltas[0].insert[len(number_prefix)] in ").":
                # "1. 2. 3.", "1) 2) 3)", etc.
                list_header_deltas.append(
                    deltas.InsertOp(insert=paragraph_deltas[0].insert[: len(number_prefix) + 1], attributes=paragraph_deltas[0].attributes)
                )
                paragraph_deltas[0].insert = paragraph_deltas[0].insert[len(number_prefix) + 1 :].lstrip()
            elif (
                len(paragraph_deltas[0].insert) > 1
                and paragraph_deltas[0].insert[0] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                and paragraph_deltas[0].insert[1] in ")."
            ):
                # "a. b. c.", "A) B) C)", etc.
                list_header_deltas.append(deltas.InsertOp(insert=paragraph_deltas[0].insert[:2], attributes=paragraph_deltas[0].attributes))
                paragraph_deltas[0].insert = paragraph_deltas[0].insert[2:].lstrip()
            elif len(paragraph_deltas[0].insert) > 0 and paragraph_deltas[0].insert[0] in "◆■":
                # "◆", "■", etc.
                list_header_deltas.append(deltas.InsertOp(insert=paragraph_deltas[0].insert[0], attributes=paragraph_deltas[0].attributes))
                paragraph_deltas[0].insert = paragraph_deltas[0].insert[1:].lstrip()

            return (list_header_deltas, paragraph_deltas)

    __apostrophes = [
        # https://fr.wikipedia.org/wiki/Apostrophe_(typographie) mentions one more encoding than https://en.wikipedia.org/wiki/Apostrophe
        "\u2019",
        "\u0027",
        "\u02BC",
    ]

    def postprocess_section(self, section: renderable.Section) -> renderable.Section:
        section = copy.deepcopy(section)
        for paragraph in section.paragraphs:
            fixed_tokens = []
            for token in paragraph.tokens:
                if token.type == "whitespace" and len(fixed_tokens) == 0:
                    pass
                elif token.type == "whitespace" and len(fixed_tokens) > 0 and fixed_tokens[-1].type == "whitespace":
                    pass
                elif (
                    token.type in ["plainText", "selectableText", "boxedText"]
                    and token.text in self.__apostrophes
                    and len(fixed_tokens) > 0
                    and fixed_tokens[-1].type in ["selectableText", "boxedText"]
                ):
                    fixed_tokens[-1].text += token.text
                else:
                    fixed_tokens.append(token)
            while len(fixed_tokens) > 0 and fixed_tokens[-1].type == "whitespace":
                fixed_tokens.pop(-1)
            paragraph.tokens = fixed_tokens
        section.paragraphs = list(filter(lambda p: len(p.tokens) > 0, section.paragraphs))
        return section

    def gather_choices(self, deltas):
        for delta in deltas:
            if "choices2" in delta.attributes:
                choices_settings = delta.attributes["choices2"]
                yield (
                    choices_settings["start"] or None,
                    choices_settings["separator1"] or None,
                    choices_settings["separator2"] or None,
                    choices_settings["stop"] or None,
                    choices_settings["placeholder"],
                    delta.insert,
                )

    def separate_choices(self, start, separator1, separator2, stop, placeholder, text):
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


def new_adapt(exercise: exercises.Exercise) -> new_renderable.Exercise | None:
    return _NewAdapter(exercise).adapted


class _NewAdapter:
    def __init__(self, exercise: exercises.Exercise):
        self.show_mcq_choices_by_default = exercise.adaptation.show_mcq_choices_by_default
        self.show_arrow_before_mcq_fields = exercise.adaptation.show_arrow_before_mcq_fields
        self.global_placeholders: list[tuple[str, new_renderable.AnyRenderable]] = []
        self.letters_are_items = False
        self.words_are_items = False
        self.punctuation_is_items = False
        self.sentences_are_items = False
        self.manual_items_are_items = False
        self.items_are_selectable = False
        self.items_are_boxed = False
        self.colors_for_selectable_items = []
        self.items_have_mcq_beside = exercise.adaptation.items_have_mcq_beside
        self.mcq_beside_items = None
        self.items_have_mcq_below = exercise.adaptation.items_have_mcq_below
        self.mcq_below_items = None

        if exercise.adaptation.placeholder_for_fill_with_free_text is not None:
            self.global_placeholders.append((exercise.adaptation.placeholder_for_fill_with_free_text, new_renderable.FreeTextInput(kind="freeTextInput")))

        if exercise.adaptation.items is not None:
            self.letters_are_items = exercise.adaptation.items.kind == "characters" and exercise.adaptation.items.letters
            self.words_are_items = exercise.adaptation.items.kind == "tokens" and exercise.adaptation.items.words
            self.punctuation_is_items = exercise.adaptation.items.kind == "tokens" and exercise.adaptation.items.punctuation
            self.sentences_are_items = exercise.adaptation.items.kind == "sentences"
            self.manual_items_are_items = exercise.adaptation.items.kind == "manual"
            self.items_are_boxed = exercise.adaptation.items_are_boxed
            if exercise.adaptation.items_are_selectable is not None:
                self.items_are_selectable = True
                self.colors_for_selectable_items = exercise.adaptation.items_are_selectable.colors

        for start, separator1, separator2, stop, placeholder, text in self.gather_choices(exercise.instructions):
            if placeholder == "":
                mcq = new_renderable.MultipleChoicesInput(
                    kind="multipleChoicesInput",
                    show_arrow_before=self.show_arrow_before_mcq_fields,
                    choices=self.separate_choices(start, separator1, separator2, stop, placeholder, text),
                    show_choices_by_default=self.show_mcq_choices_by_default,
                )
                if self.items_have_mcq_beside:
                    self.mcq_beside_items = mcq
                elif self.items_have_mcq_below:
                    self.mcq_below_items = mcq
            else:
                self.global_placeholders.append(
                    (
                        placeholder,
                        new_renderable.MultipleChoicesInput(
                            kind="multipleChoicesInput",
                            show_arrow_before=self.show_arrow_before_mcq_fields,
                            choices=self.separate_choices(start, separator1, separator2, stop, placeholder, text),
                            show_choices_by_default=self.show_mcq_choices_by_default,
                        ),
                    ),
                )

        instructions = self.postprocess_section(
            new_renderable.Section(
                paragraphs=list(
                    itertools.chain.from_iterable(
                        self.adapt_instructions(part)
                        for part in [
                            exercise.instructions,
                            exercise.example,
                            exercise.clue,
                        ]
                    )
                )
            )
        )

        pagelets = list(
            new_renderable.Pagelet(
                instructions=instructions,
                wording=self.postprocess_section(new_renderable.Section(paragraphs=wording_paragraphs)),
            )
            for wording_paragraphs in self.adapt_wording(exercise.wording, exercise.wording_paragraphs_per_pagelet)
        )

        if exercise.text_reference != deltas.empty:
            pagelets.append(
                new_renderable.Pagelet(
                    instructions=self.postprocess_section(new_renderable.Section(paragraphs=list(self.adapt_instructions(exercise.text_reference)))),
                    wording=new_renderable.Section(paragraphs=[]),
                )
            )

        self.adapted = new_renderable.Exercise(number=exercise.number, textbook_page=exercise.textbook_page, pagelets=pagelets)

    def adapt_instructions(self, instructions: deltas.Deltas) -> Iterable[new_renderable.Paragraph]:
        for paragraph_deltas in self.split_deltas(instructions, r"\s*\n\s*\n\s*"):
            for sentence_deltas in self.split_deltas_into_sentences(paragraph_deltas):
                yield new_renderable.Paragraph(contents=list(self.adapt_instructions_sentence(sentence_deltas)))

    def adapt_instructions_sentence(self, sentence_deltas: deltas.Deltas):
        for delta in sentence_deltas:
            if delta.attributes == {}:
                for text in re.split(r"(\.\.\.|\s+|\W)", delta.insert):
                    if text != "":
                        if text.strip() == "":
                            yield new_renderable.Whitespace(kind="whitespace")
                        else:
                            yield new_renderable.Text(kind="text", text=text)

            elif "sel" in delta.attributes:
                assert delta.attributes == {"sel": delta.attributes["sel"]}

                if len(self.colors_for_selectable_items) > delta.attributes["sel"] - 1:
                    yield new_renderable.Text(kind="text", text=delta.insert, highlighted=self.colors_for_selectable_items[delta.attributes["sel"] - 1])
                else:
                    yield new_renderable.Text(kind="text", text=delta.insert)

            elif "choices2" in delta.attributes:
                assert delta.attributes == {"choices2": delta.attributes["choices2"]}

                start = delta.attributes["choices2"]["start"] or None
                separator1 = delta.attributes["choices2"]["separator1"] or None
                separator2 = delta.attributes["choices2"]["separator2"] or None
                stop = delta.attributes["choices2"]["stop"] or None
                placeholder = delta.attributes["choices2"]["placeholder"] or None
                text = delta.insert

                choices = self.separate_choices(start, separator1, separator2, stop, placeholder, text)
                # Always format choices the same way in instructions: https://github.com/jacquev6/Gabby/issues/74
                yield new_renderable.PassiveSequence(kind="passiveSequence", contents=choices[0], boxed=True)
                for choice in choices[1:-1]:
                    yield new_renderable.Text(kind="text", text=",")
                    yield new_renderable.Whitespace(kind="whitespace")
                    yield new_renderable.PassiveSequence(kind="passiveSequence", contents=choice, boxed=True)
                if len(choices) > 1:
                    yield new_renderable.Whitespace(kind="whitespace")
                    yield new_renderable.Text(kind="text", text="ou")  # @todo Fix this if we ever support exercises in English
                    yield new_renderable.Whitespace(kind="whitespace")
                    yield new_renderable.PassiveSequence(kind="passiveSequence", contents=choices[-1], boxed=True)

            elif "bold" in delta.attributes or "italic" in delta.attributes:
                assert set(delta.attributes.keys()) <= {"bold", "italic"}

                yield new_renderable.Text(
                    kind="text",
                    text=delta.insert,
                    bold=delta.attributes.get("bold", False),
                    italic=delta.attributes.get("italic", False),
                )

            else:
                assert False, f"Unknown attributes: {delta.attributes}"

    def adapt_wording(self, wording: deltas.Deltas, wording_paragraphs_per_pagelet: int | None) -> Iterable[list[new_renderable.Paragraph]]:
        current_pagelet = []
        has_yielded = False
        for pagelet_deltas in self.split_deltas(wording, r"\s*\n\s*\n\s*\n\s*"):
            if len(pagelet_deltas) != 0:
                for paragraph in self.adapt_wording_pagelet(pagelet_deltas):
                    current_pagelet.append(paragraph)
                    if len(current_pagelet) == wording_paragraphs_per_pagelet:
                        yield current_pagelet
                        current_pagelet = []
                        has_yielded = True
            if len(current_pagelet) > 0:
                yield current_pagelet
                current_pagelet = []
                has_yielded = True
        if not has_yielded:
            yield []

    def adapt_wording_pagelet(self, pagelet_deltas: deltas.Deltas) -> Iterable[new_renderable.Paragraph]:
        for delta in pagelet_deltas:
            if delta.attributes == {}:
                for index, (placeholder, _token) in enumerate(self.global_placeholders):
                    delta.insert = delta.insert.replace(placeholder, f"ph{index}hp")

        return [
            new_renderable.Paragraph(contents=list(self.adapt_wording_paragraph(paragraph_deltas)))
            for paragraph_deltas in self.split_deltas(pagelet_deltas, r"\s*\n\s*")
        ]

    def adapt_wording_paragraph(self, paragraph_deltas: deltas.Deltas):
        sentence_specific_placeholders = []

        for (
            start,
            separator1,
            separator2,
            stop,
            placeholder,
            text,
        ) in self.gather_choices(paragraph_deltas):
            if placeholder != "":
                sentence_specific_placeholders.append(
                    (
                        placeholder,
                        new_renderable.MultipleChoicesInput(
                            kind="multipleChoicesInput",
                            show_arrow_before=self.show_arrow_before_mcq_fields,
                            choices=self.separate_choices(start, separator1, separator2, stop, placeholder, text),
                            show_choices_by_default=self.show_mcq_choices_by_default,
                        ),
                    ),
                )

        for delta in paragraph_deltas:
            if delta.attributes == {}:
                for index, (placeholder, _token) in enumerate(sentence_specific_placeholders):
                    delta.insert = delta.insert.replace(placeholder, f"ph{len(self.global_placeholders) + index}hp")

        sentence_placeholders = list(itertools.chain(self.global_placeholders, sentence_specific_placeholders))

        list_header_deltas, paragraph_deltas = self.split_list_header(paragraph_deltas)

        if len(list_header_deltas) > 0:
            for delta in list_header_deltas:
                for text in re.split(r"(\.\.\.|\s+|\W|ph\d+hp)", delta.insert):
                    if text != "":
                        yield new_renderable.Text(kind="text", text=text)
            yield new_renderable.Whitespace(kind="whitespace")

        if self.sentences_are_items:
            assert not self.letters_are_items
            assert not self.words_are_items
            assert not self.punctuation_is_items
            is_first_sentence = True
            for sentence_deltas in self.split_deltas_into_sentences(paragraph_deltas):
                if not is_first_sentence:
                    yield new_renderable.Whitespace(kind="whitespace")
                is_first_sentence = False
                contents = list(self.adapt_wording_sentence(sentence_deltas, sentence_placeholders))
                while contents[0].kind == "whitespace":
                    contents.pop(0)
                if self.items_are_selectable:
                    contents = [
                        new_renderable.SelectableInput(
                            kind="selectableInput",
                            contents=contents,
                            colors=self.colors_for_selectable_items,
                            boxed=self.items_are_boxed,
                        )
                    ]
                elif self.items_are_boxed:
                    contents = [new_renderable.Boxed(contents=contents)]
                else:
                    pass
                if self.mcq_below_items is None:
                    yield from contents
                    if self.mcq_beside_items is not None:
                        yield new_renderable.Whitespace(kind="whitespace")
                        yield self.mcq_beside_items
                else:
                    yield new_renderable.AnySequence(
                        kind="sequence",
                        contents=[
                            new_renderable.AnySequence(kind="sequence", contents=contents),
                            self.mcq_below_items,
                        ],
                        vertical=True,
                    )
        else:
            yield from self.adapt_wording_sentence(paragraph_deltas, sentence_placeholders)

    def adapt_wording_sentence(
        self,
        sentence_deltas: deltas.Deltas,
        sentence_placeholders: list[tuple[str, new_renderable.SentenceToken]],
    ):
        for delta in sentence_deltas:
            if delta.attributes == {}:
                for i, text in enumerate(re.split(r"(\.\.\.|\s+|\W|ph\d+hp)", delta.insert)):
                    if text != "":
                        if i % 2 == 1:
                            # Separator: punctuation, spacing, placeholders
                            if text.strip() == "":
                                yield new_renderable.Whitespace(kind="whitespace")
                            elif text.startswith("ph") and text.endswith("hp"):
                                index = int(text[2:-2])
                                yield sentence_placeholders[index][1]
                            else:
                                if self.punctuation_is_items:
                                    if self.items_are_selectable:
                                        item = new_renderable.SelectableInput(
                                            kind="selectableInput",
                                            contents=[new_renderable.Text(kind="text", text=text)],
                                            colors=self.colors_for_selectable_items,
                                            boxed=self.items_are_boxed,
                                        )
                                    elif self.items_are_boxed:
                                        item = new_renderable.PassiveSequence(
                                            kind="passiveSequence",
                                            contents=[new_renderable.Text(kind="text", text=text)],
                                            boxed=True,
                                        )
                                    else:
                                        item = new_renderable.Text(kind="text", text=text)
                                    if self.mcq_below_items is None:
                                        yield item
                                        if self.mcq_beside_items is not None:
                                            yield new_renderable.Whitespace(kind="whitespace")
                                            yield self.mcq_beside_items
                                    else:
                                        yield new_renderable.AnySequence(
                                            kind="sequence",
                                            contents=[item, self.mcq_below_items],
                                            vertical=True,
                                        )
                                else:
                                    yield new_renderable.Text(kind="text", text=text)
                        else:
                            # Separated: words
                            if self.letters_are_items:
                                for letter in text:
                                    if self.items_are_selectable:
                                        item = new_renderable.SelectableInput(
                                            kind="selectableInput",
                                            contents=[new_renderable.Text(kind="text", text=letter)],
                                            colors=self.colors_for_selectable_items,
                                            boxed=self.items_are_boxed,
                                        )
                                    elif self.items_are_boxed:
                                        item = new_renderable.PassiveSequence(
                                            kind="passiveSequence",
                                            contents=[new_renderable.Text(kind="text", text=letter)],
                                            boxed=True,
                                        )
                                    else:
                                        item = new_renderable.Text(kind="text", text=letter)
                                    if self.mcq_below_items is None:
                                        yield item
                                        if self.mcq_beside_items is not None:
                                            yield new_renderable.Whitespace(kind="whitespace")
                                            yield self.mcq_beside_items
                                    else:
                                        yield new_renderable.AnySequence(
                                            kind="sequence",
                                            contents=[item, self.mcq_below_items],
                                            vertical=True,
                                        )
                            elif self.words_are_items:
                                if self.items_are_selectable:
                                    item = new_renderable.SelectableInput(
                                        kind="selectableInput",
                                        contents=[new_renderable.Text(kind="text", text=text)],
                                        colors=self.colors_for_selectable_items,
                                        boxed=self.items_are_boxed,
                                    )
                                elif self.items_are_boxed:
                                    item = new_renderable.PassiveSequence(
                                        kind="passiveSequence",
                                        contents=[new_renderable.Text(kind="text", text=text)],
                                        boxed=True,
                                    )
                                else:
                                    item = new_renderable.Text(kind="text", text=text)
                                if self.mcq_below_items is None:
                                    yield item
                                    if self.mcq_beside_items is not None:
                                        yield new_renderable.Whitespace(kind="whitespace")
                                        yield self.mcq_beside_items
                                else:
                                    yield new_renderable.AnySequence(
                                        kind="sequence",
                                        contents=[item, self.mcq_below_items],
                                        vertical=True,
                                    )
                            else:
                                yield new_renderable.Text(kind="text", text=text)

            elif "manual-item" in delta.attributes:
                assert delta.attributes == {"manual-item": delta.attributes["manual-item"]}

                for text in re.split(r"(\.\.\.|\s+|\W)", delta.insert):
                    if text != "":
                        if text.strip() == "":
                            yield new_renderable.Whitespace(kind="whitespace")
                        else:
                            if self.manual_items_are_items:
                                if self.items_are_selectable:
                                    item = new_renderable.SelectableInput(
                                        kind="selectableInput",
                                        contents=[new_renderable.Text(kind="text", text=text)],
                                        colors=self.colors_for_selectable_items,
                                        boxed=self.items_are_boxed,
                                    )
                                elif self.items_are_boxed:
                                    item = new_renderable.PassiveSequence(
                                        kind="passiveSequence",
                                        contents=[new_renderable.Text(kind="text", text=text)],
                                        boxed=True,
                                    )
                                else:
                                    item = new_renderable.Text(kind="text", text=text)
                                if self.mcq_below_items is None:
                                    yield item
                                    if self.mcq_beside_items is not None:
                                        yield new_renderable.Whitespace(kind="whitespace")
                                        yield self.mcq_beside_items
                                else:
                                    yield new_renderable.AnySequence(
                                        kind="sequence",
                                        contents=[item, self.mcq_below_items],
                                        vertical=True,
                                    )
                            else:
                                yield new_renderable.Text(kind="text", text=text)

            elif "bold" in delta.attributes or "italic" in delta.attributes:
                assert set(delta.attributes.keys()) <= {"bold", "italic"}

                yield new_renderable.Text(
                    kind="text",
                    text=delta.insert,
                    bold=delta.attributes.get("bold", False),
                    italic=delta.attributes.get("italic", False),
                )

            elif "choices2" in delta.attributes:
                assert delta.attributes == {"choices2": delta.attributes["choices2"]}

                choices_settings = delta.attributes["choices2"]
                placeholder = choices_settings["placeholder"] or None
                if placeholder is None:
                    start = choices_settings["start"] or None
                    separator1 = choices_settings["separator1"] or None
                    separator2 = choices_settings["separator2"] or None
                    stop = choices_settings["stop"] or None
                    yield new_renderable.MultipleChoicesInput(
                        kind="multipleChoicesInput",
                        show_arrow_before=self.show_arrow_before_mcq_fields,
                        choices=self.separate_choices(
                            start,
                            separator1,
                            separator2,
                            stop,
                            placeholder,
                            delta.insert,
                        ),
                        show_choices_by_default=self.show_mcq_choices_by_default,
                    )

            else:
                assert False, f"Unknown attributes: {delta.attributes}"

    def split_deltas(self, section_deltas: deltas.Deltas, explicit_paragraph_separator_pattern: str) -> Iterable[deltas.Deltas]:
        section_deltas = copy.deepcopy(section_deltas)
        assert len(section_deltas) > 0
        section_deltas[0].insert = section_deltas[0].insert.lstrip()
        section_deltas[-1].insert = section_deltas[-1].insert.rstrip()

        current_paragraph = []
        for delta in section_deltas:
            if "choices2" in delta.attributes:
                current_paragraph.append(delta)
            else:
                for i, paragraph_part in enumerate(re.split(explicit_paragraph_separator_pattern, delta.insert)):
                    if i > 0:
                        yield current_paragraph
                        current_paragraph = []
                    if paragraph_part != "":
                        current_paragraph.append(d.InsertOp(insert=paragraph_part, attributes=delta.attributes))
        yield current_paragraph

    def split_deltas_into_sentences(self, paragraph_deltas: deltas.Deltas) -> Iterable[deltas.Deltas]:
        current_sentence = []
        for delta in paragraph_deltas:
            if "choices2" in delta.attributes:
                current_sentence.append(delta)
            else:
                for i, sentence_part in enumerate(re.split(r"(\.\.\.|[.!?…])", delta.insert)):
                    if sentence_part != "":
                        if i % 2 == 0 and i > 1:
                            yield current_sentence
                            current_sentence = []
                        current_sentence.append(d.InsertOp(insert=sentence_part, attributes=delta.attributes))
        yield current_sentence

    def split_list_header(self, paragraph_deltas: deltas.Deltas) -> tuple[deltas.Deltas, deltas.Deltas]:
        if len(paragraph_deltas) == 0:
            return ([], [])
        else:
            # WARNING: keep the list formats supported here consistent with what's supported in 'listFormats' in 'TextPicker.vue'
            list_header_deltas = []
            paragraph_deltas = copy.deepcopy(paragraph_deltas)

            number_prefix = re.match(r"^\d+", paragraph_deltas[0].insert)
            if number_prefix is not None:
                number_prefix = number_prefix.group(0)

            if number_prefix is not None and len(paragraph_deltas[0].insert) > len(number_prefix) and paragraph_deltas[0].insert[len(number_prefix)] in ").":
                # "1. 2. 3.", "1) 2) 3)", etc.
                list_header_deltas.append(
                    deltas.InsertOp(
                        insert=paragraph_deltas[0].insert[: len(number_prefix) + 1],
                        attributes=paragraph_deltas[0].attributes,
                    )
                )
                paragraph_deltas[0].insert = paragraph_deltas[0].insert[len(number_prefix) + 1 :].lstrip()
            elif (
                len(paragraph_deltas[0].insert) > 1
                and paragraph_deltas[0].insert[0] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                and paragraph_deltas[0].insert[1] in ")."
            ):
                # "a. b. c.", "A) B) C)", etc.
                list_header_deltas.append(
                    deltas.InsertOp(
                        insert=paragraph_deltas[0].insert[:2],
                        attributes=paragraph_deltas[0].attributes,
                    )
                )
                paragraph_deltas[0].insert = paragraph_deltas[0].insert[2:].lstrip()
            elif len(paragraph_deltas[0].insert) > 0 and paragraph_deltas[0].insert[0] in "◆■":
                # "◆", "■", etc.
                list_header_deltas.append(
                    deltas.InsertOp(
                        insert=paragraph_deltas[0].insert[0],
                        attributes=paragraph_deltas[0].attributes,
                    )
                )
                paragraph_deltas[0].insert = paragraph_deltas[0].insert[1:].lstrip()

            return (list_header_deltas, paragraph_deltas)

    __apostrophes = [
        # https://fr.wikipedia.org/wiki/Apostrophe_(typographie) mentions one more encoding than https://en.wikipedia.org/wiki/Apostrophe
        "\u2019",
        "\u0027",
        "\u02BC",
    ]

    def postprocess_section(self, section: new_renderable.Section) -> new_renderable.Section:
        section = copy.deepcopy(section)
        for paragraph in section.paragraphs:
            fixed_contents = []
            for content in paragraph.contents:
                if content.kind == "whitespace" and len(fixed_contents) == 0:
                    pass
                elif content.kind == "whitespace" and len(fixed_contents) > 0 and fixed_contents[-1].kind == "whitespace":
                    pass
                elif (
                    content.kind == "text"
                    and content.text in self.__apostrophes
                    and len(fixed_contents) > 0
                    and fixed_contents[-1].kind in ["selectableInput", "passiveSequence"]
                ):
                    fixed_contents[-1].contents.append(content)
                elif (
                    content.kind == "passiveSequence"
                    and len(content.contents) == 1
                    and content.contents[0].kind == "text"
                    and content.contents[0].text in self.__apostrophes
                    and len(fixed_contents) > 0
                    and fixed_contents[-1].kind in ["selectableInput", "passiveSequence"]
                ):
                    fixed_contents[-1].contents.append(content.contents[0])
                else:
                    fixed_contents.append(content)
            while len(fixed_contents) > 0 and fixed_contents[-1].kind == "whitespace":
                fixed_contents.pop(-1)
            paragraph.contents = fixed_contents
        section.paragraphs = list(filter(lambda p: len(p.contents) > 0, section.paragraphs))
        return section

    def gather_choices(self, deltas):
        for delta in deltas:
            if "choices2" in delta.attributes:
                choices_settings = delta.attributes["choices2"]
                yield (
                    choices_settings["start"] or None,
                    choices_settings["separator1"] or None,
                    choices_settings["separator2"] or None,
                    choices_settings["stop"] or None,
                    choices_settings["placeholder"],
                    delta.insert,
                )

    def separate_choices(self, start, separator1, separator2, stop, placeholder, text):
        text = text.strip()
        if start is not None and stop is not None and text.startswith(start) and text.endswith(stop):
            text = text[len(start) : -len(stop)]
        if separator1 is None:
            choices = [text]
        else:
            choices = text.split(separator1)
        if separator2 is not None:
            choices[-1:] = choices[-1].split(separator2)
        return list([new_renderable.Text(kind="text", text=text)] for text in filter(lambda c: c != "", [choice.strip() for choice in choices]))


class AdaptationTestCase(unittest.TestCase):
    maxDiff = None
    generate_frontend_tests = True

    @classmethod
    def setUpClass(cls):
        cls.tests_to_generate = []
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        def generate_old():
            yield "import TricolorSection from './OldTricolorSection.vue'"
            yield ""
            yield f"describe('TricolorSection for {cls.__name__}', () => " "{"
            yield "  beforeEach(() => {"
            yield "    cy.viewport(1000, 100)"
            yield "  })"
            seen_paragraphs = set()
            for (test_id, old_adapted, _) in cls.tests_to_generate:
                for pagelet_index, pagelet in enumerate(old_adapted.pagelets):
                    for section_name in ["instructions", "wording"]:
                        paragraphs = json.dumps(getattr(pagelet, section_name).model_dump()["paragraphs"])
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

        def generate_new():
            yield "import TricolorSection from './NewTricolorSection.vue'"
            yield ""
            yield f"describe('TricolorSection for {cls.__name__}', () => " "{"
            yield "  beforeEach(() => {"
            yield "    cy.viewport(1000, 100)"
            yield "  })"
            seen_paragraphs = set()
            for (test_id, _, new_adapted) in cls.tests_to_generate:
                for pagelet_index, pagelet in enumerate(new_adapted.pagelets):
                    for section_name in ["instructions", "wording"]:
                        paragraphs = json.dumps(getattr(pagelet, section_name).model_dump()["paragraphs"])
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
            with open(f"../frontend/src/adapted/components/OldTricolorSection.{cls.__name__}.generated.cy.js", "w") as f:
                for line in generate_old():
                    f.write(line)
                    f.write("\n")

            with open(f"../frontend/src/adapted/components/NewTricolorSection.{cls.__name__}.generated.cy.js", "w") as f:
                for line in generate_new():
                    f.write(line)
                    f.write("\n")

        return super().tearDownClass()

    def do_test(self, exercise, expected_old_adapted, expected_new_adapted):
        actual_old_adapted = exercise.make_old_adapted()
        if actual_old_adapted != expected_old_adapted:
            print("actual_old_adapted:", [actual_old_adapted])
        self.assertEqual(actual_old_adapted, expected_old_adapted)
        actual_new_adapted = exercise.make_new_adapted()
        if actual_new_adapted != expected_new_adapted:
            calling_frame = traceback.extract_stack()[-2]
            print(
                f"actual_new_adapted at {calling_frame.filename}:{calling_frame.lineno}:",
                repr([actual_new_adapted])[1:-1]
                .replace("bold=False, ", "")
                .replace("italic=False, ", "")
                .replace("highlighted=None, ", "")
                .replace("boxed=False, ", "")
                .replace("show_arrow_before=False, ", "")
                .replace("show_choices_by_default=False, ", "")
                .replace("vertical=False, ", "")
                .replace("Exercise(", "nr.Exercise(")
                .replace("Pagelet(", "nr.Pagelet(")
                .replace("Section(", "nr.Section(")
                .replace("Paragraph(", "nr.Paragraph(")
                .replace("Text(", "nr.Text(")
                .replace("Whitespace(", "nr.Whitespace(")
                .replace("FreeTextInput(", "nr.FreeTextInput(")
                .replace("MultipleChoicesInput(", "nr.MultipleChoicesInput(")
                .replace("SelectableInput(", "nr.SelectableInput(")
                .replace("PassiveSequence(", "nr.PassiveSequence(")
                .replace("AnySequence(", "nr.AnySequence("),
            )
        self.assertEqual(actual_new_adapted, expected_new_adapted)

        self.tests_to_generate.append((self.id(), expected_old_adapted, expected_new_adapted))


class WordingPaginationTestCase(AdaptationTestCase):
    def test_empty(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.InsertOp(insert="\n", attributes={})],
                wording=[d.InsertOp(insert="\n", attributes={})],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[]),
                        wording=r.Section(paragraphs=[]),
                    )
                ],
            ),
            nr.Exercise(number="number", textbook_page=None, pagelets=[nr.Pagelet(instructions=nr.Section(paragraphs=[]), wording=nr.Section(paragraphs=[]))]),
        )

    def test_single_paragraph(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.InsertOp(insert="\n", attributes={})],
                wording=[d.InsertOp(insert="wording\n", attributes={})],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(tokens=[r.PlainText(text="wording")]),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(paragraphs=[]), wording=nr.Section(paragraphs=[nr.Paragraph(contents=[nr.Text(kind="text", text="wording")])])
                    )
                ],
            ),
        )

    def test_full_pagelet(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.InsertOp(insert="\n", attributes={})],
                wording=[d.InsertOp(insert="wording 1\nwording 2\nwording 3\n", attributes={})],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(tokens=[r.PlainText(text="wording"), r.Whitespace(), r.PlainText("1")]),
                                r.Paragraph(tokens=[r.PlainText(text="wording"), r.Whitespace(), r.PlainText("2")]),
                                r.Paragraph(tokens=[r.PlainText(text="wording"), r.Whitespace(), r.PlainText("3")]),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(paragraphs=[]),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(contents=[nr.Text(kind="text", text="wording"), nr.Whitespace(kind="whitespace"), nr.Text(kind="text", text="1")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="wording"), nr.Whitespace(kind="whitespace"), nr.Text(kind="text", text="2")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="wording"), nr.Whitespace(kind="whitespace"), nr.Text(kind="text", text="3")]),
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_single_paragraph_on_second_page(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.InsertOp(insert="instructions\n", attributes={})],
                wording=[d.InsertOp(insert="wording 1\nwording 2\nwording 3\n", attributes={})],
                example=[d.InsertOp(insert="example\n", attributes={})],
                clue=[d.InsertOp(insert="clue\n", attributes={})],
                wording_paragraphs_per_pagelet=2,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(tokens=[r.PlainText(text="instructions")]),
                                r.Paragraph(tokens=[r.PlainText(text="example")]),
                                r.Paragraph(tokens=[r.PlainText(text="clue")]),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(tokens=[r.PlainText(text="wording"), r.Whitespace(), r.PlainText("1")]),
                                r.Paragraph(tokens=[r.PlainText(text="wording"), r.Whitespace(), r.PlainText("2")]),
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(tokens=[r.PlainText(text="instructions")]),
                                r.Paragraph(tokens=[r.PlainText(text="example")]),
                                r.Paragraph(tokens=[r.PlainText(text="clue")]),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(tokens=[r.PlainText(text="wording"), r.Whitespace(), r.PlainText("3")]),
                            ]
                        ),
                    ),
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(contents=[nr.Text(kind="text", text="instructions")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="example")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="clue")]),
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(contents=[nr.Text(kind="text", text="wording"), nr.Whitespace(kind="whitespace"), nr.Text(kind="text", text="1")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="wording"), nr.Whitespace(kind="whitespace"), nr.Text(kind="text", text="2")]),
                            ]
                        ),
                    ),
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(contents=[nr.Text(kind="text", text="instructions")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="example")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="clue")]),
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(contents=[nr.Text(kind="text", text="wording"), nr.Whitespace(kind="whitespace"), nr.Text(kind="text", text="3")])
                            ]
                        ),
                    ),
                ],
            ),
        )

    def test_no_pagination(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.InsertOp(insert="instructions\n", attributes={})],
                wording=[d.InsertOp(insert="wording 1\nwording 2\nwording 3\nwording 4\nwording 5\nwording 6\n", attributes={})],
                example=[d.InsertOp(insert="example\n", attributes={})],
                clue=[d.InsertOp(insert="clue\n", attributes={})],
                wording_paragraphs_per_pagelet=None,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(tokens=[r.PlainText(text="instructions")]),
                                r.Paragraph(tokens=[r.PlainText(text="example")]),
                                r.Paragraph(tokens=[r.PlainText(text="clue")]),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(tokens=[r.PlainText(text="wording"), r.Whitespace(), r.PlainText("1")]),
                                r.Paragraph(tokens=[r.PlainText(text="wording"), r.Whitespace(), r.PlainText("2")]),
                                r.Paragraph(tokens=[r.PlainText(text="wording"), r.Whitespace(), r.PlainText("3")]),
                                r.Paragraph(tokens=[r.PlainText(text="wording"), r.Whitespace(), r.PlainText("4")]),
                                r.Paragraph(tokens=[r.PlainText(text="wording"), r.Whitespace(), r.PlainText("5")]),
                                r.Paragraph(tokens=[r.PlainText(text="wording"), r.Whitespace(), r.PlainText("6")]),
                            ]
                        ),
                    ),
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(contents=[nr.Text(kind="text", text="instructions")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="example")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="clue")]),
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(contents=[nr.Text(kind="text", text="wording"), nr.Whitespace(kind="whitespace"), nr.Text(kind="text", text="1")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="wording"), nr.Whitespace(kind="whitespace"), nr.Text(kind="text", text="2")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="wording"), nr.Whitespace(kind="whitespace"), nr.Text(kind="text", text="3")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="wording"), nr.Whitespace(kind="whitespace"), nr.Text(kind="text", text="4")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="wording"), nr.Whitespace(kind="whitespace"), nr.Text(kind="text", text="5")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="wording"), nr.Whitespace(kind="whitespace"), nr.Text(kind="text", text="6")]),
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_only_manual_pagination(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.InsertOp(insert="instructions\n", attributes={})],
                wording=[d.InsertOp(insert="wording 1\n\nwording 2\n\n\nwording 3\n\nwording 4\n\nwording 5\n\nwording 6\n\n", attributes={})],
                example=[d.InsertOp(insert="example\n", attributes={})],
                clue=[d.InsertOp(insert="clue\n", attributes={})],
                wording_paragraphs_per_pagelet=None,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(tokens=[r.PlainText(text="instructions")]),
                                r.Paragraph(tokens=[r.PlainText(text="example")]),
                                r.Paragraph(tokens=[r.PlainText(text="clue")]),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(tokens=[r.PlainText(text="wording"), r.Whitespace(), r.PlainText("1")]),
                                r.Paragraph(tokens=[r.PlainText(text="wording"), r.Whitespace(), r.PlainText("2")]),
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(tokens=[r.PlainText(text="instructions")]),
                                r.Paragraph(tokens=[r.PlainText(text="example")]),
                                r.Paragraph(tokens=[r.PlainText(text="clue")]),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(tokens=[r.PlainText(text="wording"), r.Whitespace(), r.PlainText("3")]),
                                r.Paragraph(tokens=[r.PlainText(text="wording"), r.Whitespace(), r.PlainText("4")]),
                                r.Paragraph(tokens=[r.PlainText(text="wording"), r.Whitespace(), r.PlainText("5")]),
                                r.Paragraph(tokens=[r.PlainText(text="wording"), r.Whitespace(), r.PlainText("6")]),
                            ]
                        ),
                    ),
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(contents=[nr.Text(kind="text", text="instructions")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="example")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="clue")]),
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(contents=[nr.Text(kind="text", text="wording"), nr.Whitespace(kind="whitespace"), nr.Text(kind="text", text="1")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="wording"), nr.Whitespace(kind="whitespace"), nr.Text(kind="text", text="2")]),
                            ]
                        ),
                    ),
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(contents=[nr.Text(kind="text", text="instructions")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="example")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="clue")]),
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(contents=[nr.Text(kind="text", text="wording"), nr.Whitespace(kind="whitespace"), nr.Text(kind="text", text="3")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="wording"), nr.Whitespace(kind="whitespace"), nr.Text(kind="text", text="4")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="wording"), nr.Whitespace(kind="whitespace"), nr.Text(kind="text", text="5")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="wording"), nr.Whitespace(kind="whitespace"), nr.Text(kind="text", text="6")]),
                            ]
                        ),
                    ),
                ],
            ),
        )

    def test_manual_and_automated_pagination(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.InsertOp(insert="instructions\n", attributes={})],
                wording=[d.InsertOp(insert="wording 1\n\nwording 2\n\n\nwording 3\n\nwording 4\n\nwording 5\n\nwording 6\n\n", attributes={})],
                example=[d.InsertOp(insert="example\n", attributes={})],
                clue=[d.InsertOp(insert="clue\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(tokens=[r.PlainText(text="instructions")]),
                                r.Paragraph(tokens=[r.PlainText(text="example")]),
                                r.Paragraph(tokens=[r.PlainText(text="clue")]),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(tokens=[r.PlainText(text="wording"), r.Whitespace(), r.PlainText("1")]),
                                r.Paragraph(tokens=[r.PlainText(text="wording"), r.Whitespace(), r.PlainText("2")]),
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(tokens=[r.PlainText(text="instructions")]),
                                r.Paragraph(tokens=[r.PlainText(text="example")]),
                                r.Paragraph(tokens=[r.PlainText(text="clue")]),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(tokens=[r.PlainText(text="wording"), r.Whitespace(), r.PlainText("3")]),
                                r.Paragraph(tokens=[r.PlainText(text="wording"), r.Whitespace(), r.PlainText("4")]),
                                r.Paragraph(tokens=[r.PlainText(text="wording"), r.Whitespace(), r.PlainText("5")]),
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(tokens=[r.PlainText(text="instructions")]),
                                r.Paragraph(tokens=[r.PlainText(text="example")]),
                                r.Paragraph(tokens=[r.PlainText(text="clue")]),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(tokens=[r.PlainText(text="wording"), r.Whitespace(), r.PlainText("6")]),
                            ]
                        ),
                    ),
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(contents=[nr.Text(kind="text", text="instructions")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="example")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="clue")]),
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(contents=[nr.Text(kind="text", text="wording"), nr.Whitespace(kind="whitespace"), nr.Text(kind="text", text="1")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="wording"), nr.Whitespace(kind="whitespace"), nr.Text(kind="text", text="2")]),
                            ]
                        ),
                    ),
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(contents=[nr.Text(kind="text", text="instructions")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="example")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="clue")]),
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(contents=[nr.Text(kind="text", text="wording"), nr.Whitespace(kind="whitespace"), nr.Text(kind="text", text="3")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="wording"), nr.Whitespace(kind="whitespace"), nr.Text(kind="text", text="4")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="wording"), nr.Whitespace(kind="whitespace"), nr.Text(kind="text", text="5")]),
                            ]
                        ),
                    ),
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(contents=[nr.Text(kind="text", text="instructions")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="example")]),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="clue")]),
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(contents=[nr.Text(kind="text", text="wording"), nr.Whitespace(kind="whitespace"), nr.Text(kind="text", text="6")])
                            ]
                        ),
                    ),
                ],
            ),
        )


# Tests below this line follow a legacy organization, based on classes that have been deleted.
# There is some duplication because tests have been kept through refactoring.
# Tests above focus on specific features of the adaptation process.
# A reorganization would be beneficial, future me!


class FillWithFreeTextAdaptationTestCase(AdaptationTestCase):
    def test_single_sentence(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="The wording of this ... is a ... sentence.\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="fill-with-free-text",
                    placeholder_for_fill_with_free_text="...",
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="instructions"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
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
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(paragraphs=[nr.Paragraph(contents=[nr.Text(kind="text", text="instructions")])]),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="The"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="wording"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="of"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="this"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.FreeTextInput(kind="freeTextInput"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="a"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.FreeTextInput(kind="freeTextInput"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="sentence"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_start_and_end_with_placeholder(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.InsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="@ a @\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="fill-with-free-text",
                    placeholder_for_fill_with_free_text="@",
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="instructions"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.FreeTextInput(),
                                        r.Whitespace(),
                                        r.PlainText(text="a"),
                                        r.Whitespace(),
                                        r.FreeTextInput(),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(paragraphs=[nr.Paragraph(contents=[nr.Text(kind="text", text="instructions")])]),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.FreeTextInput(kind="freeTextInput"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="a"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.FreeTextInput(kind="freeTextInput"),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_multiple_lines_in_instructions(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="instructions\nare\n\non\n\nmultiple\nlines\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="wording\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="fill-with-free-text",
                    placeholder_for_fill_with_free_text="...",
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="instructions"),
                                        r.Whitespace(),
                                        r.PlainText(text="are"),
                                    ]
                                ),
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="on"),
                                    ]
                                ),
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="multiple"),
                                        r.Whitespace(),
                                        r.PlainText(text="lines"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="wording"),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[nr.Text(kind="text", text="instructions"), nr.Whitespace(kind="whitespace"), nr.Text(kind="text", text="are")]
                                ),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="on")]),
                                nr.Paragraph(
                                    contents=[nr.Text(kind="text", text="multiple"), nr.Whitespace(kind="whitespace"), nr.Text(kind="text", text="lines")]
                                ),
                            ]
                        ),
                        wording=nr.Section(paragraphs=[nr.Paragraph(contents=[nr.Text(kind="text", text="wording")])]),
                    )
                ],
            ),
        )

    def test_multiple_lines_in_wording(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="foo toto : ...\n\nbar : ...\n\nbaz : ...\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="fill-with-free-text",
                    placeholder_for_fill_with_free_text="...",
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="instructions"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="foo"),
                                        r.Whitespace(),
                                        r.PlainText(text="toto"),
                                        r.Whitespace(),
                                        r.PlainText(text=":"),
                                        r.Whitespace(),
                                        r.FreeTextInput(),
                                    ]
                                ),
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="bar"),
                                        r.Whitespace(),
                                        r.PlainText(text=":"),
                                        r.Whitespace(),
                                        r.FreeTextInput(),
                                    ]
                                ),
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="baz"),
                                        r.Whitespace(),
                                        r.PlainText(text=":"),
                                        r.Whitespace(),
                                        r.FreeTextInput(),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(paragraphs=[nr.Paragraph(contents=[nr.Text(kind="text", text="instructions")])]),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="foo"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="toto"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text=":"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.FreeTextInput(kind="freeTextInput"),
                                    ]
                                ),
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="bar"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text=":"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.FreeTextInput(kind="freeTextInput"),
                                    ]
                                ),
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="baz"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text=":"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.FreeTextInput(kind="freeTextInput"),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_unknown_tags(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="{tag|abc}\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="{tag|def}\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="fill-with-free-text",
                    placeholder_for_fill_with_free_text="...",
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="{"),
                                        r.PlainText(text="tag"),
                                        r.PlainText(text="|"),
                                        r.PlainText(text="abc"),
                                        r.PlainText(text="}"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="{"),
                                        r.PlainText(text="tag"),
                                        r.PlainText(text="|"),
                                        r.PlainText(text="def"),
                                        r.PlainText(text="}"),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="{"),
                                        nr.Text(kind="text", text="tag"),
                                        nr.Text(kind="text", text="|"),
                                        nr.Text(kind="text", text="abc"),
                                        nr.Text(kind="text", text="}"),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="{"),
                                        nr.Text(kind="text", text="tag"),
                                        nr.Text(kind="text", text="|"),
                                        nr.Text(kind="text", text="def"),
                                        nr.Text(kind="text", text="}"),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_strip_whitespace(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="   abc   \n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="   def   \n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="fill-with-free-text",
                    placeholder_for_fill_with_free_text="...",
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="abc"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="def"),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(paragraphs=[nr.Paragraph(contents=[nr.Text(kind="text", text="abc")])]),
                        wording=nr.Section(paragraphs=[nr.Paragraph(contents=[nr.Text(kind="text", text="def")])]),
                    )
                ],
            ),
        )

    def test_example_and_clue(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="This @ is the wording.\n", attributes={}),
                ],
                example=[
                    d.InsertOp(insert="This @ is the example.\n", attributes={}),
                ],
                clue=[
                    d.InsertOp(insert="This @ is the clue.\n", attributes={}),
                ],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="fill-with-free-text",
                    placeholder_for_fill_with_free_text="@",
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="instructions"),
                                    ]
                                ),
                                r.Paragraph(
                                    tokens=[
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
                                    ]
                                ),
                                r.Paragraph(
                                    tokens=[
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
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
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
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(contents=[nr.Text(kind="text", text="instructions")]),
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="This"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="@"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="the"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="example"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                ),
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="This"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="@"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="the"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="clue"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="This"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.FreeTextInput(kind="freeTextInput"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="the"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="wording"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )


class ItemizedAdaptationTestCase(AdaptationTestCase):
    def test_selectable_letters(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.InsertOp(insert="Instructions\n", attributes={})],
                wording=[d.InsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "characters", "letters": True},
                    items_are_selectable={"colors": ["red"]},
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Instructions"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.SelectableText(text="T", colors=["red"], boxed=False),
                                        r.SelectableText(text="h", colors=["red"], boxed=False),
                                        r.SelectableText(text="i", colors=["red"], boxed=False),
                                        r.SelectableText(text="s", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="i", colors=["red"], boxed=False),
                                        r.SelectableText(text="s", colors=["red"], boxed=False),
                                        r.PlainText(text=","),
                                        r.Whitespace(),
                                        r.SelectableText(text="t", colors=["red"], boxed=False),
                                        r.SelectableText(text="h", colors=["red"], boxed=False),
                                        r.SelectableText(text="e", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="w", colors=["red"], boxed=False),
                                        r.SelectableText(text="o", colors=["red"], boxed=False),
                                        r.SelectableText(text="r", colors=["red"], boxed=False),
                                        r.SelectableText(text="d", colors=["red"], boxed=False),
                                        r.SelectableText(text="i", colors=["red"], boxed=False),
                                        r.SelectableText(text="n", colors=["red"], boxed=False),
                                        r.SelectableText(text="g", colors=["red"], boxed=False),
                                        r.PlainText(text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(paragraphs=[nr.Paragraph(contents=[nr.Text(kind="text", text="Instructions")])]),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="T")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="h")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="i")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="s")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="i")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="s")]),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="t")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="h")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="e")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="w")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="o")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="r")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="d")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="i")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="n")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="g")]),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_selectable_words__plain(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.InsertOp(insert="Instructions\n", attributes={})],
                wording=[d.InsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": False},
                    items_are_selectable={"colors": ["red", "blue"]},
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Instructions"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.SelectableText(text="This", colors=["red", "blue"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="is", colors=["red", "blue"], boxed=False),
                                        r.PlainText(text=","),
                                        r.Whitespace(),
                                        r.SelectableText(text="the", colors=["red", "blue"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="wording", colors=["red", "blue"], boxed=False),
                                        r.PlainText(text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(paragraphs=[nr.Paragraph(contents=[nr.Text(kind="text", text="Instructions")])]),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[nr.Text(kind="text", text="This")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[nr.Text(kind="text", text="is")]),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[nr.Text(kind="text", text="the")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[nr.Text(kind="text", text="wording")]),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_selectable_words_and_punctuation(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.InsertOp(insert="Instructions\n", attributes={})],
                wording=[d.InsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": True},
                    items_are_selectable={"colors": ["green", "yellow", "orange"]},
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Instructions"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.SelectableText(text="This", colors=["green", "yellow", "orange"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="is", colors=["green", "yellow", "orange"], boxed=False),
                                        r.SelectableText(text=",", colors=["green", "yellow", "orange"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="the", colors=["green", "yellow", "orange"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="wording", colors=["green", "yellow", "orange"], boxed=False),
                                        r.SelectableText(text=".", colors=["green", "yellow", "orange"], boxed=False),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(paragraphs=[nr.Paragraph(contents=[nr.Text(kind="text", text="Instructions")])]),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.SelectableInput(
                                            kind="selectableInput", colors=["green", "yellow", "orange"], contents=[nr.Text(kind="text", text="This")]
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(
                                            kind="selectableInput", colors=["green", "yellow", "orange"], contents=[nr.Text(kind="text", text="is")]
                                        ),
                                        nr.SelectableInput(
                                            kind="selectableInput", colors=["green", "yellow", "orange"], contents=[nr.Text(kind="text", text=",")]
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(
                                            kind="selectableInput", colors=["green", "yellow", "orange"], contents=[nr.Text(kind="text", text="the")]
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(
                                            kind="selectableInput", colors=["green", "yellow", "orange"], contents=[nr.Text(kind="text", text="wording")]
                                        ),
                                        nr.SelectableInput(
                                            kind="selectableInput", colors=["green", "yellow", "orange"], contents=[nr.Text(kind="text", text=".")]
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_selectable_punctuation_only(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.InsertOp(insert="Instructions\n", attributes={})],
                wording=[d.InsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": False, "punctuation": True},
                    items_are_selectable={"colors": ["green", "yellow", "orange"]},
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Instructions"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="This"),
                                        r.Whitespace(),
                                        r.PlainText(text="is"),
                                        r.SelectableText(text=",", colors=["green", "yellow", "orange"], boxed=False),
                                        r.Whitespace(),
                                        r.PlainText(text="the"),
                                        r.Whitespace(),
                                        r.PlainText(text="wording"),
                                        r.SelectableText(text=".", colors=["green", "yellow", "orange"], boxed=False),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(paragraphs=[nr.Paragraph(contents=[nr.Text(kind="text", text="Instructions")])]),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="This"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.SelectableInput(
                                            kind="selectableInput", colors=["green", "yellow", "orange"], contents=[nr.Text(kind="text", text=",")]
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="the"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="wording"),
                                        nr.SelectableInput(
                                            kind="selectableInput", colors=["green", "yellow", "orange"], contents=[nr.Text(kind="text", text=".")]
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_selectable_words__boxed(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.InsertOp(insert="Instructions\n", attributes={})],
                wording=[d.InsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": False},
                    items_are_selectable={"colors": ["red", "blue"]},
                    items_are_boxed=True,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Instructions"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.SelectableText(text="This", colors=["red", "blue"], boxed=True),
                                        r.Whitespace(),
                                        r.SelectableText(text="is", colors=["red", "blue"], boxed=True),
                                        r.PlainText(text=","),
                                        r.Whitespace(),
                                        r.SelectableText(text="the", colors=["red", "blue"], boxed=True),
                                        r.Whitespace(),
                                        r.SelectableText(text="wording", colors=["red", "blue"], boxed=True),
                                        r.PlainText(text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(paragraphs=[nr.Paragraph(contents=[nr.Text(kind="text", text="Instructions")])]),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.SelectableInput(
                                            kind="selectableInput", colors=["red", "blue"], boxed=True, contents=[nr.Text(kind="text", text="This")]
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(
                                            kind="selectableInput", colors=["red", "blue"], boxed=True, contents=[nr.Text(kind="text", text="is")]
                                        ),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(
                                            kind="selectableInput", colors=["red", "blue"], boxed=True, contents=[nr.Text(kind="text", text="the")]
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(
                                            kind="selectableInput", colors=["red", "blue"], boxed=True, contents=[nr.Text(kind="text", text="wording")]
                                        ),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_selectable_tokens__in_lettered_list(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.InsertOp(insert="Instructions\n", attributes={})],
                wording=[d.InsertOp(insert="a. First list element.\nb. Second element, still in list.\nc. Third element. The last one!", attributes={})],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=2,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": True},
                    items_are_selectable={"colors": ["red"]},
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Instructions"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="a"),
                                        r.PlainText(text="."),
                                        r.Whitespace(),
                                        r.SelectableText(text="First", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="list", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="element", colors=["red"], boxed=False),
                                        r.SelectableText(text=".", colors=["red"], boxed=False),
                                    ]
                                ),
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="b"),
                                        r.PlainText(text="."),
                                        r.Whitespace(),
                                        r.SelectableText(text="Second", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="element", colors=["red"], boxed=False),
                                        r.SelectableText(text=",", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="still", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="in", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="list", colors=["red"], boxed=False),
                                        r.SelectableText(text=".", colors=["red"], boxed=False),
                                    ]
                                ),
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Instructions"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="c"),
                                        r.PlainText(text="."),
                                        r.Whitespace(),
                                        r.SelectableText(text="Third", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="element", colors=["red"], boxed=False),
                                        r.SelectableText(text=".", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="The", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="last", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="one", colors=["red"], boxed=False),
                                        r.SelectableText(text="!", colors=["red"], boxed=False),
                                    ]
                                ),
                            ]
                        ),
                    ),
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(paragraphs=[nr.Paragraph(contents=[nr.Text(kind="text", text="Instructions")])]),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="a"),
                                        nr.Text(kind="text", text="."),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="First")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="list")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="element")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text=".")]),
                                    ]
                                ),
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="b"),
                                        nr.Text(kind="text", text="."),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="Second")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="element")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text=",")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="still")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="in")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="list")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text=".")]),
                                    ]
                                ),
                            ]
                        ),
                    ),
                    nr.Pagelet(
                        instructions=nr.Section(paragraphs=[nr.Paragraph(contents=[nr.Text(kind="text", text="Instructions")])]),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="c"),
                                        nr.Text(kind="text", text="."),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="Third")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="element")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text=".")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="The")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="last")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="one")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="!")]),
                                    ]
                                )
                            ]
                        ),
                    ),
                ],
            ),
        )

    def test_selectable_tokens__in_numbered_list(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.InsertOp(insert="Instructions\n", attributes={})],
                wording=[d.InsertOp(insert="1) First list element.\n2) Second element, still in list.\n3) Third element. The last one!", attributes={})],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=2,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": True},
                    items_are_selectable={"colors": ["red"]},
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Instructions"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="1"),
                                        r.PlainText(text=")"),
                                        r.Whitespace(),
                                        r.SelectableText(text="First", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="list", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="element", colors=["red"], boxed=False),
                                        r.SelectableText(text=".", colors=["red"], boxed=False),
                                    ]
                                ),
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="2"),
                                        r.PlainText(text=")"),
                                        r.Whitespace(),
                                        r.SelectableText(text="Second", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="element", colors=["red"], boxed=False),
                                        r.SelectableText(text=",", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="still", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="in", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="list", colors=["red"], boxed=False),
                                        r.SelectableText(text=".", colors=["red"], boxed=False),
                                    ]
                                ),
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Instructions"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="3"),
                                        r.PlainText(text=")"),
                                        r.Whitespace(),
                                        r.SelectableText(text="Third", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="element", colors=["red"], boxed=False),
                                        r.SelectableText(text=".", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="The", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="last", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="one", colors=["red"], boxed=False),
                                        r.SelectableText(text="!", colors=["red"], boxed=False),
                                    ]
                                ),
                            ]
                        ),
                    ),
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(paragraphs=[nr.Paragraph(contents=[nr.Text(kind="text", text="Instructions")])]),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="1"),
                                        nr.Text(kind="text", text=")"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="First")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="list")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="element")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text=".")]),
                                    ]
                                ),
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="2"),
                                        nr.Text(kind="text", text=")"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="Second")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="element")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text=",")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="still")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="in")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="list")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text=".")]),
                                    ]
                                ),
                            ]
                        ),
                    ),
                    nr.Pagelet(
                        instructions=nr.Section(paragraphs=[nr.Paragraph(contents=[nr.Text(kind="text", text="Instructions")])]),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="3"),
                                        nr.Text(kind="text", text=")"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="Third")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="element")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text=".")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="The")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="last")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="one")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="!")]),
                                    ]
                                )
                            ]
                        ),
                    ),
                ],
            ),
        )

    def test_selectable_tokens__in_bullet_list(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.InsertOp(insert="Instructions\n", attributes={})],
                wording=[d.InsertOp(insert="◆ First list element.\n◆ Second element, still in list.\n◆ Third element. The last one!", attributes={})],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=2,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": True},
                    items_are_selectable={"colors": ["red"]},
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Instructions"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="◆"),
                                        r.Whitespace(),
                                        r.SelectableText(text="First", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="list", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="element", colors=["red"], boxed=False),
                                        r.SelectableText(text=".", colors=["red"], boxed=False),
                                    ]
                                ),
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="◆"),
                                        r.Whitespace(),
                                        r.SelectableText(text="Second", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="element", colors=["red"], boxed=False),
                                        r.SelectableText(text=",", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="still", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="in", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="list", colors=["red"], boxed=False),
                                        r.SelectableText(text=".", colors=["red"], boxed=False),
                                    ]
                                ),
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Instructions"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="◆"),
                                        r.Whitespace(),
                                        r.SelectableText(text="Third", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="element", colors=["red"], boxed=False),
                                        r.SelectableText(text=".", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="The", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="last", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="one", colors=["red"], boxed=False),
                                        r.SelectableText(text="!", colors=["red"], boxed=False),
                                    ]
                                ),
                            ]
                        ),
                    ),
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(paragraphs=[nr.Paragraph(contents=[nr.Text(kind="text", text="Instructions")])]),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="◆"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="First")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="list")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="element")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text=".")]),
                                    ]
                                ),
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="◆"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="Second")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="element")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text=",")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="still")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="in")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="list")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text=".")]),
                                    ]
                                ),
                            ]
                        ),
                    ),
                    nr.Pagelet(
                        instructions=nr.Section(paragraphs=[nr.Paragraph(contents=[nr.Text(kind="text", text="Instructions")])]),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="◆"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="Third")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="element")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text=".")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="The")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="last")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="one")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="!")]),
                                    ]
                                )
                            ]
                        ),
                    ),
                ],
            ),
        )

    def test_selectable_sentences(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.InsertOp(insert="Instructions\n", attributes={})],
                wording=[
                    d.InsertOp(
                        insert="Affirmative sentence. Exclamative sentence! Phrase exclamative ! Interrogative sentence? Phrase interrogative ? Suspens...\n",
                        attributes={},
                    )
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "sentences"},
                    items_are_selectable={"colors": ["red", "blue"]},
                    items_are_boxed=True,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Instructions"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.Selectable(
                                            contents=[
                                                r.PlainText(text="Affirmative"),
                                                r.Whitespace(),
                                                r.PlainText(text="sentence"),
                                                r.PlainText(text="."),
                                            ],
                                            colors=["red", "blue"],
                                            boxed=True,
                                        ),
                                        r.Whitespace(),
                                        r.Selectable(
                                            contents=[
                                                r.PlainText(text="Exclamative"),
                                                r.Whitespace(),
                                                r.PlainText(text="sentence"),
                                                r.PlainText(text="!"),
                                            ],
                                            colors=["red", "blue"],
                                            boxed=True,
                                        ),
                                        r.Whitespace(),
                                        r.Selectable(
                                            contents=[
                                                r.PlainText(text="Phrase"),
                                                r.Whitespace(),
                                                r.PlainText(text="exclamative"),
                                                r.Whitespace(),
                                                r.PlainText(text="!"),
                                            ],
                                            colors=["red", "blue"],
                                            boxed=True,
                                        ),
                                        r.Whitespace(),
                                        r.Selectable(
                                            contents=[
                                                r.PlainText(text="Interrogative"),
                                                r.Whitespace(),
                                                r.PlainText(text="sentence"),
                                                r.PlainText(text="?"),
                                            ],
                                            colors=["red", "blue"],
                                            boxed=True,
                                        ),
                                        r.Whitespace(),
                                        r.Selectable(
                                            contents=[
                                                r.PlainText(text="Phrase"),
                                                r.Whitespace(),
                                                r.PlainText(text="interrogative"),
                                                r.Whitespace(),
                                                r.PlainText(text="?"),
                                            ],
                                            colors=["red", "blue"],
                                            boxed=True,
                                        ),
                                        r.Whitespace(),
                                        r.Selectable(
                                            contents=[
                                                r.PlainText(text="Suspens"),
                                                r.PlainText(text="..."),
                                            ],
                                            colors=["red", "blue"],
                                            boxed=True,
                                        ),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(paragraphs=[nr.Paragraph(contents=[nr.Text(kind="text", text="Instructions")])]),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.SelectableInput(
                                            kind="selectableInput",
                                            colors=["red", "blue"],
                                            boxed=True,
                                            contents=[
                                                nr.Text(kind="text", text="Affirmative"),
                                                nr.Whitespace(kind="whitespace"),
                                                nr.Text(kind="text", text="sentence"),
                                                nr.Text(kind="text", text="."),
                                            ],
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(
                                            kind="selectableInput",
                                            colors=["red", "blue"],
                                            boxed=True,
                                            contents=[
                                                nr.Text(kind="text", text="Exclamative"),
                                                nr.Whitespace(kind="whitespace"),
                                                nr.Text(kind="text", text="sentence"),
                                                nr.Text(kind="text", text="!"),
                                            ],
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(
                                            kind="selectableInput",
                                            colors=["red", "blue"],
                                            boxed=True,
                                            contents=[
                                                nr.Text(kind="text", text="Phrase"),
                                                nr.Whitespace(kind="whitespace"),
                                                nr.Text(kind="text", text="exclamative"),
                                                nr.Whitespace(kind="whitespace"),
                                                nr.Text(kind="text", text="!"),
                                            ],
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(
                                            kind="selectableInput",
                                            colors=["red", "blue"],
                                            boxed=True,
                                            contents=[
                                                nr.Text(kind="text", text="Interrogative"),
                                                nr.Whitespace(kind="whitespace"),
                                                nr.Text(kind="text", text="sentence"),
                                                nr.Text(kind="text", text="?"),
                                            ],
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(
                                            kind="selectableInput",
                                            colors=["red", "blue"],
                                            boxed=True,
                                            contents=[
                                                nr.Text(kind="text", text="Phrase"),
                                                nr.Whitespace(kind="whitespace"),
                                                nr.Text(kind="text", text="interrogative"),
                                                nr.Whitespace(kind="whitespace"),
                                                nr.Text(kind="text", text="?"),
                                            ],
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(
                                            kind="selectableInput",
                                            colors=["red", "blue"],
                                            boxed=True,
                                            contents=[nr.Text(kind="text", text="Suspens"), nr.Text(kind="text", text="...")],
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_selectable_manual_items__plain(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.InsertOp(insert="Instructions\n", attributes={})],
                wording=[
                    d.InsertOp(insert="This ", attributes={}),
                    d.InsertOp(insert="is,", attributes={"manual-item": True}),
                    d.InsertOp(insert=" ", attributes={}),
                    d.InsertOp(insert="the", attributes={"manual-item": True}),
                    d.InsertOp(insert=" wording.\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "manual"},
                    items_are_selectable={"colors": ["red", "blue"]},
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Instructions"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="This"),
                                        r.Whitespace(),
                                        r.SelectableText(text="is", colors=["red", "blue"], boxed=False),
                                        r.SelectableText(text=",", colors=["red", "blue"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="the", colors=["red", "blue"], boxed=False),
                                        r.Whitespace(),
                                        r.PlainText(text="wording"),
                                        r.PlainText(text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(paragraphs=[nr.Paragraph(contents=[nr.Text(kind="text", text="Instructions")])]),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="This"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[nr.Text(kind="text", text="is")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[nr.Text(kind="text", text=",")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[nr.Text(kind="text", text="the")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="wording"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_selectable_manual_items__boxed(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.InsertOp(insert="Instructions\n", attributes={})],
                wording=[
                    d.InsertOp(insert="This ", attributes={}),
                    d.InsertOp(insert="is,", attributes={"manual-item": True}),
                    d.InsertOp(insert=" ", attributes={}),
                    d.InsertOp(insert="the", attributes={"manual-item": True}),
                    d.InsertOp(insert=" wording.\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "manual"},
                    items_are_selectable={"colors": ["red", "blue"]},
                    items_are_boxed=True,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Instructions"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="This"),
                                        r.Whitespace(),
                                        r.SelectableText(text="is", colors=["red", "blue"], boxed=True),
                                        r.SelectableText(text=",", colors=["red", "blue"], boxed=True),
                                        r.Whitespace(),
                                        r.SelectableText(text="the", colors=["red", "blue"], boxed=True),
                                        r.Whitespace(),
                                        r.PlainText(text="wording"),
                                        r.PlainText(text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(paragraphs=[nr.Paragraph(contents=[nr.Text(kind="text", text="Instructions")])]),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="This"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(
                                            kind="selectableInput", colors=["red", "blue"], boxed=True, contents=[nr.Text(kind="text", text="is")]
                                        ),
                                        nr.SelectableInput(
                                            kind="selectableInput", colors=["red", "blue"], boxed=True, contents=[nr.Text(kind="text", text=",")]
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(
                                            kind="selectableInput", colors=["red", "blue"], boxed=True, contents=[nr.Text(kind="text", text="the")]
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="wording"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_boxed_words(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.InsertOp(insert="Instructions\n", attributes={})],
                wording=[d.InsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": False},
                    items_are_selectable=None,
                    items_are_boxed=True,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Instructions"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.BoxedText(text="This"),
                                        r.Whitespace(),
                                        r.BoxedText(text="is"),
                                        r.PlainText(text=","),
                                        r.Whitespace(),
                                        r.BoxedText(text="the"),
                                        r.Whitespace(),
                                        r.BoxedText(text="wording"),
                                        r.PlainText(text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(paragraphs=[nr.Paragraph(contents=[nr.Text(kind="text", text="Instructions")])]),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="This")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="is")], boxed=True),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="the")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="wording")], boxed=True),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_sel_tags(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.InsertOp(insert="abc", attributes={"sel": 1}),
                    d.InsertOp(insert=" ", attributes={}),
                    d.InsertOp(insert="def", attributes={"sel": 2}),
                    d.InsertOp(insert=" ", attributes={}),
                    d.InsertOp(insert="ghi", attributes={"sel": 3}),
                    d.InsertOp(insert=" ", attributes={}),
                    d.InsertOp(insert="jkl", attributes={"sel": 4}),
                    d.InsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="wording\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": False},
                    items_are_selectable={"colors": ["red", "green", "blue"]},
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.SelectedText(text="abc", color="red"),
                                        r.Whitespace(),
                                        r.SelectedText(text="def", color="green"),
                                        r.Whitespace(),
                                        r.SelectedText(text="ghi", color="blue"),
                                        r.Whitespace(),
                                        r.PlainText(text="jkl"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.SelectableText(text="wording", colors=["red", "green", "blue"], boxed=False),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", highlighted="red", text="abc"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", highlighted="green", text="def"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", highlighted="blue", text="ghi"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="jkl"),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.SelectableInput(
                                            kind="selectableInput", colors=["red", "green", "blue"], contents=[nr.Text(kind="text", text="wording")]
                                        )
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_mcq_beside_letters(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Instructions ", attributes={}),
                    d.InsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.InsertOp(insert="\n", attributes={}),
                ],
                wording=[d.InsertOp(insert="Abcd\n", attributes={})],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "characters", "letters": True},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=True,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Instructions"),
                                        r.Whitespace(),
                                        r.BoxedText(text="alpha"),
                                        r.PlainText(text=","),
                                        r.Whitespace(),
                                        r.BoxedText(text="bravo"),
                                        r.Whitespace(),
                                        r.PlainText(text="ou"),
                                        r.Whitespace(),
                                        r.BoxedText(text="charlie"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="A"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False),
                                        r.PlainText(text="b"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False),
                                        r.PlainText(text="c"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False),
                                        r.PlainText(text="d"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Instructions"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="alpha")], boxed=True),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="bravo")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="ou"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="A"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [nr.Text(kind="text", text="alpha")],
                                                [nr.Text(kind="text", text="bravo")],
                                                [nr.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Text(kind="text", text="b"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [nr.Text(kind="text", text="alpha")],
                                                [nr.Text(kind="text", text="bravo")],
                                                [nr.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Text(kind="text", text="c"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [nr.Text(kind="text", text="alpha")],
                                                [nr.Text(kind="text", text="bravo")],
                                                [nr.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Text(kind="text", text="d"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [nr.Text(kind="text", text="alpha")],
                                                [nr.Text(kind="text", text="bravo")],
                                                [nr.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_mcq_beside_words(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Instructions ", attributes={}),
                    d.InsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.InsertOp(insert="\n", attributes={}),
                ],
                wording=[d.InsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": False},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=True,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Instructions"),
                                        r.Whitespace(),
                                        r.BoxedText(text="alpha"),
                                        r.PlainText(text=","),
                                        r.Whitespace(),
                                        r.BoxedText(text="bravo"),
                                        r.Whitespace(),
                                        r.PlainText(text="ou"),
                                        r.Whitespace(),
                                        r.BoxedText(text="charlie"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="This"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.PlainText(text="is"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False),
                                        r.PlainText(text=","),
                                        r.Whitespace(),
                                        r.PlainText(text="the"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.PlainText(text="wording"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False),
                                        r.PlainText(text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Instructions"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="alpha")], boxed=True),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="bravo")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="ou"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="This"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [nr.Text(kind="text", text="alpha")],
                                                [nr.Text(kind="text", text="bravo")],
                                                [nr.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [nr.Text(kind="text", text="alpha")],
                                                [nr.Text(kind="text", text="bravo")],
                                                [nr.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="the"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [nr.Text(kind="text", text="alpha")],
                                                [nr.Text(kind="text", text="bravo")],
                                                [nr.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="wording"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [nr.Text(kind="text", text="alpha")],
                                                [nr.Text(kind="text", text="bravo")],
                                                [nr.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_mcq_beside_words_and_punctuation(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Instructions ", attributes={}),
                    d.InsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.InsertOp(insert="\n", attributes={}),
                ],
                wording=[d.InsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": True},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=True,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Instructions"),
                                        r.Whitespace(),
                                        r.BoxedText(text="alpha"),
                                        r.PlainText(text=","),
                                        r.Whitespace(),
                                        r.BoxedText(text="bravo"),
                                        r.Whitespace(),
                                        r.PlainText(text="ou"),
                                        r.Whitespace(),
                                        r.BoxedText(text="charlie"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="This"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.PlainText(text="is"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False),
                                        r.PlainText(text=","),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.PlainText(text="the"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.PlainText(text="wording"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False),
                                        r.PlainText(text="."),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Instructions"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="alpha")], boxed=True),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="bravo")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="ou"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="This"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [nr.Text(kind="text", text="alpha")],
                                                [nr.Text(kind="text", text="bravo")],
                                                [nr.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [nr.Text(kind="text", text="alpha")],
                                                [nr.Text(kind="text", text="bravo")],
                                                [nr.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [nr.Text(kind="text", text="alpha")],
                                                [nr.Text(kind="text", text="bravo")],
                                                [nr.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="the"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [nr.Text(kind="text", text="alpha")],
                                                [nr.Text(kind="text", text="bravo")],
                                                [nr.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="wording"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [nr.Text(kind="text", text="alpha")],
                                                [nr.Text(kind="text", text="bravo")],
                                                [nr.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Text(kind="text", text="."),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [nr.Text(kind="text", text="alpha")],
                                                [nr.Text(kind="text", text="bravo")],
                                                [nr.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_mcq_beside_punctuation(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Instructions ", attributes={}),
                    d.InsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.InsertOp(insert="\n", attributes={}),
                ],
                wording=[d.InsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": False, "punctuation": True},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=True,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Instructions"),
                                        r.Whitespace(),
                                        r.BoxedText(text="alpha"),
                                        r.PlainText(text=","),
                                        r.Whitespace(),
                                        r.BoxedText(text="bravo"),
                                        r.Whitespace(),
                                        r.PlainText(text="ou"),
                                        r.Whitespace(),
                                        r.BoxedText(text="charlie"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="This"),
                                        r.Whitespace(),
                                        r.PlainText(text="is"),
                                        r.PlainText(text=","),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.PlainText(text="the"),
                                        r.Whitespace(),
                                        r.PlainText(text="wording"),
                                        r.PlainText(text="."),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Instructions"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="alpha")], boxed=True),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="bravo")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="ou"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="This"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [nr.Text(kind="text", text="alpha")],
                                                [nr.Text(kind="text", text="bravo")],
                                                [nr.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="the"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="wording"),
                                        nr.Text(kind="text", text="."),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [nr.Text(kind="text", text="alpha")],
                                                [nr.Text(kind="text", text="bravo")],
                                                [nr.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_mcq_beside_sentences(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Instructions ", attributes={}),
                    d.InsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.InsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(
                        insert="Affirmative sentence. Exclamative sentence! Phrase exclamative ! Interrogative sentence? Phrase interrogative ? Suspens...\n",
                        attributes={},
                    )
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "sentences"},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=True,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Instructions"),
                                        r.Whitespace(),
                                        r.BoxedText(text="alpha"),
                                        r.PlainText(text=","),
                                        r.Whitespace(),
                                        r.BoxedText(text="bravo"),
                                        r.Whitespace(),
                                        r.PlainText(text="ou"),
                                        r.Whitespace(),
                                        r.BoxedText(text="charlie"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Affirmative"),
                                        r.Whitespace(),
                                        r.PlainText(text="sentence"),
                                        r.PlainText(text="."),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.PlainText(text="Exclamative"),
                                        r.Whitespace(),
                                        r.PlainText(text="sentence"),
                                        r.PlainText(text="!"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.PlainText(text="Phrase"),
                                        r.Whitespace(),
                                        r.PlainText(text="exclamative"),
                                        r.Whitespace(),
                                        r.PlainText(text="!"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.PlainText(text="Interrogative"),
                                        r.Whitespace(),
                                        r.PlainText(text="sentence"),
                                        r.PlainText(text="?"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.PlainText(text="Phrase"),
                                        r.Whitespace(),
                                        r.PlainText(text="interrogative"),
                                        r.Whitespace(),
                                        r.PlainText(text="?"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.PlainText(text="Suspens"),
                                        r.PlainText(text="..."),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Instructions"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="alpha")], boxed=True),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="bravo")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="ou"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Affirmative"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="sentence"),
                                        nr.Text(kind="text", text="."),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [nr.Text(kind="text", text="alpha")],
                                                [nr.Text(kind="text", text="bravo")],
                                                [nr.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="Exclamative"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="sentence"),
                                        nr.Text(kind="text", text="!"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [nr.Text(kind="text", text="alpha")],
                                                [nr.Text(kind="text", text="bravo")],
                                                [nr.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="Phrase"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="exclamative"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="!"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [nr.Text(kind="text", text="alpha")],
                                                [nr.Text(kind="text", text="bravo")],
                                                [nr.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="Interrogative"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="sentence"),
                                        nr.Text(kind="text", text="?"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [nr.Text(kind="text", text="alpha")],
                                                [nr.Text(kind="text", text="bravo")],
                                                [nr.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="Phrase"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="interrogative"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="?"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [nr.Text(kind="text", text="alpha")],
                                                [nr.Text(kind="text", text="bravo")],
                                                [nr.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="Suspens"),
                                        nr.Text(kind="text", text="..."),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [nr.Text(kind="text", text="alpha")],
                                                [nr.Text(kind="text", text="bravo")],
                                                [nr.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_mcq_beside_manual_items(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Instructions ", attributes={}),
                    d.InsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.InsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="This ", attributes={}),
                    d.InsertOp(insert="is", attributes={"manual-item": True}),
                    d.InsertOp(insert=", ", attributes={}),
                    d.InsertOp(insert="the", attributes={"manual-item": True}),
                    d.InsertOp(insert=" wording.\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "manual"},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=True,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Instructions"),
                                        r.Whitespace(),
                                        r.BoxedText(text="alpha"),
                                        r.PlainText(text=","),
                                        r.Whitespace(),
                                        r.BoxedText(text="bravo"),
                                        r.Whitespace(),
                                        r.PlainText(text="ou"),
                                        r.Whitespace(),
                                        r.BoxedText(text="charlie"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="This"),
                                        r.Whitespace(),
                                        r.PlainText(text="is"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False),
                                        r.PlainText(text=","),
                                        r.Whitespace(),
                                        r.PlainText(text="the"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.PlainText(text="wording"),
                                        r.PlainText(text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Instructions"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="alpha")], boxed=True),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="bravo")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="ou"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="This"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [nr.Text(kind="text", text="alpha")],
                                                [nr.Text(kind="text", text="bravo")],
                                                [nr.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="the"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [nr.Text(kind="text", text="alpha")],
                                                [nr.Text(kind="text", text="bravo")],
                                                [nr.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="wording"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_mcq_below_letters(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Instructions ", attributes={}),
                    d.InsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.InsertOp(insert="\n", attributes={}),
                ],
                wording=[d.InsertOp(insert="Abcd\n", attributes={})],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "characters", "letters": True},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=True,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Instructions"),
                                        r.Whitespace(),
                                        r.BoxedText(text="alpha"),
                                        r.PlainText(text=","),
                                        r.Whitespace(),
                                        r.BoxedText(text="bravo"),
                                        r.Whitespace(),
                                        r.PlainText(text="ou"),
                                        r.Whitespace(),
                                        r.BoxedText(text="charlie"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.Stack(
                                            type="stack",
                                            contents=[
                                                r.PlainText(text="A"),
                                                r.MultipleChoicesInput(
                                                    show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False
                                                ),
                                            ],
                                        ),
                                        r.Stack(
                                            type="stack",
                                            contents=[
                                                r.PlainText(text="b"),
                                                r.MultipleChoicesInput(
                                                    show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False
                                                ),
                                            ],
                                        ),
                                        r.Stack(
                                            type="stack",
                                            contents=[
                                                r.PlainText(text="c"),
                                                r.MultipleChoicesInput(
                                                    show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False
                                                ),
                                            ],
                                        ),
                                        r.Stack(
                                            type="stack",
                                            contents=[
                                                r.PlainText(text="d"),
                                                r.MultipleChoicesInput(
                                                    show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False
                                                ),
                                            ],
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Instructions"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="alpha")], boxed=True),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="bravo")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="ou"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                nr.Text(kind="text", text="A"),
                                                nr.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [nr.Text(kind="text", text="alpha")],
                                                        [nr.Text(kind="text", text="bravo")],
                                                        [nr.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        nr.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                nr.Text(kind="text", text="b"),
                                                nr.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [nr.Text(kind="text", text="alpha")],
                                                        [nr.Text(kind="text", text="bravo")],
                                                        [nr.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        nr.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                nr.Text(kind="text", text="c"),
                                                nr.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [nr.Text(kind="text", text="alpha")],
                                                        [nr.Text(kind="text", text="bravo")],
                                                        [nr.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        nr.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                nr.Text(kind="text", text="d"),
                                                nr.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [nr.Text(kind="text", text="alpha")],
                                                        [nr.Text(kind="text", text="bravo")],
                                                        [nr.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_mcq_below_words(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Instructions ", attributes={}),
                    d.InsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.InsertOp(insert="\n", attributes={}),
                ],
                wording=[d.InsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": False},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=True,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Instructions"),
                                        r.Whitespace(),
                                        r.BoxedText(text="alpha"),
                                        r.PlainText(text=","),
                                        r.Whitespace(),
                                        r.BoxedText(text="bravo"),
                                        r.Whitespace(),
                                        r.PlainText(text="ou"),
                                        r.Whitespace(),
                                        r.BoxedText(text="charlie"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.Stack(
                                            type="stack",
                                            contents=[
                                                r.PlainText(text="This"),
                                                r.MultipleChoicesInput(
                                                    show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False
                                                ),
                                            ],
                                        ),
                                        r.Whitespace(),
                                        r.Stack(
                                            type="stack",
                                            contents=[
                                                r.PlainText(text="is"),
                                                r.MultipleChoicesInput(
                                                    show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False
                                                ),
                                            ],
                                        ),
                                        r.PlainText(text=","),
                                        r.Whitespace(),
                                        r.Stack(
                                            type="stack",
                                            contents=[
                                                r.PlainText(text="the"),
                                                r.MultipleChoicesInput(
                                                    show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False
                                                ),
                                            ],
                                        ),
                                        r.Whitespace(),
                                        r.Stack(
                                            type="stack",
                                            contents=[
                                                r.PlainText(text="wording"),
                                                r.MultipleChoicesInput(
                                                    show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False
                                                ),
                                            ],
                                        ),
                                        r.PlainText(text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Instructions"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="alpha")], boxed=True),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="bravo")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="ou"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                nr.Text(kind="text", text="This"),
                                                nr.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [nr.Text(kind="text", text="alpha")],
                                                        [nr.Text(kind="text", text="bravo")],
                                                        [nr.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                nr.Text(kind="text", text="is"),
                                                nr.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [nr.Text(kind="text", text="alpha")],
                                                        [nr.Text(kind="text", text="bravo")],
                                                        [nr.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                nr.Text(kind="text", text="the"),
                                                nr.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [nr.Text(kind="text", text="alpha")],
                                                        [nr.Text(kind="text", text="bravo")],
                                                        [nr.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                nr.Text(kind="text", text="wording"),
                                                nr.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [nr.Text(kind="text", text="alpha")],
                                                        [nr.Text(kind="text", text="bravo")],
                                                        [nr.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_mcq_below_words_and_punctuation(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Instructions ", attributes={}),
                    d.InsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.InsertOp(insert="\n", attributes={}),
                ],
                wording=[d.InsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": True},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=True,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Instructions"),
                                        r.Whitespace(),
                                        r.BoxedText(text="alpha"),
                                        r.PlainText(text=","),
                                        r.Whitespace(),
                                        r.BoxedText(text="bravo"),
                                        r.Whitespace(),
                                        r.PlainText(text="ou"),
                                        r.Whitespace(),
                                        r.BoxedText(text="charlie"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.Stack(
                                            type="stack",
                                            contents=[
                                                r.PlainText(text="This"),
                                                r.MultipleChoicesInput(
                                                    show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False
                                                ),
                                            ],
                                        ),
                                        r.Whitespace(),
                                        r.Stack(
                                            type="stack",
                                            contents=[
                                                r.PlainText(text="is"),
                                                r.MultipleChoicesInput(
                                                    show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False
                                                ),
                                            ],
                                        ),
                                        r.Stack(
                                            type="stack",
                                            contents=[
                                                r.PlainText(text=","),
                                                r.MultipleChoicesInput(
                                                    show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False
                                                ),
                                            ],
                                        ),
                                        r.Whitespace(),
                                        r.Stack(
                                            type="stack",
                                            contents=[
                                                r.PlainText(text="the"),
                                                r.MultipleChoicesInput(
                                                    show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False
                                                ),
                                            ],
                                        ),
                                        r.Whitespace(),
                                        r.Stack(
                                            type="stack",
                                            contents=[
                                                r.PlainText(text="wording"),
                                                r.MultipleChoicesInput(
                                                    show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False
                                                ),
                                            ],
                                        ),
                                        r.Stack(
                                            type="stack",
                                            contents=[
                                                r.PlainText(text="."),
                                                r.MultipleChoicesInput(
                                                    show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False
                                                ),
                                            ],
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Instructions"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="alpha")], boxed=True),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="bravo")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="ou"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                nr.Text(kind="text", text="This"),
                                                nr.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [nr.Text(kind="text", text="alpha")],
                                                        [nr.Text(kind="text", text="bravo")],
                                                        [nr.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                nr.Text(kind="text", text="is"),
                                                nr.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [nr.Text(kind="text", text="alpha")],
                                                        [nr.Text(kind="text", text="bravo")],
                                                        [nr.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        nr.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                nr.Text(kind="text", text=","),
                                                nr.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [nr.Text(kind="text", text="alpha")],
                                                        [nr.Text(kind="text", text="bravo")],
                                                        [nr.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                nr.Text(kind="text", text="the"),
                                                nr.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [nr.Text(kind="text", text="alpha")],
                                                        [nr.Text(kind="text", text="bravo")],
                                                        [nr.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                nr.Text(kind="text", text="wording"),
                                                nr.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [nr.Text(kind="text", text="alpha")],
                                                        [nr.Text(kind="text", text="bravo")],
                                                        [nr.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        nr.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                nr.Text(kind="text", text="."),
                                                nr.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [nr.Text(kind="text", text="alpha")],
                                                        [nr.Text(kind="text", text="bravo")],
                                                        [nr.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_mcq_below_punctuation(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Instructions ", attributes={}),
                    d.InsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.InsertOp(insert="\n", attributes={}),
                ],
                wording=[d.InsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": False, "punctuation": True},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=True,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Instructions"),
                                        r.Whitespace(),
                                        r.BoxedText(text="alpha"),
                                        r.PlainText(text=","),
                                        r.Whitespace(),
                                        r.BoxedText(text="bravo"),
                                        r.Whitespace(),
                                        r.PlainText(text="ou"),
                                        r.Whitespace(),
                                        r.BoxedText(text="charlie"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="This"),
                                        r.Whitespace(),
                                        r.PlainText(text="is"),
                                        r.Stack(
                                            type="stack",
                                            contents=[
                                                r.PlainText(text=","),
                                                r.MultipleChoicesInput(
                                                    show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False
                                                ),
                                            ],
                                        ),
                                        r.Whitespace(),
                                        r.PlainText(text="the"),
                                        r.Whitespace(),
                                        r.PlainText(text="wording"),
                                        r.Stack(
                                            type="stack",
                                            contents=[
                                                r.PlainText(text="."),
                                                r.MultipleChoicesInput(
                                                    show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False
                                                ),
                                            ],
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Instructions"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="alpha")], boxed=True),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="bravo")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="ou"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="This"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                nr.Text(kind="text", text=","),
                                                nr.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [nr.Text(kind="text", text="alpha")],
                                                        [nr.Text(kind="text", text="bravo")],
                                                        [nr.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="the"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="wording"),
                                        nr.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                nr.Text(kind="text", text="."),
                                                nr.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [nr.Text(kind="text", text="alpha")],
                                                        [nr.Text(kind="text", text="bravo")],
                                                        [nr.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_mcq_below_sentences(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Instructions ", attributes={}),
                    d.InsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.InsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(
                        insert="Affirmative sentence. Exclamative sentence! Phrase exclamative ! Interrogative sentence? Phrase interrogative ? Suspens...\n",
                        attributes={},
                    )
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "sentences"},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=True,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Instructions"),
                                        r.Whitespace(),
                                        r.BoxedText(text="alpha"),
                                        r.PlainText(text=","),
                                        r.Whitespace(),
                                        r.BoxedText(text="bravo"),
                                        r.Whitespace(),
                                        r.PlainText(text="ou"),
                                        r.Whitespace(),
                                        r.BoxedText(text="charlie"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.Stack(
                                            type="stack",
                                            contents=[
                                                r.Line(
                                                    type="line",
                                                    contents=[
                                                        r.PlainText(text="Affirmative"),
                                                        r.Whitespace(),
                                                        r.PlainText(text="sentence"),
                                                        r.PlainText(text="."),
                                                    ],
                                                ),
                                                r.MultipleChoicesInput(
                                                    show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False
                                                ),
                                            ],
                                        ),
                                        r.Whitespace(),
                                        r.Stack(
                                            type="stack",
                                            contents=[
                                                r.Line(
                                                    type="line",
                                                    contents=[
                                                        r.PlainText(text="Exclamative"),
                                                        r.Whitespace(),
                                                        r.PlainText(text="sentence"),
                                                        r.PlainText(text="!"),
                                                    ],
                                                ),
                                                r.MultipleChoicesInput(
                                                    show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False
                                                ),
                                            ],
                                        ),
                                        r.Whitespace(),
                                        r.Stack(
                                            type="stack",
                                            contents=[
                                                r.Line(
                                                    type="line",
                                                    contents=[
                                                        r.PlainText(text="Phrase"),
                                                        r.Whitespace(),
                                                        r.PlainText(text="exclamative"),
                                                        r.Whitespace(),
                                                        r.PlainText(text="!"),
                                                    ],
                                                ),
                                                r.MultipleChoicesInput(
                                                    show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False
                                                ),
                                            ],
                                        ),
                                        r.Whitespace(),
                                        r.Stack(
                                            type="stack",
                                            contents=[
                                                r.Line(
                                                    type="line",
                                                    contents=[
                                                        r.PlainText(text="Interrogative"),
                                                        r.Whitespace(),
                                                        r.PlainText(text="sentence"),
                                                        r.PlainText(text="?"),
                                                    ],
                                                ),
                                                r.MultipleChoicesInput(
                                                    show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False
                                                ),
                                            ],
                                        ),
                                        r.Whitespace(),
                                        r.Stack(
                                            type="stack",
                                            contents=[
                                                r.Line(
                                                    type="line",
                                                    contents=[
                                                        r.PlainText(text="Phrase"),
                                                        r.Whitespace(),
                                                        r.PlainText(text="interrogative"),
                                                        r.Whitespace(),
                                                        r.PlainText(text="?"),
                                                    ],
                                                ),
                                                r.MultipleChoicesInput(
                                                    show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False
                                                ),
                                            ],
                                        ),
                                        r.Whitespace(),
                                        r.Stack(
                                            type="stack",
                                            contents=[
                                                r.Line(
                                                    type="line",
                                                    contents=[
                                                        r.PlainText(text="Suspens"),
                                                        r.PlainText(text="..."),
                                                    ],
                                                ),
                                                r.MultipleChoicesInput(
                                                    show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False
                                                ),
                                            ],
                                        ),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Instructions"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="alpha")], boxed=True),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="bravo")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="ou"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                nr.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        nr.Text(kind="text", text="Affirmative"),
                                                        nr.Whitespace(kind="whitespace"),
                                                        nr.Text(kind="text", text="sentence"),
                                                        nr.Text(kind="text", text="."),
                                                    ],
                                                    vertical=False,
                                                ),
                                                nr.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [nr.Text(kind="text", text="alpha")],
                                                        [nr.Text(kind="text", text="bravo")],
                                                        [nr.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                nr.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        nr.Text(kind="text", text="Exclamative"),
                                                        nr.Whitespace(kind="whitespace"),
                                                        nr.Text(kind="text", text="sentence"),
                                                        nr.Text(kind="text", text="!"),
                                                    ],
                                                    vertical=False,
                                                ),
                                                nr.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [nr.Text(kind="text", text="alpha")],
                                                        [nr.Text(kind="text", text="bravo")],
                                                        [nr.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                nr.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        nr.Text(kind="text", text="Phrase"),
                                                        nr.Whitespace(kind="whitespace"),
                                                        nr.Text(kind="text", text="exclamative"),
                                                        nr.Whitespace(kind="whitespace"),
                                                        nr.Text(kind="text", text="!"),
                                                    ],
                                                    vertical=False,
                                                ),
                                                nr.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [nr.Text(kind="text", text="alpha")],
                                                        [nr.Text(kind="text", text="bravo")],
                                                        [nr.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                nr.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        nr.Text(kind="text", text="Interrogative"),
                                                        nr.Whitespace(kind="whitespace"),
                                                        nr.Text(kind="text", text="sentence"),
                                                        nr.Text(kind="text", text="?"),
                                                    ],
                                                    vertical=False,
                                                ),
                                                nr.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [nr.Text(kind="text", text="alpha")],
                                                        [nr.Text(kind="text", text="bravo")],
                                                        [nr.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                nr.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        nr.Text(kind="text", text="Phrase"),
                                                        nr.Whitespace(kind="whitespace"),
                                                        nr.Text(kind="text", text="interrogative"),
                                                        nr.Whitespace(kind="whitespace"),
                                                        nr.Text(kind="text", text="?"),
                                                    ],
                                                    vertical=False,
                                                ),
                                                nr.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [nr.Text(kind="text", text="alpha")],
                                                        [nr.Text(kind="text", text="bravo")],
                                                        [nr.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                nr.AnySequence(
                                                    kind="sequence",
                                                    contents=[nr.Text(kind="text", text="Suspens"), nr.Text(kind="text", text="...")],
                                                    vertical=False,
                                                ),
                                                nr.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [nr.Text(kind="text", text="alpha")],
                                                        [nr.Text(kind="text", text="bravo")],
                                                        [nr.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_mcq_below_manual_items(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Instructions ", attributes={}),
                    d.InsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.InsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="This ", attributes={}),
                    d.InsertOp(insert="is", attributes={"manual-item": True}),
                    d.InsertOp(insert=", ", attributes={}),
                    d.InsertOp(insert="the", attributes={"manual-item": True}),
                    d.InsertOp(insert=" wording.\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "manual"},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=True,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Instructions"),
                                        r.Whitespace(),
                                        r.BoxedText(text="alpha"),
                                        r.PlainText(text=","),
                                        r.Whitespace(),
                                        r.BoxedText(text="bravo"),
                                        r.Whitespace(),
                                        r.PlainText(text="ou"),
                                        r.Whitespace(),
                                        r.BoxedText(text="charlie"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="This"),
                                        r.Whitespace(),
                                        r.Stack(
                                            type="stack",
                                            contents=[
                                                r.PlainText(text="is"),
                                                r.MultipleChoicesInput(
                                                    show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False
                                                ),
                                            ],
                                        ),
                                        r.PlainText(text=","),
                                        r.Whitespace(),
                                        r.Stack(
                                            type="stack",
                                            contents=[
                                                r.PlainText(text="the"),
                                                r.MultipleChoicesInput(
                                                    show_arrow_before=False, choices=["alpha", "bravo", "charlie"], show_choices_by_default=False
                                                ),
                                            ],
                                        ),
                                        r.Whitespace(),
                                        r.PlainText(text="wording"),
                                        r.PlainText(text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Instructions"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="alpha")], boxed=True),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="bravo")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="ou"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="This"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                nr.Text(kind="text", text="is"),
                                                nr.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [nr.Text(kind="text", text="alpha")],
                                                        [nr.Text(kind="text", text="bravo")],
                                                        [nr.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                nr.Text(kind="text", text="the"),
                                                nr.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [nr.Text(kind="text", text="alpha")],
                                                        [nr.Text(kind="text", text="bravo")],
                                                        [nr.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="wording"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )


class MultipleChoicesInInstructionsAdaptationTestCase(AdaptationTestCase):
    def test_simple(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Choose ", attributes={}),
                    d.InsertOp(insert="a or b", attributes={"choices2": {"start": "", "separator1": "or", "separator2": "", "stop": "", "placeholder": "..."}}),
                    d.InsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="A ... B ...\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="multiple-choices",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Choose"),
                                        r.Whitespace(),
                                        r.BoxedText(text="a"),
                                        r.Whitespace(),
                                        r.PlainText(text="ou"),
                                        r.Whitespace(),
                                        r.BoxedText(text="b"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="A"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["a", "b"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.PlainText(text="B"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["a", "b"], show_choices_by_default=False),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Choose"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="a")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="ou"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="b")], boxed=True),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="A"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="a")], [nr.Text(kind="text", text="b")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="B"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="a")], [nr.Text(kind="text", text="b")]],
                                            show_choices_by_default=False,
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_example_and_clue(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Choose ", attributes={}),
                    d.InsertOp(insert="a or b", attributes={"choices2": {"start": "", "separator1": "or", "separator2": "", "stop": "", "placeholder": "@"}}),
                    d.InsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="A @ B @\n", attributes={}),
                ],
                example=[
                    d.InsertOp(insert="This {choices2||/||||is} the @ example.\n", attributes={}),
                ],
                clue=[
                    d.InsertOp(insert="This is {choices2||/||||the} @ clue.\n", attributes={}),
                ],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="multiple-choices",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Choose"),
                                        r.Whitespace(),
                                        r.BoxedText(text="a"),
                                        r.Whitespace(),
                                        r.PlainText(text="ou"),
                                        r.Whitespace(),
                                        r.BoxedText(text="b"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                                r.Paragraph(
                                    tokens=[
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
                                    ]
                                ),
                                r.Paragraph(
                                    tokens=[
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
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="A"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["a", "b"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.PlainText(text="B"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["a", "b"], show_choices_by_default=False),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Choose"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="a")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="ou"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="b")], boxed=True),
                                        nr.Text(kind="text", text="."),
                                    ]
                                ),
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="This"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="{"),
                                        nr.Text(kind="text", text="choices2"),
                                        nr.Text(kind="text", text="|"),
                                        nr.Text(kind="text", text="|"),
                                        nr.Text(kind="text", text="/"),
                                        nr.Text(kind="text", text="|"),
                                        nr.Text(kind="text", text="|"),
                                        nr.Text(kind="text", text="|"),
                                        nr.Text(kind="text", text="|"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Text(kind="text", text="}"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="the"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="@"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="example"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                ),
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="This"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="{"),
                                        nr.Text(kind="text", text="choices2"),
                                        nr.Text(kind="text", text="|"),
                                        nr.Text(kind="text", text="|"),
                                        nr.Text(kind="text", text="/"),
                                        nr.Text(kind="text", text="|"),
                                        nr.Text(kind="text", text="|"),
                                        nr.Text(kind="text", text="|"),
                                        nr.Text(kind="text", text="|"),
                                        nr.Text(kind="text", text="the"),
                                        nr.Text(kind="text", text="}"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="@"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="clue"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="A"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="a")], [nr.Text(kind="text", text="b")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="B"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="a")], [nr.Text(kind="text", text="b")]],
                                            show_choices_by_default=False,
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_choices2(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Choose ", attributes={}),
                    d.InsertOp(insert="a or b", attributes={"choices2": {"start": "", "separator1": "or", "separator2": "", "stop": "", "placeholder": "..."}}),
                    d.InsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="A ... B ...\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="multiple-choices",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Choose"),
                                        r.Whitespace(),
                                        r.BoxedText(text="a"),
                                        r.Whitespace(),
                                        r.PlainText(text="ou"),
                                        r.Whitespace(),
                                        r.BoxedText(text="b"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="A"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["a", "b"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.PlainText(text="B"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["a", "b"], show_choices_by_default=False),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Choose"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="a")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="ou"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="b")], boxed=True),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="A"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="a")], [nr.Text(kind="text", text="b")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="B"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="a")], [nr.Text(kind="text", text="b")]],
                                            show_choices_by_default=False,
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_choices2_with_empty_separator(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Choose ", attributes={}),
                    d.InsertOp(insert="a b", attributes={"choices2": {"start": "", "separator1": "", "separator2": "", "stop": "", "placeholder": "..."}}),
                    d.InsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="A ... B ...\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="multiple-choices",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Choose"),
                                        r.Whitespace(),
                                        r.BoxedText(text="a b"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="A"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["a b"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.PlainText(text="B"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["a b"], show_choices_by_default=False),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Choose"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="a b")], boxed=True),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="A"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput", choices=[[nr.Text(kind="text", text="a b")]], show_choices_by_default=False
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="B"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput", choices=[[nr.Text(kind="text", text="a b")]], show_choices_by_default=False
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_choices2_with_two_separators(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Choose ", attributes={}),
                    d.InsertOp(
                        insert="a, b, c or d", attributes={"choices2": {"start": "", "separator1": ",", "separator2": "or", "stop": "", "placeholder": "..."}}
                    ),
                    d.InsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="A ... B ...\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="multiple-choices",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
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
                                        r.PlainText(text="ou"),
                                        r.Whitespace(),
                                        r.BoxedText(text="d"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="A"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["a", "b", "c", "d"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.PlainText(text="B"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["a", "b", "c", "d"], show_choices_by_default=False),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Choose"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="a")], boxed=True),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="b")], boxed=True),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="c")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="ou"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="d")], boxed=True),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="A"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [nr.Text(kind="text", text="a")],
                                                [nr.Text(kind="text", text="b")],
                                                [nr.Text(kind="text", text="c")],
                                                [nr.Text(kind="text", text="d")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="B"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [nr.Text(kind="text", text="a")],
                                                [nr.Text(kind="text", text="b")],
                                                [nr.Text(kind="text", text="c")],
                                                [nr.Text(kind="text", text="d")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_choices2_with_oxford_comma(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Choose ", attributes={}),
                    d.InsertOp(
                        insert="a, b, c, or d", attributes={"choices2": {"start": "", "separator1": ",", "separator2": "or", "stop": "", "placeholder": "..."}}
                    ),
                    d.InsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="A ... B ...\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="multiple-choices",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
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
                                        r.PlainText(text="ou"),
                                        r.Whitespace(),
                                        r.BoxedText(text="d"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="A"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["a", "b", "c", "d"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.PlainText(text="B"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["a", "b", "c", "d"], show_choices_by_default=False),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Choose"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="a")], boxed=True),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="b")], boxed=True),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="c")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="ou"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="d")], boxed=True),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="A"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [nr.Text(kind="text", text="a")],
                                                [nr.Text(kind="text", text="b")],
                                                [nr.Text(kind="text", text="c")],
                                                [nr.Text(kind="text", text="d")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="B"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [nr.Text(kind="text", text="a")],
                                                [nr.Text(kind="text", text="b")],
                                                [nr.Text(kind="text", text="c")],
                                                [nr.Text(kind="text", text="d")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_choices2_with_successive_separators(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Choose ", attributes={}),
                    d.InsertOp(
                        insert="a / b // c", attributes={"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": "..."}}
                    ),
                    d.InsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="A ... B ...\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="multiple-choices",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Choose"),
                                        r.Whitespace(),
                                        r.BoxedText(text="a"),
                                        r.PlainText(text=","),
                                        r.Whitespace(),
                                        r.BoxedText(text="b"),
                                        r.Whitespace(),
                                        r.PlainText(text="ou"),
                                        r.Whitespace(),
                                        r.BoxedText(text="c"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="A"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["a", "b", "c"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.PlainText(text="B"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["a", "b", "c"], show_choices_by_default=False),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Choose"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="a")], boxed=True),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="b")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="ou"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="c")], boxed=True),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="A"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="a")], [nr.Text(kind="text", text="b")], [nr.Text(kind="text", text="c")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="B"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="a")], [nr.Text(kind="text", text="b")], [nr.Text(kind="text", text="c")]],
                                            show_choices_by_default=False,
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_choices2_with_start_and_stop(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Choose ", attributes={}),
                    d.InsertOp(
                        insert="(a or b)", attributes={"choices2": {"start": "(", "separator1": "or", "separator2": "", "stop": ")", "placeholder": "..."}}
                    ),
                    d.InsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="A ... B ...\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="multiple-choices",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Choose"),
                                        r.Whitespace(),
                                        r.BoxedText(text="a"),
                                        r.Whitespace(),
                                        r.PlainText(text="ou"),
                                        r.Whitespace(),
                                        r.BoxedText(text="b"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="A"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["a", "b"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.PlainText(text="B"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["a", "b"], show_choices_by_default=False),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Choose"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="a")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="ou"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="b")], boxed=True),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="A"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="a")], [nr.Text(kind="text", text="b")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="B"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="a")], [nr.Text(kind="text", text="b")]],
                                            show_choices_by_default=False,
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_two_choices2(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Choose ", attributes={}),
                    d.InsertOp(insert="a or b", attributes={"choices2": {"start": "", "separator1": "or", "separator2": "", "stop": "", "placeholder": "..."}}),
                    d.InsertOp(insert=" and ", attributes={}),
                    d.InsertOp(insert="c or d", attributes={"choices2": {"start": "", "separator1": "or", "separator2": "", "stop": "", "placeholder": "@@@"}}),
                    d.InsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="A ... @@@\nB ... @@@\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="multiple-choices",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Choose"),
                                        r.Whitespace(),
                                        r.BoxedText(text="a"),
                                        r.Whitespace(),
                                        r.PlainText(text="ou"),
                                        r.Whitespace(),
                                        r.BoxedText(text="b"),
                                        r.Whitespace(),
                                        r.PlainText(text="and"),
                                        r.Whitespace(),
                                        r.BoxedText(text="c"),
                                        r.Whitespace(),
                                        r.PlainText(text="ou"),
                                        r.Whitespace(),
                                        r.BoxedText(text="d"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="A"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["a", "b"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["c", "d"], show_choices_by_default=False),
                                    ]
                                ),
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="B"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["a", "b"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["c", "d"], show_choices_by_default=False),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Choose"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="a")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="ou"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="b")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="and"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="c")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="ou"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="d")], boxed=True),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="A"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="a")], [nr.Text(kind="text", text="b")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="c")], [nr.Text(kind="text", text="d")]],
                                            show_choices_by_default=False,
                                        ),
                                    ]
                                ),
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="B"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="a")], [nr.Text(kind="text", text="b")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="c")], [nr.Text(kind="text", text="d")]],
                                            show_choices_by_default=False,
                                        ),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
        )

    # https://github.com/jacquev6/Gabby/issues/3#issuecomment-2462720676
    def test_chose_a_single_letter_to_complete_a_word(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Complète les mots avec ", attributes={}),
                    d.InsertOp(insert="m ou n", attributes={"choices2": {"start": "", "separator1": "ou", "separator2": "", "stop": "", "placeholder": "..."}}),
                    d.InsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="i...mense i...juste\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="multiple-choices",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Complète"),
                                        r.Whitespace(),
                                        r.PlainText(text="les"),
                                        r.Whitespace(),
                                        r.PlainText(text="mots"),
                                        r.Whitespace(),
                                        r.PlainText(text="avec"),
                                        r.Whitespace(),
                                        r.BoxedText(text="m"),
                                        r.Whitespace(),
                                        r.PlainText(text="ou"),
                                        r.Whitespace(),
                                        r.BoxedText(text="n"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="i"),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["m", "n"], show_choices_by_default=False),
                                        r.PlainText(text="mense"),
                                        r.Whitespace(),
                                        r.PlainText(text="i"),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["m", "n"], show_choices_by_default=False),
                                        r.PlainText(text="juste"),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Complète"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="les"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="mots"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="avec"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="m")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="ou"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="n")], boxed=True),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="i"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="m")], [nr.Text(kind="text", text="n")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Text(kind="text", text="mense"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="i"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="m")], [nr.Text(kind="text", text="n")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Text(kind="text", text="juste"),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )


class MultipleChoicesInWordingAdaptationTestCase(AdaptationTestCase):
    def test_simple(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Choose wisely.\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="A ", attributes={}),
                    d.InsertOp(insert="a/b/c", attributes={"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": ""}}),
                    d.InsertOp(insert=" B ", attributes={}),
                    d.InsertOp(insert="d#e", attributes={"choices2": {"start": "", "separator1": "#", "separator2": "", "stop": "", "placeholder": ""}}),
                    d.InsertOp(insert=".\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="multiple-choices",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Choose"),
                                        r.Whitespace(),
                                        r.PlainText(text="wisely"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="A"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["a", "b", "c"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.PlainText(text="B"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["d", "e"], show_choices_by_default=False),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Choose"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="wisely"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="A"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="a")], [nr.Text(kind="text", text="b")], [nr.Text(kind="text", text="c")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="B"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="d")], [nr.Text(kind="text", text="e")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_choices2_without_placeholder(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Choose wisely.\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="A ", attributes={}),
                    d.InsertOp(
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
                    d.InsertOp(insert=".\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="multiple-choices",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Choose"),
                                        r.Whitespace(),
                                        r.PlainText(text="wisely"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="A"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["blah", "blih"], show_choices_by_default=False),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Choose"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="wisely"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="A"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="blah")], [nr.Text(kind="text", text="blih")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_choices2_with_spaces(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Choose wisely.\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="A ", attributes={}),
                    d.InsertOp(
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
                    d.InsertOp(insert=".\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="multiple-choices",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Choose"),
                                        r.Whitespace(),
                                        r.PlainText(text="wisely"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="A"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["blah", "blih"], show_choices_by_default=False),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Choose"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="wisely"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="A"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="blah")], [nr.Text(kind="text", text="blih")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_choices2_with_empty_start_and_stop(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Choose wisely.\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="A ", attributes={}),
                    d.InsertOp(
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
                    d.InsertOp(insert=".\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="multiple-choices",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Choose"),
                                        r.Whitespace(),
                                        r.PlainText(text="wisely"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="A"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["blah", "blih"], show_choices_by_default=False),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Choose"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="wisely"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="A"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="blah")], [nr.Text(kind="text", text="blih")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_choices2_with_empty_separator(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Choose wisely.\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="A ", attributes={}),
                    d.InsertOp(
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
                    d.InsertOp(insert=".\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="multiple-choices",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Choose"),
                                        r.Whitespace(),
                                        r.PlainText(text="wisely"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="A"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["blah / blih"], show_choices_by_default=False),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Choose"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="wisely"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="A"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput", choices=[[nr.Text(kind="text", text="blah / blih")]], show_choices_by_default=False
                                        ),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_choices2_with_longer_separators(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Choose wisely.\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="A ", attributes={}),
                    d.InsertOp(
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
                    d.InsertOp(insert=".\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="multiple-choices",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Choose"),
                                        r.Whitespace(),
                                        r.PlainText(text="wisely"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="A"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["blah", "blih"], show_choices_by_default=False),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Choose"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="wisely"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="A"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="blah")], [nr.Text(kind="text", text="blih")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_choices2_with_escaped_separators(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Choose wisely.\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="A ", attributes={}),
                    d.InsertOp(
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
                    d.InsertOp(insert=".\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="multiple-choices",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Choose"),
                                        r.Whitespace(),
                                        r.PlainText(text="wisely"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="A"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["blah", "blih"], show_choices_by_default=False),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Choose"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="wisely"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="A"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="blah")], [nr.Text(kind="text", text="blih")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_choices2_with_placeholder_before(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Choose wisely.\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="The sky is @@. ", attributes={}),
                    d.InsertOp(
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
                    d.InsertOp(insert=" \n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="multiple-choices",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Choose"),
                                        r.Whitespace(),
                                        r.PlainText(text="wisely"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="The"),
                                        r.Whitespace(),
                                        r.PlainText(text="sky"),
                                        r.Whitespace(),
                                        r.PlainText(text="is"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["blue", "red"], show_choices_by_default=False),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Choose"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="wisely"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="The"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="sky"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="blue")], [nr.Text(kind="text", text="red")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_choices2_with_placeholder_after(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Choose wisely.\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(
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
                    d.InsertOp(insert=" The sky is ....\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="multiple-choices",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Choose"),
                                        r.Whitespace(),
                                        r.PlainText(text="wisely"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="The"),
                                        r.Whitespace(),
                                        r.PlainText(text="sky"),
                                        r.Whitespace(),
                                        r.PlainText(text="is"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["blue", "red"], show_choices_by_default=False),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Choose"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="wisely"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="The"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="sky"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="blue")], [nr.Text(kind="text", text="red")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_choices2_with_two_placeholders(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Choose wisely.\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(
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
                    d.InsertOp(insert=" The sky is ..., the sun is ....\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="multiple-choices",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Choose"),
                                        r.Whitespace(),
                                        r.PlainText(text="wisely"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="The"),
                                        r.Whitespace(),
                                        r.PlainText(text="sky"),
                                        r.Whitespace(),
                                        r.PlainText(text="is"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["blue", "yellow"], show_choices_by_default=False),
                                        r.PlainText(text=","),
                                        r.Whitespace(),
                                        r.PlainText(text="the"),
                                        r.Whitespace(),
                                        r.PlainText(text="sun"),
                                        r.Whitespace(),
                                        r.PlainText(text="is"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["blue", "yellow"], show_choices_by_default=False),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Choose"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="wisely"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="The"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="sky"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="blue")], [nr.Text(kind="text", text="yellow")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="the"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="sun"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="blue")], [nr.Text(kind="text", text="yellow")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_two_choices2_with_matching_placeholders(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Choose wisely.\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(
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
                    d.InsertOp(insert=" ", attributes={}),
                    d.InsertOp(
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
                    d.InsertOp(insert=" The sky is @1, the sun is @2.\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="multiple-choices",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Choose"),
                                        r.Whitespace(),
                                        r.PlainText(text="wisely"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="The"),
                                        r.Whitespace(),
                                        r.PlainText(text="sky"),
                                        r.Whitespace(),
                                        r.PlainText(text="is"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["blue", "red"], show_choices_by_default=False),
                                        r.PlainText(text=","),
                                        r.Whitespace(),
                                        r.PlainText(text="the"),
                                        r.Whitespace(),
                                        r.PlainText(text="sun"),
                                        r.Whitespace(),
                                        r.PlainText(text="is"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["green", "yellow"], show_choices_by_default=False),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Choose"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="wisely"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="The"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="sky"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="blue")], [nr.Text(kind="text", text="red")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="the"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="sun"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="green")], [nr.Text(kind="text", text="yellow")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_two_choices2_with_identical_placeholders(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Choose wisely.\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="The sky is @@. ", attributes={}),
                    d.InsertOp(
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
                    d.InsertOp(insert="\n\nThe sun is @@. ", attributes={}),
                    d.InsertOp(
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
                    d.InsertOp(insert="\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="multiple-choices",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Choose"),
                                        r.Whitespace(),
                                        r.PlainText(text="wisely"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="The"),
                                        r.Whitespace(),
                                        r.PlainText(text="sky"),
                                        r.Whitespace(),
                                        r.PlainText(text="is"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["blue", "red"], show_choices_by_default=False),
                                        r.PlainText(text="."),
                                    ]
                                ),
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="The"),
                                        r.Whitespace(),
                                        r.PlainText(text="sun"),
                                        r.Whitespace(),
                                        r.PlainText(text="is"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["green", "yellow"], show_choices_by_default=False),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Choose"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="wisely"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="The"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="sky"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="blue")], [nr.Text(kind="text", text="red")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Text(kind="text", text="."),
                                    ]
                                ),
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="The"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="sun"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="green")], [nr.Text(kind="text", text="yellow")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Text(kind="text", text="."),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_two_choices2_with_spaces_between_them(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Choose wisely.\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="The sky is @1, ", attributes={}),
                    d.InsertOp(
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
                    d.InsertOp(insert=" ", attributes={}),
                    d.InsertOp(
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
                    d.InsertOp(insert=" the sun is @2.\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="multiple-choices",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Choose"),
                                        r.Whitespace(),
                                        r.PlainText(text="wisely"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="The"),
                                        r.Whitespace(),
                                        r.PlainText(text="sky"),
                                        r.Whitespace(),
                                        r.PlainText(text="is"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["blue", "red"], show_choices_by_default=False),
                                        r.PlainText(text=","),
                                        r.Whitespace(),
                                        r.PlainText(text="the"),
                                        r.Whitespace(),
                                        r.PlainText(text="sun"),
                                        r.Whitespace(),
                                        r.PlainText(text="is"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["green", "yellow"], show_choices_by_default=False),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Choose"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="wisely"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="The"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="sky"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="blue")], [nr.Text(kind="text", text="red")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="the"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="sun"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="green")], [nr.Text(kind="text", text="yellow")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )


class SelectThingsAdaptationTestCase(AdaptationTestCase):
    def test_single_sentence(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.InsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="The wording of this exercise is a single sentence.\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red", "blue"]),
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="instructions"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
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
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(paragraphs=[nr.Paragraph(contents=[nr.Text(kind="text", text="instructions")])]),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[nr.Text(kind="text", text="The")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[nr.Text(kind="text", text="wording")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[nr.Text(kind="text", text="of")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[nr.Text(kind="text", text="this")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[nr.Text(kind="text", text="exercise")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[nr.Text(kind="text", text="is")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[nr.Text(kind="text", text="a")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[nr.Text(kind="text", text="single")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[nr.Text(kind="text", text="sentence")]),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_sel_tags(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.InsertOp(insert="abc", attributes={"sel": 1}),
                    d.InsertOp(insert=" ", attributes={}),
                    d.InsertOp(insert="def", attributes={"sel": 2}),
                    d.InsertOp(insert=" ", attributes={}),
                    d.InsertOp(insert="ghi", attributes={"sel": 3}),
                    d.InsertOp(insert=" ", attributes={}),
                    d.InsertOp(insert="jkl", attributes={"sel": 4}),
                    d.InsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="wording\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red", "green", "blue"]),
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.SelectedText(text="abc", color="red"),
                                        r.Whitespace(),
                                        r.SelectedText(text="def", color="green"),
                                        r.Whitespace(),
                                        r.SelectedText(text="ghi", color="blue"),
                                        r.Whitespace(),
                                        r.PlainText(text="jkl"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.SelectableText(text="wording", colors=["red", "green", "blue"], boxed=False),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", highlighted="red", text="abc"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", highlighted="green", text="def"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", highlighted="blue", text="ghi"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="jkl"),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.SelectableInput(
                                            kind="selectableInput", colors=["red", "green", "blue"], contents=[nr.Text(kind="text", text="wording")]
                                        )
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_single_color(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.InsertOp(insert="abc", attributes={"sel": 1}),
                    d.InsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="wording\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red"]),
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.SelectedText(text="abc", color="red"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.SelectableText(text="wording", colors=["red"], boxed=False),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(paragraphs=[nr.Paragraph(contents=[nr.Text(kind="text", highlighted="red", text="abc")])]),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="wording")])]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_multiple_lines_in_instructions(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="instructions\nare\n\non\n\nmultiple\nlines\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="wording\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red"]),
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="instructions"),
                                        r.Whitespace(),
                                        r.PlainText(text="are"),
                                    ]
                                ),
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="on"),
                                    ]
                                ),
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="multiple"),
                                        r.Whitespace(),
                                        r.PlainText(text="lines"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.SelectableText(text="wording", colors=["red"], boxed=False),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[nr.Text(kind="text", text="instructions"), nr.Whitespace(kind="whitespace"), nr.Text(kind="text", text="are")]
                                ),
                                nr.Paragraph(contents=[nr.Text(kind="text", text="on")]),
                                nr.Paragraph(
                                    contents=[nr.Text(kind="text", text="multiple"), nr.Whitespace(kind="whitespace"), nr.Text(kind="text", text="lines")]
                                ),
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="wording")])]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_multiple_lines_in_wording(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="wording is\n\non\n\nmultiple lines\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red"]),
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="instructions"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.SelectableText(text="wording", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="is", colors=["red"], boxed=False),
                                    ]
                                ),
                                r.Paragraph(
                                    tokens=[
                                        r.SelectableText(text="on", colors=["red"], boxed=False),
                                    ]
                                ),
                                r.Paragraph(
                                    tokens=[
                                        r.SelectableText(text="multiple", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="lines", colors=["red"], boxed=False),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(paragraphs=[nr.Paragraph(contents=[nr.Text(kind="text", text="instructions")])]),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="wording")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="is")]),
                                    ]
                                ),
                                nr.Paragraph(contents=[nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="on")])]),
                                nr.Paragraph(
                                    contents=[
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="multiple")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="lines")]),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_unknown_tags(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="{tag|abc}\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="{tag|def}\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red"]),
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="{"),
                                        r.PlainText(text="tag"),
                                        r.PlainText(text="|"),
                                        r.PlainText(text="abc"),
                                        r.PlainText(text="}"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="{"),
                                        r.SelectableText(text="tag", colors=["red"], boxed=False),
                                        r.PlainText(text="|"),
                                        r.SelectableText(text="def", colors=["red"], boxed=False),
                                        r.PlainText(text="}"),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="{"),
                                        nr.Text(kind="text", text="tag"),
                                        nr.Text(kind="text", text="|"),
                                        nr.Text(kind="text", text="abc"),
                                        nr.Text(kind="text", text="}"),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="{"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="tag")]),
                                        nr.Text(kind="text", text="|"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="def")]),
                                        nr.Text(kind="text", text="}"),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_strip_whitespace(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="   abc   \n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="   def   \n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red"]),
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="abc"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.SelectableText(text="def", colors=["red"], boxed=False),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(paragraphs=[nr.Paragraph(contents=[nr.Text(kind="text", text="abc")])]),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(contents=[nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="def")])])
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_example_and_clue(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.InsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="wording\n", attributes={}),
                ],
                example=[
                    d.InsertOp(insert="This is the example.\n", attributes={}),
                ],
                clue=[
                    d.InsertOp(insert="This is the clue.\n", attributes={}),
                ],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red"]),
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="instructions"),
                                    ]
                                ),
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="This"),
                                        r.Whitespace(),
                                        r.PlainText(text="is"),
                                        r.Whitespace(),
                                        r.PlainText(text="the"),
                                        r.Whitespace(),
                                        r.PlainText(text="example"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="This"),
                                        r.Whitespace(),
                                        r.PlainText(text="is"),
                                        r.Whitespace(),
                                        r.PlainText(text="the"),
                                        r.Whitespace(),
                                        r.PlainText(text="clue"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.SelectableText(text="wording", colors=["red"], boxed=False),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(contents=[nr.Text(kind="text", text="instructions")]),
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="This"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="the"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="example"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                ),
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="This"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="the"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="clue"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="wording")])]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_example_and_clue_with_sel_tags(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.InsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="wording\n", attributes={}),
                ],
                example=[
                    d.InsertOp(insert="abc", attributes={"sel": 1}),
                    d.InsertOp(insert=" ", attributes={}),
                    d.InsertOp(insert="def", attributes={"sel": 2}),
                    d.InsertOp(insert="\n", attributes={}),
                ],
                clue=[
                    d.InsertOp(insert="ghi", attributes={"sel": 3}),
                    d.InsertOp(insert=" ", attributes={}),
                    d.InsertOp(insert="jkl", attributes={"sel": 4}),
                    d.InsertOp(insert="\n", attributes={}),
                ],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red", "green", "blue"]),
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="instructions"),
                                    ]
                                ),
                                r.Paragraph(
                                    tokens=[
                                        r.SelectedText(text="abc", color="red"),
                                        r.Whitespace(),
                                        r.SelectedText(text="def", color="green"),
                                    ]
                                ),
                                r.Paragraph(
                                    tokens=[
                                        r.SelectedText(text="ghi", color="blue"),
                                        r.Whitespace(),
                                        r.PlainText(text="jkl"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.SelectableText(text="wording", colors=["red", "green", "blue"], boxed=False),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(contents=[nr.Text(kind="text", text="instructions")]),
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", highlighted="red", text="abc"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", highlighted="green", text="def"),
                                    ]
                                ),
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", highlighted="blue", text="ghi"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="jkl"),
                                    ]
                                ),
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.SelectableInput(
                                            kind="selectableInput", colors=["red", "green", "blue"], contents=[nr.Text(kind="text", text="wording")]
                                        )
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_french_elision_of_articles__without_punctuation(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.InsertOp(insert="Selectionne les articles.\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="La maison est belle. L'école est fermée. L’automobile est verte.\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red"]),
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Selectionne"),
                                        r.Whitespace(),
                                        r.PlainText(text="les"),
                                        r.Whitespace(),
                                        r.PlainText(text="articles"),
                                        r.PlainText(text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.SelectableText(text="La", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="maison", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="est", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="belle", colors=["red"], boxed=False),
                                        r.PlainText(text="."),
                                        r.Whitespace(),
                                        r.SelectableText(text="L'", colors=["red"], boxed=False),
                                        r.SelectableText(text="école", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="est", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="fermée", colors=["red"], boxed=False),
                                        r.PlainText(text="."),
                                        r.Whitespace(),
                                        r.SelectableText(text="L’", colors=["red"], boxed=False),
                                        r.SelectableText(text="automobile", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="est", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="verte", colors=["red"], boxed=False),
                                        r.PlainText(text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Selectionne"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="les"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="articles"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="La")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="maison")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="est")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="belle")]),
                                        nr.Text(kind="text", text="."),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(
                                            kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="L"), nr.Text(kind="text", text="'")]
                                        ),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="école")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="est")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="fermée")]),
                                        nr.Text(kind="text", text="."),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(
                                            kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="L"), nr.Text(kind="text", text="’")]
                                        ),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="automobile")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="est")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="verte")]),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_french_elision_of_articles__punctuation_only(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.InsertOp(insert="Selectionne les articles.\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="La maison est belle. L'école est fermée. L’automobile est verte.\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=False, punctuation=True),
                    items_are_selectable=Selectable(colors=["red"]),
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Selectionne"),
                                        r.Whitespace(),
                                        r.PlainText(text="les"),
                                        r.Whitespace(),
                                        r.PlainText(text="articles"),
                                        r.PlainText(text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="La"),
                                        r.Whitespace(),
                                        r.PlainText(text="maison"),
                                        r.Whitespace(),
                                        r.PlainText(text="est"),
                                        r.Whitespace(),
                                        r.PlainText(text="belle"),
                                        r.SelectableText(text=".", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.PlainText(text="L"),
                                        r.SelectableText(text="'", colors=["red"], boxed=False),
                                        r.PlainText(text="école"),
                                        r.Whitespace(),
                                        r.PlainText(text="est"),
                                        r.Whitespace(),
                                        r.PlainText(text="fermée"),
                                        r.SelectableText(text=".", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.PlainText(text="L"),
                                        r.SelectableText(text="’", colors=["red"], boxed=False),
                                        r.PlainText(text="automobile"),
                                        r.Whitespace(),
                                        r.PlainText(text="est"),
                                        r.Whitespace(),
                                        r.PlainText(text="verte"),
                                        r.SelectableText(text=".", colors=["red"], boxed=False),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Selectionne"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="les"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="articles"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="La"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="maison"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="est"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="belle"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text=".")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="L"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="'")]),
                                        nr.Text(kind="text", text="école"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="est"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="fermée"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text=".")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="L"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="’")]),
                                        nr.Text(kind="text", text="automobile"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="est"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="verte"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text=".")]),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_french_elision_of_articles__with_punctuation(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.InsertOp(insert="Selectionne les articles.\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="La maison est belle. L'école est fermée. L’automobile est verte.\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=True),
                    items_are_selectable=Selectable(colors=["red"]),
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Selectionne"),
                                        r.Whitespace(),
                                        r.PlainText(text="les"),
                                        r.Whitespace(),
                                        r.PlainText(text="articles"),
                                        r.PlainText(text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.SelectableText(text="La", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="maison", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="est", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="belle", colors=["red"], boxed=False),
                                        r.SelectableText(text=".", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="L'", colors=["red"], boxed=False),
                                        r.SelectableText(text="école", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="est", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="fermée", colors=["red"], boxed=False),
                                        r.SelectableText(text=".", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="L’", colors=["red"], boxed=False),
                                        r.SelectableText(text="automobile", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="est", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="verte", colors=["red"], boxed=False),
                                        r.SelectableText(text=".", colors=["red"], boxed=False),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Selectionne"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="les"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="articles"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="La")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="maison")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="est")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="belle")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text=".")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="L")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="'")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="école")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="est")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="fermée")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text=".")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="L")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="’")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="automobile")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="est")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="verte")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text=".")]),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_french_elision_of_articles__without_punctuation__boxed_only(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.InsertOp(insert="Selectionne les articles.\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="La maison est belle. L'école est fermée. L’automobile est verte.\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=None,
                    items_are_boxed=True,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Selectionne"),
                                        r.Whitespace(),
                                        r.PlainText(text="les"),
                                        r.Whitespace(),
                                        r.PlainText(text="articles"),
                                        r.PlainText(text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.BoxedText(text="La"),
                                        r.Whitespace(),
                                        r.BoxedText(text="maison"),
                                        r.Whitespace(),
                                        r.BoxedText(text="est"),
                                        r.Whitespace(),
                                        r.BoxedText(text="belle"),
                                        r.PlainText(text="."),
                                        r.Whitespace(),
                                        r.BoxedText(text="L'"),
                                        r.BoxedText(text="école"),
                                        r.Whitespace(),
                                        r.BoxedText(text="est"),
                                        r.Whitespace(),
                                        r.BoxedText(text="fermée"),
                                        r.PlainText(text="."),
                                        r.Whitespace(),
                                        r.BoxedText(text="L’"),
                                        r.BoxedText(text="automobile"),
                                        r.Whitespace(),
                                        r.BoxedText(text="est"),
                                        r.Whitespace(),
                                        r.BoxedText(text="verte"),
                                        r.PlainText(text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Selectionne"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="les"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="articles"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="La")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="maison")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="est")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="belle")], boxed=True),
                                        nr.Text(kind="text", text="."),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(
                                            kind="passiveSequence", contents=[nr.Text(kind="text", text="L"), nr.Text(kind="text", text="'")], boxed=True
                                        ),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="école")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="est")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="fermée")], boxed=True),
                                        nr.Text(kind="text", text="."),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(
                                            kind="passiveSequence", contents=[nr.Text(kind="text", text="L"), nr.Text(kind="text", text="’")], boxed=True
                                        ),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="automobile")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="est")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="verte")], boxed=True),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_french_elision_of_articles__punctuation_only__boxed_only(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.InsertOp(insert="Selectionne les articles.\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="La maison est belle. L'école est fermée. L’automobile est verte.\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=False, punctuation=True),
                    items_are_selectable=None,
                    items_are_boxed=True,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Selectionne"),
                                        r.Whitespace(),
                                        r.PlainText(text="les"),
                                        r.Whitespace(),
                                        r.PlainText(text="articles"),
                                        r.PlainText(text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="La"),
                                        r.Whitespace(),
                                        r.PlainText(text="maison"),
                                        r.Whitespace(),
                                        r.PlainText(text="est"),
                                        r.Whitespace(),
                                        r.PlainText(text="belle"),
                                        r.BoxedText(text="."),
                                        r.Whitespace(),
                                        r.PlainText(text="L"),
                                        r.BoxedText(text="'"),
                                        r.PlainText(text="école"),
                                        r.Whitespace(),
                                        r.PlainText(text="est"),
                                        r.Whitespace(),
                                        r.PlainText(text="fermée"),
                                        r.BoxedText(text="."),
                                        r.Whitespace(),
                                        r.PlainText(text="L"),
                                        r.BoxedText(text="’"),
                                        r.PlainText(text="automobile"),
                                        r.Whitespace(),
                                        r.PlainText(text="est"),
                                        r.Whitespace(),
                                        r.PlainText(text="verte"),
                                        r.BoxedText(text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Selectionne"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="les"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="articles"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="La"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="maison"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="est"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="belle"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text=".")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="L"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="'")], boxed=True),
                                        nr.Text(kind="text", text="école"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="est"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="fermée"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text=".")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="L"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="’")], boxed=True),
                                        nr.Text(kind="text", text="automobile"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="est"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="verte"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text=".")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_french_elision_of_articles__with_punctuation__boxed_only(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.InsertOp(insert="Selectionne les articles.\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="La maison est belle. L'école est fermée. L’automobile est verte.\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=True),
                    items_are_selectable=None,
                    items_are_boxed=True,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Selectionne"),
                                        r.Whitespace(),
                                        r.PlainText(text="les"),
                                        r.Whitespace(),
                                        r.PlainText(text="articles"),
                                        r.PlainText(text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.BoxedText(text="La"),
                                        r.Whitespace(),
                                        r.BoxedText(text="maison"),
                                        r.Whitespace(),
                                        r.BoxedText(text="est"),
                                        r.Whitespace(),
                                        r.BoxedText(text="belle"),
                                        r.BoxedText(text="."),
                                        r.Whitespace(),
                                        r.BoxedText(text="L'"),
                                        r.BoxedText(text="école"),
                                        r.Whitespace(),
                                        r.BoxedText(text="est"),
                                        r.Whitespace(),
                                        r.BoxedText(text="fermée"),
                                        r.BoxedText(text="."),
                                        r.Whitespace(),
                                        r.BoxedText(text="L’"),
                                        r.BoxedText(text="automobile"),
                                        r.Whitespace(),
                                        r.BoxedText(text="est"),
                                        r.Whitespace(),
                                        r.BoxedText(text="verte"),
                                        r.BoxedText(text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Selectionne"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="les"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="articles"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="La")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="maison")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="est")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="belle")], boxed=True),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text=".")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="L"), nr.Text(kind="text", text="'")], boxed=True),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="école")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="est")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="fermée")], boxed=True),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text=".")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="L"), nr.Text(kind="text", text="’")], boxed=True),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="automobile")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="est")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="verte")], boxed=True),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text=".")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )


class LenientParagraphTestCase(AdaptationTestCase):
    def test_bold_and_italic(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.InsertOp(insert="This is a ", attributes={}),
                    d.InsertOp(insert="strict", attributes={"bold": True}),
                    d.InsertOp(insert=" instructions ", attributes={}),
                    d.InsertOp(insert="paragraph", attributes={"italic": True}),
                    d.InsertOp(insert=".\n\nAnd this is a ", attributes={}),
                    d.InsertOp(insert="lenient", attributes={"bold": True}),
                    d.InsertOp(insert=" instructions ", attributes={}),
                    d.InsertOp(insert="paragraph", attributes={"italic": True}),
                    d.InsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="This is a ", attributes={}),
                    d.InsertOp(insert="strict", attributes={"bold": True}),
                    d.InsertOp(insert=" wording ", attributes={}),
                    d.InsertOp(insert="paragraph", attributes={"italic": True}),
                    d.InsertOp(insert=".\nAnd this is a ", attributes={}),
                    d.InsertOp(insert="lenient", attributes={"bold": True}),
                    d.InsertOp(insert=" wording ", attributes={}),
                    d.InsertOp(insert="paragraph", attributes={"italic": True}),
                    d.InsertOp(insert="\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="This"),
                                        r.Whitespace(),
                                        r.PlainText(text="is"),
                                        r.Whitespace(),
                                        r.PlainText(text="a"),
                                        r.Whitespace(),
                                        r.PassiveFormattedText(type="passiveFormattedText", text="strict", bold=True, italic=False),
                                        r.Whitespace(),
                                        r.PlainText(text="instructions"),
                                        r.Whitespace(),
                                        r.PassiveFormattedText(type="passiveFormattedText", text="paragraph", bold=False, italic=True),
                                        r.PlainText(text="."),
                                    ]
                                ),
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="And"),
                                        r.Whitespace(),
                                        r.PlainText(text="this"),
                                        r.Whitespace(),
                                        r.PlainText(text="is"),
                                        r.Whitespace(),
                                        r.PlainText(text="a"),
                                        r.Whitespace(),
                                        r.PassiveFormattedText(type="passiveFormattedText", text="lenient", bold=True, italic=False),
                                        r.Whitespace(),
                                        r.PlainText(text="instructions"),
                                        r.Whitespace(),
                                        r.PassiveFormattedText(type="passiveFormattedText", text="paragraph", bold=False, italic=True),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="This"),
                                        r.Whitespace(),
                                        r.PlainText(text="is"),
                                        r.Whitespace(),
                                        r.PlainText(text="a"),
                                        r.Whitespace(),
                                        r.PassiveFormattedText(type="passiveFormattedText", text="strict", bold=True, italic=False),
                                        r.Whitespace(),
                                        r.PlainText(text="wording"),
                                        r.Whitespace(),
                                        r.PassiveFormattedText(type="passiveFormattedText", text="paragraph", bold=False, italic=True),
                                        r.PlainText(text="."),
                                    ]
                                ),
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="And"),
                                        r.Whitespace(),
                                        r.PlainText(text="this"),
                                        r.Whitespace(),
                                        r.PlainText(text="is"),
                                        r.Whitespace(),
                                        r.PlainText(text="a"),
                                        r.Whitespace(),
                                        r.PassiveFormattedText(type="passiveFormattedText", text="lenient", bold=True, italic=False),
                                        r.Whitespace(),
                                        r.PlainText(text="wording"),
                                        r.Whitespace(),
                                        r.PassiveFormattedText(type="passiveFormattedText", text="paragraph", bold=False, italic=True),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="This"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="a"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", bold=True, text="strict"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="instructions"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", italic=True, text="paragraph"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                ),
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="And"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="this"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="a"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", bold=True, text="lenient"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="instructions"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", italic=True, text="paragraph"),
                                    ]
                                ),
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="This"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="a"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", bold=True, text="strict"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="wording"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", italic=True, text="paragraph"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                ),
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="And"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="this"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="a"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", bold=True, text="lenient"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="wording"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", italic=True, text="paragraph"),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_select_words_without_punctuation(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.InsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="This is a strict paragraph, with... some punctuation.\n\nAnd this, is a... lenient paragraph\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red"]),
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="instructions"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
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
                                        r.Whitespace(),
                                        r.SelectableText(text="some", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="punctuation", colors=["red"], boxed=False),
                                        r.PlainText(text="."),
                                    ]
                                ),
                                r.Paragraph(
                                    tokens=[
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
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(paragraphs=[nr.Paragraph(contents=[nr.Text(kind="text", text="instructions")])]),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="This")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="is")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="a")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="strict")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="paragraph")]),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="with")]),
                                        nr.Text(kind="text", text="..."),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="some")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="punctuation")]),
                                        nr.Text(kind="text", text="."),
                                    ]
                                ),
                                nr.Paragraph(
                                    contents=[
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="And")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="this")]),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="is")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="a")]),
                                        nr.Text(kind="text", text="..."),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="lenient")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="paragraph")]),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_select_words_with_punctuation(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.InsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="This is a strict paragraph, with... some punctuation.\n\nAnd this, is a... lenient paragraph\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=True),
                    items_are_selectable=Selectable(colors=["red"]),
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="instructions"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
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
                                        r.Whitespace(),
                                        r.SelectableText(text="some", colors=["red"], boxed=False),
                                        r.Whitespace(),
                                        r.SelectableText(text="punctuation", colors=["red"], boxed=False),
                                        r.SelectableText(text=".", colors=["red"], boxed=False),
                                    ]
                                ),
                                r.Paragraph(
                                    tokens=[
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
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(paragraphs=[nr.Paragraph(contents=[nr.Text(kind="text", text="instructions")])]),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="This")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="is")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="a")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="strict")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="paragraph")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text=",")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="with")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="...")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="some")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="punctuation")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text=".")]),
                                    ]
                                ),
                                nr.Paragraph(
                                    contents=[
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="And")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="this")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text=",")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="is")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="a")]),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="...")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="lenient")]),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.SelectableInput(kind="selectableInput", colors=["red"], contents=[nr.Text(kind="text", text="paragraph")]),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_fill_with_free_text(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.InsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="This is a ... strict paragraph. With some punctuation.\n\nAnd this, is a ... lenient paragraph\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text="...",
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="instructions"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
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
                                        r.Whitespace(),
                                        r.PlainText(text="With"),
                                        r.Whitespace(),
                                        r.PlainText(text="some"),
                                        r.Whitespace(),
                                        r.PlainText(text="punctuation"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                                r.Paragraph(
                                    tokens=[
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
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(paragraphs=[nr.Paragraph(contents=[nr.Text(kind="text", text="instructions")])]),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="This"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="a"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.FreeTextInput(kind="freeTextInput"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="strict"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="paragraph"),
                                        nr.Text(kind="text", text="."),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="With"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="some"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="punctuation"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                ),
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="And"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="this"),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="a"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.FreeTextInput(kind="freeTextInput"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="lenient"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="paragraph"),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_multiple_choices(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.InsertOp(insert="Choose ", attributes={}),
                    d.InsertOp(
                        insert="alpha/bravo", attributes={"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": "..."}}
                    ),
                    d.InsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="This is a ... strict paragraph. With some punctuation.\n\nAnd this, is a ... lenient paragraph\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Choose"),
                                        r.Whitespace(),
                                        r.BoxedText(text="alpha"),
                                        r.Whitespace(),
                                        r.PlainText(text="ou"),
                                        r.Whitespace(),
                                        r.BoxedText(text="bravo"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="This"),
                                        r.Whitespace(),
                                        r.PlainText(text="is"),
                                        r.Whitespace(),
                                        r.PlainText(text="a"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["alpha", "bravo"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.PlainText(text="strict"),
                                        r.Whitespace(),
                                        r.PlainText(text="paragraph"),
                                        r.PlainText(text="."),
                                        r.Whitespace(),
                                        r.PlainText(text="With"),
                                        r.Whitespace(),
                                        r.PlainText(text="some"),
                                        r.Whitespace(),
                                        r.PlainText(text="punctuation"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="And"),
                                        r.Whitespace(),
                                        r.PlainText(text="this"),
                                        r.PlainText(text=","),
                                        r.Whitespace(),
                                        r.PlainText(text="is"),
                                        r.Whitespace(),
                                        r.PlainText(text="a"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["alpha", "bravo"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.PlainText(text="lenient"),
                                        r.Whitespace(),
                                        r.PlainText(text="paragraph"),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Choose"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="alpha")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="ou"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="bravo")], boxed=True),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="This"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="a"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="alpha")], [nr.Text(kind="text", text="bravo")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="strict"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="paragraph"),
                                        nr.Text(kind="text", text="."),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="With"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="some"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="punctuation"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                ),
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="And"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="this"),
                                        nr.Text(kind="text", text=","),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="a"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="alpha")], [nr.Text(kind="text", text="bravo")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="lenient"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="paragraph"),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
        )


class MultipleAdaptationEffectsTestCase(AdaptationTestCase):
    def test_fill_with_free_text_and_multiple_choices_in_instructions(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="instructions ", attributes={}),
                    d.InsertOp(
                        insert="short/long", attributes={"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": "@@@"}}
                    ),
                    d.InsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="The wording of this ... is a @@@ sentence.\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text="...",
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="instructions"),
                                        r.Whitespace(),
                                        r.BoxedText(text="short"),
                                        r.Whitespace(),
                                        r.PlainText(text="ou"),
                                        r.Whitespace(),
                                        r.BoxedText(text="long"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
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
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["short", "long"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.PlainText(text="sentence"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="instructions"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="short")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="ou"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="long")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="The"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="wording"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="of"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="this"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.FreeTextInput(kind="freeTextInput"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="is"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="a"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="short")], [nr.Text(kind="text", text="long")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="sentence"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_multiple_choices_in_instructions_and_wording(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.InsertOp(insert="Choose wisely ", attributes={}),
                    d.InsertOp(
                        insert="alpha/bravo", attributes={"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": "@@@"}}
                    ),
                    d.InsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.InsertOp(insert="A ", attributes={}),
                    d.InsertOp(insert="a/b/c", attributes={"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": ""}}),
                    d.InsertOp(insert=" B ", attributes={}),
                    d.InsertOp(insert="d/e", attributes={"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": ""}}),
                    d.InsertOp(insert=" C @@@.\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                wording_paragraphs_per_pagelet=3,
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Choose"),
                                        r.Whitespace(),
                                        r.PlainText(text="wisely"),
                                        r.Whitespace(),
                                        r.BoxedText(text="alpha"),
                                        r.Whitespace(),
                                        r.PlainText(text="ou"),
                                        r.Whitespace(),
                                        r.BoxedText(text="bravo"),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="A"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["a", "b", "c"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.PlainText(text="B"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["d", "e"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.PlainText(text="C"),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["alpha", "bravo"], show_choices_by_default=False),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Choose"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="wisely"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="alpha")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="ou"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="bravo")], boxed=True),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="A"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="a")], [nr.Text(kind="text", text="b")], [nr.Text(kind="text", text="c")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="B"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="d")], [nr.Text(kind="text", text="e")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="C"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="alpha")], [nr.Text(kind="text", text="bravo")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_many_adaptations_in_same_exercise(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[
                    d.InsertOp(insert="Choose wisely ", attributes={}),
                    # Multiple choices in instructions
                    d.InsertOp(
                        insert="alpha/bravo", attributes={"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": "@@@"}}
                    ),
                ],
                wording=[
                    d.InsertOp(insert="Hello @@@ $$$ ....", attributes={}),
                    # Multiple choices in wording
                    d.InsertOp(
                        insert="(charlie|delta)",
                        attributes={"choices2": {"start": "(", "separator1": "|", "separator2": "", "stop": ")", "placeholder": "$$$"}},
                    ),
                    d.InsertOp(insert="\n", attributes={}),
                ],
                example=[d.InsertOp(insert="\n", attributes={})],
                clue=[d.InsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    placeholder_for_fill_with_free_text="...",
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red", "yellow"]),
                    items_are_boxed=True,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.PlainText(text="Choose"),
                                        r.Whitespace(),
                                        r.PlainText(text="wisely"),
                                        r.Whitespace(),
                                        r.BoxedText(text="alpha"),
                                        r.Whitespace(),
                                        r.PlainText(text="ou"),
                                        r.Whitespace(),
                                        r.BoxedText(text="bravo"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    tokens=[
                                        r.SelectableText(text="Hello", colors=["red", "yellow"], boxed=True),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["alpha", "bravo"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.MultipleChoicesInput(show_arrow_before=False, choices=["charlie", "delta"], show_choices_by_default=False),
                                        r.Whitespace(),
                                        r.FreeTextInput(),
                                        r.PlainText(text="."),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
            nr.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    nr.Pagelet(
                        instructions=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.Text(kind="text", text="Choose"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="wisely"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="alpha")], boxed=True),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.Text(kind="text", text="ou"),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.PassiveSequence(kind="passiveSequence", contents=[nr.Text(kind="text", text="bravo")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=nr.Section(
                            paragraphs=[
                                nr.Paragraph(
                                    contents=[
                                        nr.SelectableInput(
                                            kind="selectableInput", colors=["red", "yellow"], boxed=True, contents=[nr.Text(kind="text", text="Hello")]
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="alpha")], [nr.Text(kind="text", text="bravo")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[nr.Text(kind="text", text="charlie")], [nr.Text(kind="text", text="delta")]],
                                            show_choices_by_default=False,
                                        ),
                                        nr.Whitespace(kind="whitespace"),
                                        nr.FreeTextInput(kind="freeTextInput"),
                                        nr.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )
