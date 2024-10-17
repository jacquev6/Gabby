<script lang="ts">
import { useApiStore } from '$frontend/stores/api'
import type { Project, Textbook, Exercise, InCache, Exists, ParsedExercise } from '$frontend/stores/api'
import { defaultColors } from './AdaptationDetailsFieldsForm.vue'


const api = useApiStore()

type Adaptation = (Exercise & InCache & Exists)['attributes']['adaptation']
type PdfRectangle = (Exercise & InCache & Exists)['attributes']['rectangles'][number]

// @todo Automate updating this type when a new adaptation type is added
export const adaptationKinds = ['null', 'fill-with-free-text', 'items-and-effects-attempt-1', 'select-things', 'multiple-choices-in-instructions', 'multiple-choices-in-wording'] as const
export type AdaptationKind = typeof adaptationKinds[number]

export const textualFieldNames = ['instructions', 'wording', 'example', 'clue'] as const
export type TextualFieldName = typeof textualFieldNames[number]

export type Model = {
  inTextbook: boolean
  number: string
  textbookPage: number | null
  instructions: string
  wording: string
  example: string
  clue: string
  wordingParagraphsPerPagelet: number
  rectangles: PdfRectangle[]
  adaptationKind: AdaptationKind
  adaptations: {[Kind in AdaptationKind]: Adaptation & {kind: Kind}}
  inProgress:
    {
      kind: 'nothing'
    } | {
      kind: 'multipleChoicesCreation'
    } | {
      kind: 'multipleChoicesEdition'
      stopWatching(): void
      settings: {
        start: string
        stop: string
        separator: string
        placeholder: string
      }
    }
}

type MakeModelOptions  = {
  inTextbook: true
  textbookPage: number
} | {
  inTextbook: false
  textbookPage: null
}

