<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import type { PDFPageProxy, RenderTask } from 'pdfjs-dist/types/src/pdf'
// @ts-ignore/* Temporary untyped */
import * as untypedPdfjs from 'pdfjs-dist/build/pdf'
import type PdfjsType from 'pdfjs-dist/types/src/pdf'

import { BBusy } from './opinion/bootstrap'


const { RenderingCancelledException } = untypedPdfjs as typeof PdfjsType

defineOptions({
  inheritAttrs: false,
})

const props = defineProps<{
  page: PDFPageProxy,
}>()

const canvas = ref<HTMLCanvasElement | null>(null)
const context = computed(() => canvas.value?.getContext('2d'))

const width = ref(210)
const height = ref(297)
const transform = ref<number[] | null>(null)

var renderTask : RenderTask | null = null
const busy = ref(false)

async function draw() {
  console.assert(props.page)

  const canvasContext = context.value
  if (canvasContext) {
    const startTime = performance.now()

    busy.value = true
    var resetOnExit = true

    try {
      const viewport = props.page.getViewport({scale: 1.5})
      height.value = viewport.height
      width.value = viewport.width
      transform.value = viewport.transform

      renderTask?.cancel()
      // @todo(Project management, later) Disable Chromium's warning:
      // > Canvas2D: Multiple readback operations using getImageData are faster with the willReadFrequently attribute set to true.
      // Unlikely, this seems to originate from canvases internal to PDF.js, not from our canvases.
      renderTask = props.page.render({canvasContext, viewport})
      try {
        await renderTask.promise
      } catch (e) {
        if (e instanceof RenderingCancelledException) {
          console.warn('Was interrupted rendering page', props.page.pageNumber, 'after', Math.round(performance.now() - startTime), 'ms')
          resetOnExit = false
          return
        } else {
          console.error('Failed to render page', props.page.pageNumber)
          throw e
        }
      }
      console.info('Rendered page', props.page.pageNumber, 'in', Math.round(performance.now() - startTime), 'ms')
    } finally {
      if (resetOnExit) {
        renderTask = null
        busy.value = false
      }
    }
  }
}

watch([() => props.page, context], draw, {immediate: true})

defineExpose({width, height, transform})
</script>

<template>
  <BBusy size="7rem" :busy>
    <canvas
      ref="canvas"
      :width :height
      v-bind="$attrs"
    ></canvas>
  </BBusy>
</template>
