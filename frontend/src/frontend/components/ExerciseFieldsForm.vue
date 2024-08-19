<script lang="ts">
import { useApiStore } from '$frontend/stores/api'
import type { Project, Textbook, Exercise, InCache, Exists, SelectThingsAdaptation, FillWithFreeTextAdaptation, MultipleChoicesInInstructionsAdaptation, MultipleChoicesInWordingAdaptation, ParsedExercise } from '$frontend/stores/api'
import type { SelectThingsAdaptationOptions, FillWithFreeTextAdaptationOptions, MultipleChoicesInInstructionsAdaptationOptions, MultipleChoicesInWordingAdaptationOptions, PdfRectangle } from '$frontend/stores/api'


const api = useApiStore()

// @todo Automate updating this type when a new adaptation type is added
export const adaptationTypes = ['selectThingsAdaptation', 'fillWithFreeTextAdaptation', 'multipleChoicesInInstructionsAdaptation', 'multipleChoicesInWordingAdaptation'] as const
export type AdaptationType = '-' | typeof adaptationTypes[number]

export const textualFieldNames = ['instructions', 'wording', 'example', 'clue'] as const
export type TextualFieldName = typeof textualFieldNames[number]

export interface Model {
  number: string
  adaptationType: AdaptationType
  selectThingsAdaptationOptions: SelectThingsAdaptationOptions
  fillWithFreeTextAdaptationOptions: FillWithFreeTextAdaptationOptions
  multipleChoicesInInstructionsAdaptationOptions: MultipleChoicesInInstructionsAdaptationOptions
  multipleChoicesInWordingAdaptationOptions: MultipleChoicesInWordingAdaptationOptions
  instructions: string
  wording: string
  example: string
  clue: string
  rectangles: PdfRectangle[]
}

export function makeModel(): Model {
  return {
    number: '',
    adaptationType: '-',
    selectThingsAdaptationOptions: {
      colors: 1,
      words: true,
      punctuation: false,
    },
    fillWithFreeTextAdaptationOptions: {
      placeholder: '...',
    },
    multipleChoicesInInstructionsAdaptationOptions: {
      placeholder: '...',
    },
    multipleChoicesInWordingAdaptationOptions: {},
    instructions: '',
    wording: '',
    example: '',
    clue: '',
    rectangles: [],
  }
}

export function assignModelFrom(model: Model, exercise: Exercise & InCache & Exists) {
  model.number = exercise.attributes.number
  model.adaptationType = exercise.relationships.adaptation === null ? '-' : exercise.relationships.adaptation.type
  if (exercise.relationships.adaptation !== null && exercise.relationships.adaptation.inCache && exercise.relationships.adaptation.exists) {
    switch (exercise.relationships.adaptation.type) {
      case 'selectThingsAdaptation':
        {
          const options = (exercise.relationships.adaptation as SelectThingsAdaptation & InCache & Exists).attributes
          model.selectThingsAdaptationOptions.colors = options.colors
          model.selectThingsAdaptationOptions.words = options.words
          model.selectThingsAdaptationOptions.punctuation = options.punctuation
        }
        break
      case 'fillWithFreeTextAdaptation':
        {
          const options = (exercise.relationships.adaptation as FillWithFreeTextAdaptation & InCache & Exists).attributes
          model.fillWithFreeTextAdaptationOptions.placeholder = options.placeholder
        }
        break
      case 'multipleChoicesInInstructionsAdaptation':
        {
          const options = (exercise.relationships.adaptation as MultipleChoicesInInstructionsAdaptation & InCache & Exists).attributes
          model.multipleChoicesInInstructionsAdaptationOptions.placeholder = options.placeholder
        }
        break
      case 'multipleChoicesInWordingAdaptation':
        {
          /* const options = */ (exercise.relationships.adaptation as MultipleChoicesInWordingAdaptation & InCache & Exists).attributes
          // Nothing to do
        }
        break
      default:
        ((t: never) => console.assert(false, t))(exercise.relationships.adaptation.type)
    }
  }
  model.instructions = exercise.attributes.instructions
  model.wording = exercise.attributes.wording
  model.example = exercise.attributes.example
  model.clue = exercise.attributes.clue
  model.rectangles = exercise.attributes.rectangles
}

export function resetModel(model: Model) {
  Object.assign(model, makeModel())
}

export function getAdaptationOptions(model: Model) {
  switch (model.adaptationType) {
    case '-':
      return {}
    case 'selectThingsAdaptation':
      return model.selectThingsAdaptationOptions
    case 'fillWithFreeTextAdaptation':
      return model.fillWithFreeTextAdaptationOptions
    case 'multipleChoicesInInstructionsAdaptation':
      return model.multipleChoicesInInstructionsAdaptationOptions
    case 'multipleChoicesInWordingAdaptation':
      return model.multipleChoicesInWordingAdaptationOptions
    default:
      ((t: never) => console.assert(false, t))(model.adaptationType)
      return null as never
  }
}

