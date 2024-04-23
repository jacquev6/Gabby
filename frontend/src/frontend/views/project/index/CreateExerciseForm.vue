<script setup>
import { ref } from 'vue'

import { BButton } from '../../../components/opinion/bootstrap'
import ExerciseForm from '../../../components/ExerciseForm.vue'


const props = defineProps({
  project: {type: Object, required: true},
})

const emit = defineEmits([
  'created',  // (exercise: Object) => void
])

const number = ref('')
const automaticNumber = ref(false)

function created(exercise, suggestedNextExerciseNumber) {
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
