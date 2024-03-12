<script setup>
import { ref, watch, nextTick } from 'vue'

import FloatingModal from './FloatingModal.vue'
import OptionalExerciseTextArea from './OptionalExerciseTextArea.vue'
import RequiredExerciseTextArea from './RequiredExerciseTextArea.vue'
import BCheckBox from './BootstrapCheckBox.vue'
import BInput from './BootstrapInput.vue'


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
  <FloatingModal
    v-if="showTextSelectionMenu"
    :title="$t('selectedText')"
    :reference="textSelectionMenuReference"
    @dismissed="showTextSelectionMenu=false"
  >
    <BCheckBox :label="$t('doStripExerciceNumber')" v-model="doStripExerciceNumber" :disabled="!canStripExerciceNumber" />
    <RequiredExerciseTextArea :label="$t('selectedText')" v-model="textToAdd" @change="emit('extractionEvent', {kind: 'SelectedTextEdited', value: textToAdd})" />

    <p>{{ $t('addTo') }}</p>
    <button class="btn btn-primary" @click="addTextToInstructions">{{ $t('instructions') }}</button>
    &nbsp;
    <button class="btn btn-primary" @click="addTextToExample">{{ $t('example') }}</button>
    &nbsp;
    <button class="btn btn-primary" @click="addTextToClue">{{ $t('clue') }}</button>
    &nbsp;
    <button class="btn btn-primary" @click="addTextToWording">{{ $t('wording') }}</button>
  </FloatingModal>

  <BInput :label="$t('exerciseNumber')" v-model="model.number" :disabled="fixedNumber" @change="emit('extractionEvent', {kind: 'ExerciseNumberSetManually', value: model.number})"/>

  <RequiredExerciseTextArea ref="instructionsTextArea" :label="$t('instructions')" v-model="model.instructions" @change="emit('extractionEvent', {kind: 'InstructionsSetManually', value: model.instructions})"/>
  <OptionalExerciseTextArea ref="exampleTextArea" :label="$t('example')" v-model="model.example" @change="emit('extractionEvent', {kind: 'ExampleSetManually', value: model.example})"/>
  <OptionalExerciseTextArea ref="clueTextArea" :label="$t('clue')" v-model="model.clue" @change="emit('extractionEvent', {kind: 'ClueSetManually', value: model.clue})"/>
  <RequiredExerciseTextArea ref="wordingTextArea" :label="$t('wording')" v-model="model.wording" @change="emit('extractionEvent', {kind: 'WordingSetManually', value: model.wording})"/>
</template>
