<script setup>
import { ref, watch } from 'vue'

import FloatingModal from './FloatingModal.vue'
import OptionalExerciseTextArea from './OptionalExerciseTextArea.vue'
import RequiredExerciseTextArea from './RequiredExerciseTextArea.vue'
import BCheckBox from './BootstrapCheckBox.vue'
import BInput from './BootstrapInput.vue'


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
    <BCheckBox :label="$t('doStripExerciceNumber')" v-model="doStripExerciceNumber" />
    <RequiredExerciseTextArea :label="$t('selectedText')" v-model="textToAdd" />

    <p>{{ $t('addTo') }}</p>
    <button class="btn btn-primary" @click="model.instructions += textToAdd; showTextSelectionMenu=false">{{ $t('instructions') }}</button>
    &nbsp;
    <button class="btn btn-primary" @click="model.example += textToAdd; showTextSelectionMenu=false">{{ $t('example') }}</button>
    &nbsp;
    <button class="btn btn-primary" @click="model.clue += textToAdd; showTextSelectionMenu=false">{{ $t('clue') }}</button>
    &nbsp;
    <button class="btn btn-primary" @click="model.wording += textToAdd; showTextSelectionMenu=false">{{ $t('wording') }}</button>
  </FloatingModal>

  <BInput :label="$t('exerciseNumber')" type="number" min="1" v-model="model.number" :disabled="fixedNumber"/>

  <RequiredExerciseTextArea :label="$t('instructions')" v-model="model.instructions" />
  <OptionalExerciseTextArea :label="$t('example')" v-model="model.example" />
  <OptionalExerciseTextArea :label="$t('clue')" v-model="model.clue" />
  <RequiredExerciseTextArea :label="$t('wording')" v-model="model.wording" />
</template>
