<script setup>
import AdaptedExercise from './components/AdaptedExercise.vue'

const params = new URLSearchParams(window.location.search)
const data = JSON.parse(params.get('data') || '{{ data}}')
const exercise = data.exercises[params.get('exerciseId')]
</script>

<template>
  <AdaptedExercise :exercise="exercise" />
</template>
