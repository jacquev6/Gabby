<script lang="ts">
import { useApiStore } from '$frontend/stores/api'
import type { Project, Textbook, Exercise, InCache, Exists } from '$frontend/stores/api'
import deepEqual from 'deep-equal'
import { type Model as Deltas } from '$frontend/components/Quill.vue'
import { Delta } from 'quill/core'


const api = useApiStore()

type Adaptation = (Exercise & InCache & Exists)['attributes']['adaptation']
type PdfRectangle = (Exercise & InCache & Exists)['attributes']['rectangles'][number]

const emptyDeltas: Deltas = [{insert: '\n', attributes: {}}]

export const adaptationKinds: Adaptation['kind'][] = ['generic', 'fill-with-free-text', 'multiple-choices']

export const textualFieldNames = ['instructions', 'wording', 'example', 'clue', 'textReference'] as const
export type TextualFieldName = typeof textualFieldNames[number]

type MakeModelOptions  = {
  inTextbook: true
  textbookPage: number
} | {
  inTextbook: false
  textbookPage: null
}

// This model contains all things visible on the exercise form, including:
// - anything in progress
// - its addendum in the "Tools" column
export type Model = MakeModelOptions & {
  number: string
  instructions: Deltas
  wording: Deltas
  example: Deltas
  clue: Deltas
  textReference: Deltas
  rectangles: PdfRectangle[]
  adaptationSettings: {
    kind: Adaptation['kind']
    wordingParagraphsPerPagelet: number | null
    singleItemPerParagraph: boolean
    placeholderForFillWithFreeText: string | null  // @todo Remove null: translate '' to null in makeAdaptation
    showArrowBeforeMcqFields: boolean
    showMcqChoicesByDefault: boolean
    itemized: {
      items: {
        isLetters: boolean
        isWords: boolean
        isPunctuation: boolean
        isSentences: boolean
        isManual: boolean
        isSeparated: boolean
        separator: string
      }
      effects: {
        isSelectable: boolean
        selectable: {
          colorsCount: number
          allColors: string[]
        }
        isBoxed: boolean
        hasMcqBeside: boolean
        hasMcqBelow: boolean
        hasGenderMcq: boolean
        hasNumberMcq: boolean
        repeatedWithMcq: boolean
      }
    }
  }
  inProgress:
    {
      kind: 'nothing'
    } | {
      kind: 'multipleChoicesCreation'
    } | {
      kind: 'multipleChoicesEdition'
      initial: boolean
      stopWatching(): void
      deleted: boolean
      delete(): void
      settings: {
        start: string
        stop: string
        separator1: string
        separator2: string
        placeholder: string
        mcqFieldUid: string | null
      }
    } | {
      kind: 'newMcqField'
      uid: string
    }
}

// Colors provided by the client, in display order
export const allColorsForSelectableEffect = [
  '#ffff00',  // yellow
  '#ffcf4c',  // orange
  '#ff8084',  // red
  '#ffc0cb',  // pink
  '#d49cff',  // purple
  '#8177ff',  // dark blue
  '#bbbbff',  // light blue
  '#bbffbb',  // light green
  '#68e495',  // dark green
  '#632f2b',  // brown
  '#bbbbbb',  // grey
  '#000000',  // black
]

export const defaultAdaptationSettings: Model["adaptationSettings"] = {
  kind: 'generic',
  wordingParagraphsPerPagelet: null,
  singleItemPerParagraph: false,
  placeholderForFillWithFreeText: null,
  showArrowBeforeMcqFields: false,
  showMcqChoicesByDefault: false,
  itemized: {
    items: {
      isLetters: false,
      isWords: false,
      isPunctuation: false,
      isSentences: false,
      isManual: false,
      isSeparated: false,
      separator: '',
    },
    effects: {
      isSelectable: false,
      selectable: {
        colorsCount: 2,
        allColors: [
          allColorsForSelectableEffect[0],
          allColorsForSelectableEffect[3],
          allColorsForSelectableEffect[6],
          allColorsForSelectableEffect[7],
          allColorsForSelectableEffect[10],
        ],
      },
      isBoxed: false,
      hasMcqBeside: false,
      hasMcqBelow: false,
      hasGenderMcq: false,
      hasNumberMcq: false,
      repeatedWithMcq: false,
    },
  },
}

