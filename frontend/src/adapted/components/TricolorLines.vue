<script setup lang="ts">
import { ref, watch } from 'vue'
import { onMounted, onUpdated, nextTick } from 'vue'
import { useElementSize } from '@vueuse/core'


const container = ref<HTMLDivElement | null>(null)
const { width } = useElementSize(container)
watch(width, () => nextTick(recolor))
onMounted(recolor)
onUpdated(recolor)

const colors = ['red', 'green', 'blue']

function recolor() {
  if (container.value !== null) {
    let colorIndex = -1
    let previousOffset: number | null = null

    const paragraphElements = container.value.children as HTMLCollectionOf<HTMLParagraphElement>
    for (let paragraphIndex = 0; paragraphIndex < paragraphElements.length; paragraphIndex++) {
      const paragraphElement = paragraphElements[paragraphIndex]
      const spanElements = paragraphElement.children as HTMLCollectionOf<HTMLSpanElement>
      for (let spanIndex = 0; spanIndex < spanElements.length; spanIndex++) {
        const spanElement = spanElements[spanIndex]
        const offset = spanElement.offsetLeft
        if (previousOffset === null || offset < previousOffset) {
          colorIndex++
        }
        previousOffset = offset
        spanElement.style.color = colors[colorIndex % colors.length]
      }
    }
  }
}
</script>

<template>
  <div ref="container"><slot></slot></div>
</template>
