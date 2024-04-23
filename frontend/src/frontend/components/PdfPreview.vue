<script setup lang="ts">
import { ref, toRaw } from 'vue'
import { computedAsync } from '@vueuse/core'
import type { PDFDocumentProxy } from 'pdfjs-dist/types/src/display/api'

import PdfNavigationControls from './PdfNavigationControls.vue'
import PdfRenderer from './PdfRenderer.vue'


const props = defineProps<{
  pdf: PDFDocumentProxy,
}>()

const pageNumber = ref(1)

const page = computedAsync(
  async () => {
    return await toRaw(props.pdf).getPage(pageNumber.value)
  },
  null,
)
</script>

<template>
  <PdfNavigationControls :pagesCount="pdf.numPages" v-model="pageNumber" :disabled="false" />
  <template v-if="page">
    <PdfRenderer
      class="img img-fluid"
      style="border: 1px solid black"
      :page="page"
    />
  </template>
</template>
