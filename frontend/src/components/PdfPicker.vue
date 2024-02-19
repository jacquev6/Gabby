<script setup>
import { ref, onMounted, watch } from 'vue'
import * as pdfjs from 'pdfjs-dist/build/pdf'
pdfjs.GlobalWorkerOptions.workerSrc = '/pdf.worker.min.js'
import shajs from 'sha.js'


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

var textSpacingTolerance = 0

var container = null
const pdfCanvas = ref(null)
var pdfContext = null
const uiCanvas = ref(null)
var uiContext = null
var loadedPdf = null
const busy = ref(false)

var document = null
var textContent = []

console.info('PdfPicker::setup', props.pdf)

onMounted(async () => {
  console.info('PdfPicker::onMounted', props.pdf, pdfCanvas, uiCanvas)

  pdfContext = pdfCanvas.value.getContext('2d')
  uiContext = uiCanvas.value.getContext('2d')

  await load()
  await display(1)
})

watch(() => props.pdf, () => load().then(() => display(1)))

async function load() {
  console.info('PdfPicker loading ', props.pdf)
  busy.value = true
  try {
    pdfCanvas.value.height = 2970
    pdfCanvas.value.width = 2100
    uiCanvas.value.height = 2970
    uiCanvas.value.width = 2100
    clearCanvas(pdfContext)
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
      return
    }
    const sha256 = await hexSha256(await document.getData())
    emit('loaded', sha256, document.numPages)
    loadedPdf = props.pdf
    console.info('PdfPicker loaded ', props.pdf)
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
    pdfCanvas.value.height = viewport.height
    pdfCanvas.value.width = viewport.width
    uiCanvas.value.height = viewport.height
    uiCanvas.value.width = viewport.width

    // Somewhat arbitrary. If the tolerance is too small, then the selected text will contain too many spaces,
    // not a big deal. If the tolerance is too big, then the selected text could contain too few spaces,
    // which is a problem.
    textSpacingTolerance = Math.min(viewport.width, viewport.height) / 1e3
    // console.log('textSpacingTolerance', textSpacingTolerance)

    uiContext.setTransform(viewport.transform[0], viewport.transform[1], viewport.transform[2], viewport.transform[3], viewport.transform[4], viewport.transform[5])

    renderTask?.cancel()
    // @todo(Project management, later) Disable Chromium's warning:
    // > Canvas2D: Multiple readback operations using getImageData are faster with the willReadFrequently attribute set to true.
    // Unlikely, this seems to originate from canvases internal to PDF.js, not from our canvases.
    renderTask = pdfPage.render({
      canvasContext: pdfContext,
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

    textContent = []
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

var startPoint = null

function pointerdown(event) {
  if (props.disabled) { return }
  startPoint = makeCanvasPoint(event)
  uiCanvas.value.setPointerCapture(event.pointerId)
}

function pointermove(event) {
  if (startPoint !== null) {
    clearCanvas(uiContext)

    const r = selectionRectangle(startPoint, makeCanvasPoint(event))

    uiContext.save()
    uiContext.beginPath()
    for (var item of textContent.filter(r.contains)) {
      uiContext.rect(item.left, item.bottom, item.width, item.height)
    }
    uiContext.fillStyle = 'rgba(255, 255, 0, 0.5)'
    uiContext.strokeStyle = 'rgba(255, 128, 0, 0.5)'
    uiContext.fill()
    uiContext.stroke()
    uiContext.restore()

    uiContext.beginPath()
    uiContext.rect(r.minX, r.minY, r.maxX - r.minX, r.maxY - r.minY)
    uiContext.stroke()
  }
}

function pointerup(event) {
  uiCanvas.value.releasePointerCapture(event.pointerId)
  if (startPoint !== null) {
    clearCanvas(uiContext)

    const r = selectionRectangle(startPoint, makeCanvasPoint(event))

    const lines = ['']
    var previousItem = null
    for (const item of textContent.filter(r.contains)) {
      if (previousItem !== null) {
        if (Math.abs(previousItem.bottom - item.bottom) > textSpacingTolerance) {
          lines.push('')
        } else if(previousItem.right + textSpacingTolerance < item.left) {
          lines[lines.length - 1] += ' '
        }
      }

      lines[lines.length - 1] += item.str
      previousItem = item
    }

    var text = ''
    for (var line of lines) {
      line = line.replace(/[ \t]+/g, ' ').trim()
      if (line !== '') {
        if (text !== '') {
          text += '\n'
        }
        text += line
      }
    }

    if (text !== '') {
      emit('text-selected', text, {clientX: event.clientX, clientY: event.clientY})
    }

    startPoint = null
  }
}

function makeCanvasPoint(event) {
  const rect = uiCanvas.value.getBoundingClientRect()
  const scaleX = uiCanvas.value.width / rect.width
  const scaleY = uiCanvas.value.height / rect.height
  return uiContext.getTransform().inverse().transformPoint(
    new DOMPoint((event.clientX - rect.left) * scaleX, (event.clientY - rect.top) * scaleY)
  )
}

function selectionRectangle(startPoint, endPoint) {
  const minX = Math.min(startPoint.x, endPoint.x)
  const maxX = Math.max(startPoint.x, endPoint.x)
  const minY = Math.min(startPoint.y, endPoint.y)
  const maxY = Math.max(startPoint.y, endPoint.y)

  return {
    minX, maxX, minY, maxY,
    contains(item) {
      return (
        item.left >= minX && item.right <= maxX
        && item.bottom >= minY && item.top <= maxY
      )
    },
  }
}

function clearCanvas(context) {
  context.save()
  context.setTransform(1, 0, 0, 1, 0, 0)
  context.clearRect(0, 0, uiCanvas.value.width, uiCanvas.value.height)
  context.restore()
}
</script>

<template>
  <div style="position: relative" ref="container">
    <canvas ref="pdfCanvas" class="img img-fluid" style="border: 1px solid black"></canvas>
    <canvas
      ref="uiCanvas" class="img img-fluid" style="position: absolute; top: 0; left: 0"
      @pointerdown="pointerdown" @pointermove="pointermove" @pointerup="pointerup"
    ></canvas>
    <div v-if="busy" class="d-flex justify-content-center align-items-center" style="position: absolute; top: 0; left: 0; height: 100%; width: 100%; background: rgba(0,0,0,0.5)">
      <div class="spinner-border" style="width: 7rem; height: 7rem;" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
  </div>
</template>
