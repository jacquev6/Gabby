<script setup>
import { computed } from 'vue'


const props = defineProps({
  sm: {
    type: Boolean,
    default: false,
  },
  primary: {
    type: Boolean,
    default: false,
  },
})

const classes = computed(() => {
  return [
    'btn',
    {
      'btn-sm': props.sm,
      'btn-primary': props.primary,
    },
  ]
})
</script>

<template>
  <button :class="classes"><slot></slot></button>
</template>