<script setup lang="ts">
import SelectedText from './SelectedText.vue'


const props = defineProps<{
  colors: string[],
}>()

const colorIndex = defineModel<number>({default: 0})

function increment() {
  colorIndex.value = (colorIndex.value + 1) % (props.colors.length + 1)
}
</script>

<template>
  <span v-if="colorIndex === 0" @click="increment"><slot></slot></span>
  <SelectedText v-else @click="increment" :color="colors[colorIndex - 1]"><slot></slot></SelectedText>
</template>

<style scoped>
span {
  cursor: pointer;
  user-select: none;
  padding: 3.2px 16px;
}

span:hover {
  outline: rgb(238, 238, 238) dotted 3px;
}
</style>