function makeModel(options: MakeModelOptions): Model {
  return {
    ...options,
    number: '',
    instructions: [{insert: '\n', attributes: {}}],
    wording: [{insert: '\n', attributes: {}}],
    example: [{insert: '\n', attributes: {}}],
    clue: [{insert: '\n', attributes: {}}],
    textReference: [{insert: '\n', attributes: {}}],
    rectangles: [],
    adaptationSettings: deepCopy(defaultAdaptationSettings),
    inProgress: {
      kind: 'nothing',
    },
  }
}

export function makeModelInTextbook(textbookPage: number): Model {
  return makeModel({inTextbook: true, textbookPage})
}

export function makeModelNotInTextbook(): Model {
  return makeModel({inTextbook: false, textbookPage: null})
}

export function assignModelFrom(model: Model, exercise: Exercise & InCache & Exists) {
  model.inTextbook = exercise.attributes.textbookPage !== null
  model.textbookPage = exercise.attributes.textbookPage
  model.number = exercise.attributes.number
  model.instructions = deepCopy(exercise.attributes.instructions)
  model.wording = deepCopy(exercise.attributes.wording)
  model.example = deepCopy(exercise.attributes.example)
  model.clue = deepCopy(exercise.attributes.clue)
  model.textReference = deepCopy(exercise.attributes.textReference)
  model.rectangles = deepCopy(exercise.attributes.rectangles)
  model.adaptationSettings = makeAdaptationSettings(exercise.attributes.adaptation, defaultAdaptationSettings),
  model.inProgress = {
    kind: 'nothing',
  }
}

function resetModel(model: Model, options: MakeModelOptions) {
  Object.assign(model, makeModel(options))
}

export function resetModelInTextbook(model: Model, textbookPage: number) {
  resetModel(model, {inTextbook: true, textbookPage})
}

export function resetModelNotInTextbook(model: Model) {
  resetModel(model, {inTextbook: false, textbookPage: null})
}

export function modelIsEmpty(model: Model) {
  return true
    // model.number can be set, model is still considered empty
    && deepEqual(model.instructions, emptyDeltas)
    && deepEqual(model.wording, emptyDeltas)
    && deepEqual(model.example, emptyDeltas)
    && deepEqual(model.clue, emptyDeltas)
    && deepEqual(model.textReference, emptyDeltas)
    // model.rectangles are set only when setting another field. If they are set then the field is emptied, we do want to consider the model empty
    && deepEqual(model.adaptationSettings, defaultAdaptationSettings)
    // model.inProgress also doesn't count
}

export function cleanupModel(model: Model) {
  const hasManualItems = model.adaptationSettings.itemized.items.isManual
  const colorsCount = model.adaptationSettings.itemized.effects.isSelectable ? model.adaptationSettings.itemized.effects.selectable.colorsCount : 0
  for (const fieldName of ['instructions', 'wording', 'example'] as const) {
    const newOps = new Delta()
    for (const delta of model[fieldName]) {
      if (typeof delta.insert === 'string') {
        console.assert('attributes' in delta)
        if ('sel' in delta.attributes && (delta.attributes.sel as number) > colorsCount) {
          newOps.insert(delta.insert, {})
        } else if ('manual-item' in delta.attributes && !hasManualItems) {
          newOps.insert(delta.insert, {})
        } else {
          newOps.insert(delta.insert, delta.attributes)
        }
      } else {
        newOps.insert(delta.insert)
      }
    }
    model[fieldName] = newOps.ops.map(op => {
      console.assert(typeof op.insert === 'string')
      return {insert: op.insert, attributes: op.attributes ?? {}}
    })
  }
}

export function disableItemizedEffects(model: Model) {
  model.adaptationSettings.itemized.effects.isSelectable = false
  model.adaptationSettings.itemized.effects.isBoxed = false
  model.adaptationSettings.itemized.effects.hasMcqBeside = false
  model.adaptationSettings.itemized.effects.hasMcqBelow = false
  model.adaptationSettings.itemized.effects.hasGenderMcq = false
  model.adaptationSettings.itemized.effects.hasNumberMcq = false
  model.adaptationSettings.itemized.effects.repeatedWithMcq = false
  model.adaptationSettings.singleItemPerParagraph = false
}

