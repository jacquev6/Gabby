<script setup lang="ts">
import { computed } from 'vue'
import { inject } from 'vue'

import type { Data, Settings } from '$adapted/types'
import Exercise from '$adapted/components/Exercise.vue'


const props = defineProps<{
  exerciseId: string,
}>()

const data = inject<Data>('data')!
const settings = inject<Settings>('settings')!
const isPreview = inject<boolean>('isPreview')!

const exercise = computed(() => {
  return data.exercises[props.exerciseId]
})
</script>

<template>
  <p v-if="!isPreview"><router-link :to="{name: 'index'}">Retour</router-link></p>
  <Exercise :projectId="data.projectId" :exerciseId :exercise :settings :isPreview />
</template>
