<script setup lang="ts">
import { computed } from 'vue'
import { BBusy } from '$frontend/components/opinion/bootstrap'
import { useApiStore } from '$frontend/stores/api'
import type { Textbook, Exercise } from '$frontend/types/api'


const props = defineProps<{
  textbook: Textbook,
  page: number,
}>()

const api = useApiStore()

const exercises = computed(() => api.auto.getAll<Exercise>(
  'exercise',
  {filters: {'textbook': props.textbook.id, 'textbookPage': props.page.toString()}}
))

function ellipsis(s: string) {
  return s.length > 25 ? s.slice(0, 25) + '…' : s
}

defineExpose({
  exercises,
})
</script>

<template>
  <BBusy :busy="exercises.loading">
    <template v-if="exercises.items.length">
      <p>{{ $t('existingExercises') }}</p>
      <ul>
        <template v-for="exercise in exercises.items">
          <li v-if="exercise.exists">
            <strong>{{ exercise.attributes!.number }}</strong> {{ ellipsis(exercise.attributes!.instructions) }}
            <slot :exercise></slot>
          </li>
        </template>
      </ul>
    </template>
    <p v-else>{{ $t('noExercises') }}</p>
  </BBusy>
</template>
