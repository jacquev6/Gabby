<script lang="ts">
import type { Exercise, Exists, InCache } from '$/frontend/stores/api'
import type { PdfRectangle } from '$/frontend/stores/api'

export type Point = { x: number, y: number }
export type Rectangle = { start: Point, stop: Point }

export function makeBoundingRectangle(/* @todo pdf_sha256: string, pdf_page: number,*/ rectangles: PdfRectangle[]) {
  console.assert(rectangles.every(r => r.coordinates === 'pdfjs'))

  let relevantRectangles = rectangles.filter(
    r => /* @todo r.pdf_sha256 === pdf_sha256 && r.pdf_page === pdf_page
    && */ r.role !== 'bounding'
    && r.coordinates === 'pdfjs'
  )

  // Special case where the exercise only has role='bounding' rectangle(s). Should only happen for test fixture 'test-exercises'.
  if (relevantRectangles.length === 0) {
    relevantRectangles = rectangles
  }

  if (relevantRectangles.length === 0) {
    return null
  } else {
    const left = Math.min(...relevantRectangles.map(r => r.start.x), ...relevantRectangles.map(r => r.stop.x));
    const right = Math.max(...relevantRectangles.map(r => r.start.x), ...relevantRectangles.map(r => r.stop.x));
    const top = Math.min(...relevantRectangles.map(r => r.start.y), ...relevantRectangles.map(r => r.stop.y));
    const bottom = Math.max(...relevantRectangles.map(r => r.start.y), ...relevantRectangles.map(r => r.stop.y));
    return { start: { x: left, y: top }, stop: { x: right, y: bottom } };
  }
}

export function makeBoundingRectangles(/* @todo pdf_sha256: string, pdf_page: number,*/ exercises: readonly (Exercise & InCache & Exists)[]) {
  return exercises
    .map(exercise => makeBoundingRectangle(exercise.attributes.rectangles))
    .filter((x): x is Rectangle => x !== null)
}
</script>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'


const props = defineProps<{
  width: number,
  height: number,
  transform: number[],
  greyRectangles: Rectangle[],
  surroundedRectangles: Rectangle[],
}>()

const canvas = ref<HTMLCanvasElement | null>(null)
const context = computed(() => canvas.value?.getContext('2d') ?? null)

interface DrawnRectangle {
  left: number
  top: number
  width: number
  height: number
}
interface DrawnRectangles {
  grey: DrawnRectangle[]
  surrounded: DrawnRectangle[]
}
const drawnRectangles = ref<DrawnRectangles>({grey: [], surrounded: []})

watch([props, context], () => {
  console.assert(canvas.value !== null)
  console.assert(context.value !== null)

  canvas.value.width = props.width
  canvas.value.height = props.height

  context.value.setTransform(props.transform[0], props.transform[1], props.transform[2], props.transform[3], props.transform[4], props.transform[5])

  drawnRectangles.value = {grey: [], surrounded: []}

  for (const rectangle of props.greyRectangles) {
    const left = Math.min(rectangle.start.x, rectangle.stop.x)
    const top = Math.min(rectangle.start.y, rectangle.stop.y)
    const width = Math.abs(rectangle.start.x - rectangle.stop.x)
    const height = Math.abs(rectangle.start.y - rectangle.stop.y)
    drawnRectangles.value.grey.push({left, top, width, height})
    context.value.rect(left, top, width, height)
  }
  context.value.fillStyle = 'rgba(128, 128, 128, 0.4)'
  context.value.fill()
  
  context.value.beginPath()
  for (const rectangle of props.surroundedRectangles) {
    const left = Math.min(rectangle.start.x, rectangle.stop.x)
    const top = Math.min(rectangle.start.y, rectangle.stop.y)
    const width = Math.abs(rectangle.start.x - rectangle.stop.x)
    const height = Math.abs(rectangle.start.y - rectangle.stop.y)
    drawnRectangles.value.surrounded.push({left, top, width, height})
    context.value.rect(left, top, width, height)
  }
  context.value.fillStyle = 'rgb(0, 0, 255, 0.15)'
  context.value.fill()
})
</script>

<template>
  <canvas ref="canvas" :data-cy-drawnRectangles="JSON.stringify(drawnRectangles)"></canvas>
</template>