export function makeItems(adaptationSettings: Model["adaptationSettings"]): Adaptation["items"] {
  const items = adaptationSettings.itemized.items
  if (items.isLetters) {
    return {kind: 'characters', letters: true}
  } else if (items.isWords || items.isPunctuation) {
    return {kind: 'tokens', words: items.isWords, punctuation: items.isPunctuation}
  } else if (items.isSentences) {
    return {kind: 'sentences'}
  } else if (items.isManual) {
    return {kind: 'manual'}
  } else if (items.isSeparated && items.separator !== '') {
    return {kind: 'separated', separator: items.separator}
  } else {
    return null
  }
}

function makeAdaptation(model: Model): Adaptation {
  const adaptationSettings = model.adaptationSettings

  const items = makeItems(adaptationSettings)
  const items_are_selectable = adaptationSettings.itemized.effects.isSelectable ? {
    colors: adaptationSettings.itemized.effects.selectable.allColors.slice(0, adaptationSettings.itemized.effects.selectable.colorsCount),
  } : null

  const adaptation = {
    kind: adaptationSettings.kind,
    wording_paragraphs_per_pagelet: adaptationSettings.wordingParagraphsPerPagelet,
    single_item_per_paragraph: adaptationSettings.singleItemPerParagraph,
    placeholder_for_fill_with_free_text: adaptationSettings.placeholderForFillWithFreeText,
    items,
    items_are_selectable,
    items_are_boxed: adaptationSettings.itemized.effects.isBoxed,
    items_have_mcq_beside: adaptationSettings.itemized.effects.hasMcqBeside,
    items_have_mcq_below: adaptationSettings.itemized.effects.hasMcqBelow,
    items_have_predefined_mcq: {
      grammatical_gender: adaptationSettings.itemized.effects.hasGenderMcq,
      grammatical_number: adaptationSettings.itemized.effects.hasNumberMcq,
    },
    items_are_repeated_with_mcq: adaptationSettings.itemized.effects.repeatedWithMcq,
    show_arrow_before_mcq_fields: adaptationSettings.showArrowBeforeMcqFields,
    show_mcq_choices_by_default: adaptationSettings.showMcqChoicesByDefault,
  }

  const remadeAdaptationSettings = makeAdaptationSettings(adaptation, adaptationSettings)
  if (!deepEqual(remadeAdaptationSettings, adaptationSettings)) {
    throw new Error(`Adaptation settings are not equal: from adaptation settings '${JSON.stringify(adaptationSettings)}', we got adaptation '${JSON.stringify(adaptation)}', but got back different adaptation settings '${JSON.stringify(remadeAdaptationSettings)}'`)
  }

  return adaptation
}

