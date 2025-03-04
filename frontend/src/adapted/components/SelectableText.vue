<script setup lang="ts">
import { computed } from 'vue'

import SelectedText from './SelectedText.vue'


const props = defineProps<{
  colors: string[]
  boxed: boolean
  padding: [number, number] | undefined
}>()

const colorIndex = defineModel<number>({default: 0})

function increment() {
  colorIndex.value = (colorIndex.value + 1) % (props.colors.length + 1)
}

const style = computed(() => {
  if (props.padding !== undefined) {
    return {
      padding: `${props.padding[0]}px ${props.padding[1]}px`,
    }
  } else {
    return {}
  }
})
</script>

<template>
  <span v-if="colorIndex === 0" data-cy="selectable" @click="increment" :class="{boxed}" :style><slot></slot></span>
  <SelectedText v-else data-cy="selectable" @click="increment" :color="colors[colorIndex - 1]" :boxed :style><slot></slot></SelectedText>
</template>

<style scoped>
span {
  cursor: pointer;
  user-select: none;
  padding: 3.2px 0px;
}

span:hover {
  outline: 3px dotted #EEE;
}

span.boxed {
  padding: 4px;
  border: 2px solid black;
}
</style>
