<script setup>
import { ref, watch } from 'vue'

import FloatingModal from './FloatingModal.vue'


const props = defineProps({
  fields: {
    type: Array,
    required: true,
  },
  pdfSha256: {
    type: String,
    required: true,
  },
  pdfPage: {
    type: Number,
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
    <div class="form-check">
      <label class="form-check-label">
        <input class="form-check-input" type="checkbox" :disabled="!canStripExerciceNumber" v-model="doStripExerciceNumber">
        {{ $t('doStripExerciceNumber') }}
      </label>
    </div>

    <textarea class="form-control" rows="5" v-model="textToAdd"></textarea>
    <p>{{ $t('addTo') }}</p>
    <template v-for="(field, index) in props.fields">
      <template v-if="index !== 0">&nbsp;</template>
      <button class="btn btn-primary" @click="model[field] += textToAdd; showTextSelectionMenu=false">{{ $t(field) }}</button>
    </template>
  </FloatingModal>

  <div v-for="field in props.fields" class="mb-3">
    <label class="form-label">{{ $t(field) }}</label>
    <textarea class="form-control" rows="3" v-model="model[field]"></textarea>
  </div>
</template>
