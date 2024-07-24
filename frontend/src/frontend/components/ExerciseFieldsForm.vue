<script lang="ts">
import { nextTick } from 'vue'

import { useApiStore } from '$frontend/stores/api'
import type { Rectangle } from '$frontend/views/project/textbook/page/TextPicker.vue'
import type { Project, Textbook, Exercise, InCache, Exists, SelectThingsAdaptation, FillWithFreeTextAdaptation, MultipleChoicesInInstructionsAdaptation, MultipleChoicesInWordingAdaptation } from '$frontend/stores/api'


const api = useApiStore()

// @todo Automate updating this type when a new adaptation type is added
export const adaptationTypes = ['selectThingsAdaptation', 'fillWithFreeTextAdaptation', 'multipleChoicesInInstructionsAdaptation', 'multipleChoicesInWordingAdaptation'] as const
export type AdaptationType = '-' | typeof adaptationTypes[number]

export const textualFieldNames = ['instructions', 'wording', 'example', 'clue'] as const
export type TextualFieldName = typeof textualFieldNames[number]

export interface Selection {
  fieldName: TextualFieldName
  text: string
}

export interface Model {
  number: string
  boundingRectangle: Rectangle | null,
  adaptationType: AdaptationType
  selectThingsAdaptationOptions: {
    colors: number
    words: boolean
    punctuation: boolean
  }
  fillWithFreeTextAdaptationOptions: {
    placeholder: string
  }
  multipleChoicesInInstructionsAdaptationOptions: {
    placeholder: string
  }
  multipleChoicesInWordingAdaptationOptions: {}
  instructions: string
  wording: string
  example: string
  clue: string
}

export function makeModel(): Model {
  return {
    number: '',
    boundingRectangle: null,
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
  }
}

export function assignModelFrom(model: Model, exercise: Exercise & InCache & Exists, extractionEvents: object[]) {
  model.number = exercise.attributes.number
  model.boundingRectangle = exercise.attributes.boundingRectangle
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

  extractionEvents.splice(0, extractionEvents.length)
}

export function resetModel(model: Model, extractionEvents: object[]) {
  Object.assign(model, makeModel())

  extractionEvents.splice(0, extractionEvents.length)
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

export async function getAdapted(model: Model) {
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
  try {
    const adapted = await api.client.createOne('adaptedExercise', attributes, {})
    console.assert(adapted.exists)
    return adapted.attributes.adapted
  } catch (e) {
    console.error(e)
    return null
  }
}

export async function create(project: Project, textbook: Textbook | null, textbookPage: number | null, model: Model, extractionEvents: object[]) {
  const operations: any/* @todo Type */[] = [
    [
      'add', 'exercise', 'ex',
      {
        textbookPage,
        boundingRectangle: model.boundingRectangle,
        number: model.number,
        instructions: model.instructions,
        wording: model.wording,
        example: model.example,
        clue: model.clue,
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
  for (const event of extractionEvents) {
    operations.push([
      'add', 'extractionEvent', null,
      {event: JSON.stringify(event)},
      {exercise: {type: 'exercise', lid: 'ex'}},
    ])
  }
  const results = await api.client.batch(...operations)
  return results[0] as Exercise & InCache & Exists  // @todo Remove type assertion when batch is typed
}

export async function save(exercise: Exercise & InCache & Exists, model: Model, extractionEvents: object[]) {
  // @todo Use a *single* batch request (when batch requests support 'update' and 'delete' operations)
  await exercise.patch(
    {
      boundingRectangle: model.boundingRectangle,
      instructions: model.instructions,
      wording: model.wording,
      example: model.example,
      clue: model.clue,
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
  const operations = []
  for (const event of extractionEvents) {
    operations.push([
      'add', 'extractionEvent', null,
      {event: JSON.stringify(event)},
      {exercise},
    ])
  }
  await api.client.batch(...operations)
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

defineProps<{
  fixedNumber: boolean
  extractionEvents: object[]
}>()

const emit = defineEmits<{
  selected: [Selection]
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

const noClueNoExample = computed(() => !exampleTextArea.value?.expanded && !clueTextArea.value?.expanded)

const saveDisabled = computed(() => model.value.number === '')

const settingSelectionRange = ref(false)
function emitSelected(fieldName: TextualFieldName, e: Event) {
  if (!settingSelectionRange.value) {
    const textArea = e.target as HTMLTextAreaElement
    const text = textArea.value.substring(textArea.selectionStart, textArea.selectionEnd)
    emit('selected', {fieldName, text})
  }
  settingSelectionRange.value = false
}

function highlightSelection(fieldName: TextualFieldName, text: string, {start, end}: {start: number, end: number}) {
  console.assert(model.value[fieldName].endsWith(text))
  const textArea = textAreas[fieldName].value
  console.assert(textArea !== null)
  nextTick(() => {
    textArea.focus()
    settingSelectionRange.value = true
    textArea.setSelectionRange(start, end)
  })
}

defineExpose({
  saveDisabled,
  highlightSelection
})
</script>

<template>
  <BLabeledInput :label="$t('exerciseNumber')" v-model="model.number" :disabled="fixedNumber" @change="extractionEvents.push({kind: 'ExerciseNumberSetManually', value: model.number})" />
  <div style="position: relative">
    <BLabeledSelect
      :label="$t('adaptationType')" v-model="model.adaptationType"
      :options="['-', ...adaptationTypes.map(kind => ({value: kind, label: $t(kind)}))]"
    />
    <BLabeledTextarea
      ref="instructionsTextArea"
      :label="$t('exerciseInstructions')"
      v-model="model.instructions"
      @select="(e: Event) => emitSelected('instructions', e)"
      @change="extractionEvents.push({kind: 'InstructionsSetManually', value: model.instructions})"
    />
    <BLabeledTextarea
      ref="wordingTextArea"
      :label="$t('exerciseWording')"
      v-model="model.wording"
      @select="(e: Event) => emitSelected('wording', e)"
      @change="extractionEvents.push({kind: 'WordingSetManually', value: model.wording})"
    />
    <div :class="{'container-fluid': noClueNoExample}">
      <div :class="{row: noClueNoExample}">
        <div :class="{col: noClueNoExample}" style="padding: 0;">
          <OptionalTextarea
            ref="exampleTextArea"
            :label="$t('exerciseExample')"
            v-model="model.example"
            @select="(e: Event) => emitSelected('example', e)"
            @change="extractionEvents.push({kind: 'ExampleSetManually', value: model.example})"
          />
        </div>
        <div :class="{col: noClueNoExample}" style="padding: 0;">
          <OptionalTextarea
            ref="clueTextArea"
            :label="$t('exerciseClue')"
            v-model="model.clue"
            @select="(e: Event) => emitSelected('clue', e)"
            @change="extractionEvents.push({kind: 'ClueSetManually', value: model.clue})"
          />
        </div>
      </div>
    </div>

    <slot name="overlay"></slot>
  </div>
</template>
