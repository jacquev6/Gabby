<script setup>
import { ref, computed, watch } from 'vue'

import { BBusy, BLabeledInput, BLabeledTextarea } from './opinion/bootstrap'
import OptionalTextarea from './optional-textarea.vue'
import { useApiStore } from '../stores/api'


const props = defineProps({
  project: {type: Object, required: true},
  number: {type: String, default: ''},
  fixedNumber: {type: Boolean, default: false},
})

const emit = defineEmits([
  'extractionEvent',  // (event: Object) => void
  'created',  // (exercise: Object, suggestedNextExerciseNumber: string) => void
])

const api = useApiStore()

const number = ref('')
const instructions = ref('')
const wording = ref('')
const example = ref('')
const clue = ref('')

watch(
  () => props.number,
  () => {
    number.value = props.number
  },
  {immediate: true},
)

const disabled = computed(() => !number.value)
const busy = ref(false)

function tryIncrement(s) {
  const n = parseInt(s)
  if (Number.isInteger(n)) {
    return (n + 1).toString()
  } else {
    return ''
  }
}

async function create() {
  busy.value = true
  const exercise = await api.client.post(
    'exercise',
    {
      number: number.value,
      instructions: instructions.value,
      wording: wording.value,
      example: example.value,
      clue: clue.value,
    },
    {project: props.project},
  )
  busy.value = false
  number.value = ''
  instructions.value = ''
  wording.value = ''
  example.value = ''
  clue.value = ''

  emit('created', exercise, tryIncrement(exercise.attributes.number))
}
</script>

<template>
  <b-busy :busy>
    <b-labeled-input :label="$t('exerciseNumber')" v-model="number" :disabled="fixedNumber" @change="emit('extractionEvent', {kind: 'ExerciseNumberSetManually', value: number})" />

    <b-labeled-textarea :label="$t('exerciseInstructions')" v-model="instructions" @change="emit('extractionEvent', {kind: 'InstructionsSetManually', value: instructions})" />
    <b-labeled-textarea :label="$t('exerciseWording')" v-model="wording" @change="emit('extractionEvent', {kind: 'WordingSetManually', value: wording})" />
    <optional-textarea :label="$t('exerciseExample')" v-model="example" @change="emit('extractionEvent', {kind: 'ExampleSetManually', value: example})" />
    <optional-textarea :label="$t('exerciseClue')" v-model="clue" @change="emit('extractionEvent', {kind: 'ClueSetManually', value: clue})" />
    <slot :disabled :create></slot>
  </b-busy>
</template>
