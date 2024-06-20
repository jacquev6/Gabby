<script setup lang="ts">
import { ref, watch } from 'vue'
// @ts-ignore/* @todo Use @types/bootstrap */
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle.min.js'

import { BButton } from '.'


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

const inDom = ref(false)
function show() {
  inDom.value = true
}

const modalElement = ref<HTMLDivElement | null>(null)
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

function hide() {
  modal?.hide()
}

defineExpose({show, hide, active})
</script>

<template>
  <div v-if="inDom" class="modal fade" ref="modalElement" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <slot name="header"></slot>
          <b-button v-if="close" close aria-label="Close" @click="hide"></b-button>
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
