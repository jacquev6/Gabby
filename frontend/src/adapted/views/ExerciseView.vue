<script setup lang="ts">
import { computed } from 'vue'
import { inject } from 'vue'

import { type Data } from '../types'
import Exercise from '../components/Exercise.vue'


const props = defineProps<{
  exerciseIndex: string,
}>()

const data = inject('data') as Data
const isPreview = inject('isPreview') as boolean

const exercise = computed(() => {
  return data.exercises[props.exerciseIndex]
})
</script>

<template>
  <p v-if="!isPreview"><router-link :to="{name: 'index'}">Retour</router-link></p>
  <Exercise :exercise="exercise.adapted" />
</template>
