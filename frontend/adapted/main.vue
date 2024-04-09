<script setup>
import { ref, computed } from 'vue'

import SelectWords from './components/select-words.vue'
import ColoredParagraph from './components/colored-paragraph.vue'


// @todo Use Vue-router in hash mode
// Cf. https://router.vuejs.org/guide/essentials/history-mode.html#Hash-Mode
const params = new URLSearchParams(window.location.search)
const data = JSON.parse(params.get('data') || '{{ data }}')
const initialExerciseId = params.get('exerciseId')
const exerciseId = ref(initialExerciseId)
const exercise = computed(() => exerciseId.value ? data.exercises[exerciseId.value] : null)
</script>

<template>
  <template v-if="exerciseId">
    <p v-if="!initialExerciseId"><a href="#" @click.prevent="exerciseId = null">Retour</a></p>
    <colored-paragraph :text="exercise.instructions || ''" />
    <SelectWords v-if="exercise.adaptation.type === 'selectWords'" :exercise="exercise" />
  </template>
  <template v-else>
    <ul>
      <li v-for="(ex, id) in data.exercises">
        <a href="#" @click.prevent="exerciseId = id">{{ ex.number }} page {{ ex.textbookPage }}</a>
      </li>
    </ul>
  </template>
</template>

<style>
* {
  font-family: sans-serif;
  font-size: 20px;
  line-height: 30px;
}
</style>
