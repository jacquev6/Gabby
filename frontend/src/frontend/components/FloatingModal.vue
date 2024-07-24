<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import { useFloating, shift } from '@floating-ui/vue'
// @ts-ignore/* @todo Use @types/bootstrap */
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle.min.js'
// import { useMouse } from '@vueuse/core'

import { BButton } from '$/frontend/components/opinion/bootstrap'


const props = withDefaults(defineProps<{
  close?: boolean,
  backdrop?: boolean | 'static',
  keyboard?: boolean,
  // focus:
}>(), {
  close: true,
  backdrop: true,
  keyboard: true,
})

// const mouse = useMouse()

export interface Point {
  x: number
  y: number
}

const lastShownAt = ref<Point | null>(null)

const inDom = computed(() => lastShownAt.value !== null)
function show(at: Point) {
  lastShownAt.value = at
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
      lastShownAt.value = null
    })
    modal = new bootstrap.Modal(element, {backdrop: props.backdrop, keyboard: props.keyboard})
    modal.show()
  }
})

const floatingReference = computed(() => {
  if (lastShownAt.value !== null) {
    let {x, y} = lastShownAt.value

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

function hide() {
  modal?.hide()
}

defineExpose({show, hide, active})
</script>

<template>
  <div v-if="inDom" ref="modalElement" class="modal">
    <div ref="dialogElement" class="modal-dialog modal-xl" :style="{...floatingStyles, margin: 0}">
      <div class="modal-content">
        <div class="modal-header">
          <slot name="header"></slot>
          <BButton v-if="close" close aria-label="Close" @click="hide"></BButton>
        </div>
        <div class="modal-body">
          <slot></slot>
        </div>
      </div>
    </div>
  </div>
</template>
