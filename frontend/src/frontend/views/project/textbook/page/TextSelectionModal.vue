<script setup lang="ts">
import { ref, computed, watch } from 'vue'

import { BLabeledCheckbox, BLabeledTextarea, BButton } from '$/frontend/components/opinion/bootstrap'
import { textualFieldNames } from '$/frontend/components/ExerciseFieldsForm.vue'
import type { Model, TextualFieldName } from '$frontend/components/ExerciseFieldsForm.vue'
import { BModal } from '$frontend/components/opinion/bootstrap'
import type { Point, Rectangle } from './RectanglesHighlighter.vue'


const model = defineModel<Model>({required: true})

const emit = defineEmits<{
  textAdded: [fieldName: TextualFieldName, text: string],
}>()

const modal = ref<InstanceType<typeof BModal> | null>(null)
const textarea = ref<InstanceType<typeof BLabeledTextarea> | null>(null)

const selectedText = ref('')
const textToAdd = ref('')
const pdfSha256 = ref('')
const pdfPage = ref(0)
const start = ref<Point>({x: 0, y: 0})
const stop = ref<Point>({x: 0, y: 0})

const canStripExerciceNumber = computed(() => model.value.number !== '' && selectedText.value.startsWith(model.value.number))
const doStripExerciceNumber = ref(true)

function show(options: {
  selectedText: string
  at: Point
  pdfSha256: string
  pdfPage: number
  rectangle: Rectangle
}) {
  console.assert(modal.value !== null)
  selectedText.value = options.selectedText
  pdfSha256.value = options.pdfSha256
  pdfPage.value = options.pdfPage
  start.value = options.rectangle.start
  stop.value = options.rectangle.stop
  modal.value.show({at: options.at})
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
  if (model.value[fieldName] !== '' && !model.value[fieldName].endsWith('\n')) {
    model.value[fieldName] += '\n'
  }
  model.value[fieldName] += textToAdd.value
  model.value.rectangles.push({
    pdf_sha256: pdfSha256.value,
    pdf_page: pdfPage.value,
    coordinates: 'pdfjs',
    start: start.value,
    stop: stop.value,
    text: textToAdd.value,
    role: fieldName,
  })
  console.assert(modal.value !== null)
  modal.value.hide()
  emit('textAdded', fieldName, textToAdd.value)
}

defineExpose({
  show,
})
</script>

<template>
  <BModal ref="modal" :fade="false">
    <template #header>
      <h1>{{ $t('selectedText') }}</h1>
    </template>

    <template #body>
      <BLabeledCheckbox :label="$t('doStripExerciceNumber')" v-model="doStripExerciceNumber" :disabled="!canStripExerciceNumber" />
      <BLabeledTextarea ref="textarea" :maxRows="15" v-model="textToAdd" />

      <p>{{ $t('addTo') }}</p>
      <p>
        <template v-for="fieldName in textualFieldNames">
          <BButton primary @click="addTextTo(fieldName)">{{ $t(fieldName) }}</BButton>
          <wbr />
        </template>
      </p>
    </template>
  </BModal>
</template>
