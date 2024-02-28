<script setup>
import { computed } from 'vue'


const props = defineProps({
  sm: {type: Boolean, default: false},
  primary: {type: Boolean, default: false},
  secondary: {type: Boolean, default: false},
  close: {type: Boolean, default: false},
})

const classes = computed(() => {
  return [
    'btn',
    {
      'btn-sm': props.sm,
      'btn-primary': props.primary,
      'btn-secondary': props.secondary,
      'btn-close': props.close,
    },
  ]
})
</script>

<template>
  <button type="button" :class="classes"><slot></slot></button>
</template>
