from typing import Annotated, ClassVar, Literal
import itertools

import lark
import pydantic

from . import exercise_delta
from . import renderable
from mydantic import PydanticBase


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


class DeltaMaker(lark.Transformer):
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
        if len(self.selection_colors) > 0:
            return exercise_delta.TextInsertOp(insert=args[0], attributes={"sel": 1})
        else:
            return exercise_delta.TextInsertOp(insert=args[0], attributes={})

    def sel2_tag(self, args):
        if len(self.selection_colors) > 1:
            return exercise_delta.TextInsertOp(insert=args[0], attributes={"sel": 2})
        else:
            return exercise_delta.TextInsertOp(insert=args[0], attributes={})

    def sel3_tag(self, args):
        if len(self.selection_colors) > 2:
            return exercise_delta.TextInsertOp(insert=args[0], attributes={"sel": 3})
        else:
            return exercise_delta.TextInsertOp(insert=args[0], attributes={})

    def sel4_tag(self, args):
        if len(self.selection_colors) > 3:
            return exercise_delta.TextInsertOp(insert=args[0], attributes={"sel": 4})
        else:
            return exercise_delta.TextInsertOp(insert=args[0], attributes={})

    def sel5_tag(self, args):
        if len(self.selection_colors) > 4:
            return exercise_delta.TextInsertOp(insert=args[0], attributes={"sel": 5})
        else:
            return exercise_delta.TextInsertOp(insert=args[0], attributes={})


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
        effects: list[AdaptationEffect],
        instructions: str,
        wording: str,
        example: str,
        clue: str,
    ):
        for effect in effects:
            (instructions, wording, example, clue) = effect.preprocess(instructions, wording, example, clue)
        (instructions, wording, example, clue) = self.preprocess(instructions, wording, example, clue)

        instructions_adapter_constructor_kwds = {}
        wording_adapter_constructor_kwds = {}
        example_adapter_constructor_kwds = {}
        clue_adapter_constructor_kwds = {}
        for effect in effects:
            instructions_adapter_constructor_kwds.update(effect.make_instructions_adapter_constructor_kwds())
            wording_adapter_constructor_kwds.update(effect.make_wording_adapter_constructor_kwds())
            example_adapter_constructor_kwds.update(effect.make_example_adapter_constructor_kwds())
            clue_adapter_constructor_kwds.update(effect.make_clue_adapter_constructor_kwds())
        wording_adapter_constructor_kwds.update(self.make_wording_adapter_constructor_kwds(instructions))

        instructions = _instructions_parser.parse(instructions)
        wording = _wording_parser.parse(wording)
        example = _example_and_clue_parser.parse(example)
        clue = _example_and_clue_parser.parse(clue)

        self.instructions_delta = self.make_deltas_for_instructions(instructions, **instructions_adapter_constructor_kwds)
        self.wording_delta = self.make_deltas_for_wording(wording, **wording_adapter_constructor_kwds)
        self.example_delta = self.make_deltas_for_example(example, **example_adapter_constructor_kwds)
        self.clue_delta = self.make_deltas_for_clue(clue, **clue_adapter_constructor_kwds)

        self.adapted_instructions = self.adapt_instructions(instructions, **instructions_adapter_constructor_kwds)
        self.adapted_wording = self.adapt_wording(wording, **wording_adapter_constructor_kwds)
        self.adapted_example = self.adapt_example(example, **example_adapter_constructor_kwds)
        self.adapted_clue = self.adapt_clue(clue, **clue_adapter_constructor_kwds)

    def preprocess(self, instructions, wording, example, clue):
        placeholders = set(choice[4] for choice in itertools.chain(self.gather_choices(instructions), self.gather_choices(wording)))
        for placeholder in placeholders:
            wording = wording.replace(placeholder, f"{{placeholder2|{placeholder}}}").replace(f"|{{placeholder2|{placeholder}}}|", f"|{placeholder}|")
        return (instructions, wording, example, clue)

    def make_wording_adapter_constructor_kwds(self, instructions):
        multiple_choices = {}
        for (start, separator1, separator2, stop, placeholder, text) in self.gather_choices(instructions):
            multiple_choices[placeholder] = _separate_choices(start, separator1, separator2, stop, placeholder, text)
        return {
            "multiple_choices": multiple_choices,
        }

    def gather_choices(self, instructions):
        return ChoicesGatherer().transform(_instructions_parser.parse(instructions))

    def adapt_instructions(self, instructions, **kwds):
        return InstructionsAdapter(**kwds).transform(instructions)

    def adapt_example(self, example, **kwds):
        return InstructionsAdapter(**kwds).transform(example)

    def adapt_clue(self, clue, **kwds):
        return InstructionsAdapter(**kwds).transform(clue)

    def adapt_wording(self, wording, **kwds):
        return WordingAdapter(**kwds).transform(wording)

    def make_deltas_for_instructions(self, instructions, **kwds):
        return DeltaMaker(**kwds).transform(instructions)

    def make_deltas_for_example(self, example, **kwds):
        return DeltaMaker(**kwds).transform(example)

    def make_deltas_for_clue(self, clue, **kwds):
        return DeltaMaker(**kwds).transform(clue)

    def make_deltas_for_wording(self, wording, **kwds):
        return DeltaMaker(**kwds).transform(wording)
