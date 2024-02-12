<script setup>
import { ref, watch } from 'vue'

import FloatingModal from './FloatingModal.vue'
import OptionalExerciseTextArea from './OptionalExerciseTextArea.vue'
import RequiredExerciseTextArea from './RequiredExerciseTextArea.vue'


const props = defineProps({
  pdfSha256: {
    type: String,
    required: true,
  },
  pdfPage: {
    type: Number,
    required: true,
  },
  fixedNumber: {
    type: Boolean,
    required: true,
  },
})

const model = defineModel({ type: Object })

const numberFieldId = self.crypto.randomUUID()
const doStripCheckboxId = self.crypto.randomUUID()

const selectedText = ref(null)
const doStripExerciceNumber = ref(true)
const textToAdd = ref(null)
const canStripExerciceNumber = ref(null)
const showTextSelectionMenu = ref(false)
const textSelectionMenuReference = ref({x: 0, y: 0})

function updateTextToAdd() {
  const originalText = selectedText.value
  const number = model.value.number.toString()
  canStripExerciceNumber.value = originalText.startsWith(number)
  textToAdd.value = canStripExerciceNumber.value && doStripExerciceNumber.value ? originalText.slice(number.length).trim() : originalText
}

watch(doStripExerciceNumber, updateTextToAdd)

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
    <div class="form-check">
      <label class="form-check-label" :for="doStripCheckboxId">{{ $t('doStripExerciceNumber') }}</label>
      <input class="form-check-input" :id="doStripCheckboxId" type="checkbox" :disabled="!canStripExerciceNumber" v-model="doStripExerciceNumber">
    </div>

    <textarea class="form-control" rows="5" v-model="textToAdd"></textarea>
    <p>{{ $t('addTo') }}</p>
    <button class="btn btn-primary" @click="model.instructions += textToAdd; showTextSelectionMenu=false">{{ $t('instructions') }}</button>
    &nbsp;
    <button class="btn btn-primary" @click="model.example += textToAdd; showTextSelectionMenu=false">{{ $t('example') }}</button>
    &nbsp;
    <button class="btn btn-primary" @click="model.clue += textToAdd; showTextSelectionMenu=false">{{ $t('clue') }}</button>
    &nbsp;
    <button class="btn btn-primary" @click="model.wording += textToAdd; showTextSelectionMenu=false">{{ $t('wording') }}</button>
  </FloatingModal>

  <div class="mb-3">
    <label class="form-label" :for="numberFieldId">{{ $t('exerciseNumber') }}</label>
    <input class="form-control" :id="numberFieldId" type="number" min="1" v-model="model.number" :disabled="fixedNumber"/>
  </div>
  <RequiredExerciseTextArea v-model="model.instructions">{{ $t('instructions') }}</RequiredExerciseTextArea>
  <OptionalExerciseTextArea v-model="model.example">{{ $t('example') }}</OptionalExerciseTextArea>
  <OptionalExerciseTextArea v-model="model.clue">{{ $t('clue') }}</OptionalExerciseTextArea>
  <RequiredExerciseTextArea v-model="model.wording">{{ $t('wording') }}</RequiredExerciseTextArea>
</template>