function makeAdaptationSettings(adaptation: Adaptation, baseAdaptationSettings: Model["adaptationSettings"]): Model["adaptationSettings"] {
  const allColors = deepCopy(defaultAdaptationSettings.itemized.effects.selectable.allColors)
  if (adaptation.items_are_selectable !== null) {
    allColors.splice(0, adaptation.items_are_selectable.colors.length, ...adaptation.items_are_selectable.colors)
  }

  const adaptationSettings: Model["adaptationSettings"] = {
    kind: adaptation.kind,
    wordingParagraphsPerPagelet: adaptation.wording_paragraphs_per_pagelet,
    singleItemPerParagraph: adaptation.single_item_per_paragraph,
    placeholderForFillWithFreeText: adaptation.placeholder_for_fill_with_free_text,
    showArrowBeforeMcqFields: adaptation.show_arrow_before_mcq_fields,
    showMcqChoicesByDefault: adaptation.show_mcq_choices_by_default,
    itemized: {
      items: {
        isLetters: adaptation.items !== null && adaptation.items.kind === 'characters' && adaptation.items.letters,
        isWords: adaptation.items !== null && adaptation.items.kind === 'tokens' && adaptation.items.words,
        isPunctuation: adaptation.items !== null && adaptation.items.kind === 'tokens' && adaptation.items.punctuation,
        isSentences: adaptation.items !== null && adaptation.items.kind === 'sentences',
        isManual: adaptation.items !== null && adaptation.items.kind === 'manual',
        isSeparated: adaptation.items !== null && adaptation.items.kind === 'separated',
        separator: adaptation.items !== null && adaptation.items.kind === 'separated' ? adaptation.items.separator : '',
      },
      effects: {
        isSelectable: adaptation.items_are_selectable !== null,
        selectable: {
          colorsCount: adaptation.items_are_selectable !== null ? adaptation.items_are_selectable.colors.length : defaultAdaptationSettings.itemized.effects.selectable.colorsCount,
          allColors,
        },
        isBoxed: adaptation.items_are_boxed,
        hasMcqBeside: adaptation.items_have_mcq_beside,
        hasMcqBelow: adaptation.items_have_mcq_below,
        hasGenderMcq: adaptation.items_have_predefined_mcq.grammatical_gender,
        hasNumberMcq: adaptation.items_have_predefined_mcq.grammatical_number,
        repeatedWithMcq: adaptation.items_are_repeated_with_mcq,
      }
    }
  }

  // Fix attributes that are absent (on purpose) from the adaptation
  if (adaptation.items === null) {
    adaptationSettings.itemized.items.isSeparated = baseAdaptationSettings.itemized.items.isSeparated
    adaptationSettings.itemized.items.separator = baseAdaptationSettings.itemized.items.separator
  }
  adaptationSettings.itemized.effects.selectable.allColors.splice(
    adaptationSettings.itemized.effects.selectable.colorsCount,
    adaptationSettings.itemized.effects.selectable.allColors.length - adaptationSettings.itemized.effects.selectable.colorsCount,
    ...baseAdaptationSettings.itemized.effects.selectable.allColors.slice(adaptationSettings.itemized.effects.selectable.colorsCount),
  )
  if (!adaptationSettings.itemized.effects.isSelectable) {
    adaptationSettings.itemized.effects.selectable.colorsCount = baseAdaptationSettings.itemized.effects.selectable.colorsCount
  }

  return adaptationSettings
}

export async function getParsed(model: Model) {
  const parsed = await api.client.createOne(
    'parsedExercise', {
      number: model.number,
      instructions: model.instructions,
      wording: model.wording,
      example: model.example,
      clue: model.clue,
      textReference: model.textReference,
      adaptation: makeAdaptation(model),
    },
    {},
  )
  console.assert(parsed.exists)
  return parsed
}

export async function create(project: Project, textbook: Textbook | null, model: Model) {
  return await api.client.createOne(
    'exercise',
    {
      number: model.number,
      textbookPage: model.textbookPage,
      instructions: model.instructions,
      wording: model.wording,
      example: model.example,
      clue: model.clue,
      textReference: model.textReference,
      adaptation: makeAdaptation(model),
      rectangles: model.rectangles,
    },
    {
      project,
      textbook,
    },
    {
      include: ['textbook'],
    },
  )
}

export async function save(exercise: Exercise & InCache & Exists, model: Model) {
  await exercise.patch(
    {
      instructions: model.instructions,
      wording: model.wording,
      example: model.example,
      clue: model.clue,
      textReference: model.textReference,
      adaptation: makeAdaptation(model),
      rectangles: model.rectangles,
    },
    {},
    {
      include: ['textbook'],
    },
  )
}

export function suggestNextNumber(number: string) {
  const n = parseInt(number)
  if (Number.isInteger(n)) {
    return (n + 1).toString()
  } else {
    return ''
  }
}
</script>

<script setup lang="ts">
import { ref, computed } from 'vue'
import deepCopy from 'deep-copy'

import { BRow, BCol, BLabeledInput, BLabeledNumberInput, BLabeledSelect } from '../../../../components/opinion/bootstrap'
import WysiwygEditor from '$frontend/components/WysiwygEditor.vue'
import { wysiwygBlots, wysiwygCompatibleFormats, wysiwygContagiousFormats } from './ExerciseToolsColumn.vue'
import OptionalWysiwygEditor from '$frontend/components/OptionalWysiwygEditor.vue'


defineProps<{
  fixedNumber: boolean
  displayedPage: number | null
}>()

const model = defineModel<Model>({required: true})

