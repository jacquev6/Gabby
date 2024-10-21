<script setup lang="ts">
import { useFloating, arrow, shift } from '@floating-ui/vue'
import { Vue3ColorPicker as ColorPicker } from '@cyhnkckali/vue3-color-picker'
import '@cyhnkckali/vue3-color-picker/dist/style.css'
import { computed, ref } from 'vue'

import { BButton } from './opinion/bootstrap'
import ContextMenu from './ContextMenu.vue'


const props = defineProps<{
  default: string
  backdropCovers1: string
  backdropCovers2: string
}>()

const model = defineModel<string>({required: true})
const initialValue = ref('')


const contextMenu = ref<InstanceType<typeof ContextMenu> | null>(null)
function show(ref: HTMLElement) {
  console.assert(contextMenu.value !== null)

  initialValue.value = model.value
  contextMenu.value.show(ref)
}

function reset() {
  model.value = props.default
  commit()
}

function rollback() {
  model.value = initialValue.value
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
    <ColorPicker
      v-model="model"
      mode="solid"
      type="HEX"
      :showColorList="false"
      :showEyeDrop="false"
      :showAlpha="false"
      :showInputMenu="false"
      :showInputSet="false"
      :showPickerMode="false"
    />
    <BButton sm secondary @click="reset">{{ $t('resetColorToDefault') }} <span class="default-color" :style="{background: props.default}"></span></BButton>
    <BButton sm primary @click="commit">OK</BButton>
  </ContextMenu>
</template>

<style scoped>
span.default-color {
  display: inline flow-root;
  width: 1.25em;
  height: 1.25em;
}
</style>
