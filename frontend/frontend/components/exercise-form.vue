<script setup>
import { ref, reactive, computed, watch } from 'vue'
import { computedAsync } from '@vueuse/core'
import { nextTick } from 'vue'

import { BBusy, BLabeledInput, BLabeledTextarea, BButton, BSelect } from './opinion/bootstrap'
import TextSelectionMenu from './exercise-form-text-selection-menu.vue'
import OptionalTextarea from './optional-textarea.vue'
import { useApiStore } from '../stores/api'
import adaptedForms from './adapted-forms'


const props = defineProps({
  project: {type: Object, required: true},
  textbook: {required: true},
  textbookPage: {required: true},
  section: {required: true},
  pdf: {required: true},
  number: {type: String, required: true},
  automaticNumber: {type: Boolean, required: true},
  editMode: {type: Boolean, required: true},
  exercise: {type: Object, required: false},
})

const emit = defineEmits([
  'created',  // (exercise: Object, suggestedNextExerciseNumber: string) => void
  'saved',  // () => void
])

const api = useApiStore()

var extractionEvents = []
const number = ref('')
const boundingRectangle = ref(null)
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
const adaptedType = ref('-')
const adaptedAttributes = reactive({'-': {}})
for (const kind of Object.keys(adaptedForms)) {
  adaptedAttributes[kind] = {}
}