const instructionsEditor = ref<InstanceType<typeof WysiwygEditor> | null>(null)
const wordingEditor = ref<InstanceType<typeof WysiwygEditor> | null>(null)
const exampleEditor = ref<InstanceType<typeof OptionalWysiwygEditor> | null>(null)
const clueEditor = ref<InstanceType<typeof OptionalWysiwygEditor> | null>(null)
const textReferenceEditor = ref<InstanceType<typeof OptionalWysiwygEditor> | null>(null)
const editors = {
  instructions: instructionsEditor,
  wording: wordingEditor,
  example: exampleEditor,
  clue: clueEditor,
  textReference: textReferenceEditor,
}

const allOptionalsAreCollapsed = computed(() => {
  return !exampleEditor.value?.expanded && !clueEditor.value?.expanded && !textReferenceEditor.value?.expanded
})

const saveDisabled = computed(() => model.value.number === '')

function highlightSuffix(fieldName: TextualFieldName, suffix: string) {
  const editor = editors[fieldName].value
  console.assert(editor !== null)
  editor.focus()
  editor.setSelection(editor.getLength() - suffix.length - 1, suffix.length)
}

function toggle(format: string, value: unknown = true) {
  if (focusedWysiwygField.value !== null) {
    const editor = editors[focusedWysiwygField.value]
    console.assert(editor.value !== null)
    editor.value.toggle(format, value)
  }
}

const focusedWysiwygField = computed(() => {
  if (instructionsEditor.value?.hasFocus) {
    return 'instructions'
  } else if (wordingEditor.value?.hasFocus) {
    return 'wording'
  } else if (exampleEditor.value?.hasFocus) {
    return 'example'
  } else if (clueEditor.value?.hasFocus) {
    return 'clue'
  } else if (textReferenceEditor.value?.hasFocus) {
    return 'textReference'
  } else {
    return null
  }
})

const currentWysiwygFormat = computed(() => {
  if (instructionsEditor.value?.hasFocus) {
    return instructionsEditor.value.currentFormat
  } else if (wordingEditor.value?.hasFocus) {
    return wordingEditor.value.currentFormat
  } else if (exampleEditor.value?.hasFocus) {
    return exampleEditor.value.currentFormat
  } else if (clueEditor.value?.hasFocus) {
    return clueEditor.value.currentFormat
  } else if (textReferenceEditor.value?.hasFocus) {
    return textReferenceEditor.value.currentFormat
  } else {
    return {}
  }
})


const selBlotColors = computed(() => {
  return Object.fromEntries(model.value.adaptationSettings.itemized.effects.selectable.allColors.map((color, i) => [`--sel-blot-color-${i + 1}`, color]))
})

function selectionChangeInInstructionsOrWording(fieldName: 'instructions' | 'wording', range: {index: number, length: number}) {
  console.assert(wordingEditor.value !== null)
  console.assert(wordingEditor.value.quill !== null)
  console.assert(instructionsEditor.value !== null)
  console.assert(instructionsEditor.value.quill !== null)

  function guessSettings(deltas: Deltas, baseSettings: {mcqFieldUid: string | null}) {
    const selected = deltas.map(delta => delta.insert).join('').slice(range.index, range.index + range.length)

    const [start, stop] = (() => {
      for (const [start, stop] of [['(', ')'], ['[', ']']]) {
        if (selected.startsWith(start) && selected.endsWith(stop)) {
          return [start, stop]
        }
      }
      return ['', '']
    })()

    const separator1 = (() => {
      for (const separator of ['/', '|', ',', '*', '◆', '●', '-', '–', '—']) {
        if (selected.includes(separator)) {
          return separator
        }
      }
      for (const separator of ['ou']) {
        if (selected.includes(' ' + separator + ' ')) {
          return separator
        }
      }
      return ''
    })()

    const separator2 = (() => {
      for (const separator of ['ou']) {
        if (separator1 !== separator && selected.includes(' ' + separator + ' ')) {
          return separator
        }
      }
      return ''
    })()

    return {
      start,
      stop,
      separator1,
      separator2,
      placeholder: '',
      justCreated: true,
      ...baseSettings,
    }
  }

  if (model.value.inProgress.kind === 'multipleChoicesCreation') {
    toggle('choices2', guessSettings(model.value[fieldName], {mcqFieldUid: null}))
  } else if (model.value.inProgress.kind === 'newMcqField') {
    if (fieldName === 'wording' && range.length === 0) {
      // Add space after?
      if (![' ', '\n'].includes(wordingEditor.value.quill.getText(range.index, 1))) {
        wordingEditor.value.quill.insertText(range.index, ' ', 'user')
      }
      // wordingEditor.value.quill.insertText(range.index, model.value.inProgress.uid/*, 'mcq-placeholder', true*/, 'user')
      wordingEditor.value.quill.insertEmbed(range.index, 'mcq-field', model.value.inProgress.uid, 'user')
      // Add space before?
      if (range.index !== 0 && ![' ', '\n'].includes(wordingEditor.value.quill.getText(range.index - 1, 1))) {
        wordingEditor.value.quill.insertText(range.index, ' ', 'user')
        wordingEditor.value.quill.setSelection(range.index + 1, 0, 'silent')
      }
    } else if (fieldName === 'instructions' && range.length !== 0) {
      instructionsEditor.value.toggle('choices2', guessSettings(model.value[fieldName], {mcqFieldUid: model.value.inProgress.uid}))
    }
  }
}

