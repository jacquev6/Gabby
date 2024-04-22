<script setup lang="ts">
import { reactive, computed, watch } from 'vue'
import chroma from 'chroma-js'

import ColoredParagraph from '../ColoredParagraph.vue'
import { type Exercise, type SelectWordsAdaptation } from '../../types'


const props = defineProps<{
  exercise: Exercise<SelectWordsAdaptation>,
}>()

const colors = computed(() => chroma.scale('Set2').colors(props.exercise.adaptation.colors))

const wordColors = reactive<{[index: number]: number}>({})
watch(() => props.exercise, () => {
  for (const key in wordColors) {
    delete wordColors[key]
  }
})

function toggle(index: number) {
  wordColors[index] = ((wordColors[index] || 0) + 1) % (colors.value.length + 1)
  if (wordColors[index] === 0) {
    delete wordColors[index]
  }
}

function style(index: number) {
  if (wordColors[index]) {
    return {
      background: colors.value[wordColors[index] - 1]
    }
  } else {
    return {}
  }
}
</script>

<template>
  <ColoredParagraph :text="exercise.wording || ''">
    <template v-slot="{ token, index }">
      <span :style="style(index)" @click="toggle(index)">{{ token.text }}</span>
    </template>
  </ColoredParagraph>
</template>

<style scoped>
span {
  border: none;
  border-top: 2px solid transparent;
  border-bottom: 2px solid transparent;
  margin: 0;
  padding: 0;
  background: none;
  cursor: pointer;
  user-select: none;
}

span:hover {
  border-color: grey;
}
</style>
