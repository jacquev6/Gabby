<script setup lang="ts">
import { ref } from 'vue'
import { onMounted, onBeforeUpdate } from 'vue'


const model = defineModel<string>()

const span = ref<HTMLSpanElement | null>(null)

function updateModel() {
  console.assert(span.value !== null)
  model.value = span.value.innerText
}

// Can't just put '{{ model }}' in the 'span' because it resets the caret to the beginning after each change
function updateContent() {
  console.assert(span.value !== null)
  const innerText = model.value ?? ''
  if (span.value.innerText !== innerText) {  // Avoid resetting the caret to the beginning: change only if necessary
    span.value.innerText = innerText
  }
}

onMounted(updateContent)
onBeforeUpdate(updateContent)  // For re-used components

function forbidNewlines(event: KeyboardEvent) {
  if (event.key === 'Enter') {
    event.preventDefault()
  }
}
</script>

<template>
  <span ref="span" contenteditable @input="updateModel" @keypress="forbidNewlines"></span>
</template>

<style scoped>
span {
  padding: 0 1ch;
  border: 2px solid black;
}
</style>
