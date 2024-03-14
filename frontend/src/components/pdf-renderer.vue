<script setup>
import { ref, computed, watch } from 'vue'

import { BBusy } from './opinion/bootstrap'


defineOptions({
  inheritAttrs: false,
})

const props = defineProps({
  page: {
    type: Object,
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

async function draw([page, canvasContext]) {
  console.assert(page)

  if (canvasContext) {
    const startTime = performance.now()

    busy.value = true
    var resetOnExit = true

    try {
      const viewport = page.getViewport({scale: 1.5})
      height.value = viewport.height
      width.value = viewport.width
      transform.value = viewport.transform

      renderTask?.cancel()
      // @todo(Project management, later) Disable Chromium's warning:
      // > Canvas2D: Multiple readback operations using getImageData are faster with the willReadFrequently attribute set to true.
      // Unlikely, this seems to originate from canvases internal to PDF.js, not from our canvases.
      renderTask = page.render({canvasContext, viewport})
      try {
        await renderTask.promise
      } catch (e) {
        if (e.name === 'RenderingCancelledException') {
          console.warn('Was interrupted rendering page', page.pageNumber, 'after', Math.round(performance.now() - startTime), 'ms')
          resetOnExit = false
          return
        } else {
          console.error('Failed to render page', page.pageNumber)
          throw e
        }
      }
      console.info('Rendered page', page.pageNumber, 'in', Math.round(performance.now() - startTime), 'ms')
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
  <b-busy size="7rem" :busy>
    <canvas
      ref="canvas"
      :width :height
      v-bind="$attrs"
    ></canvas>
  </b-busy>
</template>
