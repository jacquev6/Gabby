<script setup>
import SelectWords from './SelectWords.vue'

const props = defineProps({
  exercise: {
    type: Object,
    required: true
  }
})
</script>

<template>
  <p>{{ exercise.instructions }}</p>

  <SelectWords v-if="exercise.adaptation.type === 'selectWords'" :exercise="exercise" />
</template>
