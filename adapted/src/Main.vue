<script setup>
import SelectWords from './components/select-words.vue'
import ColoredParagraph from './components/colored-paragraph.vue'


const params = new URLSearchParams(window.location.search)
const data = JSON.parse(params.get('data') || '{{ data}}')
const exercise = data.exercises[params.get('exerciseId')]
</script>

<template>
  <colored-paragraph :text="exercise.instructions" />

  <SelectWords v-if="exercise.adaptation.type === 'selectWords'" :exercise="exercise" />
</template>

<style>
* {
  font-family: sans-serif;
  font-size: 20px;
  line-height: 30px;
}
</style>
