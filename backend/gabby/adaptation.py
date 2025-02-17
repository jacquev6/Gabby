from __future__ import annotations

from typing import Iterable
import copy
import itertools
import json
import re
import traceback
import unittest

import mydantic

from . import deltas
from . import deltas as d
from . import exercises
from . import exercises as e
from . import renderable
from . import renderable as r
from .api_models import Adaptation, TokensItems, Selectable, PredefinedMcq


def adapt(exercise: exercises.Exercise) -> renderable.Exercise | None:
    return _Adapter(exercise).adapted


class McqDefinition(mydantic.PydanticBase):
    start: str | None
    separator1: str | None
    separator2: str | None
    stop: str | None
    placeholder: str | None = None
    mcq_field_uid: str | None = None
    text: str


class _Adapter:
    paragraph_separator = object()

    def __init__(self, exercise: exercises.Exercise):
        self.wording_paragraphs_per_pagelet = exercise.adaptation.wording_paragraphs_per_pagelet
        self.single_item_per_paragraph = exercise.adaptation.single_item_per_paragraph
        self.show_mcq_choices_by_default = exercise.adaptation.show_mcq_choices_by_default
        self.show_arrow_before_mcq_fields = exercise.adaptation.show_arrow_before_mcq_fields
        self.global_placeholders: list[tuple[str, renderable.AnyRenderable]] = []
        self.letters_are_items = False
        self.words_are_items = False
        self.punctuation_is_items = False
        self.sentences_are_items = False
        self.manual_items_are_items = False
        self.items_separator = None
        self.items_are_selectable = False
        self.items_are_boxed = False
        self.colors_for_selectable_items = []
        self.items_have_mcq_beside = exercise.adaptation.items_have_mcq_beside
        self.mcq_beside_items = None
        self.items_have_mcq_below = exercise.adaptation.items_have_mcq_below
        self.mcq_below_items = None
        self.items_have_gender_mcq_beside = exercise.adaptation.items_have_predefined_mcq.grammatical_gender
        self.items_have_number_mcq_beside = exercise.adaptation.items_have_predefined_mcq.grammatical_number
        self.items_are_repeated_with_mcq = exercise.adaptation.items_are_repeated_with_mcq
        if self.items_are_repeated_with_mcq:
            assert exercise.adaptation.items is None
            self.sentences_are_items = True
        self.mcq_for_placeholders = None
        self.mcqs_by_uid = {}

        if exercise.adaptation.placeholder_for_fill_with_free_text is not None:
            self.global_placeholders.append((exercise.adaptation.placeholder_for_fill_with_free_text, renderable.FreeTextInput(kind="freeTextInput")))

        if exercise.adaptation.items is not None:
            self.letters_are_items = exercise.adaptation.items.kind == "characters" and exercise.adaptation.items.letters
            self.words_are_items = exercise.adaptation.items.kind == "tokens" and exercise.adaptation.items.words
            self.punctuation_is_items = exercise.adaptation.items.kind == "tokens" and exercise.adaptation.items.punctuation
            self.sentences_are_items = exercise.adaptation.items.kind == "sentences"
            self.manual_items_are_items = exercise.adaptation.items.kind == "manual"
            self.items_separator = re.escape(exercise.adaptation.items.separator) if exercise.adaptation.items.kind == "separated" else None
            self.items_are_boxed = exercise.adaptation.items_are_boxed
            if exercise.adaptation.items_are_selectable is not None:
                self.items_are_selectable = True
                self.colors_for_selectable_items = exercise.adaptation.items_are_selectable.colors

        for mcq_definition in self.gather_choices(exercise.instructions):
            mcq = renderable.MultipleChoicesInput(
                kind="multipleChoicesInput",
                show_arrow_before=self.show_arrow_before_mcq_fields,
                choices=self.separate_choices(mcq_definition),
                show_choices_by_default=self.show_mcq_choices_by_default,
            )

            if mcq_definition.placeholder == "":
                if mcq_definition.mcq_field_uid is None:
                    if self.items_have_mcq_beside:
                        self.mcq_beside_items = mcq
                    elif self.items_have_mcq_below:
                        self.mcq_below_items = mcq
                    elif self.items_are_repeated_with_mcq:
                        self.mcq_for_placeholders = mcq
                else:
                    self.mcqs_by_uid[mcq_definition.mcq_field_uid] = mcq
            else:
                self.global_placeholders.append((mcq_definition.placeholder, mcq))

        instructions = self.postprocess_section(
            renderable.Section(
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
            renderable.Pagelet(
                instructions=instructions,
                wording=self.postprocess_section(renderable.Section(paragraphs=wording_paragraphs)),
            )
            for wording_paragraphs in self.adapt_wording(exercise.wording, self.wording_paragraphs_per_pagelet)
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
                yield renderable.Paragraph(contents=list(self.adapt_instructions_sentence(sentence_deltas)))

    def adapt_instructions_sentence(self, sentence_deltas: deltas.Deltas):
        for delta in sentence_deltas:
            if delta.attributes == deltas.TextInsertOpAttributes():
                for text in re.split(r"(\.\.\.|\s+|\W)", delta.insert):
                    if text != "":
                        if text.strip() == "":
                            yield renderable.Whitespace(kind="whitespace")
                        else:
                            yield renderable.Text(kind="text", text=text)

            elif delta.attributes.sel is not None:
                assert delta.attributes == deltas.TextInsertOpAttributes(sel=delta.attributes.sel)

                if len(self.colors_for_selectable_items) > delta.attributes.sel - 1:
                    yield renderable.Text(kind="text", text=delta.insert, highlighted=self.colors_for_selectable_items[delta.attributes.sel - 1])
                else:
                    yield renderable.Text(kind="text", text=delta.insert)

            elif delta.attributes.choices2 is not None:
                assert delta.attributes == deltas.TextInsertOpAttributes(choices2=delta.attributes.choices2)

                mcq_definition = McqDefinition(
                    start=delta.attributes.choices2.start or None,
                    separator1=delta.attributes.choices2.separator1 or None,
                    separator2=delta.attributes.choices2.separator2 or None,
                    stop=delta.attributes.choices2.stop or None,
                    placeholder=delta.attributes.choices2.placeholder or None,
                    text=delta.insert,
                )

                choices = self.separate_choices(mcq_definition)
                # Always format choices the same way in instructions: https://github.com/jacquev6/Gabby/issues/74
                yield renderable.PassiveSequence(kind="passiveSequence", contents=choices[0], boxed=True)
                for choice in choices[1:-1]:
                    yield renderable.Text(kind="text", text=",")
                    yield renderable.Whitespace(kind="whitespace")
                    yield renderable.PassiveSequence(kind="passiveSequence", contents=choice, boxed=True)
                if len(choices) > 1:
                    yield renderable.Whitespace(kind="whitespace")
                    yield renderable.Text(kind="text", text="ou")  # @todo Fix this if we ever support exercises in English
                    yield renderable.Whitespace(kind="whitespace")
                    yield renderable.PassiveSequence(kind="passiveSequence", contents=choices[-1], boxed=True)

            elif delta.attributes.bold or delta.attributes.italic:
                assert delta.attributes == deltas.TextInsertOpAttributes(bold=delta.attributes.bold, italic=delta.attributes.italic)

                yield renderable.Text(
                    kind="text",
                    text=delta.insert,
                    bold=delta.attributes.bold,
                    italic=delta.attributes.italic,
                )

            else:
                assert False, f"Unknown attributes: {delta!r}"

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
            if delta.kind == "text" and delta.attributes == deltas.TextInsertOpAttributes():
                for index, (placeholder, _token) in enumerate(self.global_placeholders):
                    delta.insert = delta.insert.replace(placeholder, f"ph{index}hp")

        paragraphs = []

        for paragraph_deltas in self.split_deltas(pagelet_deltas, r"\s*\n\s*"):
            for is_separator, contents in itertools.groupby(self.adapt_wording_paragraph(paragraph_deltas), lambda c: c is self.paragraph_separator):
                if not is_separator:
                    paragraphs.append(renderable.Paragraph(contents=list(contents)))

        return paragraphs

    def adapt_wording_paragraph(self, paragraph_deltas: deltas.Deltas):
        sentence_specific_placeholders = []

        for mcq_definition in self.gather_choices(paragraph_deltas):
            if mcq_definition.placeholder != "":
                sentence_specific_placeholders.append(
                    (
                        mcq_definition.placeholder,
                        renderable.MultipleChoicesInput(
                            kind="multipleChoicesInput",
                            show_arrow_before=self.show_arrow_before_mcq_fields,
                            choices=self.separate_choices(mcq_definition),
                            show_choices_by_default=self.show_mcq_choices_by_default,
                        ),
                    ),
                )

        for delta in paragraph_deltas:
            if delta.kind == "text" and delta.attributes == deltas.TextInsertOpAttributes():
                for index, (mcq_definition.placeholder, _token) in enumerate(sentence_specific_placeholders):
                    delta.insert = delta.insert.replace(mcq_definition.placeholder, f"ph{len(self.global_placeholders) + index}hp")

        sentence_placeholders = list(itertools.chain(self.global_placeholders, sentence_specific_placeholders))

        list_header_deltas, paragraph_deltas = self.split_list_header(paragraph_deltas)

        if len(list_header_deltas) > 0:
            for delta in list_header_deltas:
                for text in re.split(r"(\.\.\.|\s+|\W|ph\d+hp)", delta.insert):
                    if text != "":
                        yield renderable.Text(kind="text", text=text)
            yield renderable.Whitespace(kind="whitespace")

        if self.sentences_are_items:
            is_first_sentence = True
            for sentence_deltas in self.split_deltas_into_sentences(paragraph_deltas):
                if not is_first_sentence:
                    yield renderable.Whitespace(kind="whitespace")
                is_first_sentence = False
                contents = list(
                    self.adapt_wording_sentence(
                        sentence_deltas,
                        sentence_placeholders,
                        make_mcq_placeholder_replacement=lambda delta: renderable.Text(kind="text", text=delta.insert, highlighted="#ffff00"),
                    )
                )
                while contents[0].kind == "whitespace":
                    contents.pop(0)
                if self.items_are_repeated_with_mcq:
                    contents2 = list(
                        self.adapt_wording_sentence(
                            sentence_deltas, sentence_placeholders, make_mcq_placeholder_replacement=lambda _: self.mcq_for_placeholders
                        )
                    )
                    while contents2[0].kind == "whitespace":
                        contents2.pop(0)
                    yield renderable.AnySequence(
                        kind="sequence",
                        contents=[renderable.AnySequence(kind="sequence", contents=contents), renderable.AnySequence(kind="sequence", contents=contents2)],
                        vertical=True,
                    )
                else:
                    yield from self.decorate_item(contents)
        elif self.items_separator is not None:
            is_first_item = True
            for item_deltas in self.split_deltas(paragraph_deltas, self.items_separator):
                if not is_first_item:
                    yield renderable.Whitespace(kind="whitespace")
                is_first_item = False
                contents = list(self.adapt_wording_sentence(item_deltas, sentence_placeholders))
                while len(contents) > 0 and contents[0].kind == "whitespace":
                    contents.pop(0)
                while len(contents) > 0 and contents[-1].kind == "whitespace":
                    contents.pop(-1)
                yield from self.decorate_item(contents)
        else:
            yield from self.adapt_wording_sentence(paragraph_deltas, sentence_placeholders)

    def adapt_wording_sentence(
        self,
        sentence_deltas: deltas.Deltas,
        sentence_placeholders: list[tuple[str, renderable.SentenceToken]],
        make_mcq_placeholder_replacement: renderable.AnyRenderable | None = None,
    ):
        for delta in sentence_deltas:
            if delta.kind == "text":
                if make_mcq_placeholder_replacement is None:
                    delta.attributes.mcq_placeholder = False

                if delta.attributes == deltas.TextInsertOpAttributes():
                    for i, text in enumerate(re.split(r"(\.\.\.|\s+|\W|ph\d+hp)", delta.insert)):
                        if text != "":
                            if i % 2 == 1:
                                # Separator: punctuation, spacing, placeholders
                                if text.strip() == "":
                                    yield renderable.Whitespace(kind="whitespace")
                                elif text.startswith("ph") and text.endswith("hp"):
                                    index = int(text[2:-2])
                                    yield sentence_placeholders[index][1]
                                else:
                                    item = renderable.Text(kind="text", text=text)
                                    if self.punctuation_is_items:
                                        yield from self.decorate_item([item])
                                    else:
                                        yield item
                            else:
                                # Separated: words
                                if self.letters_are_items:
                                    for letter in text:
                                        yield from self.decorate_item([renderable.Text(kind="text", text=letter)])
                                elif self.words_are_items:
                                    yield from self.decorate_item([renderable.Text(kind="text", text=text)])
                                else:
                                    yield renderable.Text(kind="text", text=text)

                elif delta.attributes.mcq_placeholder:
                    assert delta.attributes == deltas.TextInsertOpAttributes(mcq_placeholder=delta.attributes.mcq_placeholder)

                    yield make_mcq_placeholder_replacement(delta)

                elif delta.attributes.manual_item:
                    assert delta.attributes == deltas.TextInsertOpAttributes(manual_item=delta.attributes.manual_item)

                    for text in re.split(r"(\.\.\.|\s+|\W)", delta.insert):
                        if text != "":
                            if text.strip() == "":
                                yield renderable.Whitespace(kind="whitespace")
                            else:
                                item = renderable.Text(kind="text", text=text)
                                if self.manual_items_are_items:
                                    yield from self.decorate_item([item])
                                else:
                                    yield item

                elif delta.attributes.bold or delta.attributes.italic:
                    assert delta.attributes == deltas.TextInsertOpAttributes(bold=delta.attributes.bold, italic=delta.attributes.italic)

                    yield renderable.Text(
                        kind="text",
                        text=delta.insert,
                        bold=delta.attributes.bold,
                        italic=delta.attributes.italic,
                    )

                elif delta.attributes.choices2 is not None:
                    assert delta.attributes == deltas.TextInsertOpAttributes(choices2=delta.attributes.choices2)

                    choices_settings = delta.attributes.choices2
                    placeholder = choices_settings.placeholder or None
                    if placeholder is None:
                        mcq_definition = McqDefinition(
                            start=choices_settings.start or None,
                            separator1=choices_settings.separator1 or None,
                            separator2=choices_settings.separator2 or None,
                            stop=choices_settings.stop or None,
                            text=delta.insert,
                        )
                        yield renderable.MultipleChoicesInput(
                            kind="multipleChoicesInput",
                            show_arrow_before=self.show_arrow_before_mcq_fields,
                            choices=self.separate_choices(mcq_definition),
                            show_choices_by_default=self.show_mcq_choices_by_default,
                        )

                else:
                    assert False, f"Unknown attributes: {delta!r}"
            else:
                assert delta.insert.kind == "mcq-field"
                yield self.mcqs_by_uid.get(delta.insert.mcq_field, renderable.MultipleChoicesInput(kind="multipleChoicesInput", choices=[]))

    def decorate_item(self, contents):
        if self.items_are_selectable:
            contents = [
                renderable.SelectableInput(
                    kind="selectableInput",
                    contents=contents,
                    colors=self.colors_for_selectable_items,
                    boxed=self.items_are_boxed,
                )
            ]
        elif self.items_are_boxed:
            contents = [
                renderable.PassiveSequence(
                    kind="passiveSequence",
                    contents=contents,
                    boxed=True,
                )
            ]
        else:
            pass
        if self.mcq_below_items is None:
            yield from contents
            if self.mcq_beside_items is not None:
                yield renderable.Whitespace(kind="whitespace")
                yield self.mcq_beside_items
            if self.items_have_gender_mcq_beside:
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
                    show_arrow_before=not self.items_have_gender_mcq_beside,
                    choices=[
                        # @todo Support exercises in English?
                        [renderable.Text(kind="text", text="singulier")],
                        [renderable.Text(kind="text", text="pluriel")],
                    ],
                    show_choices_by_default=self.show_mcq_choices_by_default,
                )
        else:
            yield renderable.AnySequence(
                kind="sequence",
                contents=[contents[0] if len(contents) == 1 else renderable.AnySequence(kind="sequence", contents=contents), self.mcq_below_items],
                vertical=True,
            )
        if self.single_item_per_paragraph:
            yield self.paragraph_separator

    def split_deltas(self, section_deltas: deltas.Deltas, separator_pattern: str) -> Iterable[deltas.Deltas]:
        section_deltas = copy.deepcopy(section_deltas)
        assert len(section_deltas) > 0
        if section_deltas[0].kind == "text":
            section_deltas[0].insert = section_deltas[0].insert.lstrip()
        if section_deltas[-1].kind == "text":
            section_deltas[-1].insert = section_deltas[-1].insert.rstrip()

        current_paragraph = []
        for delta in section_deltas:
            if delta.kind == "text":
                if delta.attributes.choices2 is not None:
                    current_paragraph.append(delta)
                else:
                    for i, paragraph_part in enumerate(re.split(separator_pattern, delta.insert)):
                        if i > 0:
                            yield current_paragraph
                            current_paragraph = []
                        if paragraph_part != "":
                            current_paragraph.append(d.TextInsertOp(insert=paragraph_part, attributes=delta.attributes))
            else:
                current_paragraph.append(delta)
        yield current_paragraph

    def split_deltas_into_sentences(self, paragraph_deltas: deltas.Deltas) -> Iterable[deltas.Deltas]:
        current_sentence = []
        for delta in paragraph_deltas:
            if delta.attributes.choices2 is not None:
                current_sentence.append(delta)
            else:
                for i, sentence_part in enumerate(re.split(r"(\.\.\.|[.!?…])", delta.insert)):
                    if sentence_part != "":
                        if i % 2 == 0 and i > 1:
                            yield current_sentence
                            current_sentence = []
                        current_sentence.append(d.TextInsertOp(insert=sentence_part, attributes=delta.attributes))
        yield current_sentence

    def split_list_header(self, paragraph_deltas: deltas.Deltas) -> tuple[deltas.Deltas, deltas.Deltas]:
        if len(paragraph_deltas) == 0 or paragraph_deltas[0].kind != "text":
            return ([], paragraph_deltas)
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
                    deltas.TextInsertOp(
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
                    deltas.TextInsertOp(
                        insert=paragraph_deltas[0].insert[:2],
                        attributes=paragraph_deltas[0].attributes,
                    )
                )
                paragraph_deltas[0].insert = paragraph_deltas[0].insert[2:].lstrip()
            elif len(paragraph_deltas[0].insert) > 0 and paragraph_deltas[0].insert[0] in "◆■":
                # "◆", "■", etc.
                list_header_deltas.append(
                    deltas.TextInsertOp(
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

    def postprocess_section(self, section: renderable.Section) -> renderable.Section:
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

    def gather_choices(self, deltas_):
        for delta in deltas_:
            if delta.kind == "text" and delta.attributes.choices2 is not None:
                choices_settings = delta.attributes.choices2
                yield McqDefinition(
                    start=choices_settings.start or None,
                    separator1=choices_settings.separator1 or None,
                    separator2=choices_settings.separator2 or None,
                    stop=choices_settings.stop or None,
                    placeholder=choices_settings.placeholder,
                    mcq_field_uid=choices_settings.mcqFieldUid,
                    text=delta.insert,
                )

    def separate_choices(self, definition: McqDefinition):
        text = definition.text.strip()
        if definition.start is not None and definition.stop is not None and text.startswith(definition.start) and text.endswith(definition.stop):
            text = text[len(definition.start) : -len(definition.stop)]
        if definition.separator1 is None:
            choices = [text]
        else:
            choices = text.split(definition.separator1)
        if definition.separator2 is not None:
            choices[-1:] = choices[-1].split(definition.separator2)
        return list([renderable.Text(kind="text", text=text)] for text in filter(lambda c: c != "", [choice.strip() for choice in choices]))


class AdaptationTestCase(unittest.TestCase):
    maxDiff = None
    generate_frontend_tests = True

    @classmethod
    def setUpClass(cls):
        cls.tests_to_generate = []
        return super().setUpClass()

    @classmethod
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
            with open(f"../frontend/src/adapted/components/TricolorSection.{cls.__name__}.generated.cy.js", "w") as f:
                for line in generate():
                    f.write(line)
                    f.write("\n")

        return super().tearDownClass()

    def do_test(self, exercise, expected_adapted):
        self.tests_to_generate.append((self.id(), expected_adapted))

        actual_adapted = exercise.make_adapted()
        if actual_adapted != expected_adapted:
            calling_frame = traceback.extract_stack()[-2]
            print(
                f"actual_adapted at {calling_frame.filename}:{calling_frame.lineno}:",
                repr([actual_adapted])[1:-1]
                .replace("bold=False, ", "")
                .replace("bold=False,", "")
                .replace("bold=False", "")
                .replace("italic=False, ", "")
                .replace("italic=False,", "")
                .replace("italic=False", "")
                .replace("highlighted=None, ", "")
                .replace("highlighted=None,", "")
                .replace("highlighted=None", "")
                .replace("boxed=False, ", "")
                .replace("boxed=False,", "")
                .replace("boxed=False", "")
                .replace("show_arrow_before=False, ", "")
                .replace("show_arrow_before=False,", "")
                .replace("show_arrow_before=False", "")
                .replace("show_choices_by_default=False, ", "")
                .replace("show_choices_by_default=False,", "")
                .replace("show_choices_by_default=False", "")
                .replace("vertical=False, ", "")
                .replace("vertical=False,", "")
                .replace("vertical=False", "")
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
                .replace("AnySequence(", "r.AnySequence("),
            )
        self.assertEqual(actual_adapted, expected_adapted)


class WordingPaginationTestCase(AdaptationTestCase):
    def test_empty(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="\n", attributes={})],
                wording=[d.TextInsertOp(insert="\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(number="number", textbook_page=None, pagelets=[r.Pagelet(instructions=r.Section(paragraphs=[]), wording=r.Section(paragraphs=[]))]),
        )

    def test_single_paragraph(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="\n", attributes={})],
                wording=[d.TextInsertOp(insert="wording\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[]), wording=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="wording")])])
                    )
                ],
            ),
        )

    def test_full_pagelet(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="\n", attributes={})],
                wording=[d.TextInsertOp(insert="wording 1\nwording 2\nwording 3\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="1")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="2")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="3")]),
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
                instructions=[d.TextInsertOp(insert="instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="wording 1\nwording 2\nwording 3\n", attributes={})],
                example=[d.TextInsertOp(insert="example\n", attributes={})],
                clue=[d.TextInsertOp(insert="clue\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=2,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                r.Paragraph(contents=[r.Text(kind="text", text="instructions")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="example")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="clue")]),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="1")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="2")]),
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="instructions")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="example")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="clue")]),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="3")])
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
                instructions=[d.TextInsertOp(insert="instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="wording 1\nwording 2\nwording 3\nwording 4\nwording 5\nwording 6\n", attributes={})],
                example=[d.TextInsertOp(insert="example\n", attributes={})],
                clue=[d.TextInsertOp(insert="clue\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=None,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                r.Paragraph(contents=[r.Text(kind="text", text="instructions")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="example")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="clue")]),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="1")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="2")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="3")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="4")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="5")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="6")]),
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
                instructions=[d.TextInsertOp(insert="instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="wording 1\n\nwording 2\n\n\nwording 3\n\nwording 4\n\nwording 5\n\nwording 6\n\n", attributes={})],
                example=[d.TextInsertOp(insert="example\n", attributes={})],
                clue=[d.TextInsertOp(insert="clue\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=None,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                r.Paragraph(contents=[r.Text(kind="text", text="instructions")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="example")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="clue")]),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="1")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="2")]),
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="instructions")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="example")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="clue")]),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="3")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="4")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="5")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="6")]),
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
                instructions=[d.TextInsertOp(insert="instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="wording 1\n\nwording 2\n\n\nwording 3\n\nwording 4\n\nwording 5\n\nwording 6\n\n", attributes={})],
                example=[d.TextInsertOp(insert="example\n", attributes={})],
                clue=[d.TextInsertOp(insert="clue\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                r.Paragraph(contents=[r.Text(kind="text", text="instructions")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="example")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="clue")]),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="1")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="2")]),
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="instructions")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="example")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="clue")]),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="3")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="4")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="5")]),
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="instructions")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="example")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="clue")]),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="wording"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="6")])
                            ]
                        ),
                    ),
                ],
            ),
        )

    def test_one_letter_per_paragraph(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="a b c d\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=True,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "characters", "letters": True},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="a")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="b")]),
                                r.Paragraph(contents=[r.Text(kind="text", text="c")]),
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="d")]),
                            ]
                        ),
                    ),
                ],
            ),
        )

    def test_one_word_per_paragraph(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="a. worda wordb\nb. wordc wordd\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=True,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": False},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="a"),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="worda"),
                                    ]
                                ),
                                r.Paragraph(contents=[r.Text(kind="text", text="wordb")]),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="b"),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wordc"),
                                    ]
                                ),
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.Text(kind="text", text="wordd")]),
                            ]
                        ),
                    ),
                ],
            ),
        )

    def test_one_punctuation_per_paragraph(self):
        # This is probably not an actual use case. But this behavior is consistent with the others, so we capture it with a test.
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="a. word, word\nb. word! word\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=True,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": False, "punctuation": True},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="a"),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="word"),
                                        r.Text(kind="text", text=","),
                                    ]
                                ),
                                r.Paragraph(contents=[r.Text(kind="text", text="word")]),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="b"),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="word"),
                                        r.Text(kind="text", text="!"),
                                    ]
                                ),
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="instructions")])]),
                        wording=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="word")])]),
                    ),
                ],
            ),
        )

    def test_one_sentence_per_paragraph(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=None,
                instructions=[d.TextInsertOp(insert="instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="Il fait beau. Il fait chaud. Il ne pleut pas.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=2,
                    single_item_per_paragraph=True,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "sentences"},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="Il"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="fait"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="beau"),
                                        r.Text(kind="text", text="."),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="Il"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="fait"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="chaud"),
                                        r.Text(kind="text", text="."),
                                    ]
                                ),
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="Il"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ne"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="pleut"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="pas"),
                                        r.Text(kind="text", text="."),
                                    ]
                                ),
                            ]
                        ),
                    ),
                ],
            ),
        )

    def test_one_manual_item_per_paragraph(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[
                    d.TextInsertOp(insert="This ", attributes={}),
                    d.TextInsertOp(insert="is", attributes={"manual-item": True}),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(insert="the", attributes={"manual-item": True}),
                    d.TextInsertOp(insert=" wording.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=None,
                    single_item_per_paragraph=True,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "manual"},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                    ],
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="the"),
                                    ],
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="wording"),
                                        r.Text(kind="text", text="."),
                                    ],
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        )


