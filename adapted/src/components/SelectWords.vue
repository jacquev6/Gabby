<script setup>
import { reactive, computed } from 'vue'

import chroma from "chroma-js"


const props = defineProps({
  exercise: {
    type: Object,
    required: true
  },
})

const words = computed(() => {
  return props.exercise.wording.match(/[\p{L}\p{M}]+|\d+|\p{Zs}+|[^\p{L}\p{M}\p{Zs}]/gu).map(word => word.trim() === '' ? null : word)
})

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
  <p>Select words ({{ exercise.adaptation.colors }} types:
    <template v-for="color in colors">
      <span :style="{background: color}">{{ color }}</span>
      <template> </template>
    </template>
  )</p>
  <p>{{ exercise.wording }}</p>
  <p>{{ words }}</p>
  <p>
    <template v-for="(token, index) in words">
      <template v-if="token === null">
        <wbr> <!-- The two <wbr> element work around Vue.js removing spaces despite 'whitespace: 'preserve' in its configuration --><wbr>
      </template>
      <template v-else>
        <button :style="styles[index]" @click="toggle(index)">{{ token }}</button>
      </template>
    </template>
  </p>
</template>

<style scoped>
* {
  font-family: sans-serif;
  font-size: 20px;
  line-height: 30px;
}

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
