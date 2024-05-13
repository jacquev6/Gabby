<script setup lang="ts">
import { ref, reactive, computed, watch } from 'vue'
import { computedAsync } from '@vueuse/core'
import { nextTick } from 'vue'

import { BBusy, BLabeledInput, BLabeledTextarea, BButton, BSelect } from './opinion/bootstrap'
import TextSelectionMenu from './ExerciseFormTextSelectionMenu.vue'
import OptionalTextarea from './OptionalTextarea.vue'
import { useApiStore } from '$frontend/stores/api'
import adaptationOptionsForms from './adaptation-options-forms'
import type { Project, Textbook, Section, Exercise, AdaptedExercise } from '$frontend/types/api'


const props = defineProps<{
  project: Project,
  textbook: Textbook | null,
  textbookPage: number | null,
  section: Section | null,
  pdf: {page: {pageNumber: number}} | null,
  number: string,
  automaticNumber: boolean,
  editMode: boolean,
  exercise?: Exercise,
}>()

const emit = defineEmits<{
  created: [exercise: Exercise, suggestedNextExerciseNumber: string],
  saved: [],
}>()

const api = useApiStore()

var extractionEvents: object[] = []
const number = ref('')
const boundingRectangle = ref<object | null>(null)
const needsBoundingRectangle = computed(() => {
  if (props.textbook !== null && props.pdf !== null && !props.editMode) {
    return boundingRectangle.value === null
  } else {
    return false
  }
})
const instructions = ref('')
const wording = ref('')
const example = ref('')
const clue = ref('')
const fields = {
  instructions,
  wording,
  example,
  clue,
}

type AdaptationType = '-' | keyof typeof adaptationOptionsForms
const adaptationType = ref<AdaptationType>('-')
const adaptationOptions = reactive<{[key: string]: object}>({})
function resetAdaptationOptions() {
  adaptationType.value = '-'
  adaptationOptions['-'] = {}
  for (const [kind, component] of Object.entries(adaptationOptionsForms)) {
    adaptationOptions[kind] = Object.assign({}, component.props.modelValue.default)
  }
}
resetAdaptationOptions()

const alreadyExists = computedAsync(
  async () => {
    if (props.editMode) {
      return true
    } else if (number.value === '') {
      return false
    } else if (props.textbook !== null) {
      console.assert(props.textbookPage !== null)
      const exercises = await api.client.getAll(
        'exercises',
        {
          filter: {
            textbook: props.textbook.id,
            textbookPage: props.textbookPage.toString(),
            number: number.value,
          }
        },
      )
      console.assert(exercises.length <= 1)
      return exercises.length === 1
    } else {
      // @todo Detect duplicate independent exercise
      return false
    }
  },
  false,
)

watch(
  [() => props.number, () => props.automaticNumber],
  () => {
    number.value = props.number
    if (props.automaticNumber) {
      extractionEvents.push({kind: 'ExerciseNumberSetAutomatically', value: number.value})
    }
  },
  {immediate: true},
)
watch(
  () => props.exercise,
  () => {
    if (props.exercise !== undefined) {
      console.assert(props.exercise.attributes !== undefined)
      console.assert(props.exercise.relationships !== undefined)

      boundingRectangle.value = props.exercise.attributes.boundingRectangle ?? null

      instructions.value = props.exercise.attributes.instructions ?? ''
      wording.value = props.exercise.attributes.wording ?? ''
      example.value = props.exercise.attributes.example ?? ''
      clue.value = props.exercise.attributes.clue ?? ''

      if (props.exercise.relationships.adaptation === null) {
        adaptationType.value = '-'
      } else {
        adaptationType.value = props.exercise.relationships.adaptation.type as AdaptationType
        Object.assign(adaptationOptions[adaptationType.value], props.exercise.relationships.adaptation.attributes)
      }
    }
  },
  {immediate: true},
)

const disabled = computed(() => (!props.editMode && alreadyExists.value) || !number.value)
const busy = ref(false)

const showTextSelectionMenu = ref(false)
const selectedText = ref('')
const selectedRectangle = ref<object | null>(null)
const selectedTextReference = ref<{x: number, y: number}>({x: 0, y: 0})
function textSelected(text: string, point: {clientX: number, clientY: number}, textItems: [], rectangle: object) {
  console.assert(props.section?.relationships?.pdfFile.relationships?.namings[0].attributes !== undefined)
  console.assert(props.pdf !== null)

  if (needsBoundingRectangle.value) {
    extractionEvents.push({
      kind: "BoundingRectangleSelectedInPdf",
      pdf: {
        name: props.section.relationships.pdfFile.relationships.namings[0].attributes.name,
        sha256: props.section.relationships.pdfFile.id,
        page: props.pdf.page.pageNumber,
        rectangle,
      },
    })
    boundingRectangle.value = rectangle
  } else {
    extractionEvents.push({
      kind: "TextSelectedInPdf",
      pdf: {
        name: props.section.relationships.pdfFile.relationships.namings[0].attributes.name,
        sha256: props.section.relationships.pdfFile.id,
        page: props.pdf.page.pageNumber,
        rectangle,
      },
      value: text,
      textItems,
    })
    selectedText.value = text
    selectedRectangle.value = rectangle
    selectedTextReference.value = {x: point.clientX, y: point.clientY}
    showTextSelectionMenu.value = true
  }
}

