<script setup>
import { ref, watch } from 'vue'
import { onMounted } from 'vue'


const props = defineProps({
  width: {type: Number, required: true},
  height: {type: Number, required: true},
  transform: {type: Array, required: true},
  rectangles: {type: Array, required: true},
})

const canvas = ref(null)
var context = null

onMounted(() => {
  context = canvas.value.getContext('2d')

  canvas.value.width = props.width
  canvas.value.height = props.height
  context.setTransform(props.transform[0], props.transform[1], props.transform[2], props.transform[3], props.transform[4], props.transform[5])

  draw()
})

watch(() => props.rectangles, draw)

function draw() {
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
