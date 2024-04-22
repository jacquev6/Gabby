<script setup>
import { ref, onMounted } from 'vue'


// WARNING: this component doesn't handle well when its props are changed after it's mounted.
const props = defineProps({
  width: Number,
  height: Number,
  transform: Array,
  textContent: Array,
})

const emit = defineEmits([
  'text-selected',  // (text: string, point: {clientX: number, clientY: number}) => void
])

const canvas = ref(null)
var context = null
var textSpacingTolerance = 0

onMounted(() => {
  context = canvas.value.getContext('2d')

  canvas.value.width = props.width
  canvas.value.height = props.height
  context.setTransform(
    props.transform[0], props.transform[1], props.transform[2], props.transform[3], props.transform[4], props.transform[5])

  // Somewhat arbitrary. If the tolerance is too small, then the selected text will contain too many spaces,
  // not a big deal. If the tolerance is too big, then the selected text could contain too few spaces,
  // which is a problem.
  textSpacingTolerance = Math.min(props.width, props.height) / 1e3
  // console.log('textSpacingTolerance', textSpacingTolerance)
})


var startPoint = null

function pointerdown(event) {
  startPoint = makeCanvasPoint(event)
  canvas.value.setPointerCapture(event.pointerId)
}

function pointermove(event) {
  if (startPoint !== null) {
    clearCanvas()

    const r = selectionRectangle(startPoint, makeCanvasPoint(event))

    context.save()
    context.beginPath()
    for (var item of props.textContent.filter(r.contains)) {
      context.rect(item.left, item.bottom, item.width, item.height)
    }
    context.fillStyle = 'rgba(255, 255, 0, 0.5)'
    context.strokeStyle = 'rgba(255, 128, 0, 0.5)'
    context.fill()
    context.stroke()
    context.restore()

    context.beginPath()
    context.rect(r.minX, r.minY, r.maxX - r.minX, r.maxY - r.minY)
    context.stroke()
  }
}

function pointerup(event) {
  canvas.value.releasePointerCapture(event.pointerId)
  if (startPoint !== null) {
    clearCanvas()

    const stopPoint = makeCanvasPoint(event)
    const r = selectionRectangle(startPoint, stopPoint)

    const lines = ['']
    var previousItem = null
    const items = []
    for (const item of props.textContent.filter(r.contains)) {
      items.push(item)
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
      emit(
        'text-selected',
        text,
        {clientX: event.clientX, clientY: event.clientY},
        items,
        {start: {x: startPoint.x, y: startPoint.y}, stop: {x: stopPoint.x, y: stopPoint.y}},
      )
    }

    startPoint = null
  }
}

function makeCanvasPoint(event) {
  const rect = canvas.value.getBoundingClientRect()
  const scaleX = canvas.value.width / rect.width
  const scaleY = canvas.value.height / rect.height
  return context.getTransform().inverse().transformPoint(
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

function clearCanvas() {
  context.save()
  context.setTransform(1, 0, 0, 1, 0, 0)
  context.clearRect(0, 0, canvas.value.width, canvas.value.height)
  context.restore()
}
</script>

<template>
  <canvas ref="canvas" @pointerdown="pointerdown" @pointermove="pointermove" @pointerup="pointerup"></canvas>
</template>
