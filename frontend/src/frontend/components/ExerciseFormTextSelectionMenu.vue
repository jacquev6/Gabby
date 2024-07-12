<script setup lang="ts">
import { ref, computed, watch } from 'vue'

import FloatingModal from './FloatingModal.vue'
import { BLabeledTextarea, BLabeledCheckbox } from './opinion/bootstrap'


const props = defineProps<{
  number: string,
  text: string,
  reference: {x: number, y: number},
}>()

const show = defineModel<boolean>('show')

const emit = defineEmits<{
  extractionEvent: [event: object],
}>()

const canStripExerciceNumber = computed(() => props.number !== '' && props.text.startsWith(props.number))
const doStripExerciceNumber = ref(true)

const selectedText = ref<typeof BLabeledTextarea | null>(null)

const textToAdd = ref('')
watch(
  [() => props.text, doStripExerciceNumber],
  () => {
    textToAdd.value = canStripExerciceNumber.value && doStripExerciceNumber.value ? props.text.slice(props.number.length).trimStart() : props.text
  },
  {immediate: true})
</script>

<template>
  <FloatingModal
    v-if="show" @shown="selectedText.focus()" @hidden="show = false"
    :title="$t('selectedText')"
    :reference
  >
    <BLabeledCheckbox :label="$t('doStripExerciceNumber')" v-model="doStripExerciceNumber" :disabled="!canStripExerciceNumber" />
    <BLabeledTextarea ref="selectedText" :maxRows="15" v-model="textToAdd" @change="emit('extractionEvent', {kind: 'SelectedTextEdited', value: textToAdd})" />

    <slot :textToAdd :hide="() => { show = false }"></slot>
  </FloatingModal>
</template>
