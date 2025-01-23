<script setup lang="ts">
import { ref } from 'vue'

import ContextMenu from './ContextMenu.vue'


defineProps<{
  colors: string[]
  backdropCovers1: string
  backdropCovers2: string
}>()

const model = defineModel<string>({required: true})

const contextMenu = ref<InstanceType<typeof ContextMenu> | null>(null)
function show(ref: HTMLElement) {
  console.assert(contextMenu.value !== null)
  contextMenu.value.show(ref)
}

function commit(value: string) {
  model.value = value
  console.assert(contextMenu.value !== null)
  contextMenu.value.hide()
}

defineExpose({show})
</script>

<template>
  <ContextMenu ref="contextMenu" :backdropCovers1 :backdropCovers2>
    <span class="color" :style="{background: color}" v-for="color in colors" @click="commit(color)"></span>
  </ContextMenu>
</template>

<style scoped>
span.color {
  display: inline flow-root;
  width: 1.25em;
  height: 1.25em;
  margin-left: 0.25em;
  margin-right: 0.25em;
  cursor: pointer;
}
</style>
