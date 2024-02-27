<script setup>
import { ref, watch } from 'vue'
import { computedAsync } from '@vueuse/core'

import { BButton } from '../components/bootstrap'
import PdfRenderer from './PdfRenderer.vue'

const props = defineProps({
  pdf: {
    type: Object,
    required: true,
  },
})

const pageNumber = ref(1)
const requestedPageNumber = ref(1)
watch(requestedPageNumber, (n) => {
  const page = Number.parseInt(n, 10)
  if (Number.isInteger(page) && page >= 1 && page <= props.pdf.numPages) {
    pageNumber.value = page
  }
})

const page = computedAsync(
  async () => {
    return await props.pdf.getPage(pageNumber.value)
  },
  null,
)
</script>

<template>
  <p class="text-center">
    <b-button sm primary :disabled="pageNumber <= 1" @click="--requestedPageNumber">&lt;</b-button>
    <label>{{ $t('Page') }} <input class="number-no-spin" type="number" min="1" :max="pdf.numPages" v-model="requestedPageNumber" @blur="requestedPageNumber = pageNumber" /> {{ $t('pageOver', props.pdf.numPages) }}</label>
    <b-button sm primary :disabled="pageNumber >= pdf.numPages" @click="++requestedPageNumber">&gt;</b-button>
  </p>
  <template v-if="page">
    <pdf-renderer
      class="img img-fluid"
      style="border: 1px solid black"
      :page="page"
    />
  </template>
</template>