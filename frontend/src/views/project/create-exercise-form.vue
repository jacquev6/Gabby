<script setup>
import { ref } from 'vue'

import { BButton } from '../../components/opinion/bootstrap'
import ExerciseForm from '../../components/exercise-form.vue'


const emit = defineEmits([
  'created',  // (exercise: Object) => void
])

const number = ref('')

function created(exercise, suggestedNextExerciseNumber) {
  number.value = suggestedNextExerciseNumber
  emit('created', exercise)
}
</script>

<template>
  <exercise-form :number v-slot="{ disabled, create }" @created="created">
    <b-button primary :disabled="disabled" @click="create">{{ $t('createExercise' )}}</b-button>
  </exercise-form>
</template>
