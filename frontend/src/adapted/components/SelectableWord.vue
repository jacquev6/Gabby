<script setup lang="ts">
import { computed } from 'vue'
import chroma from 'chroma-js'


const props = defineProps<{
  colors: number,
}>()

const colorIndex = defineModel<number>({default: 0})

const colors = computed(() => chroma.scale('Set2').colors(props.colors))

function increment() {
  colorIndex.value = (colorIndex.value + 1) % (props.colors + 1)
}

const style = computed(() => {
  if (colorIndex) {
    return {
      background: colors.value[colorIndex.value - 1]
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
