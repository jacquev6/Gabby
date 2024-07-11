<script setup lang="ts">
import { ref, computed } from 'vue'
import { onMounted, onBeforeUnmount } from 'vue'
import { useFloating, shift } from '@floating-ui/vue'
// @ts-ignore/* @todo Use @types/bootstrap */
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle.min.js'
// import { useMouse } from '@vueuse/core';


const props = defineProps<{
  title: string
  reference: {x: number, y: number}
}>()

const emit = defineEmits<{
  shown: []
  hidden: []
}>()

// const mouse = useMouse()

const modalElement = ref<HTMLDivElement | null>(null)
let modal: any/* @todo @types/bootstrap */ = null
const dialog = ref(null)
const shown = ref(false)
const floatingReference = computed(() => {
  if (shown.value) {
    let {x, y} = props.reference

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
const {floatingStyles} = useFloating(floatingReference, dialog, { placement: 'top', middleware: [shift({crossAxis: true})] })

onMounted(() => {
  console.assert(modalElement.value !== null)
  modal = new bootstrap.Modal(modalElement.value, {backdrop: true, keyboard: true})
  modalElement.value.addEventListener('shown.bs.modal', () => emit('shown'))
  modalElement.value.addEventListener('hidden.bs.modal', () => emit('hidden'))
  modal.show()
  shown.value = true
})

onBeforeUnmount(() => {
  modal.hide()
})
</script>

<template>
  <div ref="modalElement" class="modal">
    <div ref="dialog" class="modal-dialog modal-xl" :style="{...floatingStyles, margin: 0}">
      <div class="modal-content">
        <div class="modal-header">
          <h3 class="modal-title">{{ title }}</h3>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <slot></slot>
        </div>
      </div>
    </div>
  </div>
</template>
