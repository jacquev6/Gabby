<script setup lang="ts">
import { computed, ref, watch } from 'vue'
// @ts-ignore/* @todo Use @types/bootstrap */
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle.min.js'
import { useFloating, shift } from '@floating-ui/vue'
// import { useMouse } from '@vueuse/core'

import { BButton } from '.'


const props = withDefaults(defineProps<{
  close?: boolean
  backdrop?: boolean | 'static'
  keyboard?: boolean
  // focus:
  fade?: boolean
}>(), {
  close: true,
  backdrop: true,
  keyboard: true,
  fade: true,
})

interface Point {
  x: number
  y: number
}

const inDom = ref(false)
const showAt = ref<Point | null>(null)
function show(options: {at: Point | null} = {at: null}) {
  inDom.value = true
  showAt.value = options.at
}

const modalElement = ref<HTMLDivElement | null>(null)
const dialogElement = ref<HTMLDivElement | null>(null)
var modal: any/* @todo Use @types/bootstrap */ = null
const transitioning = ref(false)
const active = ref(false)
watch(modalElement, (element) => {
  if (element) {
    element.addEventListener('show.bs.modal', () => {
      transitioning.value = true
    })
    element.addEventListener('shown.bs.modal', () => {
      transitioning.value = false
      active.value = true
    })
    element.addEventListener('hide.bs.modal', () => {
      active.value = false
      transitioning.value = true
    })
    element.addEventListener('hidden.bs.modal', () => {
      transitioning.value = false
      modal.dispose()
      modal = null
      inDom.value = false
    })
    modal = new bootstrap.Modal(element, {backdrop: props.backdrop, keyboard: props.keyboard})
    modal.show()
  }
})

// const mouse = useMouse()
const floatingReference = computed(() => {
  if (showAt.value !== null) {
    console.assert(!props.fade)

    let {x, y} = showAt.value

    // if (mouse.sourceType.value !== null) {
    //   x = mouse.x.value
    //   y = mouse.y.value
    // }

    return {
      getBoundingClientRect() {
        return {width: 0, height: 0, x, left: x, right: x, y, top: y, bottom: y}
      }
    }
  } else {
    return null
  }
})
const {floatingStyles} = useFloating(floatingReference, dialogElement, { placement: 'top', middleware: [shift({crossAxis: true})] })

const dialogElementStyle = computed(() => {
  if (showAt.value === null) {
    return {}
  } else {
    return {
      ...floatingStyles.value,
      margin: 0,
    }
  }
})

function hide() {
  modal?.hide()
}

defineExpose({show, hide, active, transitioning})
</script>

<template>
  <div v-if="inDom" ref="modalElement" class="modal" :class="{fade}" tabindex="-1" aria-hidden="true">
    <div ref="dialogElement" class="modal-dialog modal-xl" :style="dialogElementStyle">
      <div class="modal-content">
        <div class="modal-header">
          <slot name="header"></slot>
          <BButton v-if="close" close aria-label="Close" @click="hide"></BButton>
        </div>
        <div class="modal-body">
          <slot name="body"></slot>
        </div>
        <div class="modal-footer">
          <slot name="footer"></slot>
        </div>
      </div>
    </div>
  </div>
</template>
