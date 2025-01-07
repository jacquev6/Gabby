<script setup lang="ts">
import { ref, watch } from 'vue'
import { onMounted, onUpdated, nextTick } from 'vue'
import { useElementSize } from '@vueuse/core'


const container = ref<HTMLDivElement | null>(null)
const { width } = useElementSize(container)
watch(width, () => nextTick(recolor))
onMounted(recolor)
onUpdated(recolor)

/* Colors provided by client */
const colors = ['#00F', '#F00', '#0C0']

function recolor() {
  if (container.value !== null) {
    const tricolorables = Array.from(container.value.getElementsByClassName('tricolorable') as HTMLCollectionOf<HTMLElement>)

    let colorIndex = -1
    let previousOffsetLeft: number | null = null

    tricolorables.forEach(element => {
      const offsetLeft = element.offsetLeft
      if (previousOffsetLeft === null || offsetLeft <= previousOffsetLeft) {
        colorIndex++
      }
      previousOffsetLeft = offsetLeft
      element.style.color = colors[colorIndex % colors.length]
    })
  }
}

defineExpose({ recolor })
</script>

<template>
  <div ref="container"><slot></slot></div>
</template>

<style>
.tricolorable .tricolorable {
  background-color: rgba(255, 0, 0, 0.5);
}

.tricolorable .tricolorable::after {
  content: 'THERE IS A BUG (nested tricolorable)';
  color: black;
}
</style>
