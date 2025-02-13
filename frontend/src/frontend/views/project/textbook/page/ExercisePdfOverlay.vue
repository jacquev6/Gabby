<script setup lang="ts">
import { ref, watch } from 'vue'
import { nextTick } from 'vue'
import type { PDFPageProxy } from 'pdfjs-dist'

import RectanglesHighlighter, { type Rectangle } from './RectanglesHighlighter.vue'
import TextPicker, { type SelectedText } from './TextPicker.vue'
import type { PdfFile, ParsedExercise, InCache, Exists } from '$frontend/stores/api'
import TextSelectionModal from './TextSelectionModal.vue'
import { type Model } from './ExerciseFieldsForm.vue'
import type { TextualFieldName } from './ExerciseFieldsForm.vue'
import type ExerciseFieldsForm from './ExerciseFieldsForm.vue'


const textSelectionModal = ref<InstanceType<typeof TextSelectionModal> | null>(null)

const props = defineProps<{
  pdfFile: PdfFile & InCache & Exists
  width: number
  height: number
  transform: number[]
  greyRectangles: Rectangle[]
  surroundedRectangles: Rectangle[]
  pdf: any/* @todo Type */
  fields: InstanceType<typeof ExerciseFieldsForm>
  parsedExercise: ParsedExercise & InCache & Exists
}>()

const model = defineModel<Model>({required: true})

function textSelected(pdfFile: PdfFile, pdf: {page: PDFPageProxy}, selectedText: SelectedText, point: {clientX: number, clientY: number}, rectangle: Rectangle) {
  console.assert(pdfFile.inCache && pdfFile.exists)
  console.assert(pdfFile.relationships.namings.length > 0)
  console.assert(pdfFile.relationships.namings[0].inCache && pdfFile.relationships.namings[0].exists)
  console.assert(textSelectionModal.value !== null)
  textSelectionModal.value.show({
    selectedText,
    at: {x: point.clientX, y: point.clientY},
    pdfSha256: pdfFile.attributes.sha256,
    pdfPage: pdf.page.pageNumber,
    rectangle,
  })
}

const suffixToHighlight = ref<{fieldName: TextualFieldName, text: string} | null>(null)
function highlightSuffix(fieldName: TextualFieldName, text: string) {
  suffixToHighlight.value = {fieldName, text}
}

watch(() => props.parsedExercise, () => {
  if (suffixToHighlight.value !== null) {
    const {fieldName, text} = suffixToHighlight.value
    suffixToHighlight.value = null
    nextTick(() => {
      props.fields.highlightSuffix(fieldName, text)
    })
  }
})
</script>

<template>
  <TextSelectionModal ref="textSelectionModal" v-model="model" @textAdded="highlightSuffix" />
  <RectanglesHighlighter
    v-if="pdfFile.inCache && pdfFile.exists"
    class="img w-100" style="position: absolute; top: 0; left: 0"
    :width :height :transform
    :greyRectangles
    :surroundedRectangles
  />
  <TextPicker
    class="img w-100" style="position: absolute; top: 0; left: 0"
    :width :height :transform
    :textContent="pdf.textContent"
    @textSelected="(text, point, rectangle) => textSelected(pdfFile, pdf, text, point, rectangle)"
  />
</template>
