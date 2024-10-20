<script setup lang="ts">
import { useFloating, arrow, shift } from '@floating-ui/vue'
import { Vue3ColorPicker as ColorPicker } from '@cyhnkckali/vue3-color-picker'
import '@cyhnkckali/vue3-color-picker/dist/style.css'
import { computed, ref } from 'vue'

import { BButton } from './opinion/bootstrap'


const props = defineProps<{
  default: string
}>()

const model = defineModel<string>({required: true})
const initialValue = ref('')

const inDom = ref(false)
const floatingReference = ref<HTMLElement | null>(null)
const floatingContainer = ref<HTMLElement | null>(null)
const floatingArrow = ref<HTMLElement | null>(null)
function show(ref: HTMLElement) {
  inDom.value = true
  floatingReference.value = ref
  initialValue.value = model.value
}

// @todo Use 'ContextMenu' component
const {floatingStyles, middlewareData} = useFloating(
  floatingReference,
  floatingContainer,
  {
    middleware: [
      shift(),
      arrow({element: floatingArrow}),
    ],
    placement: 'bottom',
  },
)

const floatingArrowStyles = computed(() => {
  const arrow = middlewareData.value.arrow
  if (arrow === undefined) {
    return {}
  } else {
    console.assert(arrow.x !== undefined)
    return {
      left: `${arrow.x}px`,
    }
  }
})

function reset() {
  model.value = props.default
  commit()
}

function rollback() {
  model.value = initialValue.value
  commit()
}

function commit() {
  inDom.value = false
}

defineExpose({show})
</script>

<template>
  <template v-if="inDom">
    <div
      class="floating-backdrop"
      @click="rollback" @contextmenu.prevent="rollback"
    ></div>
    <div
      ref="floatingContainer"
      class="floating-container"
      :style="floatingStyles"
    >
      <div
        ref="floatingArrow"
        class="floating-arrow"
        :style="floatingArrowStyles"
      ></div>
      <div class="floating-content">
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
      </div>
    </div>
  </template>
</template>

<style scoped>
span.default-color {
  display: inline flow-root;
  width: 1.25em;
  height: 1.25em;
}

div.floating-backdrop {
  position: fixed;
  z-index: 10;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0);
}

div.floating-container {
  z-index: 11;
}

div.floating-content {
  border: 1px solid black;
  background: white;
  position: relative;
  top: 10px;
}

div.floating-arrow {
  position: absolute;
  /* CSS Triangle trick: https://css-tricks.com/snippets/css/css-triangle/ */
  width: 0;
  height: 0;
  border-left: 0.75em solid transparent;
  border-right: 0.75em solid transparent;
  border-bottom: 0.75em solid black;
}
</style>