export async function getParsed(model: Model) {
  const attributes = {
    number: model.number,
    // textbookPage: props.page,
    instructions: model.instructions,
    wording: model.wording,
    example: model.example,
    clue: model.clue,
    type: model.adaptationType,
    adaptationOptions: getAdaptationOptions(model),
  }
  const parsed = await api.client.createOne('parsedExercise', attributes, {})
  console.assert(parsed.exists)
  return parsed
}

export async function create(project: Project, textbook: Textbook | null, textbookPage: number | null, model: Model) {
  const operations: any/* @todo Type */[] = [
    [
      'add', 'exercise', 'ex',
      {
        textbookPage,
        number: model.number,
        instructions: model.instructions,
        wording: model.wording,
        example: model.example,
        clue: model.clue,
        rectangles: model.rectangles,
      },
      {
        project,
        textbook,
      },
    ],
  ]
  if (model.adaptationType !== '-') {
    operations.push([
      'add', model.adaptationType, null,
      getAdaptationOptions(model),
      {exercise: {type: 'exercise', lid: 'ex'}},
    ])
  }
  const results = await api.client.batch(...operations)
  return results[0] as Exercise & InCache & Exists  // @todo Remove type assertion when batch is typed
}

export async function save(exercise: Exercise & InCache & Exists, model: Model) {
  // @todo Use a *single* batch request (when batch requests support 'update' and 'delete' operations)
  await exercise.patch(
    {
      instructions: model.instructions,
      wording: model.wording,
      example: model.example,
      clue: model.clue,
      rectangles: model.rectangles,
    },
    {},
  )
  if (model.adaptationType === '-') {
    if (exercise.relationships.adaptation !== null) {
      await exercise.relationships.adaptation.delete()
    }
  } else {
    await api.client.createOne(
      model.adaptationType,
      getAdaptationOptions(model),
      {exercise},
    )
  }
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

import { BLabeledInput, BLabeledTextarea, BLabeledSelect } from './opinion/bootstrap'
import OptionalTextarea from './OptionalTextarea.vue'
import WysiwygEditor from './WysiwygEditor.vue'
import { instructionsFormats, basicFormats } from './WysiwygEditor.vue'
import OptionalWysiwygEditor from './OptionalWysiwygEditor.vue'


const props = defineProps<{
  fixedNumber: boolean
  wysiwyg: boolean
  deltas: (ParsedExercise & InCache & Exists)['attributes']['delta'] | null
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

const actuallyWysiwyg = computed(() => props.wysiwyg && model.value.adaptationType === 'multipleChoicesInInstructionsAdaptation')

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
  if (actuallyWysiwyg.value) {
    return !exampleEditor.value?.expanded && !clueEditor.value?.expanded
  } else {
    return !exampleTextArea.value?.expanded && !clueTextArea.value?.expanded
  }
})

const saveDisabled = computed(() => model.value.number === '')

function highlightSuffix(fieldName: TextualFieldName, suffix: string) {
  const text = model.value[fieldName]
  console.assert(text.endsWith(suffix))
  if (actuallyWysiwyg.value) {
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

function toggle(format: string) {
  if (focusedWysiwygField.value !== null) {
    const editor = editors[focusedWysiwygField.value]
    console.assert(editor.value !== null)
    editor.value.toggle(format)
  }
}

const focusedWysiwygField = computed(() => {
  if (actuallyWysiwyg.value) {
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

defineExpose({
  saveDisabled,
  highlightSuffix,
  toggle,
  focusedWysiwygField,
})
</script>

<template>
  <BLabeledInput :label="$t('exerciseNumber')" v-model="model.number" :disabled="fixedNumber" />
  <div style="position: relative">
    <BLabeledSelect
      :label="$t('adaptationType')" v-model="model.adaptationType"
      :options="['-', ...adaptationTypes.map(kind => ({value: kind, label: $t(kind)}))]"
    />
    <WysiwygEditor
      v-if="actuallyWysiwyg"
      ref="instructionsEditor"
      :label="$t('exerciseInstructions')"
      :formats="instructionsFormats"
      v-model="model.instructions" :delta="deltas === null ? [] : deltas.instructions"
    />
    <BLabeledTextarea
      v-else
      ref="instructionsTextArea"
      :label="$t('exerciseInstructions')"
      v-model="model.instructions"
    />
    <WysiwygEditor
      v-if="actuallyWysiwyg"
      ref="wordingEditor"
      :label="$t('exerciseWording')"
      :formats="basicFormats"
      v-model="model.wording" :delta="deltas === null ? [] : deltas.wording"
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
            v-if="actuallyWysiwyg"
            ref="exampleEditor"
            :label="$t('exerciseExample')"
            :formats="basicFormats"
            :delta="deltas === null ? [] : deltas.example"
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
            v-if="actuallyWysiwyg"
            ref="clueEditor"
            :label="$t('exerciseClue')"
            :formats="basicFormats"
            :delta="deltas === null ? [] : deltas.clue"
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
