<script setup lang="ts">
import SelectedText from './SelectedText.vue'


const props = defineProps<{
  colors: string[]
  boxed: boolean
}>()

const colorIndex = defineModel<number>({default: 0})

function increment() {
  colorIndex.value = (colorIndex.value + 1) % (props.colors.length + 1)
}
</script>

<template>
  <span v-if="colorIndex === 0" data-cy="selectable" @click="increment" :class="{boxed_: boxed}"><slot></slot></span>
  <SelectedText v-else data-cy="selectable" @click="increment" :color="colors[colorIndex - 1]" :boxed><slot></slot></SelectedText>
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

span.boxed_ {
  outline: black solid 3px;
}

/* span.boxed:hover {
  outline: black dotted 5px;
} */
</style>
