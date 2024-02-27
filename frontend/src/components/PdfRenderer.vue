<script setup>
import { ref, computed, watch } from 'vue'

import Loading from './Loading.vue'


defineOptions({
  inheritAttrs: false,
})

const props = defineProps({
  pdf: {
    type: Object,
    required: true,
  },
  page: {
    type: Number,
    required: true,
  },
})

const canvas = ref(null)
const context = computed(() => canvas.value?.getContext('2d'))

const width = ref(210)
const height = ref(297)
const transform = ref(null)

var renderTask = null
const busy = ref(false)

async function draw() {
  const pdf = props.pdf
  const page = props.page

  console.info('PdfRendered rendering page ', page, '/', pdf.numPages)
  const startTime = performance.now()

  busy.value = true
  var resetOnExit = true
  width.value = 2100
  height.value = 2970

  try {
    const pdfPage = await pdf.getPage(page)

    const viewport = pdfPage.getViewport({scale: 1.5})
    height.value = viewport.height
    width.value = viewport.width
    transform.value = viewport.transform

    renderTask?.cancel()
    // @todo(Project management, later) Disable Chromium's warning:
    // > Canvas2D: Multiple readback operations using getImageData are faster with the willReadFrequently attribute set to true.
    // Unlikely, this seems to originate from canvases internal to PDF.js, not from our canvases.
    renderTask = pdfPage.render({
      canvasContext: context.value,
      viewport,
    })
    try {
      await renderTask.promise
    } catch (e) {
      if (e.name === 'RenderingCancelledException') {
        console.warn('PdfRendered was interrupted rendering page', page, '/', pdf.numPages, 'after', performance.now() - startTime, 'ms')
        resetOnExit = false
        return
      } else {
        console.error('PdfRendered failed to render page', page, '/', pdf.numPages)
        throw e
      }
    }
    console.info('PdfRendered rendered page', page, '/', pdf.numPages, 'in', performance.now() - startTime, 'ms')
  } finally {
    if (resetOnExit) {
      renderTask = null
      busy.value = false
    }
  }
}

watch(() => [props.pdf, props.page, context], draw, {immediate: true})

defineExpose({
  width, height, transform,
})
</script>

<template>
  <loading size="7rem" :loading="busy">
    <canvas
      ref="canvas"
      :width="width" :height="height"
      v-bind="$attrs"
    ></canvas>
  </loading>
</template>
