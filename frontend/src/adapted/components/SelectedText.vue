<script setup lang="ts">
import { computed } from 'vue'
import chroma from 'chroma-js'


const props = defineProps<{
  colors: number,
  color: number,
}>()

const colors = computed(() => {
  const colors = [
    // Colors provided by the client
    "#ffff00",  // yellow
    "#ffc0cb",  // pink (light red)
    "#bbbbff",  // light blue
    "#bbffbb",  // light green
    "#bbbbbb",  // grey
    // Colors added by Vincent Jacques on the same pattern
    "#bbffff",  // light cyan
    "#ffbbff",  // light magenta
  ]
  // Additional colors just in case we ever need even more
  if (props.colors > colors.length) {
    chroma.scale('Set2').colors(props.colors - colors.length).forEach(color => colors.push(color))
  }
  return colors
})

const style = computed(() => ({
  background: colors.value[props.color - 1]
}))
</script>

<template>
  <span :style><slot></slot></span>
</template>
