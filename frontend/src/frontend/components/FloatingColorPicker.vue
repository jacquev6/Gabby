<script setup lang="ts">
import { ref } from 'vue'

import { BButton } from './opinion/bootstrap'
import ContextMenu from './ContextMenu.vue'
import { defaultColorsForSelectableEffect } from './AdaptationDetailsFieldsForm.vue'


const props = defineProps<{
  default: string
  backdropCovers1: string
  backdropCovers2: string
}>()

const model = defineModel<string>({required: true})

const colorLines = [
  defaultColorsForSelectableEffect,
  [
    // Provided by client in https://github.com/jacquev6/Gabby/issues/10#issuecomment-2462656497
    '#ffcf4c',
    '#ff8084',
    '#8177ff',
    '#68e495',
    '#632f2b',
    '#000000',
  ],
]

const contextMenu = ref<InstanceType<typeof ContextMenu> | null>(null)
function show(ref: HTMLElement) {
  console.assert(contextMenu.value !== null)
  contextMenu.value.show(ref)
}

function reset() {
  model.value = props.default
  commit()
}

function commit() {
  console.assert(contextMenu.value !== null)
  contextMenu.value.hide()
}

defineExpose({show})
</script>

<template>
  <ContextMenu ref="contextMenu" :backdropCovers1 :backdropCovers2>
    <p v-for="colorLine in colorLines">
      <span class="color" :style="{background: color}" v-for="color in colorLine" @click="model=color"></span>
    </p>
    <BButton sm secondary @click="reset">{{ $t('resetColorToDefault') }} <span class="color" :style="{background: props.default}"></span></BButton>
    <BButton sm primary @click="commit">OK</BButton>
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
