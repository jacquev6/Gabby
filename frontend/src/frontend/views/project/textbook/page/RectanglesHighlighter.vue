<script setup lang="ts">
import { ref, computed, watch } from 'vue'


export type Rectangle = { start: { x: number, y: number }, stop: { x: number, y: number } }

const props = defineProps<{
  width: number,
  height: number,
  transform: number[],
  greyRectangles: Rectangle[],
  surroundedRectangles: Rectangle[],
}>()

const canvas = ref<HTMLCanvasElement | null>(null)
const context = computed(() => canvas.value?.getContext('2d') ?? null)

watch([props, context], () => {
  console.assert(canvas.value !== null)
  console.assert(context.value !== null)

  canvas.value.width = props.width
  canvas.value.height = props.height

  context.value.setTransform(props.transform[0], props.transform[1], props.transform[2], props.transform[3], props.transform[4], props.transform[5])

  for (const rectangle of props.greyRectangles) {
    const left = Math.min(rectangle.start.x, rectangle.stop.x)
    const top = Math.min(rectangle.start.y, rectangle.stop.y)
    const width = Math.abs(rectangle.start.x - rectangle.stop.x)
    const height = Math.abs(rectangle.start.y - rectangle.stop.y)
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
    context.value.rect(left, top, width, height)
  }
  context.value.strokeStyle = 'rgb(0, 0, 255)'
  context.value.lineWidth = 2
  context.value.stroke()
})
</script>

<template>
  <canvas ref="canvas"></canvas>
</template>
