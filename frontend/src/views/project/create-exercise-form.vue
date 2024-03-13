<script setup>
import { ref } from 'vue'

import { BButton } from '../../components/opinion/bootstrap'
import ExerciseForm from '../../components/exercise-form.vue'


const emit = defineEmits([
  'created',  // (exercise: Object) => void
])

const number = ref('')

function setNextNumber(exercise) {
  const prevNumber = parseInt(exercise.attributes.number)
  if (Number.isInteger(prevNumber)) {
    number.value = (prevNumber + 1).toString()
  } else {
    number.value = ''
  }
}

function created(exercise) {
  setNextNumber(exercise)
  emit('created', exercise)
}
</script>

<template>
  <exercise-form :number v-slot="{ disabled, create }" @created="created">
    <b-button primary :disabled="disabled" @click="create">{{ $t('createExercise' )}}</b-button>
  </exercise-form>
</template>
