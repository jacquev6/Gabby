<script setup>
import { onMounted } from 'vue'

const props = defineProps({
  src: String,
  page: Number,
})

const emit = defineEmits([
  'text-selected',  // (text: string, point: {clientX: number, clientY: number}) => void
])

// @todo Upgrade pdfjs-dist. 2.4.456 is OK but I couldn't get more recent versions to work.
// (Some versions result in pdfjs being undefined; others juste fail to import.)
import pdfjs from 'pdfjs-dist/build/pdf'
pdfjs.GlobalWorkerOptions.workerSrc = `https://cdn.jsdelivr.net/npm/pdfjs-dist@${pdfjs.version}/build/pdf.worker.min.js`

var textContent = []
var textSpacingTolerance = 0

var container = null
var pdfCanvas = null
var pdfContext = null
var uiCanvas = null
var uiContext = null

onMounted(async () => {
  var pdf = await pdfjs.getDocument(props.src).promise
  var page = await pdf.getPage(1)

  var scale = 1
  var viewport = page.getViewport({scale})
  container.style.width = (viewport.width + 2) + 'px'
  container.style.height = (viewport.height + 2) + 'px'
  pdfCanvas.height = viewport.height
  pdfCanvas.width = viewport.width
  uiCanvas.height = viewport.height
  uiCanvas.width = viewport.width

  // Somewhat arbitrary. If the tolerance is too small, then the selected text will contain to many spaces,
  // not a big deal. If the tolerance is too big, then the selected text could contain too few spaces,
  // which is a problem.
  textSpacingTolerance = Math.min(viewport.width, viewport.height) / 1e3
  // console.log('textSpacingTolerance', textSpacingTolerance)

  pdfContext = pdfCanvas.getContext('2d')
  uiContext = uiCanvas.getContext('2d')
  uiContext.setTransform(viewport.transform[0], viewport.transform[1], viewport.transform[2], viewport.transform[3], viewport.transform[4], viewport.transform[5])

  await page.render({
    canvasContext: pdfContext,
    viewport,
  }).promise

  textContent = await page.getTextContent()
  for (var item of textContent.items) {
    item.left = item.transform[4]
    item.right = item.transform[4] + item.width
    item.bottom = item.transform[5]
    item.top = item.transform[5] + item.height
    delete item.transform
  }
})

var startPoint = null

function pointerdown(event) {
  startPoint = makeCanvasPoint(event)
  uiCanvas.setPointerCapture(event.pointerId)
}

function pointermove(event) {
  if (startPoint !== null) {
    clearCanvas()

    const r = selectionRectangle(startPoint, makeCanvasPoint(event))

    uiContext.save()
    uiContext.beginPath()
    for (var item of textContent.items.filter(r.contains)) {
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
  uiCanvas.releasePointerCapture(event.pointerId)
  if (startPoint !== null) {
    clearCanvas()

    const r = selectionRectangle(startPoint, makeCanvasPoint(event))

    var lines = ['']
    var previousItem = null
    for (var item of textContent.items.filter(r.contains)) {
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
        text += line + '\n'
      }
    }

    if (text !== '') {
      emit('text-selected', text, {clientX: event.clientX, clientY: event.clientY})
    }

    startPoint = null
  }
}

function makeCanvasPoint(event) {
  const rect = uiCanvas.getBoundingClientRect()
  return uiContext.getTransform().inverse().transformPoint(
    new DOMPoint(event.clientX - rect.left, event.clientY - rect.top)
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

function clearCanvas() {
  uiContext.save()
  uiContext.setTransform(1, 0, 0, 1, 0, 0)
  uiContext.clearRect(0, 0, uiCanvas.width, uiCanvas.height)
  uiContext.restore()
}
</script>

<template>
  <p>Page {{ page }} of {{ src }}:</p>
  <div ref="container" class="container">
    <canvas ref="pdfCanvas" class="pdf"></canvas>
    <canvas ref="uiCanvas" class="ui" @pointerdown="pointerdown" @pointermove="pointermove" @pointerup="pointerup"></canvas>
  </div>
</template>

<style scoped>
div.container {
  position: relative;
  border: 1px solid black;
}

canvas {
  position: absolute;
  left: 0;
  top: 0;
}

canvas.pdf {
  z-index: 0;
}

canvas.ui {
  z-index: 1;
}
</style>