function makeModel({inTextbook, textbookPage}: MakeModelOptions): Model {
  return {
    inTextbook,
    number: '',
    textbookPage,
    instructions: '',
    wording: '',
    example: '',
    clue: '',
    wordingParagraphsPerPagelet: 3,
    rectangles: [],
    adaptationKind: 'null',
    adaptations: {
      'fill-with-free-text': {
        kind: 'fill-with-free-text' as const,
        placeholder: '...',
      },
      'items-and-effects-attempt-1': {
        kind: 'items-and-effects-attempt-1' as const,
        items: {
          kind: 'words' as const,
          punctuation: false,
        },
        effects: {
          selectable: null,
          boxed: false,
        },
      },
      'null': {
        kind: 'null' as const,
      },
      'select-things': {
        kind: 'select-things' as const,
        words: true,
        punctuation: false,
        colors: [defaultColors[0]],
      },
      'multiple-choices-in-instructions': {
        kind: 'multiple-choices-in-instructions' as const,
        placeholder: '...',
      },
      'multiple-choices-in-wording': {
        kind: 'multiple-choices-in-wording' as const,
      },
    },
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
  model.number = exercise.attributes.number
  model.instructions = exercise.attributes.instructions
  model.wording = exercise.attributes.wording
  model.example = exercise.attributes.example
  model.clue = exercise.attributes.clue
  model.wordingParagraphsPerPagelet = exercise.attributes.wordingParagraphsPerPagelet
  model.adaptationKind = exercise.attributes.adaptation.kind
  model.adaptations[model.adaptationKind] = deepCopy(exercise.attributes.adaptation) as any/* @todo Fix typing issue */
  model.rectangles = deepCopy(exercise.attributes.rectangles)
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
  return model.adaptationKind === 'null' && model.instructions === '' && model.wording === '' && model.example === '' && model.clue === ''
}

export async function getParsed(model: Model) {
  const attributes = {
    number: model.number,
    // textbookPage: props.page,
    instructions: model.instructions,
    wording: model.wording,
    example: model.example,
    clue: model.clue,
    wordingParagraphsPerPagelet: model.wordingParagraphsPerPagelet,
    adaptation: model.adaptations[model.adaptationKind],
  }
  const parsed = await api.client.createOne('parsedExercise', attributes, {})
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
      wordingParagraphsPerPagelet: model.wordingParagraphsPerPagelet,
      adaptation: model.adaptations[model.adaptationKind],
      rectangles: model.rectangles,
    },
    {
      project,
      textbook,
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
      wordingParagraphsPerPagelet: model.wordingParagraphsPerPagelet,
      adaptation: model.adaptations[model.adaptationKind],
      rectangles: model.rectangles,
    },
    {},
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

import { BRow, BCol, BLabeledInput, BLabeledTextarea, BLabeledSelect } from './opinion/bootstrap'
import OptionalTextarea from './OptionalTextarea.vue'
import WysiwygEditor from './WysiwygEditor.vue'
import { wysiwygFormats } from './AdaptationDetailsFieldsForm.vue'
import OptionalWysiwygEditor from './OptionalWysiwygEditor.vue'


const props = defineProps<{
  fixedNumber: boolean
  wysiwyg: boolean
  deltas: (ParsedExercise & InCache & Exists)['attributes']['delta'] | null
  displayedPage: number | null
}>()

const model = defineModel<Model>({required: true})

const instructionsTextArea = ref<InstanceType<typeof BLabeledTextarea> | null>(null)
const wordingTextArea = ref<InstanceType<typeof BLabeledTextarea> | null>(null)
const exampleTextArea = ref<InstanceType<typeof OptionalTextarea> | null>(null)
const clueTextArea = ref<InstanceType<typeof OptionalTextarea> | null>(null)
const textAreas = {
  instructions: instructionsTextArea,
  wording: wordingTextArea,
  example: exampleTextArea,
  clue: clueTextArea,
}

const instructionsEditor = ref<InstanceType<typeof WysiwygEditor> | null>(null)
const wordingEditor = ref<InstanceType<typeof WysiwygEditor> | null>(null)
const exampleEditor = ref<InstanceType<typeof OptionalWysiwygEditor> | null>(null)
const clueEditor = ref<InstanceType<typeof OptionalWysiwygEditor> | null>(null)
const editors = {
  instructions: instructionsEditor,
  wording: wordingEditor,
  example: exampleEditor,
  clue: clueEditor,
}

const noClueNoExample = computed(() => {
  if (props.wysiwyg) {
    return !exampleEditor.value?.expanded && !clueEditor.value?.expanded
  } else {
    return !exampleTextArea.value?.expanded && !clueTextArea.value?.expanded
  }
})

const saveDisabled = computed(() => model.value.number === '')

function highlightSuffix(fieldName: TextualFieldName, suffix: string) {
  const text = model.value[fieldName]
  console.assert(text.endsWith(suffix))
  if (props.wysiwyg) {
    const editor = editors[fieldName].value
    console.assert(editor !== null)
    editor.focus()
    editor.setSelection(editor.getLength() - suffix.length - 1, suffix.length)
  } else {
    const textArea = textAreas[fieldName].value
    console.assert(textArea !== null)
    textArea.focus()
    textArea.setSelectionRange(text.length - suffix.length, text.length)
  }
}

function toggle(format: string, value: unknown = true) {
  if (focusedWysiwygField.value !== null) {
    const editor = editors[focusedWysiwygField.value]
    console.assert(editor.value !== null)
    editor.value.toggle(format, value)
  }
}

const focusedWysiwygField = computed(() => {
  if (props.wysiwyg) {
    if (instructionsEditor.value?.hasFocus) {
      return 'instructions'
    } else if (wordingEditor.value?.hasFocus) {
      return 'wording'
    } else if (exampleEditor.value?.hasFocus) {
      return 'example'
    } else if (clueEditor.value?.hasFocus) {
      return 'clue'
    } else {
      return null
    }
  } else {
    return null
  }
})

const currentWysiwygFormat = computed(() => {
  if (props.wysiwyg) {
    if (instructionsEditor.value?.hasFocus) {
      return instructionsEditor.value.currentFormat
    } else if (wordingEditor.value?.hasFocus) {
      return wordingEditor.value.currentFormat
    } else if (exampleEditor.value?.hasFocus) {
      return exampleEditor.value.currentFormat
    } else if (clueEditor.value?.hasFocus) {
      return clueEditor.value.currentFormat
    } else {
      return {}
    }
  } else {
    return {}
  }
})

const instructionsDeltas = computed(() => props.deltas === null ? [] : props.deltas.instructions)
const wordingDeltas = computed(() => props.deltas === null ? [] : props.deltas.wording)
const exampleDeltas = computed(() => props.deltas === null ? [] : props.deltas.example)
const clueDeltas = computed(() => props.deltas === null ? [] : props.deltas.clue)


const selBlotColors = computed(() => {
  const adaptation = model.value.adaptations[model.value.adaptationKind]
  if (adaptation.kind === 'select-things') {
    return Object.fromEntries(adaptation.colors.map((color, i) => [`--sel-blot-color-${i + 1}`, color]))
  } else if (adaptation.kind === 'items-and-effects-attempt-1' && adaptation.effects.selectable !== null) {
    return Object.fromEntries(adaptation.effects.selectable.colors.map((color, i) => [`--sel-blot-color-${i + 1}`, color]))
  } else {
    return {}
  }
})

function selectionChangeInWording(_range: {index: number, length: number}) {
  if (model.value.inProgress.kind === 'multipleChoicesCreation') {
    // @todo Automatically detect these settings. How? Ask client for spec.
    const settings = {
      start: '(',
      stop: ')',
      separator: '/',
      placeholder: '',
      justCreated: true,
    }

    toggle('choices2', settings)
  }
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
        <!-- @todo Add warning icon when different from displayed page -->
        <BLabeledInput :label="$t( model.textbookPage === displayedPage ? 'exercisePage' : 'exercisePageWithWarning')" v-model="model.textbookPage" data-cy-exercise-field="page" :disabled="fixedNumber" />
      </BCol>
    </BRow>
  </div>
  <div :style="{position: 'relative', ...selBlotColors}">
    <BLabeledSelect
      :label="$t('adaptationType')" v-model="model.adaptationKind"
      :options="adaptationKinds.map(kind => ({value: kind, label: $t(kind)}))"
    />
    <WysiwygEditor
      v-if="wysiwyg"
      ref="instructionsEditor"
      :label="$t('exerciseInstructions')"
      :formats="wysiwygFormats[model.adaptationKind].instructions"
      v-model="model.instructions" :delta="instructionsDeltas"
    />
    <BLabeledTextarea
      v-else
      ref="instructionsTextArea"
      :label="$t('exerciseInstructions')"
      v-model="model.instructions"
      data-cy-exercise-field="instructions"
    />
    <WysiwygEditor
      v-if="wysiwyg"
      ref="wordingEditor"
      :label="$t('exerciseWording')"
      :formats="wysiwygFormats[model.adaptationKind].wording"
      v-model="model.wording" :delta="wordingDeltas"
      @selectionChange="selectionChangeInWording"
    />
    <BLabeledTextarea
      v-else
      ref="wordingTextArea"
      :label="$t('exerciseWording')"
      v-model="model.wording"
    />
    <div :class="{'container-fluid': noClueNoExample}">
      <div :class="{row: noClueNoExample}">
        <div :class="{col: noClueNoExample}" style="padding: 0;">
          <OptionalWysiwygEditor
            v-if="wysiwyg"
            ref="exampleEditor"
            :label="$t('exerciseExample')"
            :formats="wysiwygFormats[model.adaptationKind].example"
            :delta="exampleDeltas"
            v-model="model.example"
          />
          <OptionalTextarea
            v-else
            ref="exampleTextArea"
            :label="$t('exerciseExample')"
            v-model="model.example"
          />
        </div>
        <div :class="{col: noClueNoExample}" style="padding: 0;">
          <OptionalWysiwygEditor
            v-if="wysiwyg"
            ref="clueEditor"
            :label="$t('exerciseClue')"
            :formats="wysiwygFormats[model.adaptationKind].clue"
            :delta="clueDeltas"
            v-model="model.clue"
          />
          <OptionalTextarea
            v-else
            ref="clueTextArea"
            :label="$t('exerciseClue')"
            v-model="model.clue"
          />
        </div>
      </div>
    </div>

    <slot name="overlay"></slot>
  </div>
</template>
