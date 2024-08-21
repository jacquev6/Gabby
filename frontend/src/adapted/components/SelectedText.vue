<script setup lang="ts">
import { computed } from 'vue'


const props = defineProps<{
  colors: number,
  color: number,
}>()

// Keep this array consistent with the 'style' section in 'AdaptationDetailsFieldsForm.vue'
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

const style = computed(() => ({
  background: colors[props.color - 1],
}))
</script>

<template>
  <span :style><slot></slot></span>
</template>
