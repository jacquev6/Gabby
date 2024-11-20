<script lang="ts">
import { useApiStore } from '$frontend/stores/api'
import type { Project, Textbook, Exercise, InCache, Exists, ParsedExercise } from '$frontend/stores/api'
import deepEqual from 'deep-equal'


const api = useApiStore()

type Adaptation = (Exercise & InCache & Exists)['attributes']['adaptation']
type PdfRectangle = (Exercise & InCache & Exists)['attributes']['rectangles'][number]

export const adaptationKinds: Adaptation['kind'][] = ['generic', 'fill-with-free-text', 'multiple-choices']

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
  adaptation: Adaptation
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
    instructions: '\n',
    wording: '\n',
    example: '\n',
    clue: '\n',
    wordingParagraphsPerPagelet: 3,
    rectangles: [],
    adaptation: {kind: 'generic', effects: []},
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
  model.adaptation = deepCopy(exercise.attributes.adaptation)
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
  return  model.instructions === '\n'
    && model.wording === '\n'
    && model.example === '\n'
    && model.clue === '\n'
    && deepEqual(model.adaptation, {kind: 'generic', effects: []})
}

export async function getParsed(model: Model) {
  const parsed = await api.client.createOne(
    'parsedExercise', {
      number: model.number,
      instructions: model.instructions,
      wording: model.wording,
      example: model.example,
      clue: model.clue,
      wordingParagraphsPerPagelet: model.wordingParagraphsPerPagelet,
      adaptation: model.adaptation,
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
      wordingParagraphsPerPagelet: model.wordingParagraphsPerPagelet,
      adaptation: model.adaptation,
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
      adaptation: model.adaptation,
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
import { useI18n } from 'vue-i18n'

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

const i18n = useI18n()

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

const instructionsDeltas = computed(() => props.deltas === null ? [{insert: '\n', attributes: {}}] : props.deltas.instructions)
const wordingDeltas = computed(() => props.deltas === null ? [{insert: '\n', attributes: {}}] : props.deltas.wording)
const exampleDeltas = computed(() => props.deltas === null ? [{insert: '\n', attributes: {}}] : props.deltas.example)
const clueDeltas = computed(() => props.deltas === null ? [{insert: '\n', attributes: {}}] : props.deltas.clue)


const selBlotColors = computed(() => {
  const selectableEffects = model.value.adaptation.effects.filter(effect => effect.kind === 'itemized' && effect.effects.selectable !== null)
  console.assert(selectableEffects.length <= 1)
  if (selectableEffects.length === 0) {
    return {}
  } else {
    const effect = selectableEffects[0]
    console.assert(effect.kind === 'itemized')
    console.assert(effect.effects.selectable !== null)
    return Object.fromEntries(effect.effects.selectable.colors.map((color, i) => [`--sel-blot-color-${i + 1}`, color]))
  }
})

function selectionChangeInInstructionsOrWording(_range: {index: number, length: number}) {
  if (model.value.inProgress.kind === 'multipleChoicesCreation') {
    // @todo Automatically detect these settings. How? Ask client for spec.
    const settings = {
      start: '(',
      stop: ')',
      separator1: '/',
      separator2: i18n.t('multipleChoicesSeparator2'),
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
      :label="$t('adaptationType')" v-model="model.adaptation.kind"
      :options="adaptationKinds.map(kind => ({value: kind, label: $t(kind)}))"
    />
    <WysiwygEditor
      v-if="wysiwyg"
      ref="instructionsEditor"
      :label="$t('exerciseInstructions')"
      :formats="wysiwygFormats"
      v-model="model.instructions" :delta="instructionsDeltas"
      @selectionChange="selectionChangeInInstructionsOrWording"
    />
    <BLabeledTextarea
      v-else
      ref="instructionsTextArea"
      :label="$t('exerciseInstructions')"
      :enforceTrailingLineEnd="true"
      v-model="model.instructions"
      data-cy-exercise-field="instructions"
    />
    <WysiwygEditor
      v-if="wysiwyg"
      ref="wordingEditor"
      :label="$t('exerciseWording')"
      :formats="wysiwygFormats"
      v-model="model.wording" :delta="wordingDeltas"
      @selectionChange="selectionChangeInInstructionsOrWording"
    />
    <BLabeledTextarea
      v-else
      ref="wordingTextArea"
      :label="$t('exerciseWording')"
      :enforceTrailingLineEnd="true"
      v-model="model.wording"
    />
    <div :class="{'container-fluid': noClueNoExample}">
      <div :class="{row: noClueNoExample}">
        <div :class="{col: noClueNoExample}" style="padding: 0;">
          <OptionalWysiwygEditor
            v-if="wysiwyg"
            ref="exampleEditor"
            :label="$t('exerciseExample')"
            :formats="wysiwygFormats"
            :delta="exampleDeltas"
            v-model="model.example"
          />
          <OptionalTextarea
            v-else
            ref="exampleTextArea"
            :label="$t('exerciseExample')"
            :enforceTrailingLineEnd="true"
            v-model="model.example"
          />
        </div>
        <div :class="{col: noClueNoExample}" style="padding: 0;">
          <OptionalWysiwygEditor
            v-if="wysiwyg"
            ref="clueEditor"
            :label="$t('exerciseClue')"
            :formats="wysiwygFormats"
            :delta="clueDeltas"
            v-model="model.clue"
          />
          <OptionalTextarea
            v-else
            ref="clueTextArea"
            :label="$t('exerciseClue')"
            :enforceTrailingLineEnd="true"
            v-model="model.clue"
          />
        </div>
      </div>
    </div>

    <slot name="overlay"></slot>
  </div>
</template>
