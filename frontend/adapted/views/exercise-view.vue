<script setup>
import { computed } from 'vue'
import { inject } from 'vue'

import ColoredParagraph from '../components/colored-paragraph.vue'
import SelectWords from '../components/select-words.vue'


const props = defineProps({
  exerciseIndex: {
    type: String,
    required: true
  },
})

const data = inject('data')
const isPreview = inject('isPreview')

const exercise = computed(() => data.exercises[props.exerciseIndex])
</script>

<template>
  <p v-if="!isPreview"><router-link :to="{name: 'index'}">Retour</router-link></p>
  <colored-paragraph :text="exercise.instructions || ''" />
  <SelectWords v-if="exercise.adaptation.type === 'selectWords'" :exercise="exercise" />
  <template v-else-if="exercise.adaptation.type === '-'">Sélectionnez un type d'exercise.</template>
  <p v-else>Ce type d'exercice n'est pas encore supporté. @todo</p>
</template>
