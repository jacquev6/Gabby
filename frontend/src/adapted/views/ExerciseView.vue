<script setup lang="ts">
import { computed } from 'vue'

import type { Data, Settings } from '$adapted/types'
import Exercise from '$adapted/components/Exercise.vue'


const props = defineProps<{
  data: Data,
  settings: Settings,
  exerciseId: string,
}>()

const exercise = computed(() => {
  return props.data.exercises[props.exerciseId]
})
</script>

<template>
  <p><RouterLink :to="{name: 'index'}">{{ $t('back') }}</RouterLink></p>
  <Exercise :projectId="data.projectId" :exerciseId :exercise :settings />
</template>