const instructionsTextArea = ref<typeof BLabeledTextarea | null>(null)
const wordingTextArea = ref<typeof BLabeledTextarea | null>(null)
const exampleTextArea = ref<typeof OptionalTextarea | null>(null)
const clueTextArea = ref<typeof OptionalTextarea | null>(null)
const textAreas = {
  instructions: instructionsTextArea,
  wording: wordingTextArea,
  example: exampleTextArea,
  clue: clueTextArea,
}

const noClueNoExample = computed(() => !exampleTextArea.value?.expanded && !clueTextArea.value?.expanded)

function addTextTo(fieldName: 'instructions' | 'wording' | 'example' | 'clue', text: string) {
  const field = fields[fieldName]
  const textArea = textAreas[fieldName].value
  console.assert(textArea !== null)
  const valueBefore = field.value
  if (field.value !== '' && !field.value.endsWith('\n')) {
    field.value += '\n'
  }
  const selectionBegin = field.value.length
  const selectionEnd = selectionBegin + text.length
  field.value += text
  nextTick(() => {
    textArea.focus()
    textArea.setSelectionRange(selectionBegin, selectionEnd)
  })
  extractionEvents.push({kind: `SelectedTextAddedTo${fieldName.charAt(0).toUpperCase()}${fieldName.slice(1)}`, valueBefore, valueAfter: field.value})
}

function skip() {
  boundingRectangle.value = null
  extractionEvents = []
  number.value = tryIncrement(number.value)
  instructions.value = ''
  wording.value = ''
  example.value = ''
  clue.value = ''

  resetAdaptationOptions()
}

async function create() {
  busy.value = true

  // @todo Use a batch request
  const exercise = await api.client.post<Exercise>(
    'exercise',
    {
      textbookPage: props.textbookPage,
      boundingRectangle: boundingRectangle.value,
      number: number.value,
      instructions: instructions.value,
      wording: wording.value,
      example: example.value,
      clue: clue.value,
    },
    {
      project: props.project,
      textbook: props.textbook,
    },
  )
  if (adaptationType.value !== '-') {
    await api.client.post(
      adaptationType.value,
      adaptationOptions[adaptationType.value],
      {exercise: {type: 'exercise', id: exercise.id}},
    )
  }
  for (const event of extractionEvents) {
    await api.client.post(
      'extractionEvent',
      {event: JSON.stringify(event)},
      {exercise: {type: 'exercise', id: exercise.id}},
    )
  }

  boundingRectangle.value = null
  extractionEvents = []
  number.value = ''
  instructions.value = ''
  wording.value = ''
  example.value = ''
  clue.value = ''

  resetAdaptationOptions()

  busy.value = false

  emit('created', exercise, tryIncrement(exercise.attributes.number))
}

function tryIncrement(s: string) {
  const n = parseInt(s)
  if (Number.isInteger(n)) {
    return (n + 1).toString()
  } else {
    return ''
  }
}

async function save() {
  console.assert(props.exercise?.relationships !== undefined)

  busy.value = true

  // @todo Use a batch request
  await api.client.patch(
    'exercise',
    props.exercise.id,
    {
      boundingRectangle: boundingRectangle.value,
      instructions: instructions.value,
      wording: wording.value,
      example: example.value,
      clue: clue.value,
    },
    {},
  )
  if (adaptationType.value === '-') {
    if (props.exercise.relationships.adaptation !== null) {
      await api.client.delete(props.exercise.relationships.adaptation.type, props.exercise.relationships.adaptation.id)
    }
  } else {
    await api.client.post(
      adaptationType.value,
      adaptationOptions[adaptationType.value],
      {exercise: {type: 'exercise', id: props.exercise.id}},
    )
  }
  for (const event of extractionEvents) {
    await api.client.post(
      'extractionEvent',
      {event: JSON.stringify(event)},
      {exercise: {type: 'exercise', id: props.exercise.id}},
    )
  }

  extractionEvents = []

  busy.value = false

  emit('saved')
}

