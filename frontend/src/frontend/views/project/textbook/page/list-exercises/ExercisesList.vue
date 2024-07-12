<script setup lang="ts">
import { BBusy } from '$frontend/components/opinion/bootstrap'
import type { List } from '$frontend/stores/api'


defineProps<{
  exercises: List<'exercise'>,
}>()

function ellipsis(s: string) {
  return s.length > 25 ? s.slice(0, 25) + '…' : s
}
</script>

<template>
  <BBusy :busy="exercises.loading">
    <ul v-if="exercises.items.length">
      <template v-for="exercise in exercises.items">
        <li v-if="exercise.exists">
          <strong>{{ exercise.attributes.number }}</strong>
          {{ ellipsis(exercise.attributes.instructions) }}
          <em>{{ exercise.relationships.adaptation? $t(exercise.relationships.adaptation.type) : '' }}</em>
          <slot :exercise></slot>
        </li>
      </template>
    </ul>
    <p v-else>{{ $t('noExercises') }}</p>
  </BBusy>
</template>
