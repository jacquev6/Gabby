<script setup>
import { reactive, computed } from 'vue'
import chroma from "chroma-js"

import { tokenize } from './tokenize'


const props = defineProps({
  exercise: {
    type: Object,
    required: true
  },
})

const words = computed(() => tokenize(props.exercise.wording))

const colors = computed(() => chroma.scale('Set2').colors(props.exercise.adaptation.colors))

const wordColors = reactive(words.value.map(() => 0))

function toggle(index) {
  console.log('toggle', index, wordColors[index])
  wordColors[index] += 1
  if (wordColors[index] > colors.value.length) {
    wordColors[index] = 0
  }
}

const styles = computed(() => {
  return words.value.map((_, index) => {
    if (wordColors[index] === 0) {
      return {}
    } else {
      return {
        background: colors.value[wordColors[index] - 1]
      }
    }
  })
})
</script>

<template>
  <p>
    <template v-for="(token, index) in words">
      <template v-if="token.kind === 'whitespace'">
        <wbr> <!-- The two <wbr> element work around Vue.js removing spaces despite 'whitespace: 'preserve' in its configuration --><wbr>
      </template>
      <template v-else>
        <button :style="styles[index]" @click="toggle(index)">{{ token.token }}</button>
      </template>
    </template>
  </p>
</template>

<style scoped>
button {
  border: none;
  border-top: 2px solid transparent;
  border-bottom: 2px solid transparent;
  margin: 0;
  padding: 0;
  background: none;
  cursor: pointer;
}

button:hover {
  border-color: grey;
}
</style>