const adaptedDataLoading = ref(false)
const adaptedData = computedAsync(
  async () => {
    if (adaptationType.value === '-') {
      return null
    } else {
      const attributes = {
        number: number.value,
        textbookPage: props.textbookPage,
        instructions: instructions.value,
        wording: wording.value,
        type: adaptationType.value,
        adaptationOptions: adaptationOptions[adaptationType.value],
      }
      try {
        const adapted = await api.client.post<AdaptedExercise>('adaptedExercise', attributes, {})
        return adapted.attributes.adapted
      } catch (e) {
        console.error(e)
        return null
      }
    }
  },
  null,
  adaptedDataLoading,
)

const highlightedRectangles = computed(() => {
  if (boundingRectangle.value) {
    return [boundingRectangle.value]
  } else {
    return null
  }
})

defineExpose({
  textSelected: computed(() => !props.editMode && alreadyExists.value ? null : textSelected),
  adaptedData, adaptedDataLoading,
  highlightedRectangles,
})
</script>

<template>
  <TextSelectionMenu
    v-model:show="showTextSelectionMenu"
    :number
    :text="selectedText"
    :reference="selectedTextReference"
    @extractionEvent="event => extractionEvents.push(event)"
  >
    <template v-slot="{textToAdd, hide}">
      <p><BButton secondary @click="boundingRectangle = selectedRectangle; hide()">{{ $t('setBoundingRect') }}</BButton></p>
      <p>{{ $t('addTo') }}</p>
      <p>
        <BButton primary @click="addTextTo('instructions', textToAdd); hide()">{{ $t('instructions') }}</BButton>
        <BButton primary @click="addTextTo('wording', textToAdd); hide()">{{ $t('wording') }}</BButton>
        <BButton primary @click="addTextTo('example', textToAdd); hide()">{{ $t('example') }}</BButton>
        <BButton primary @click="addTextTo('clue', textToAdd); hide()">{{ $t('clue') }}</BButton>
      </p>
    </template>
  </TextSelectionMenu>

  <BBusy :busy>
    <b-labeled-input :label="$t('exerciseNumber')" v-model="number" :disabled="editMode" @change="extractionEvents.push({kind: 'ExerciseNumberSetManually', value: number})" />
    
    <div style="position: relative">
      <BLabeledTextarea ref="instructionsTextArea" :label="$t('exerciseInstructions')" v-model="instructions" @change="extractionEvents.push({kind: 'InstructionsSetManually', value: instructions})" />
      <BLabeledTextarea ref="wordingTextArea" :label="$t('exerciseWording')" v-model="wording" @change="extractionEvents.push({kind: 'WordingSetManually', value: wording})" />
      <div :class="{'container-fluid': noClueNoExample}">
        <div :class="{row: noClueNoExample}">
          <div :class="{col: noClueNoExample}" style="padding: 0;">
            <OptionalTextarea ref="exampleTextArea" :label="$t('exerciseExample')" v-model="example" @change="extractionEvents.push({kind: 'ExampleSetManually', value: example})" />
          </div>
          <div :class="{col: noClueNoExample}" style="padding: 0;">
            <OptionalTextarea ref="clueTextArea" :label="$t('exerciseClue')" v-model="clue" @change="extractionEvents.push({kind: 'ClueSetManually', value: clue})" />
          </div>
        </div>
      </div>

      <BBusy :busy="adaptedDataLoading">
        <div class="mb-3">
          <label class="form-label" for="abc">{{ $t('adaptationType') }}</label>
            <BSelect
            id="abc"
            v-model="adaptationType"
            :options="['-', ...Object.keys(adaptationOptionsForms).map(kind => ({value: kind, label: $t(kind)}))]"
          />
        </div>
        <component
          v-if="adaptationType !== '-'"
          :is="adaptationOptionsForms[adaptationType]"
          v-model="adaptationOptions[adaptationType] as any/*Untypeable?*/"
        />
      </BBusy>

      <div v-if="!editMode && alreadyExists" style="position: absolute; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.8);" class="text-center">
        <div style="position: absolute; left: 25%; top: 25%; width: 50%; height: 50%; background-color: white">
          <p>{{ $t('exerciseAlreadyExists', {number}) }}</p>
          <p>
            <BButton primary @click="skip">{{ $t('skipExercise') }}</BButton>
          </p>
        </div>
      </div>
      <div v-else-if="needsBoundingRectangle" style="position: absolute; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.8);" class="text-center">
        <div style="position: absolute; left: 25%; top: 25%; width: 50%; height: 50%; background-color: white">
          <p>{{ $t('drawBoundingRectangle') }}</p>
        </div>
      </div>
    </div>

    <slot :disabled :create :save></slot>
  </BBusy>
</template>
