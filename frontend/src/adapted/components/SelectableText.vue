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
