<script setup lang="ts">
import { computed } from 'vue'
import { BBusy } from '$frontend/components/opinion/bootstrap'
import { useApiStore } from '$frontend/stores/api'
import type { Textbook } from '$frontend/stores/api'


const props = defineProps<{
  textbook: Textbook,
  page: number,
}>()

const api = useApiStore()

const exercises = computed(() => api.auto.getAll(
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
    <ul v-if="exercises.items.length">
      <template v-for="exercise in exercises.items">
        <li v-if="exercise.exists">
          <strong>{{ exercise.attributes!.number }}</strong> {{ ellipsis(exercise.attributes!.instructions) }}
          <slot :exercise></slot>
        </li>
      </template>
    </ul>
    <p v-else>{{ $t('noExercises') }}</p>
  </BBusy>
</template>
