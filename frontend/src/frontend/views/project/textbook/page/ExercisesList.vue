<script setup lang="ts">
import { ref } from 'vue'

import type { List, Exercise } from '$frontend/stores/api'
import { BBusy, BButton } from '$frontend/components/opinion/bootstrap'
import ConfirmationModal from '$frontend/components/ConfirmationModal.vue'


const props = defineProps<{
  exercises: List<'exercise'>
}>()

function ellipsis(s: string) {
  return s.length > 25 ? s.slice(0, 25) + '…' : s
}

const exerciseDeletionConfirmationModal = ref<InstanceType<typeof ConfirmationModal> | null>(null)
async function delete_(exercise: Exercise) {
  console.assert(exerciseDeletionConfirmationModal.value !== null)
  if (await exerciseDeletionConfirmationModal.value.show()) {
    await exercise.delete()
    await props.exercises.refresh()
  }
}
</script>

<template>
  <ConfirmationModal ref="exerciseDeletionConfirmationModal">{{ $t('exerciseDeletionConfirmationMessage') }}</ConfirmationModal>
  <BBusy :busy="exercises.loading">
    <ul v-if="exercises.existingItems.length">
      <template v-for="exercise in exercises.existingItems">
        <li>
          <BBusy :busy="exercise.busy">
            <strong>{{ exercise.attributes.number }}</strong>
            {{ ellipsis(exercise.attributes.instructions) }}
            <em>{{ exercise.attributes.adaptation.kind !== null ? $t(exercise.attributes.adaptation.kind) : '' }}</em>
            <RouterLink class="btn btn-primary btn-sm" :to="{name: 'project-textbook-page-exercise', params: {exerciseId: exercise.id}}">{{ $t('edit') }}</RouterLink>
            <BButton secondary sm @click="delete_(exercise)">{{ $t('delete') }}</BButton>
          </BBusy>
        </li>
      </template>
    </ul>
    <p v-else>{{ $t('noExercises') }}</p>
  </BBusy>
</template>
