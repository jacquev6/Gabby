<script setup>
import { ref } from 'vue'

import { BButton } from '../../components/opinion/bootstrap'
import ExerciseForm from '../../components/exercise-form.vue'


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
  <exercise-form
    :project
    :textbook="null"
    :textbookPage="null"
    :section="null"
    :pdf="null"
    :number
    :automaticNumber
    :fixedNumber="false"
    @created="created"
    v-slot="{ disabled, create }"
  >
    <b-button primary :disabled="disabled" @click="create">{{ $t('createExercise' )}}</b-button>
  </exercise-form>
</template>
