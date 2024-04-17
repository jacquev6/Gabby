<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { useFloating, shift, flip } from '@floating-ui/vue'
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle.min.js'


const props = defineProps({
  title: {type: String, required: true},
  reference: {type: Object, required: true},
})

const emit = defineEmits([
  'dismissed',  // () => void
])

const modal = ref(null)
const dialog = ref(null)
const floatingReference = ref(null)
const {floatingStyles} = useFloating(floatingReference, dialog, { placement: 'top', middleware: [flip(), shift()] })

onMounted(() => {
  bootstrap.Modal.getOrCreateInstance(modal.value).show()
  modal.value.addEventListener('hidden.bs.modal', () => { emit('dismissed') })
  floatingReference.value = {
    getBoundingClientRect() {
      const { x, y } = props.reference
      return {
        width: 0, height: 0,
        x: x, left: x, right: x,
        y: y, top: y, bottom: y,
      }
    }
  }
})

onBeforeUnmount(() => { bootstrap.Modal.getOrCreateInstance(modal.value).hide() })
</script>

<template>
  <div ref="modal" class="modal">
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
