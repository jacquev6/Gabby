<script setup>
import { ref } from 'vue'

import { BLabeledTextarea } from './opinion/bootstrap'


const model = defineModel({ type: String })

const textArea = ref(null)

defineExpose({
  focus: () => textArea.value.focus(),
  setSelectionRange: (start, end) => textArea.value.setSelectionRange(start, end),
})
</script>

<template>
  <b-labeled-textarea ref="textArea" v-model="model" :rows="model.split('\n').length + 1"><slot></slot></b-labeled-textarea>
</template>
