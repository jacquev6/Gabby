<script setup lang="ts">
import { ref } from 'vue'

import { BButton } from '$frontend/components/opinion/bootstrap'
import ExerciseForm from '$frontend/components/ExerciseForm.vue'
import type { Project, Exercise, InCache, Exists } from '$frontend/stores/api'


defineProps<{
  project: Project & InCache & Exists,
}>()

const emit = defineEmits<{
  created: [exercise: Exercise],
}>()

const number = ref('')
const automaticNumber = ref(false)

function created(exercise: Exercise, suggestedNextExerciseNumber: string) {
  number.value = suggestedNextExerciseNumber
  automaticNumber.value = true
  emit('created', exercise)
}
</script>

<template>
  <ExerciseForm
    :project
    :textbook="null"
    :textbookPage="null"
    :section="null"
    :pdf="null"
    :number
    :automaticNumber
    :editMode="false"
    @created="created"
    v-slot="{ disabled, create }"
  >
    <BButton primary :disabled="disabled" @click="create" data-cy="create-exercise">{{ $t('createExercise' )}}</BButton>
  </ExerciseForm>
</template>
