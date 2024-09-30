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
  <span :style :class="{boxed_: boxed}"><slot></slot></span>
</template>

<style scoped>
span.boxed_ {
  outline: black solid 3px;
}
</style>
