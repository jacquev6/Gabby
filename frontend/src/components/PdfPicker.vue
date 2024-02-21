<script setup>
import { ref, reactive, onMounted, watch } from 'vue'
import * as pdfjs from 'pdfjs-dist/build/pdf'
pdfjs.GlobalWorkerOptions.workerSrc = '/pdf.worker.min.js'
import shajs from 'sha.js'

import TextPicker from './TextPicker.vue'


const props = defineProps({
  pdf: null,  // string or File, but I don't know yet how to say that in JS
  page: Number,
  disabled: Boolean,
})

const emit = defineEmits([
  'loading-failed',  // (e: Exception) => void
  'loaded',  // (sha256: string, pagesCount: number) => void
  'text-selected',  // (text: string, point: {clientX: number, clientY: number}) => void
])

const canvas = ref(null)
var context = null
var loadedPdf = null
const busy = ref(false)

var document = null
const textContent = reactive([])

onMounted(async () => {
  context = canvas.value.getContext('2d')

  await load()
  await display(1)
})

const width = ref(2970)
const height = ref(2100)
const transform = ref(null)

watch(() => props.pdf, () => load().then(() => display(1)))

async function load() {
  const startTime = performance.now()
  console.info('PdfPicker loading', props.pdf)
  busy.value = true
  try {
    height.value = 2970
    width.value = 2100
    clearCanvas()
    const arg = {}
    if (typeof props.pdf === 'string') {
      arg.url = props.pdf
    } else {
      arg.data = await props.pdf.arrayBuffer()
    }
    try {
      document = await pdfjs.getDocument(arg).promise
    } catch (e) {
      emit('loading-failed', e)
      console.error('PdfPicker failed to load', props.pdf, 'after', performance.now() - startTime, 'ms')
      throw e
    }
    const sha256 = await hexSha256(await document.getData())
    emit('loaded', sha256, document.numPages)
    loadedPdf = props.pdf
    console.info('PdfPicker loaded', props.pdf, 'in', performance.now() - startTime, 'ms')
  } finally {
    busy.value = false
  }
}

async function hexSha256(data) {
  return shajs('sha256').update(data).digest('hex')
}

watch(() => props.page, () => { if (loadedPdf === props.pdf) { display(props.page) } })

var renderTask = null

async function display(page) {
  busy.value = true
  var resetBusy = true
  try {
    if (!Number.isInteger(page)) {
      console.warn('Non-integer page', page, 'requested to PdfPicker')
      page = 1
    }
    if (page < 1) {
      console.warn('Page', page, '< 1 requested to PdfPicker')
      page = 1
    }
    if (page > document.numPages) {
      console.warn('Page', page, '>', document.numPages, 'requested to PdfPicker')
      page = document.numPages
    }
    console.info('PdfPicker displaying page ', page, '/', document.numPages)
    const startTime = performance.now()

    const pdfPage = await document.getPage(page)

    const viewport = pdfPage.getViewport({scale: 1.5})
    height.value = viewport.height
    width.value = viewport.width
    transform.value = viewport.transform

    renderTask?.cancel()
    // @todo(Project management, later) Disable Chromium's warning:
    // > Canvas2D: Multiple readback operations using getImageData are faster with the willReadFrequently attribute set to true.
    // Unlikely, this seems to originate from canvases internal to PDF.js, not from our canvases.
    renderTask = pdfPage.render({
      canvasContext: context,
      viewport,
    })
    try {
      await renderTask.promise
    } catch (e) {
      if (e.name === 'RenderingCancelledException') {
        console.warn('PdfPicker was interrupted displaying page', page, '/', document.numPages, 'after', performance.now() - startTime, 'ms')
        resetBusy = false
        return
      } else {
        console.error('PdfPicker failed to display page', page, '/', document.numPages)
        throw e
      }
    }
    renderTask = null
    console.info('PdfPicker displayed page', page, '/', document.numPages, 'in', performance.now() - startTime, 'ms')

    textContent.splice(0, textContent.length)
    for (const item of (await pdfPage.getTextContent()).items) {
      textContent.push({
        str: item.str,

        font: item.fontName,

        left: item.transform[4],
        width: item.width,
        right: item.transform[4] + item.width,
        bottom: item.transform[5],
        height: item.height,
        top: item.transform[5] + item.height,
      })
    }
  } finally {
    if (resetBusy) {
      busy.value = false
    }
  }
}

function clearCanvas() {
  context.save()
  context.setTransform(1, 0, 0, 1, 0, 0)
  context.clearRect(0, 0, width.value / 2, height.value / 2)
  context.restore()
}

function textSelected(text, point) {
  emit('text-selected', text, point)
}
</script>

<template>
  <div style="position: relative; border: 1px solid black">
    <canvas
      ref="canvas"
      class="img img-fluid"
      :width="width" :height="height"
    ></canvas>
    <text-picker
      v-if="!busy && !disabled"
      class="img img-fluid" style="position: absolute; top: 0; left: 0"
      :width="width" :height="height" :transform="transform"
      :textContent="textContent"
      @text-selected="textSelected"
    />
    <div v-if="busy" class="d-flex justify-content-center align-items-center" style="position: absolute; top: 0; left: 0; height: 100%; width: 100%; background: rgba(0,0,0,0.5)">
      <div class="spinner-border" style="width: 7rem; height: 7rem;" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
  </div>
</template>
