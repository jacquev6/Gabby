<script setup>
import { ref, toRaw } from 'vue'
import { computedAsync } from '@vueuse/core'

import PdfNavigationControls from './pdf-navigation-controls.vue'
import PdfRenderer from './pdf-renderer.vue'


const props = defineProps({
  pdf: {
    type: Object,
    required: true,
  },
})

const pageNumber = ref(1)

const page = computedAsync(
  async () => {
    return await toRaw(props.pdf).getPage(pageNumber.value)
  },
  null,
)
</script>

<template>
  <pdf-navigation-controls :pagesCount="pdf.numPages" v-model="pageNumber" />
  <template v-if="page">
    <pdf-renderer
      class="img img-fluid"
      style="border: 1px solid black"
      :page="page"
    />
  </template>
</template>
