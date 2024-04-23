<script setup lang="ts">
import { ref, watch } from 'vue'
import { onMounted } from 'vue'


const props = defineProps<{
  width: number,
  height: number,
  transform: number[],
  rectangles: any/* @todo Type */[],
}>()

const canvas = ref<HTMLCanvasElement | null>(null)
var context: CanvasRenderingContext2D | null = null

onMounted(() => {
  console.assert(canvas.value !== null)
  context = canvas.value.getContext('2d')
  console.assert(context !== null)

  canvas.value.width = props.width
  canvas.value.height = props.height
  context.setTransform(props.transform[0], props.transform[1], props.transform[2], props.transform[3], props.transform[4], props.transform[5])

  draw()
})

watch(() => props.rectangles, draw)

function draw() {
  console.assert(canvas.value !== null)
  console.assert(context !== null)

  context.save()
  context.setTransform(1, 0, 0, 1, 0, 0)
  context.clearRect(0, 0, canvas.value.width, canvas.value.height)
  context.fillStyle = 'rgba(128, 128, 128, 0.5)'
  context.fillRect(0, 0, canvas.value.width, canvas.value.height)
  context.restore()
  for (const rectangle of props.rectangles) {
    context.beginPath()
    const left = Math.min(rectangle.start.x, rectangle.stop.x)
    const top = Math.min(rectangle.start.y, rectangle.stop.y)
    const width = Math.abs(rectangle.start.x - rectangle.stop.x)
    const height = Math.abs(rectangle.start.y - rectangle.stop.y)
    context.clearRect(left, top, width, height)
  }
}
</script>

<template>
  <canvas ref="canvas"></canvas>
</template>
