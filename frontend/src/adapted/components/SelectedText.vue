<script setup lang="ts">
import { computed } from 'vue'


const props = defineProps<{
  color: string,
}>()

const style = computed(() => ({
  background: props.color,
}))
</script>

<template>
  <span :style><slot></slot></span>
</template>