class WordToMcqAdaptationTestCase(AdaptationTestCase):
    def test_words_in_sentences(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha, bravo ou charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "ou", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="a. Firsta ", attributes={}),
                    d.TextInsertOp(insert="firstb", attributes={"mcq-placeholder": True}),
                    d.TextInsertOp(insert=" firstc\nb. ", attributes={}),
                    d.TextInsertOp(insert="Seconda", attributes={"mcq-placeholder": True}),
                    d.TextInsertOp(insert=" secondb secondc\nc. Thirda thirdb ", attributes={}),
                    d.TextInsertOp(insert="thirdc", attributes={"mcq-placeholder": True}),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=None,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,  # {"kind": "sentences"} is implied by items_are_repeated_with_mcq (for now?)
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=True,
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
                                    contents=[
                                        r.Text(kind="text", text="Instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="a"),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        r.Text(kind="text", text="Firsta"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="firstb", highlighted="#ffff00"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="firstc"),
                                                    ],
                                                ),
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        r.Text(kind="text", text="Firsta"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.MultipleChoicesInput(
                                                            kind="multipleChoicesInput",
                                                            choices=[
                                                                [r.Text(kind="text", text="alpha")],
                                                                [r.Text(kind="text", text="bravo")],
                                                                [r.Text(kind="text", text="charlie")],
                                                            ],
                                                        ),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="firstc"),
                                                    ],
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="b"),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        r.Text(kind="text", text="Seconda", highlighted="#ffff00"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="secondb"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="secondc"),
                                                    ],
                                                ),
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        r.MultipleChoicesInput(
                                                            kind="multipleChoicesInput",
                                                            choices=[
                                                                [r.Text(kind="text", text="alpha")],
                                                                [r.Text(kind="text", text="bravo")],
                                                                [r.Text(kind="text", text="charlie")],
                                                            ],
                                                        ),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="secondb"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="secondc"),
                                                    ],
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="c"),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        r.Text(kind="text", text="Thirda"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="thirdb"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="thirdc", highlighted="#ffff00"),
                                                    ],
                                                ),
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        r.Text(kind="text", text="Thirda"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="thirdb"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.MultipleChoicesInput(
                                                            kind="multipleChoicesInput",
                                                            choices=[
                                                                [r.Text(kind="text", text="alpha")],
                                                                [r.Text(kind="text", text="bravo")],
                                                                [r.Text(kind="text", text="charlie")],
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
        )


class ManualMcqFieldsAdaptationTestCase(AdaptationTestCase):
    def test_simplest(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(
                        insert="alpha, bravo ou charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "ou", "stop": "", "placeholder": "", "mcqFieldUid": "f34d6"}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.EmbedInsertOp(insert={"mcq-field": "f34d6"}),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=None,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                        )
                                    ],
                                ),
                            ]
                        ),
                    )
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
                    d.TextInsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="The wording of this ... is a ... sentence.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="fill-with-free-text",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text="...",
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="The"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wording"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="of"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="this"),
                                        r.Whitespace(kind="whitespace"),
                                        r.FreeTextInput(kind="freeTextInput"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="a"),
                                        r.Whitespace(kind="whitespace"),
                                        r.FreeTextInput(kind="freeTextInput"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="sentence"),
                                        r.Text(kind="text", text="."),
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
                    d.TextInsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="@ a @\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="fill-with-free-text",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text="@",
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.FreeTextInput(kind="freeTextInput"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="a"),
                                        r.Whitespace(kind="whitespace"),
                                        r.FreeTextInput(kind="freeTextInput"),
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
                    d.TextInsertOp(insert="instructions\nare\n\non\n\nmultiple\nlines\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="wording\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="fill-with-free-text",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text="...",
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[r.Text(kind="text", text="instructions"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="are")]
                                ),
                                r.Paragraph(contents=[r.Text(kind="text", text="on")]),
                                r.Paragraph(
                                    contents=[r.Text(kind="text", text="multiple"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="lines")]
                                ),
                            ]
                        ),
                        wording=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="wording")])]),
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
                    d.TextInsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="foo toto : ...\n\nbar : ...\n\nbaz : ...\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="fill-with-free-text",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text="...",
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="foo"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="toto"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text=":"),
                                        r.Whitespace(kind="whitespace"),
                                        r.FreeTextInput(kind="freeTextInput"),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="bar"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text=":"),
                                        r.Whitespace(kind="whitespace"),
                                        r.FreeTextInput(kind="freeTextInput"),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="baz"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text=":"),
                                        r.Whitespace(kind="whitespace"),
                                        r.FreeTextInput(kind="freeTextInput"),
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
                    d.TextInsertOp(insert="{tag|abc}\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="{tag|def}\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="fill-with-free-text",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text="...",
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="{"),
                                        r.Text(kind="text", text="tag"),
                                        r.Text(kind="text", text="|"),
                                        r.Text(kind="text", text="abc"),
                                        r.Text(kind="text", text="}"),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="{"),
                                        r.Text(kind="text", text="tag"),
                                        r.Text(kind="text", text="|"),
                                        r.Text(kind="text", text="def"),
                                        r.Text(kind="text", text="}"),
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
                    d.TextInsertOp(insert="   abc   \n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="   def   \n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="fill-with-free-text",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text="...",
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="abc")])]),
                        wording=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="def")])]),
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
                adaptation=Adaptation(
                    kind="fill-with-free-text",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text="@",
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                r.Paragraph(contents=[r.Text(kind="text", text="instructions")]),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="@"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="the"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="example"),
                                        r.Text(kind="text", text="."),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="@"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="the"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="clue"),
                                        r.Text(kind="text", text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.FreeTextInput(kind="freeTextInput"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="the"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wording"),
                                        r.Text(kind="text", text="."),
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
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "characters", "letters": True},
                    items_are_selectable={"colors": ["red"]},
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="T")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="h")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="i")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="s")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="i")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="s")]),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="t")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="h")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="e")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="w")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="o")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="r")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="d")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="i")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="n")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="g")]),
                                        r.Text(kind="text", text="."),
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
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": False},
                    items_are_selectable={"colors": ["red", "blue"]},
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text="This")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text="is")]),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text="the")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text="wording")]),
                                        r.Text(kind="text", text="."),
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
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": True},
                    items_are_selectable={"colors": ["green", "yellow", "orange"]},
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["green", "yellow", "orange"], contents=[r.Text(kind="text", text="This")]
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["green", "yellow", "orange"], contents=[r.Text(kind="text", text="is")]
                                        ),
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["green", "yellow", "orange"], contents=[r.Text(kind="text", text=",")]
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["green", "yellow", "orange"], contents=[r.Text(kind="text", text="the")]
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["green", "yellow", "orange"], contents=[r.Text(kind="text", text="wording")]
                                        ),
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["green", "yellow", "orange"], contents=[r.Text(kind="text", text=".")]
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
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": False, "punctuation": True},
                    items_are_selectable={"colors": ["green", "yellow", "orange"]},
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["green", "yellow", "orange"], contents=[r.Text(kind="text", text=",")]
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="the"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wording"),
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["green", "yellow", "orange"], contents=[r.Text(kind="text", text=".")]
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
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": False},
                    items_are_selectable={"colors": ["red", "blue"]},
                    items_are_boxed=True,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["red", "blue"], boxed=True, contents=[r.Text(kind="text", text="This")]
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["red", "blue"], boxed=True, contents=[r.Text(kind="text", text="is")]
                                        ),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["red", "blue"], boxed=True, contents=[r.Text(kind="text", text="the")]
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["red", "blue"], boxed=True, contents=[r.Text(kind="text", text="wording")]
                                        ),
                                        r.Text(kind="text", text="."),
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
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="a. First list element.\nb. Second element, still in list.\nc. Third element. The last one!", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=2,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": True},
                    items_are_selectable={"colors": ["red"]},
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="a"),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="First")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="list")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="element")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=".")]),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="b"),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="Second")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="element")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=",")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="still")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="in")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="list")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=".")]),
                                    ]
                                ),
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="c"),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="Third")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="element")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=".")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="The")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="last")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="one")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="!")]),
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
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="1) First list element.\n2) Second element, still in list.\n3) Third element. The last one!", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=2,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": True},
                    items_are_selectable={"colors": ["red"]},
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="1"),
                                        r.Text(kind="text", text=")"),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="First")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="list")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="element")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=".")]),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="2"),
                                        r.Text(kind="text", text=")"),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="Second")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="element")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=",")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="still")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="in")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="list")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=".")]),
                                    ]
                                ),
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="3"),
                                        r.Text(kind="text", text=")"),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="Third")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="element")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=".")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="The")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="last")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="one")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="!")]),
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
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="◆ First list element.\n◆ Second element, still in list.\n◆ Third element. The last one!", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=2,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": True},
                    items_are_selectable={"colors": ["red"]},
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="◆"),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="First")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="list")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="element")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=".")]),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="◆"),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="Second")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="element")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=",")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="still")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="in")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="list")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=".")]),
                                    ]
                                ),
                            ]
                        ),
                    ),
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="◆"),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="Third")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="element")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=".")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="The")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="last")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="one")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="!")]),
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
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[
                    d.TextInsertOp(
                        insert="Affirmative sentence. Exclamative sentence! Phrase exclamative ! Interrogative sentence? Phrase interrogative ? Suspens...\n",
                        attributes={},
                    )
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "sentences"},
                    items_are_selectable={"colors": ["red", "blue"]},
                    items_are_boxed=True,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.SelectableInput(
                                            kind="selectableInput",
                                            colors=["red", "blue"],
                                            boxed=True,
                                            contents=[
                                                r.Text(kind="text", text="Affirmative"),
                                                r.Whitespace(kind="whitespace"),
                                                r.Text(kind="text", text="sentence"),
                                                r.Text(kind="text", text="."),
                                            ],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(
                                            kind="selectableInput",
                                            colors=["red", "blue"],
                                            boxed=True,
                                            contents=[
                                                r.Text(kind="text", text="Exclamative"),
                                                r.Whitespace(kind="whitespace"),
                                                r.Text(kind="text", text="sentence"),
                                                r.Text(kind="text", text="!"),
                                            ],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(
                                            kind="selectableInput",
                                            colors=["red", "blue"],
                                            boxed=True,
                                            contents=[
                                                r.Text(kind="text", text="Phrase"),
                                                r.Whitespace(kind="whitespace"),
                                                r.Text(kind="text", text="exclamative"),
                                                r.Whitespace(kind="whitespace"),
                                                r.Text(kind="text", text="!"),
                                            ],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(
                                            kind="selectableInput",
                                            colors=["red", "blue"],
                                            boxed=True,
                                            contents=[
                                                r.Text(kind="text", text="Interrogative"),
                                                r.Whitespace(kind="whitespace"),
                                                r.Text(kind="text", text="sentence"),
                                                r.Text(kind="text", text="?"),
                                            ],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(
                                            kind="selectableInput",
                                            colors=["red", "blue"],
                                            boxed=True,
                                            contents=[
                                                r.Text(kind="text", text="Phrase"),
                                                r.Whitespace(kind="whitespace"),
                                                r.Text(kind="text", text="interrogative"),
                                                r.Whitespace(kind="whitespace"),
                                                r.Text(kind="text", text="?"),
                                            ],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(
                                            kind="selectableInput",
                                            colors=["red", "blue"],
                                            boxed=True,
                                            contents=[r.Text(kind="text", text="Suspens"), r.Text(kind="text", text="...")],
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
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[
                    d.TextInsertOp(insert="This ", attributes={}),
                    d.TextInsertOp(insert="is,", attributes={"manual-item": True}),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(insert="the", attributes={"manual-item": True}),
                    d.TextInsertOp(insert=" wording.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "manual"},
                    items_are_selectable={"colors": ["red", "blue"]},
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text="is")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text=",")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text="the")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wording"),
                                        r.Text(kind="text", text="."),
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
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[
                    d.TextInsertOp(insert="This ", attributes={}),
                    d.TextInsertOp(insert="is,", attributes={"manual-item": True}),
                    d.TextInsertOp(insert=" ", attributes={}),
                    d.TextInsertOp(insert="the", attributes={"manual-item": True}),
                    d.TextInsertOp(insert=" wording.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "manual"},
                    items_are_selectable={"colors": ["red", "blue"]},
                    items_are_boxed=True,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["red", "blue"], boxed=True, contents=[r.Text(kind="text", text="is")]
                                        ),
                                        r.SelectableInput(kind="selectableInput", colors=["red", "blue"], boxed=True, contents=[r.Text(kind="text", text=",")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["red", "blue"], boxed=True, contents=[r.Text(kind="text", text="the")]
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wording"),
                                        r.Text(kind="text", text="."),
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
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": False},
                    items_are_selectable=None,
                    items_are_boxed=True,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="This")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="is")], boxed=True),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="the")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="wording")], boxed=True),
                                        r.Text(kind="text", text="."),
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
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": False},
                    items_are_selectable={"colors": ["red", "green", "blue"]},
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", highlighted="red", text="abc"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", highlighted="green", text="def"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", highlighted="blue", text="ghi"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="jkl"),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["red", "green", "blue"], contents=[r.Text(kind="text", text="wording")]
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
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[d.TextInsertOp(insert="Abcd\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "characters", "letters": True},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=True,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="A"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="b"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="c"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="d"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
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
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[d.TextInsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": False},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=True,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="the"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wording"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
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
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[d.TextInsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": True},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=True,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="the"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wording"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
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
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[d.TextInsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": False, "punctuation": True},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=True,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="the"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wording"),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
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
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(
                        insert="Affirmative sentence. Exclamative sentence! Phrase exclamative ! Interrogative sentence? Phrase interrogative ? Suspens...\n",
                        attributes={},
                    )
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "sentences"},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=True,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="Affirmative"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="sentence"),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="Exclamative"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="sentence"),
                                        r.Text(kind="text", text="!"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="Phrase"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="exclamative"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="!"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="Interrogative"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="sentence"),
                                        r.Text(kind="text", text="?"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="Phrase"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="interrogative"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="?"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="Suspens"),
                                        r.Text(kind="text", text="..."),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
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
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="This ", attributes={}),
                    d.TextInsertOp(insert="is", attributes={"manual-item": True}),
                    d.TextInsertOp(insert=", ", attributes={}),
                    d.TextInsertOp(insert="the", attributes={"manual-item": True}),
                    d.TextInsertOp(insert=" wording.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "manual"},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=True,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="the"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="alpha")],
                                                [r.Text(kind="text", text="bravo")],
                                                [r.Text(kind="text", text="charlie")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wording"),
                                        r.Text(kind="text", text="."),
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
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[d.TextInsertOp(insert="Abcd\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "characters", "letters": True},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=True,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="A"),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="b"),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="c"),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="d"),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
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
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[d.TextInsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": False},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=True,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="This"),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="is"),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="the"),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="wording"),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Text(kind="text", text="."),
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
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[d.TextInsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": True},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=True,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="This"),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="is"),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text=","),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="the"),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="wording"),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="."),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
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
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[d.TextInsertOp(insert="This is, the wording.\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": False, "punctuation": True},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=True,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text=","),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="the"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wording"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="."),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
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
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(
                        insert="Affirmative sentence. Exclamative sentence! Phrase exclamative ! Interrogative sentence? Phrase interrogative ? Suspens...\n",
                        attributes={},
                    )
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "sentences"},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=True,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        r.Text(kind="text", text="Affirmative"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="sentence"),
                                                        r.Text(kind="text", text="."),
                                                    ],
                                                    vertical=False,
                                                ),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        r.Text(kind="text", text="Exclamative"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="sentence"),
                                                        r.Text(kind="text", text="!"),
                                                    ],
                                                    vertical=False,
                                                ),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        r.Text(kind="text", text="Phrase"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="exclamative"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="!"),
                                                    ],
                                                    vertical=False,
                                                ),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        r.Text(kind="text", text="Interrogative"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="sentence"),
                                                        r.Text(kind="text", text="?"),
                                                    ],
                                                    vertical=False,
                                                ),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        r.Text(kind="text", text="Phrase"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="interrogative"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="?"),
                                                    ],
                                                    vertical=False,
                                                ),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[r.Text(kind="text", text="Suspens"), r.Text(kind="text", text="...")],
                                                    vertical=False,
                                                ),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
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
                    d.TextInsertOp(insert="Instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha, bravo, charlie",
                        attributes={"choices2": {"start": "", "separator1": ",", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="This ", attributes={}),
                    d.TextInsertOp(insert="is", attributes={"manual-item": True}),
                    d.TextInsertOp(insert=", ", attributes={}),
                    d.TextInsertOp(insert="the", attributes={"manual-item": True}),
                    d.TextInsertOp(insert=" wording.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "manual"},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=True,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="charlie")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="is"),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.Text(kind="text", text="the"),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[
                                                        [r.Text(kind="text", text="alpha")],
                                                        [r.Text(kind="text", text="bravo")],
                                                        [r.Text(kind="text", text="charlie")],
                                                    ],
                                                    show_choices_by_default=False,
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wording"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_mcq_below_separated_items(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[
                    d.TextInsertOp(insert="Indique le genre de chacun de ces groupes nominaux (", attributes={}),
                    d.TextInsertOp(
                        insert="singulier ou pluriel",
                        attributes={"choices2": {"start": "", "separator1": "ou", "separator2": "", "stop": "", "placeholder": ""}},
                    ),
                    d.TextInsertOp(insert=")\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="a. les tables / les chaises / les fauteuils\nb. les enfants / les personnes âgées / les adultes\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "separated", "separator": "/"},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=True,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Indique"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="le"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="genre"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="de"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="chacun"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="de"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ces"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="groupes"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="nominaux"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="("),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="singulier")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="pluriel")], boxed=True),
                                        r.Text(kind="text", text=")"),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="a"),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        r.Text(kind="text", text="les"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="tables"),
                                                    ],
                                                ),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        r.Text(kind="text", text="les"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="chaises"),
                                                    ],
                                                ),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        r.Text(kind="text", text="les"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="fauteuils"),
                                                    ],
                                                ),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="b"),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        r.Text(kind="text", text="les"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="enfants"),
                                                    ],
                                                ),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        r.Text(kind="text", text="les"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="personnes"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="âgées"),
                                                    ],
                                                ),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.AnySequence(
                                            kind="sequence",
                                            contents=[
                                                r.AnySequence(
                                                    kind="sequence",
                                                    contents=[
                                                        r.Text(kind="text", text="les"),
                                                        r.Whitespace(kind="whitespace"),
                                                        r.Text(kind="text", text="adultes"),
                                                    ],
                                                ),
                                                r.MultipleChoicesInput(
                                                    kind="multipleChoicesInput",
                                                    choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                                ),
                                            ],
                                            vertical=True,
                                        ),
                                    ]
                                ),
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_gender_mcq(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="alpha bravo charlie\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": False},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=True,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=True, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="alpha"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            show_arrow_before=True,
                                            choices=[[r.Text(kind="text", text="féminin")], [r.Text(kind="text", text="masculin")]],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="bravo"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            show_arrow_before=True,
                                            choices=[[r.Text(kind="text", text="féminin")], [r.Text(kind="text", text="masculin")]],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="charlie"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            show_arrow_before=True,
                                            choices=[[r.Text(kind="text", text="féminin")], [r.Text(kind="text", text="masculin")]],
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_number_mcq(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="alpha bravo charlie\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": False},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=True,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=True),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="alpha"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            show_arrow_before=True,
                                            choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="bravo"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            show_arrow_before=True,
                                            choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="charlie"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            show_arrow_before=True,
                                            choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_gender_and_number_mcq(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="alpha bravo charlie\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": True},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=True,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=True, grammatical_number=True),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="alpha"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            show_arrow_before=True,
                                            choices=[[r.Text(kind="text", text="féminin")], [r.Text(kind="text", text="masculin")]],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="bravo"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            show_arrow_before=True,
                                            choices=[[r.Text(kind="text", text="féminin")], [r.Text(kind="text", text="masculin")]],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="charlie"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            show_arrow_before=True,
                                            choices=[[r.Text(kind="text", text="féminin")], [r.Text(kind="text", text="masculin")]],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                        ),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def test_gender_and_number_mcq__single_item_per_paragraph(self):
        self.do_test(
            e.Exercise(
                number="number",
                textbook_page=42,
                instructions=[d.TextInsertOp(insert="Instructions\n", attributes={})],
                wording=[d.TextInsertOp(insert="alpha bravo charlie\n", attributes={})],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=True,
                    placeholder_for_fill_with_free_text=None,
                    items={"kind": "tokens", "words": True, "punctuation": True},
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=True,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=True, grammatical_number=True),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="Instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="alpha"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            show_arrow_before=True,
                                            choices=[[r.Text(kind="text", text="féminin")], [r.Text(kind="text", text="masculin")]],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                        ),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="bravo"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            show_arrow_before=True,
                                            choices=[[r.Text(kind="text", text="féminin")], [r.Text(kind="text", text="masculin")]],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                        ),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="charlie"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            show_arrow_before=True,
                                            choices=[[r.Text(kind="text", text="féminin")], [r.Text(kind="text", text="masculin")]],
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="singulier")], [r.Text(kind="text", text="pluriel")]],
                                        ),
                                    ]
                                ),
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
                    d.TextInsertOp(insert="Choose ", attributes={}),
                    d.TextInsertOp(
                        insert="a or b", attributes={"choices2": {"start": "", "separator1": "or", "separator2": "", "stop": "", "placeholder": "..."}}
                    ),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ... B ...\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="multiple-choices",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="a")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="b")], boxed=True),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="A"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="a")], [r.Text(kind="text", text="b")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="B"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="a")], [r.Text(kind="text", text="b")]],
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
                    d.TextInsertOp(insert="Choose ", attributes={}),
                    d.TextInsertOp(
                        insert="a or b", attributes={"choices2": {"start": "", "separator1": "or", "separator2": "", "stop": "", "placeholder": "@"}}
                    ),
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
                adaptation=Adaptation(
                    kind="multiple-choices",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="a")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="b")], boxed=True),
                                        r.Text(kind="text", text="."),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="{"),
                                        r.Text(kind="text", text="choices2"),
                                        r.Text(kind="text", text="|"),
                                        r.Text(kind="text", text="|"),
                                        r.Text(kind="text", text="/"),
                                        r.Text(kind="text", text="|"),
                                        r.Text(kind="text", text="|"),
                                        r.Text(kind="text", text="|"),
                                        r.Text(kind="text", text="|"),
                                        r.Text(kind="text", text="is"),
                                        r.Text(kind="text", text="}"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="the"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="@"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="example"),
                                        r.Text(kind="text", text="."),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="{"),
                                        r.Text(kind="text", text="choices2"),
                                        r.Text(kind="text", text="|"),
                                        r.Text(kind="text", text="|"),
                                        r.Text(kind="text", text="/"),
                                        r.Text(kind="text", text="|"),
                                        r.Text(kind="text", text="|"),
                                        r.Text(kind="text", text="|"),
                                        r.Text(kind="text", text="|"),
                                        r.Text(kind="text", text="the"),
                                        r.Text(kind="text", text="}"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="@"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="clue"),
                                        r.Text(kind="text", text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="A"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="a")], [r.Text(kind="text", text="b")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="B"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="a")], [r.Text(kind="text", text="b")]],
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
                    d.TextInsertOp(insert="Choose ", attributes={}),
                    d.TextInsertOp(
                        insert="a or b", attributes={"choices2": {"start": "", "separator1": "or", "separator2": "", "stop": "", "placeholder": "..."}}
                    ),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ... B ...\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="multiple-choices",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="a")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="b")], boxed=True),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="A"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="a")], [r.Text(kind="text", text="b")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="B"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="a")], [r.Text(kind="text", text="b")]],
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
                    d.TextInsertOp(insert="Choose ", attributes={}),
                    d.TextInsertOp(insert="a b", attributes={"choices2": {"start": "", "separator1": "", "separator2": "", "stop": "", "placeholder": "..."}}),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ... B ...\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="multiple-choices",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="a b")], boxed=True),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="A"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="a b")]], show_choices_by_default=False
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="B"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="a b")]], show_choices_by_default=False
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
                    d.TextInsertOp(insert="Choose ", attributes={}),
                    d.TextInsertOp(
                        insert="a, b, c or d", attributes={"choices2": {"start": "", "separator1": ",", "separator2": "or", "stop": "", "placeholder": "..."}}
                    ),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ... B ...\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="multiple-choices",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="a")], boxed=True),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="b")], boxed=True),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="c")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="d")], boxed=True),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="A"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="a")],
                                                [r.Text(kind="text", text="b")],
                                                [r.Text(kind="text", text="c")],
                                                [r.Text(kind="text", text="d")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="B"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="a")],
                                                [r.Text(kind="text", text="b")],
                                                [r.Text(kind="text", text="c")],
                                                [r.Text(kind="text", text="d")],
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
                    d.TextInsertOp(insert="Choose ", attributes={}),
                    d.TextInsertOp(
                        insert="a, b, c, or d", attributes={"choices2": {"start": "", "separator1": ",", "separator2": "or", "stop": "", "placeholder": "..."}}
                    ),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ... B ...\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="multiple-choices",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="a")], boxed=True),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="b")], boxed=True),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="c")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="d")], boxed=True),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="A"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="a")],
                                                [r.Text(kind="text", text="b")],
                                                [r.Text(kind="text", text="c")],
                                                [r.Text(kind="text", text="d")],
                                            ],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="B"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[
                                                [r.Text(kind="text", text="a")],
                                                [r.Text(kind="text", text="b")],
                                                [r.Text(kind="text", text="c")],
                                                [r.Text(kind="text", text="d")],
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
                    d.TextInsertOp(insert="Choose ", attributes={}),
                    d.TextInsertOp(
                        insert="a / b // c", attributes={"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": "..."}}
                    ),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ... B ...\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="multiple-choices",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="a")], boxed=True),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="b")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="c")], boxed=True),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="A"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="a")], [r.Text(kind="text", text="b")], [r.Text(kind="text", text="c")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="B"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="a")], [r.Text(kind="text", text="b")], [r.Text(kind="text", text="c")]],
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
                    d.TextInsertOp(insert="Choose ", attributes={}),
                    d.TextInsertOp(
                        insert="(a or b)", attributes={"choices2": {"start": "(", "separator1": "or", "separator2": "", "stop": ")", "placeholder": "..."}}
                    ),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ... B ...\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="multiple-choices",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="a")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="b")], boxed=True),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="A"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="a")], [r.Text(kind="text", text="b")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="B"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="a")], [r.Text(kind="text", text="b")]],
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
                    d.TextInsertOp(insert="Choose ", attributes={}),
                    d.TextInsertOp(
                        insert="a or b", attributes={"choices2": {"start": "", "separator1": "or", "separator2": "", "stop": "", "placeholder": "..."}}
                    ),
                    d.TextInsertOp(insert=" and ", attributes={}),
                    d.TextInsertOp(
                        insert="c or d", attributes={"choices2": {"start": "", "separator1": "or", "separator2": "", "stop": "", "placeholder": "@@@"}}
                    ),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="A ... @@@\nB ... @@@\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="multiple-choices",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="a")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="b")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="and"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="c")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="d")], boxed=True),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="A"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="a")], [r.Text(kind="text", text="b")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="d")]],
                                            show_choices_by_default=False,
                                        ),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="B"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="a")], [r.Text(kind="text", text="b")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="c")], [r.Text(kind="text", text="d")]],
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
                    d.TextInsertOp(insert="Complète les mots avec ", attributes={}),
                    d.TextInsertOp(
                        insert="m ou n", attributes={"choices2": {"start": "", "separator1": "ou", "separator2": "", "stop": "", "placeholder": "..."}}
                    ),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="i...mense i...juste\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="multiple-choices",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Complète"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="les"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="mots"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="avec"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="m")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="n")], boxed=True),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="i"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="m")], [r.Text(kind="text", text="n")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="mense"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="i"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="m")], [r.Text(kind="text", text="n")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="juste"),
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
                adaptation=Adaptation(
                    kind="multiple-choices",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="A"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="a")], [r.Text(kind="text", text="b")], [r.Text(kind="text", text="c")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="B"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="d")], [r.Text(kind="text", text="e")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
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
                adaptation=Adaptation(
                    kind="multiple-choices",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="A"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="blah")], [r.Text(kind="text", text="blih")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
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
                adaptation=Adaptation(
                    kind="multiple-choices",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="A"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="blah")], [r.Text(kind="text", text="blih")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
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
                adaptation=Adaptation(
                    kind="multiple-choices",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="A"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="blah")], [r.Text(kind="text", text="blih")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
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
                adaptation=Adaptation(
                    kind="multiple-choices",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="A"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput", choices=[[r.Text(kind="text", text="blah / blih")]], show_choices_by_default=False
                                        ),
                                        r.Text(kind="text", text="."),
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
                adaptation=Adaptation(
                    kind="multiple-choices",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="A"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="blah")], [r.Text(kind="text", text="blih")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
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
                adaptation=Adaptation(
                    kind="multiple-choices",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="A"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="blah")], [r.Text(kind="text", text="blih")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
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
                adaptation=Adaptation(
                    kind="multiple-choices",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="The"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="sky"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="blue")], [r.Text(kind="text", text="red")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
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
                adaptation=Adaptation(
                    kind="multiple-choices",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="The"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="sky"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="blue")], [r.Text(kind="text", text="red")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
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
                adaptation=Adaptation(
                    kind="multiple-choices",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="The"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="sky"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="blue")], [r.Text(kind="text", text="yellow")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="the"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="sun"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="blue")], [r.Text(kind="text", text="yellow")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
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
                adaptation=Adaptation(
                    kind="multiple-choices",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="The"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="sky"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="blue")], [r.Text(kind="text", text="red")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="the"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="sun"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="green")], [r.Text(kind="text", text="yellow")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
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
                adaptation=Adaptation(
                    kind="multiple-choices",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="The"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="sky"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="blue")], [r.Text(kind="text", text="red")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="The"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="sun"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="green")], [r.Text(kind="text", text="yellow")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
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
                adaptation=Adaptation(
                    kind="multiple-choices",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="The"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="sky"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="blue")], [r.Text(kind="text", text="red")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="the"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="sun"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="green")], [r.Text(kind="text", text="yellow")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
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
                    d.TextInsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="The wording of this exercise is a single sentence.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red", "blue"]),
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text="The")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text="wording")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text="of")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text="this")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text="exercise")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text="is")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text="a")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text="single")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red", "blue"], contents=[r.Text(kind="text", text="sentence")]),
                                        r.Text(kind="text", text="."),
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
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red", "green", "blue"]),
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", highlighted="red", text="abc"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", highlighted="green", text="def"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", highlighted="blue", text="ghi"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="jkl"),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["red", "green", "blue"], contents=[r.Text(kind="text", text="wording")]
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
                    d.TextInsertOp(insert="abc", attributes={"sel": 1}),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="wording\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red"]),
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", highlighted="red", text="abc")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="wording")])]
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
                    d.TextInsertOp(insert="instructions\nare\n\non\n\nmultiple\nlines\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="wording\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red"]),
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[r.Text(kind="text", text="instructions"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="are")]
                                ),
                                r.Paragraph(contents=[r.Text(kind="text", text="on")]),
                                r.Paragraph(
                                    contents=[r.Text(kind="text", text="multiple"), r.Whitespace(kind="whitespace"), r.Text(kind="text", text="lines")]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="wording")])]
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
                    d.TextInsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="wording is\n\non\n\nmultiple lines\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red"]),
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="wording")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="is")]),
                                    ]
                                ),
                                r.Paragraph(contents=[r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="on")])]),
                                r.Paragraph(
                                    contents=[
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="multiple")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="lines")]),
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
                    d.TextInsertOp(insert="{tag|abc}\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="{tag|def}\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red"]),
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="{"),
                                        r.Text(kind="text", text="tag"),
                                        r.Text(kind="text", text="|"),
                                        r.Text(kind="text", text="abc"),
                                        r.Text(kind="text", text="}"),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="{"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="tag")]),
                                        r.Text(kind="text", text="|"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="def")]),
                                        r.Text(kind="text", text="}"),
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
                    d.TextInsertOp(insert="   abc   \n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="   def   \n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red"]),
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=42,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="abc")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(contents=[r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="def")])])
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
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red"]),
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                r.Paragraph(contents=[r.Text(kind="text", text="instructions")]),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="the"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="example"),
                                        r.Text(kind="text", text="."),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="the"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="clue"),
                                        r.Text(kind="text", text="."),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="wording")])]
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
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red", "green", "blue"]),
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                r.Paragraph(contents=[r.Text(kind="text", text="instructions")]),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", highlighted="red", text="abc"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", highlighted="green", text="def"),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", highlighted="blue", text="ghi"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="jkl"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["red", "green", "blue"], contents=[r.Text(kind="text", text="wording")]
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
                    d.TextInsertOp(insert="Selectionne les articles.\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="La maison est belle. L'école est fermée. L’automobile est verte.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red"]),
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Selectionne"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="les"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="articles"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="La")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="maison")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="est")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="belle")]),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="L"), r.Text(kind="text", text="'")]
                                        ),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="école")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="est")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="fermée")]),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="L"), r.Text(kind="text", text="’")]
                                        ),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="automobile")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="est")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="verte")]),
                                        r.Text(kind="text", text="."),
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
                    d.TextInsertOp(insert="Selectionne les articles.\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="La maison est belle. L'école est fermée. L’automobile est verte.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=False, punctuation=True),
                    items_are_selectable=Selectable(colors=["red"]),
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Selectionne"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="les"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="articles"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="La"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="maison"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="est"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="belle"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=".")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="L"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="'")]),
                                        r.Text(kind="text", text="école"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="est"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="fermée"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=".")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="L"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="’")]),
                                        r.Text(kind="text", text="automobile"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="est"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="verte"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=".")]),
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
                    d.TextInsertOp(insert="Selectionne les articles.\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="La maison est belle. L'école est fermée. L’automobile est verte.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=True),
                    items_are_selectable=Selectable(colors=["red"]),
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Selectionne"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="les"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="articles"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="La")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="maison")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="est")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="belle")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=".")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="L")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="'")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="école")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="est")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="fermée")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=".")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="L")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="’")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="automobile")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="est")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="verte")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=".")]),
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
                    d.TextInsertOp(insert="Selectionne les articles.\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="La maison est belle. L'école est fermée. L’automobile est verte.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=None,
                    items_are_boxed=True,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Selectionne"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="les"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="articles"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="La")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="maison")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="est")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="belle")], boxed=True),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(
                                            kind="passiveSequence", contents=[r.Text(kind="text", text="L"), r.Text(kind="text", text="'")], boxed=True
                                        ),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="école")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="est")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="fermée")], boxed=True),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(
                                            kind="passiveSequence", contents=[r.Text(kind="text", text="L"), r.Text(kind="text", text="’")], boxed=True
                                        ),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="automobile")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="est")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="verte")], boxed=True),
                                        r.Text(kind="text", text="."),
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
                    d.TextInsertOp(insert="Selectionne les articles.\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="La maison est belle. L'école est fermée. L’automobile est verte.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=False, punctuation=True),
                    items_are_selectable=None,
                    items_are_boxed=True,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Selectionne"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="les"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="articles"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="La"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="maison"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="est"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="belle"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text=".")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="L"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="'")], boxed=True),
                                        r.Text(kind="text", text="école"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="est"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="fermée"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text=".")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="L"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="’")], boxed=True),
                                        r.Text(kind="text", text="automobile"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="est"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="verte"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text=".")], boxed=True),
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
                    d.TextInsertOp(insert="Selectionne les articles.\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="La maison est belle. L'école est fermée. L’automobile est verte.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=True),
                    items_are_selectable=None,
                    items_are_boxed=True,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Selectionne"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="les"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="articles"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="La")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="maison")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="est")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="belle")], boxed=True),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text=".")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(
                                            kind="passiveSequence", contents=[r.Text(kind="text", text="L"), r.Text(kind="text", text="'")], boxed=True
                                        ),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="école")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="est")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="fermée")], boxed=True),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text=".")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(
                                            kind="passiveSequence", contents=[r.Text(kind="text", text="L"), r.Text(kind="text", text="’")], boxed=True
                                        ),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="automobile")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="est")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="verte")], boxed=True),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text=".")], boxed=True),
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
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="a"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", bold=True, text="strict"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", italic=True, text="paragraph"),
                                        r.Text(kind="text", text="."),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="And"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="this"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="a"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", bold=True, text="lenient"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", italic=True, text="paragraph"),
                                    ]
                                ),
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="a"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", bold=True, text="strict"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wording"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", italic=True, text="paragraph"),
                                        r.Text(kind="text", text="."),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="And"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="this"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="a"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", bold=True, text="lenient"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wording"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", italic=True, text="paragraph"),
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
                    d.TextInsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="This is a strict paragraph, with... some punctuation.\n\nAnd this, is a... lenient paragraph\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red"]),
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="This")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="is")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="a")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="strict")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="paragraph")]),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="with")]),
                                        r.Text(kind="text", text="..."),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="some")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="punctuation")]),
                                        r.Text(kind="text", text="."),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="And")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="this")]),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="is")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="a")]),
                                        r.Text(kind="text", text="..."),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="lenient")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="paragraph")]),
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
                    d.TextInsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="This is a strict paragraph, with... some punctuation.\n\nAnd this, is a... lenient paragraph\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=TokensItems(kind="tokens", words=True, punctuation=True),
                    items_are_selectable=Selectable(colors=["red"]),
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="This")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="is")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="a")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="strict")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="paragraph")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=",")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="with")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="...")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="some")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="punctuation")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=".")]),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="And")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="this")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text=",")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="is")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="a")]),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="...")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="lenient")]),
                                        r.Whitespace(kind="whitespace"),
                                        r.SelectableInput(kind="selectableInput", colors=["red"], contents=[r.Text(kind="text", text="paragraph")]),
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
                    d.TextInsertOp(insert="instructions\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="This is a ... strict paragraph. With some punctuation.\n\nAnd this, is a ... lenient paragraph\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text="...",
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
                    show_arrow_before_mcq_fields=False,
                    show_mcq_choices_by_default=False,
                ),
            ),
            r.Exercise(
                number="number",
                textbook_page=None,
                pagelets=[
                    r.Pagelet(
                        instructions=r.Section(paragraphs=[r.Paragraph(contents=[r.Text(kind="text", text="instructions")])]),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="a"),
                                        r.Whitespace(kind="whitespace"),
                                        r.FreeTextInput(kind="freeTextInput"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="strict"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="paragraph"),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="With"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="some"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="punctuation"),
                                        r.Text(kind="text", text="."),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="And"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="this"),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="a"),
                                        r.Whitespace(kind="whitespace"),
                                        r.FreeTextInput(kind="freeTextInput"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="lenient"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="paragraph"),
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
                    d.TextInsertOp(insert="Choose ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha/bravo", attributes={"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": "..."}}
                    ),
                    d.TextInsertOp(insert=".\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="This is a ... strict paragraph. With some punctuation.\n\nAnd this, is a ... lenient paragraph\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="This"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="a"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="alpha")], [r.Text(kind="text", text="bravo")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="strict"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="paragraph"),
                                        r.Text(kind="text", text="."),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="With"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="some"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="punctuation"),
                                        r.Text(kind="text", text="."),
                                    ]
                                ),
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="And"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="this"),
                                        r.Text(kind="text", text=","),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="a"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="alpha")], [r.Text(kind="text", text="bravo")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="lenient"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="paragraph"),
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
                    d.TextInsertOp(insert="instructions ", attributes={}),
                    d.TextInsertOp(
                        insert="short/long", attributes={"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": "@@@"}}
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                wording=[
                    d.TextInsertOp(insert="The wording of this ... is a @@@ sentence.\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text="...",
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="instructions"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="short")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="long")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="The"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wording"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="of"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="this"),
                                        r.Whitespace(kind="whitespace"),
                                        r.FreeTextInput(kind="freeTextInput"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="is"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="a"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="short")], [r.Text(kind="text", text="long")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="sentence"),
                                        r.Text(kind="text", text="."),
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
                    d.TextInsertOp(insert="Choose wisely ", attributes={}),
                    d.TextInsertOp(
                        insert="alpha/bravo", attributes={"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": "@@@"}}
                    ),
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
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=3,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text=None,
                    items=None,
                    items_are_selectable=None,
                    items_are_boxed=False,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.Text(kind="text", text="A"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="a")], [r.Text(kind="text", text="b")], [r.Text(kind="text", text="c")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="B"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="d")], [r.Text(kind="text", text="e")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="C"),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="alpha")], [r.Text(kind="text", text="bravo")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Text(kind="text", text="."),
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
                    d.TextInsertOp(insert="Choose wisely ", attributes={}),
                    # Multiple choices in instructions
                    d.TextInsertOp(
                        insert="alpha/bravo", attributes={"choices2": {"start": "", "separator1": "/", "separator2": "", "stop": "", "placeholder": "@@@"}}
                    ),
                ],
                wording=[
                    d.TextInsertOp(insert="Hello @@@ $$$ ....", attributes={}),
                    # Multiple choices in wording
                    d.TextInsertOp(
                        insert="(charlie|delta)",
                        attributes={"choices2": {"start": "(", "separator1": "|", "separator2": "", "stop": ")", "placeholder": "$$$"}},
                    ),
                    d.TextInsertOp(insert="\n", attributes={}),
                ],
                example=[d.TextInsertOp(insert="\n", attributes={})],
                clue=[d.TextInsertOp(insert="\n", attributes={})],
                adaptation=Adaptation(
                    kind="generic",
                    wording_paragraphs_per_pagelet=None,
                    single_item_per_paragraph=False,
                    placeholder_for_fill_with_free_text="...",
                    items=TokensItems(kind="tokens", words=True, punctuation=False),
                    items_are_selectable=Selectable(colors=["red", "yellow"]),
                    items_are_boxed=True,
                    items_have_mcq_beside=False,
                    items_have_mcq_below=False,
                    items_have_predefined_mcq=PredefinedMcq(grammatical_gender=False, grammatical_number=False),
                    items_are_repeated_with_mcq=False,
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
                                    contents=[
                                        r.Text(kind="text", text="Choose"),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="wisely"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="alpha")], boxed=True),
                                        r.Whitespace(kind="whitespace"),
                                        r.Text(kind="text", text="ou"),
                                        r.Whitespace(kind="whitespace"),
                                        r.PassiveSequence(kind="passiveSequence", contents=[r.Text(kind="text", text="bravo")], boxed=True),
                                    ]
                                )
                            ]
                        ),
                        wording=r.Section(
                            paragraphs=[
                                r.Paragraph(
                                    contents=[
                                        r.SelectableInput(
                                            kind="selectableInput", colors=["red", "yellow"], boxed=True, contents=[r.Text(kind="text", text="Hello")]
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="alpha")], [r.Text(kind="text", text="bravo")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.MultipleChoicesInput(
                                            kind="multipleChoicesInput",
                                            choices=[[r.Text(kind="text", text="charlie")], [r.Text(kind="text", text="delta")]],
                                            show_choices_by_default=False,
                                        ),
                                        r.Whitespace(kind="whitespace"),
                                        r.FreeTextInput(kind="freeTextInput"),
                                        r.Text(kind="text", text="."),
                                    ]
                                )
                            ]
                        ),
                    )
                ],
            ),
        )