function selectionChangeInInstructions(range: {index: number, length: number}) {
  selectionChangeInInstructionsOrWording('instructions', range)
}

function selectionChangeInWording(range: {index: number, length: number}) {
  selectionChangeInInstructionsOrWording('wording', range)
}

defineExpose({
  saveDisabled,
  highlightSuffix,
  toggle,
  focusedWysiwygField,
  currentWysiwygFormat,
})
</script>

<template>
  <div class="overflow-x-hidden">
    <BRow>
      <BCol>
        <BLabeledInput :label="$t('exerciseNumber')" v-model="model.number" data-cy-exercise-field="number" :disabled="fixedNumber" />
      </BCol>
      <BCol v-if="model.inTextbook">
        <BLabeledNumberInput :label="$t( model.textbookPage === displayedPage ? 'exercisePage' : 'exercisePageWithWarning')" v-model="model.textbookPage" data-cy-exercise-field="page" :disabled="fixedNumber" />
      </BCol>
    </BRow>
  </div>
  <div :style="{position: 'relative', ...selBlotColors}">
    <BLabeledSelect
      :label="$t('adaptationType')" v-model="model.adaptationSettings.kind"
      :options="adaptationKinds.map(kind => ({value: kind, label: $t(kind)}))"
    />
    <WysiwygEditor
      ref="instructionsEditor"
      :label="$t('exerciseInstructions')"
      :blots="wysiwygBlots"
      :compatibleFormats="wysiwygCompatibleFormats"
      :contagiousFormats="wysiwygContagiousFormats"
      v-model="model.instructions"
      @selectionChange="selectionChangeInInstructions"
    />
    <WysiwygEditor
      ref="wordingEditor"
      :label="$t('exerciseWording')"
      :blots="wysiwygBlots"
      :compatibleFormats="wysiwygCompatibleFormats"
      :contagiousFormats="wysiwygContagiousFormats"
      v-model="model.wording"
      @selectionChange="selectionChangeInWording"
    />
    <div :class="{'container-fluid': allOptionalsAreCollapsed}">
      <div :class="{row: allOptionalsAreCollapsed}">
        <div :class="{col: allOptionalsAreCollapsed}" style="padding: 0;">
          <OptionalWysiwygEditor
            ref="exampleEditor"
            :label="$t('exerciseExample')"
            :blots="wysiwygBlots"
            :compatibleFormats="wysiwygCompatibleFormats"
            :contagiousFormats="wysiwygContagiousFormats"
            v-model="model.example"
          />
        </div>
        <div :class="{col: allOptionalsAreCollapsed}" style="padding: 0;">
          <OptionalWysiwygEditor
            ref="clueEditor"
            :label="$t('exerciseClue')"
            :blots="wysiwygBlots"
            :compatibleFormats="wysiwygCompatibleFormats"
            :contagiousFormats="wysiwygContagiousFormats"
            v-model="model.clue"
          />
        </div>
        <div :class="{col: allOptionalsAreCollapsed}" style="padding: 0;">
          <OptionalWysiwygEditor
            ref="textReferenceEditor"
            :label="$t('exerciseTextReference')"
            :blots="wysiwygBlots"
            :compatibleFormats="wysiwygCompatibleFormats"
            :contagiousFormats="wysiwygContagiousFormats"
            v-model="model.textReference"
          />
        </div>
      </div>
    </div>

    <slot name="overlay"></slot>
  </div>
</template>
