<script setup lang="ts">
import { computed } from 'vue'


const props = defineProps<{
  color: string
  boxed: boolean
}>()

const style = computed(() => ({
  background: props.color,
}))
</script>

<template>
  <span :style :class="{boxed}"><slot></slot></span>
</template>

<style scoped>
span.boxed {
  padding: 4px;
  border: 2px solid black;
}
</style>