const alreadyExists = computedAsync(
  async () => {
    if (props.editMode) {
      return true
    } else if (number.value === '') {
      return false
    } else {
      const exercises = await api.client.getAll(
        'exercises',
        {
          filter: {
            textbook: props.textbook.id,
            textbookPage: props.textbookPage,
            number: number.value,
          }
        },
      )
      console.assert(exercises.length <= 1)
      return exercises.length === 1
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
    boundingRectangle.value = props.exercise?.attributes.boundingRectangle ?? null

    instructions.value = props.exercise?.attributes.instructions ?? ''
    wording.value = props.exercise?.attributes.wording ?? ''
    example.value = props.exercise?.attributes.example ?? ''
    clue.value = props.exercise?.attributes.clue ?? ''

    adaptedType.value = props.exercise?.relationships.adapted?.type ?? '-'
    adaptedAttributes[adaptedType.value] = props.exercise?.relationships.adapted?.attributes ?? {}
  },
  {immediate: true},
)

const disabled = computed(() => (!props.editMode && alreadyExists.value) || !number.value)
const busy = ref(false)

const showTextSelectionMenu = ref(false)
const selectedText = ref('')
const selectedRectangle = ref(null)
const selectedTextReference = ref({})
function textSelected(text, point, textItems, rectangle) {
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

const instructionsTextArea = ref(null)
const wordingTextArea = ref(null)
const exampleTextArea = ref(null)
const clueTextArea = ref(null)
const textAreas = {
  instructions: instructionsTextArea,
  wording: wordingTextArea,
  example: exampleTextArea,
  clue: clueTextArea,
}

const noClueNoExample = computed(() => !exampleTextArea.value?.expanded && !clueTextArea.value?.expanded)

function addTextTo(fieldName, text) {
  const field = fields[fieldName]
  const textArea = textAreas[fieldName].value
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

  adaptedType.value = '-'
  adaptedAttributes[adaptedType.value] = {}
}

async function create() {
  busy.value = true

  // @todo Use a batch request
  const exercise = await api.client.post(
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
  if (adaptedType.value !== '-') {
    await api.client.post(
      adaptedType.value,
      adaptedAttributes[adaptedType.value],
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

  adaptedType.value = '-'
  adaptedAttributes[adaptedType.value] = {}

  busy.value = false

  emit('created', exercise, tryIncrement(exercise.attributes.number))
}

function tryIncrement(s) {
  const n = parseInt(s)
  if (Number.isInteger(n)) {
    return (n + 1).toString()
  } else {
    return ''
  }
}

async function save() {
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
  if (adaptedType.value === '-') {
    if (props.exercise.relationships.adapted !== null) {
      await api.client.delete(props.exercise.relationships.adapted.type, props.exercise.relationships.adapted.id)
    }
  } else {
    await api.client.post(
      adaptedType.value,
      adaptedAttributes[adaptedType.value],
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

const adaptationUrl = computed(() => {
  const data = {exercises: [{
    instructions: instructions.value,
    wording: wording.value,
    adaptation: {type: adaptedType.value, ...adaptedAttributes[adaptedType.value]}
  }]}
  return `/adapted?preview&data=${JSON.stringify(data)}#/exercise/0`
})

const highlightedRectangles = computed(() => {
  if (boundingRectangle.value) {
    return [boundingRectangle.value]
  } else {
    return null
  }
})

defineExpose({
  textSelected: computed(() => !props.editMode && alreadyExists.value ? null : textSelected),
  adaptationUrl,
  highlightedRectangles,
})
</script>

<template>
  <text-selection-menu
    v-model:show="showTextSelectionMenu"
    :number
    :text="selectedText"
    :reference="selectedTextReference"
    @extractionEvent="event => extractionEvents.push(event)"
  >
    <template v-slot="{textToAdd, hide}">
      <p><b-button secondary @click="boundingRectangle = selectedRectangle; hide()">{{ $t('setBoundingRect') }}</b-button></p>
      <p>{{ $t('addTo') }}</p>
      <p>
        <b-button primary @click="addTextTo('instructions', textToAdd); hide()">{{ $t('instructions') }}</b-button>
        <b-button primary @click="addTextTo('wording', textToAdd); hide()">{{ $t('wording') }}</b-button>
        <b-button primary @click="addTextTo('example', textToAdd); hide()">{{ $t('example') }}</b-button>
        <b-button primary @click="addTextTo('clue', textToAdd); hide()">{{ $t('clue') }}</b-button>
      </p>
    </template>
  </text-selection-menu>

  <b-busy :busy>
    <b-labeled-input :label="$t('exerciseNumber')" v-model="number" :disabled="editMode" @change="extractionEvents.push({kind: 'ExerciseNumberSetManually', value: number})" />
    
    <div style="position: relative">
      <b-labeled-textarea ref="instructionsTextArea" :label="$t('exerciseInstructions')" v-model="instructions" @change="extractionEvents.push({kind: 'InstructionsSetManually', value: instructions})" />
      <b-labeled-textarea ref="wordingTextArea" :label="$t('exerciseWording')" v-model="wording" @change="extractionEvents.push({kind: 'WordingSetManually', value: wording})" />
      <div :class="{row: noClueNoExample}">
        <div :class="{col: noClueNoExample}">
          <optional-textarea ref="exampleTextArea" :label="$t('exerciseExample')" v-model="example" @change="extractionEvents.push({kind: 'ExampleSetManually', value: example})" />
        </div>
        <div :class="{col: noClueNoExample}">
          <optional-textarea ref="clueTextArea" :label="$t('exerciseClue')" v-model="clue" @change="extractionEvents.push({kind: 'ClueSetManually', value: clue})" />
        </div>
      </div>

      <div class="mb-3">
        <label class="form-label" for="abc">{{ $t('exerciseType') }}</label>
          <b-select
          id="abc"
          v-model="adaptedType"
          :options="['-', ...Object.keys(adaptedForms).map(kind => ({value: kind, label: $t(kind)}))]"
        />
      </div>
      <component
        v-if="adaptedType !== '-'"
        :is="adaptedForms[adaptedType]"
        v-model="adaptedAttributes[adaptedType]"
      />

      <div v-if="!editMode && alreadyExists" style="position: absolute; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.8);" class="text-center">
        <div style="position: absolute; left: 25%; top: 25%; width: 50%; height: 50%; background-color: white">
          <p>{{ $t('exerciseAlreadyExists', {number}) }}</p>
          <p>
            <b-button primary @click="skip">{{ $t('skipExercise') }}</b-button>
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
  </b-busy>
</template>
