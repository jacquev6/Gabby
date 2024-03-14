<script setup>
import { ref, watch, nextTick } from 'vue'

import FloatingModal from './FloatingModal.vue'
import OptionalTextarea from './optional-textarea.vue'
import { BButton, BLabeledCheckbox, BLabeledInput, BLabeledTextarea } from './opinion/bootstrap'


// @todo Factorize with exercise-form, everywhere

const props = defineProps({
  fixedNumber: {
    type: Boolean,
    required: true,
  },
})

const model = defineModel({ type: Object })

const emit = defineEmits([
  'extractionEvent'  // Object => void
])

const selectedText = ref(null)
const doStripExerciceNumber = ref(true)
const textToAdd = ref(null)
const canStripExerciceNumber = ref(null)
const showTextSelectionMenu = ref(false)
const textSelectionMenuReference = ref({x: 0, y: 0})

function updateTextToAdd() {
  const originalText = selectedText.value
  const number = model.value.number.toString()
  canStripExerciceNumber.value = number !== '' && originalText.startsWith(number)
  textToAdd.value = canStripExerciceNumber.value && doStripExerciceNumber.value ? originalText.slice(number.length).trimStart() : originalText
}

watch(doStripExerciceNumber, updateTextToAdd)

function addTextTo(field, textArea) {
  const valueBefore = model.value[field]
  if (model.value[field] !== '' && !model.value[field].endsWith('\n')) {
    model.value[field] += '\n'
  }
  const selectionBegin = model.value[field].length
  const selectionEnd = selectionBegin + textToAdd.value.length
  model.value[field] += textToAdd.value
  nextTick(() => {
    textArea.value.focus()
    textArea.value.setSelectionRange(selectionBegin, selectionEnd)
  })
  emit('extractionEvent', {kind: `SelectedTextAddedTo${field.charAt(0).toUpperCase()}${field.slice(1)}`, valueBefore, valueAfter: model.value[field]})
  showTextSelectionMenu.value = false
}

const instructionsTextArea = ref(null)

function addTextToInstructions() {
  addTextTo('instructions', instructionsTextArea)
}

const exampleTextArea = ref(null)

function addTextToExample() {
  addTextTo('example', exampleTextArea)
}

const clueTextArea = ref(null)

function addTextToClue() {
  addTextTo('clue', clueTextArea)
}

const wordingTextArea = ref(null)

function addTextToWording() {
  addTextTo('wording', wordingTextArea)
}

function textSelected(text, point) {
  selectedText.value = text
  updateTextToAdd()
  showTextSelectionMenu.value = true
  textSelectionMenuReference.value = {x: point.clientX, y: point.clientY}
}

defineExpose({
  textSelected,
})
</script>

<template>
  <floating-modal
    v-if="showTextSelectionMenu"
    :title="$t('selectedText')"
    :reference="textSelectionMenuReference"
    @dismissed="showTextSelectionMenu=false"
  >
    <b-labeled-checkbox :label="$t('doStripExerciceNumber')" v-model="doStripExerciceNumber" :disabled="!canStripExerciceNumber" />
    <b-labeled-textarea :label="$t('selectedText')" v-model="textToAdd" @change="emit('extractionEvent', {kind: 'SelectedTextEdited', value: textToAdd})" />

    <p>{{ $t('addTo') }}</p>
    <b-button primary @click="addTextToInstructions">{{ $t('instructions') }}</b-button>
    &nbsp;
    <b-button primary @click="addTextToExample">{{ $t('example') }}</b-button>
    &nbsp;
    <b-button primary @click="addTextToClue">{{ $t('clue') }}</b-button>
    &nbsp;
    <b-button primary @click="addTextToWording">{{ $t('wording') }}</b-button>
  </floating-modal>

  <b-labeled-input :label="$t('exerciseNumber')" v-model="model.number" :disabled="fixedNumber" @change="emit('extractionEvent', {kind: 'ExerciseNumberSetManually', value: model.number})" />

  <b-labeled-textarea ref="instructionsTextArea" :label="$t('instructions')" v-model="model.instructions" @change="emit('extractionEvent', {kind: 'InstructionsSetManually', value: model.instructions})" />
  <optional-textarea ref="exampleTextArea" :label="$t('example')" v-model="model.example" @change="emit('extractionEvent', {kind: 'ExampleSetManually', value: model.example})" />
  <optional-textarea ref="clueTextArea" :label="$t('clue')" v-model="model.clue" @change="emit('extractionEvent', {kind: 'ClueSetManually', value: model.clue})" />
  <b-labeled-textarea ref="wordingTextArea" :label="$t('wording')" v-model="model.wording" @change="emit('extractionEvent', {kind: 'WordingSetManually', value: model.wording})" />
</template>
./optional-textarea.vue