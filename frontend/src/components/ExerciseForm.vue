<script setup>
import { ref } from 'vue'

import FloatingModal from './FloatingModal.vue'


const props = defineProps({
  fields: {
    type: Array,
    required: true,
  },
  pdfSha1: {
    type: String,
    required: true,
  },
  pdfPage: {
    type: Number,
    required: true,
  },
})

const model = defineModel({ type: Object })

const selectedText = ref(null)
const showTextSelectionMenu = ref(false)
const textSelectionMenuReference = ref({x: 0, y: 0})

function textSelected(text, point) {
  selectedText.value = text
  showTextSelectionMenu.value = true
  textSelectionMenuReference.value = {x: point.clientX, y: point.clientY}
}

defineExpose({
  textSelected,
})
</script>

<template>
  <FloatingModal
    v-if="showTextSelectionMenu"
    :title="$t('selectedText')"
    :reference="textSelectionMenuReference"
    @dismissed="showTextSelectionMenu=false"
  >
    <!-- @todo? Consider making this an editable field (to allow editing before adding to the form) -->
    <pre>{{ selectedText }}</pre>
    <hr/>
    <p>{{ $t('addTo') }}</p>
    <template v-for="(field, index) in props.fields">
      <template v-if="index !== 0">&nbsp;</template>
      <button class="btn btn-primary" @click="model[field] += selectedText; showTextSelectionMenu=false">{{ $t(field) }}</button>
    </template>
  </FloatingModal>

  <div v-for="field in props.fields" class="mb-3">
    <label class="form-label">{{ $t(field) }}</label>
    <textarea class="form-control" rows="3" v-model="model[field]"></textarea>
  </div>
</template>
