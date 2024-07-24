<script setup lang="ts">
import { ref, computed, watch } from 'vue'

import { BLabeledCheckbox, BLabeledTextarea, BButton } from '$/frontend/components/opinion/bootstrap'
import { textualFieldNames } from '$/frontend/components/ExerciseFieldsForm.vue'
import type { Model, TextualFieldName } from '$frontend/components/ExerciseFieldsForm.vue'
import FloatingModal from '$frontend/components/FloatingModal.vue'
import type { Point } from '$frontend/components/FloatingModal.vue'



const props = defineProps<{
  extractionEvents: object[],
}>()

const model = defineModel<Model>({required: true})

const emit = defineEmits<{
  textAdded: [fieldName: TextualFieldName, text: string, range: {start: number, end: number}],
}>()

const modal = ref<InstanceType<typeof FloatingModal> | null>(null)
const textarea = ref<InstanceType<typeof BLabeledTextarea> | null>(null)

const selectedText = ref('')
const textToAdd = ref('')

const canStripExerciceNumber = computed(() => model.value.number !== '' && selectedText.value.startsWith(model.value.number))
const doStripExerciceNumber = ref(true)

function show(text: string, at: Point) {
  console.assert(modal.value !== null)
  selectedText.value = text
  modal.value.show(at)
}

watch([selectedText, doStripExerciceNumber], () => {
  if (canStripExerciceNumber.value && doStripExerciceNumber.value) {
    textToAdd.value = selectedText.value.slice(model.value.number.length).trimStart()
  } else {
    textToAdd.value = selectedText.value
  }
})

watch(computed(() => modal.value !== null && modal.value.active), active => {
  if (!active) {
    selectedText.value = ''
  }
})

function addTextTo(fieldName: TextualFieldName) {
  const valueBefore = model.value[fieldName]
  if (model.value[fieldName] !== '' && !model.value[fieldName].endsWith('\n')) {
    model.value[fieldName] += '\n'
  }
  const start = model.value[fieldName].length
  const end = start + textToAdd.value.length
  model.value[fieldName] += textToAdd.value
  console.assert(modal.value !== null)
  modal.value.hide()
  props.extractionEvents.push({kind: `SelectedTextAddedTo${fieldName.charAt(0).toUpperCase()}${fieldName.slice(1)}`, valueBefore, valueAfter: model.value[fieldName]})
  emit('textAdded', fieldName, textToAdd.value, {start, end})
}

defineExpose({
  show,
})
</script>

<template>
  <FloatingModal ref="modal">
    <template #header>
      <h1>{{ $t('selectedText') }}</h1>
    </template>

    <BLabeledCheckbox :label="$t('doStripExerciceNumber')" v-model="doStripExerciceNumber" :disabled="!canStripExerciceNumber" />
    <BLabeledTextarea ref="textarea" :maxRows="15" v-model="textToAdd" @change="extractionEvents.push({kind: 'SelectedTextEdited', value: textToAdd})" />

    <!-- <p><BButton secondary @click="state.boundingRectangle = selectedRectangle; hide()">{{ $t('setBoundingRect') }}</BButton></p> -->
    <p>{{ $t('addTo') }}</p>
    <p>
      <template v-for="fieldName in textualFieldNames">
        <BButton primary @click="addTextTo(fieldName)">{{ $t(fieldName) }}</BButton>
        <wbr />
      </template>
    </p>
  </FloatingModal>
</template>
