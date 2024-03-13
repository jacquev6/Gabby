<script setup>
import { ref, computed, watch } from 'vue'

import { BBusy, BLabeledInput } from './opinion/bootstrap'
import RequiredTextarea from './RequiredExerciseTextArea.vue'
import OptionalTextarea from './OptionalExerciseTextArea.vue'
import { useApiStore } from '../stores/api'


const props = defineProps({
  project: {type: Object, required: true},
  number: {type: String, default: ''},
  fixedNumber: {type: Boolean, default: false},
})

const emit = defineEmits([
  'extractionEvent',  // (event: Object) => void
  'created',  // (exercise: Object) => void
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
    {project: props.project, extractionEvents: []},
  )
  busy.value = false
  number.value = ''
  instructions.value = ''
  wording.value = ''
  example.value = ''
  clue.value = ''
  emit('created', exercise)
}
</script>

<template>
  <b-busy :busy>
    <b-labeled-input :label="$t('exerciseNumber')" v-model="number" :disabled="fixedNumber" @change="emit('extractionEvent', {kind: 'ExerciseNumberSetManually', value: number})" />

    <required-textarea :label="$t('exerciseInstructions')" v-model="instructions" @change="emit('extractionEvent', {kind: 'InstructionsSetManually', value: instructions})" />
    <required-textarea :label="$t('exerciseWording')" v-model="wording" @change="emit('extractionEvent', {kind: 'WordingSetManually', value: wording})" />
    <optional-textarea :label="$t('exerciseExample')" v-model="example" @change="emit('extractionEvent', {kind: 'ExampleSetManually', value: example})" />
    <optional-textarea :label="$t('exerciseClue')" v-model="clue" @change="emit('extractionEvent', {kind: 'ClueSetManually', value: clue})" />
    <slot :disabled :create></slot>
  </b-busy>
</template>
