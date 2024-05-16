<script setup lang="ts">
import { ref, computed, watch } from 'vue'


const props = defineProps<{
  width: number,
  height: number,
  transform: number[],
  rectangles: any/* @todo Type */[],
}>()

const canvas = ref<HTMLCanvasElement | null>(null)
const context = computed(() => canvas.value?.getContext('2d') ?? null)

watch([props, context], () => {
  console.assert(canvas.value !== null)
  console.assert(context.value !== null)

  canvas.value.width = props.width
  canvas.value.height = props.height

  context.value.setTransform(1, 0, 0, 1, 0, 0)
  context.value.clearRect(0, 0, props.width, props.height)
  context.value.fillStyle = 'rgba(128, 128, 128, 0.5)'
  context.value.fillRect(0, 0, props.width, props.height)

  context.value.setTransform(props.transform[0], props.transform[1], props.transform[2], props.transform[3], props.transform[4], props.transform[5])
  for (const rectangle of props.rectangles) {
    context.value.beginPath()
    const left = Math.min(rectangle.start.x, rectangle.stop.x)
    const top = Math.min(rectangle.start.y, rectangle.stop.y)
    const width = Math.abs(rectangle.start.x - rectangle.stop.x)
    const height = Math.abs(rectangle.start.y - rectangle.stop.y)
    context.value.clearRect(left, top, width, height)
  }
})
</script>

<template>
  <canvas ref="canvas"></canvas>
</template>
