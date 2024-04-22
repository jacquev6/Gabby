<script setup lang="ts">
import { computed } from 'vue'
import { inject } from 'vue'

import { type Data } from '../types'
import ColoredParagraph from '../components/ColoredParagraph.vue'
import adaptedExercises from '../components/adapted-exercises'


const props = defineProps<{
  exerciseIndex: string,
}>()

const data = inject('data') as Data
const isPreview = inject('isPreview')

const exercise = computed(() => data.exercises[props.exerciseIndex])
</script>

<template>
  <p v-if="!isPreview"><router-link :to="{name: 'index'}">Retour</router-link></p>
  <ColoredParagraph :text="exercise.instructions || ''" />
  <template v-if="exercise.adaptation.type === '-'">
    <p>Sélectionnez un type d'exercise.</p>
  </template>
  <template v-else-if="exercise.adaptation.type in adaptedExercises">
    <component :is="adaptedExercises[exercise.adaptation.type]" :exercise="exercise as any" />
  </template>
  <template v-else>
    <p>Ce type d'exercice n'est pas encore supporté. @todo</p>
  </template>
</template>
