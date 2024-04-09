<script setup>
import { ref, watch, nextTick } from 'vue'

import { BLabeledTextarea } from './opinion/bootstrap'


const props = defineProps({
  label: { type: String, required: true },
})

const model = defineModel({ type: String })

const force = ref(false)

watch(model, () => { force.value = false })

const textArea = ref(null)

function activate() {
  force.value = true
  nextTick(() => textArea.value.focus())
}

defineExpose({
  focus: () => textArea.value.focus(),
  setSelectionRange: (start, end) => textArea.value.setSelectionRange(start, end),
})
</script>

<template>
  <BLabeledTextarea v-if="model || force" ref="textArea" :label v-model="model" />
  <p v-else @click="activate">{{ label }} <button class="btn btn-sm btn-primary">+</button></p>
</template>
