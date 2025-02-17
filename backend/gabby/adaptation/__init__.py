from __future__ import annotations

from typing import Iterable
import copy
import itertools
import json
import re
import traceback
import unittest

import mydantic

from .. import deltas
from .. import exercises
from .. import renderable


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
                            current_paragraph.append(deltas.TextInsertOp(insert=paragraph_part, attributes=delta.attributes))
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
                        current_sentence.append(deltas.TextInsertOp(insert=sentence_part, attributes=delta.attributes))
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
