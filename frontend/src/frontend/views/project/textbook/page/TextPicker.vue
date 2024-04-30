<script setup lang="ts">
import { ref, computed, watch } from 'vue'


export interface TextItem {
  left: number,
  right: number,
  width: number,
  top: number,
  bottom: number,
  height: number,
  str: string,
}

// WARNING: this component doesn't handle well when its props are changed after it's mounted.
const props = defineProps<{
  width: number,
  height: number,
  transform: number[],
  textContent: TextItem[],
}>()

const emit = defineEmits<{
  textSelected: [text: string, point: {clientX: number, clientY: number}, items: TextItem[], rectangle: {start: {x: number, y: number}, stop: {x: number, y: number}}],
}>()

const canvas = ref<HTMLCanvasElement | null>(null)
const context = computed(() => canvas.value?.getContext('2d') ?? null)
const textSpacingTolerance = computed(() =>
  // Somewhat arbitrary. If the tolerance is too small, then the selected text will contain too many spaces,
  // not a big deal. If the tolerance is too big, then the selected text could contain too few spaces,
  // which is a problem.
  Math.min(props.width, props.height) / 1e3
  // console.log('textSpacingTolerance', textSpacingTolerance)
)

watch([props, context], () => {
  console.assert(canvas.value !== null)
  console.assert(context.value !== null)

  canvas.value.width = props.width
  canvas.value.height = props.height

  context.value.setTransform(props.transform[0], props.transform[1], props.transform[2], props.transform[3], props.transform[4], props.transform[5])
})

interface Point {
  x: number,
  y: number,
}

var startPoint: Point | null = null

function pointerdown(event: any/* @todo Type */) {
  console.assert(canvas.value !== null)

  startPoint = makeCanvasPoint(event)
  canvas.value.setPointerCapture(event.pointerId)
}

function pointermove(event: any/* @todo Type */) {
  console.assert(context.value !== null)

  if (startPoint !== null) {
    clearCanvas()

    const r = selectionRectangle(startPoint, makeCanvasPoint(event))

    context.value.save()
    context.value.beginPath()
    for (var item of props.textContent.filter(r.contains)) {
      context.value.rect(item.left, item.bottom, item.width, item.height)
    }
    context.value.fillStyle = 'rgba(255, 255, 0, 0.5)'
    context.value.strokeStyle = 'rgba(255, 128, 0, 0.5)'
    context.value.fill()
    context.value.stroke()
    context.value.restore()

    context.value.beginPath()
    context.value.rect(r.minX, r.minY, r.maxX - r.minX, r.maxY - r.minY)
    context.value.stroke()
  }
}

function pointerup(event: any/* @todo Type */) {
  console.assert(canvas.value !== null)

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
        if (Math.abs(previousItem.bottom - item.bottom) > textSpacingTolerance.value) {
          lines.push('')
        } else if(previousItem.right + textSpacingTolerance.value < item.left) {
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
        'textSelected',
        text,
        {clientX: event.clientX, clientY: event.clientY},
        items,
        {start: {x: startPoint.x, y: startPoint.y}, stop: {x: stopPoint.x, y: stopPoint.y}},
      )
    }

    startPoint = null
  }
}

function makeCanvasPoint(event: any/* @todo Type */) {
  console.assert(canvas.value !== null)
  console.assert(context.value !== null)

  const rect = canvas.value.getBoundingClientRect()
  const scaleX = canvas.value.width / rect.width
  const scaleY = canvas.value.height / rect.height
  return context.value.getTransform().inverse().transformPoint(
    new DOMPoint((event.clientX - rect.left) * scaleX, (event.clientY - rect.top) * scaleY)
  )
}

function selectionRectangle(startPoint: Point, endPoint: Point) {
  const minX = Math.min(startPoint.x, endPoint.x)
  const maxX = Math.max(startPoint.x, endPoint.x)
  const minY = Math.min(startPoint.y, endPoint.y)
  const maxY = Math.max(startPoint.y, endPoint.y)

  return {
    minX, maxX, minY, maxY,
    contains(item: TextItem) {
      return (
        item.left >= minX && item.right <= maxX
        && item.bottom >= minY && item.top <= maxY
      )
    },
  }
}

function clearCanvas() {
  console.assert(canvas.value !== null)
  console.assert(context.value !== null)

  context.value.save()
  context.value.setTransform(1, 0, 0, 1, 0, 0)
  context.value.clearRect(0, 0, canvas.value.width, canvas.value.height)
  context.value.restore()
}
</script>

<template>
  <canvas ref="canvas" @pointerdown="pointerdown" @pointermove="pointermove" @pointerup="pointerup"></canvas>
</template>
