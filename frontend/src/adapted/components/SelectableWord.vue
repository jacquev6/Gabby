<script setup lang="ts">
import { ref, computed } from 'vue'
import chroma from 'chroma-js'


const props = defineProps<{
  colors: number,
}>()

const colors = computed(() => chroma.scale('Set2').colors(props.colors))

const color = ref(0)

function increment() {
  color.value = (color.value + 1) % (props.colors + 1)
}

const style = computed(() => {
  if (color) {
    return {
      background: colors.value[color.value - 1]
    }
  } else {
    return {}
  }
})
</script>

<template>
  <span @click="increment" :style><slot></slot></span>
</template>

<style scoped>
span {
  border: none;
  border-top: 2px solid transparent;
  border-bottom: 2px solid transparent;
  margin: 0;
  padding: 0;
  background: none;
  cursor: pointer;
  user-select: none;
}

span:hover {
  border-color: grey;
}
</style>
