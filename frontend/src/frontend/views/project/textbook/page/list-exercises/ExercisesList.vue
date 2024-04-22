<script setup>
import { ref } from 'vue'
import { computedAsync } from '@vueuse/core'

import { BBusy } from '../../../../../components/opinion/bootstrap'
import { useApiStore } from '../../../../../stores/api'


const props = defineProps({
  textbook: {type: Object, required: true},
  page: {type: Number, required: true}
})

const api = useApiStore()

const busy = ref(false)
const exercises = computedAsync(
  async () => await api.client.getAll('exercises', {filter: {'textbook': props.textbook.id, 'textbookPage': props.page}}),
  [],
  busy,
)

function ellipsis(s) {
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
