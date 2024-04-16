<script setup>
import { ref, computed, watch } from 'vue'

import FloatingModal from './floating-modal.vue'  // @todo Move into components
import { BLabeledTextarea, BLabeledCheckbox, BButton } from './opinion/bootstrap'


const props = defineProps({
  number: {type: String, required: true},
  text: {type: String, required: true},
  reference: {type: Object, required: true},
})

const show = defineModel('show', {type: Boolean})

const emit = defineEmits([
  'extractionEvent'  // Object => void
])

const canStripExerciceNumber = computed(() => props.number !== '' && props.text.startsWith(props.number))
const doStripExerciceNumber = ref(true)

const textToAdd = ref('')
watch(
  [() => props.text, doStripExerciceNumber],
  () => {
    textToAdd.value = canStripExerciceNumber.value && doStripExerciceNumber.value ? props.text.slice(props.number.length).trimStart() : props.text
  },
  {immediate: true})
</script>

<template>
  <floating-modal
    v-if="show" @dismissed="show = false"
    :title="$t('selectedText')"
    :reference
  >
    <b-labeled-checkbox :label="$t('doStripExerciceNumber')" v-model="doStripExerciceNumber" :disabled="!canStripExerciceNumber" />
    <b-labeled-textarea :label="$t('selectedText')" v-model="textToAdd" @change="emit('extractionEvent', {kind: 'SelectedTextEdited', value: textToAdd})" />

    <slot :textToAdd :hide="() => { show = false }"></slot>
  </floating-modal>
</template>
