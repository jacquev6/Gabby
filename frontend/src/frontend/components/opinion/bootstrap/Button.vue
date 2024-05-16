<script setup lang="ts">
import { computed } from 'vue'


const props = withDefaults(defineProps<{
  sm?: boolean,
  primary?: boolean,
  secondary?: boolean,
  close?: boolean,
}>(), {
  sm: false,
  primary: false,
  secondary: false,
  close: false,
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
  <button type="button" :class="classes">
    <slot></slot>
  </button>
</template>
