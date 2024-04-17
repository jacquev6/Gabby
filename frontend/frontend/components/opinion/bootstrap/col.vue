<script setup>
import { computed } from 'vue'


const props = defineProps({
  w: {
    type: [Number],
    default: null,
  },
})

const class_ = computed(() => {
  if (props.w === null) {
    return 'col'
  } else {
    return `col-${props.w}`
  }
})
</script>

<template>
  <div :class="class_">
    <slot></slot>
  </div>
</template>
