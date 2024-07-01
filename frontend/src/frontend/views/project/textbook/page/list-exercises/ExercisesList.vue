<script setup lang="ts">
import { ref } from 'vue'
import { computedAsync } from '@vueuse/core'

import { BBusy } from '$frontend/components/opinion/bootstrap'
import { useApiStore } from '$frontend/stores/api'
import type { Textbook, Exercise } from '$frontend/types/api'


const props = defineProps<{
  textbook: Textbook,
  page: number,
}>()

const api = useApiStore()

const busy = ref(false)
const exercises = computedAsync(
  // @todo Understand why this request isn't duplicated like some others
  async () => await api.client.getAll<Exercise>('exercises', {filter: {'textbook': props.textbook.id, 'textbookPage': props.page.toString()}}),
  [] as Required<Exercise>[],
  busy,
)

function ellipsis(s: string) {
  return s.length > 25 ? s.slice(0, 25) + '…' : s
}

defineExpose({
  exercises,
})
</script>

<template>
  <BBusy :busy>
    <template v-if="exercises.length">
      <p>{{ $t('existingExercises') }}</p>
      <ul>
        <li v-for="exercise in exercises">
          <strong>{{ exercise.attributes.number }}</strong> {{ ellipsis(exercise.attributes.instructions) }}
          <slot :exercise></slot>
        </li>
      </ul>
    </template>
    <p v-else>{{ $t('noExercises') }}</p>
  </BBusy>
</template>
