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

export interface Selection {
  fieldName: TextualFieldName
  text: string
}

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
import WysiwygInstructionsEditor from './WysiwygInstructionsEditor.vue'


const props = defineProps<{
  fixedNumber: boolean
  wysiwyg: boolean
  deltas: (ParsedExercise & InCache & Exists)['attributes']['delta'] | null
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

const instructionsEditor = ref<InstanceType<typeof WysiwygInstructionsEditor> | null>(null)

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

function highlightSuffix(fieldName: TextualFieldName, suffix: string) {
  const text = model.value[fieldName]
  console.assert(text.endsWith(suffix))
  const textArea = textAreas[fieldName].value
  if(textArea === null) {
    if (fieldName === 'instructions' && props.wysiwyg) {
      console.assert(instructionsEditor.value !== null)
      instructionsEditor.value.focus()
      settingSelectionRange.value = true
      instructionsEditor.value.setSelection(instructionsEditor.value.getLength() - suffix.length - 1, suffix.length)
    }
  } else {
    textArea.focus()
    settingSelectionRange.value = true
    textArea.setSelectionRange(text.length - suffix.length, text.length)
  }
}

function toggle(format: string) {
  if (instructionsEditor.value !== null) {
    instructionsEditor.value.toggle(format)
  }
}

const wysiwygInstructionsHasFocus = computed(() => instructionsEditor.value?.hasFocus ?? false)

defineExpose({
  saveDisabled,
  highlightSuffix,
  toggle,
  wysiwygInstructionsHasFocus,
})
</script>

<template>
  <BLabeledInput :label="$t('exerciseNumber')" v-model="model.number" :disabled="fixedNumber" />
  <div style="position: relative">
    <BLabeledSelect
      :label="$t('adaptationType')" v-model="model.adaptationType"
      :options="['-', ...adaptationTypes.map(kind => ({value: kind, label: $t(kind)}))]"
    />
    <template v-if="wysiwyg && model.adaptationType === 'multipleChoicesInInstructionsAdaptation'">
      <div class="mb-3">
        <label class="form-label" @click="instructionsEditor?.focus()">{{ $t('exerciseInstructions') }}</label>
        <WysiwygInstructionsEditor ref="instructionsEditor" v-model="model.instructions" :delta="deltas === null ? [] : deltas.instructions" />
      </div>
    </template>
    <BLabeledTextarea
      v-else
      ref="instructionsTextArea"
      :label="$t('exerciseInstructions')"
      v-model="model.instructions"
      @select="(e: Event) => emitSelected('instructions', e)"
    />
    <BLabeledTextarea
      ref="wordingTextArea"
      :label="$t('exerciseWording')"
      v-model="model.wording"
      @select="(e: Event) => emitSelected('wording', e)"
    />
    <div :class="{'container-fluid': noClueNoExample}">
      <div :class="{row: noClueNoExample}">
        <div :class="{col: noClueNoExample}" style="padding: 0;">
          <OptionalTextarea
            ref="exampleTextArea"
            :label="$t('exerciseExample')"
            v-model="model.example"
            @select="(e: Event) => emitSelected('example', e)"
          />
        </div>
        <div :class="{col: noClueNoExample}" style="padding: 0;">
          <OptionalTextarea
            ref="clueTextArea"
            :label="$t('exerciseClue')"
            v-model="model.clue"
            @select="(e: Event) => emitSelected('clue', e)"
          />
        </div>
      </div>
    </div>

    <slot name="overlay"></slot>
  </div>
</template>
