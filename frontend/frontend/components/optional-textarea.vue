<script setup>
import { ref, computed } from 'vue'
import { nextTick } from 'vue'

import { BLabeledTextarea } from './opinion/bootstrap'


const props = defineProps({
  label: { type: String, required: true },
})

const model = defineModel({ type: String })

const forced = ref(false)

const textArea = ref(null)

function force() {
  forced.value = true
  nextTick(() => textArea.value.focus())
}

function unforce() {
  forced.value = false
}

const expanded = computed(() => model.value || forced.value)

defineExpose({
  expanded,
  focus: () => textArea.value.focus(),
  setSelectionRange: (start, end) => textArea.value.setSelectionRange(start, end),
})
</script>

<template>
  <BLabeledTextarea v-if="expanded" ref="textArea" :label v-model="model" @focus="force" @blur="unforce" />
  <p v-else @click="force">{{ label }} <button class="btn btn-sm btn-primary">+</button></p>
</template>
