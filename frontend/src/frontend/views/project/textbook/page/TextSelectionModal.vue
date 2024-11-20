<script setup lang="ts">
import { ref, computed, watch } from 'vue'

import { BLabeledCheckbox, BLabeledTextarea, BButton } from '$/frontend/components/opinion/bootstrap'
import { textualFieldNames } from '$/frontend/components/ExerciseFieldsForm.vue'
import type { Model, TextualFieldName } from '$frontend/components/ExerciseFieldsForm.vue'
import { BModal } from '$frontend/components/opinion/bootstrap'
import type { Point, Rectangle } from './RectanglesHighlighter.vue'
import type { SelectedText } from './TextPicker.vue'


const model = defineModel<Model>({required: true})

const emit = defineEmits<{
  textAdded: [fieldName: TextualFieldName, text: string],
}>()

const modal = ref<InstanceType<typeof BModal> | null>(null)
const textarea = ref<InstanceType<typeof BLabeledTextarea> | null>(null)

const selectedText = ref<SelectedText | null>(null)
const textToAdd = ref('')
const pdfSha256 = ref('')
const pdfPage = ref(0)
const start = ref<Point>({x: 0, y: 0})
const stop = ref<Point>({x: 0, y: 0})

const selectedString = computed(() => {
  if (selectedText.value === null) {
    return ''
  } else {
    if (doKeepAllLineEnds.value) {
      return selectedText.value.withAllLineEnds
    } else if (!doDetectLists.value) {
      return selectedText.value.withoutListsDetection
    } else {
      return selectedText.value.withoutLineEnds
    }
  }
})
const doKeepAllLineEnds = ref(false)
const doDetectLists = ref(true)

const canStripExerciceNumber = computed(() => model.value.number !== '' && selectedString.value.startsWith(model.value.number))
const doStripExerciceNumber = ref(true)


function show(options: {
  selectedText: SelectedText
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

watch([selectedString, doStripExerciceNumber], () => {
  if (canStripExerciceNumber.value && doStripExerciceNumber.value) {
    textToAdd.value = selectedString.value.slice(model.value.number.length).trimStart()
  } else {
    textToAdd.value = selectedString.value
  }
})

watch(computed(() => modal.value !== null && modal.value.active), active => {
  if (!active) {
    selectedText.value = null
  }
})

function addTextTo(fieldName: TextualFieldName) {
  console.assert(textToAdd.value.endsWith('\n'))
  if (model.value[fieldName] === '\n') {
    model.value[fieldName] = textToAdd.value
  } else {
    console.assert(model.value[fieldName].endsWith('\n'))
    model.value[fieldName] += textToAdd.value
  }
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
      <BLabeledCheckbox :label="$t('doKeepAllLineEnds')" v-model="doKeepAllLineEnds" />
      <BLabeledCheckbox :label="$t('doDetectLists')" v-model="doDetectLists" :disabled="doKeepAllLineEnds"/>
      <BLabeledTextarea ref="textarea" :enforceTrailingLineEnd="true" :maxRows="15" v-model="textToAdd" />

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
