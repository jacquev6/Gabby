<script setup lang="ts">
import { computed } from 'vue'
import chroma from 'chroma-js'


const props = defineProps<{
  colors: number,
  color: number,
}>()

const colors = computed(() => chroma.scale('Set2').colors(props.colors))

const style = computed(() => ({
  background: colors.value[props.color - 1]
}))
</script>

<template>
  <span :style><slot></slot></span>
</template>
