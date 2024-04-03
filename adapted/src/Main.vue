<script setup>
import SelectWords from './components/SelectWords.vue'


const params = new URLSearchParams(window.location.search)
const data = JSON.parse(params.get('data') || '{{ data}}')
const exercise = data.exercises[params.get('exerciseId')]
</script>

<template>
  <p>{{ exercise.instructions }}</p>

  <SelectWords v-if="exercise.adaptation.type === 'selectWords'" :exercise="exercise" />
</template>

<style>
* {
  font-family: sans-serif;
  font-size: 20px;
  line-height: 30px;
}
</style>
