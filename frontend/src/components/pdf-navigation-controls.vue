<script setup>
import { ref, watch } from 'vue'

import { BButton } from './opinion/bootstrap'


const props = defineProps({
  pagesCount: {type: Number, required: true},
})

const pageNumber = defineModel()

const requestedPageNumber = ref(1)
watch(requestedPageNumber, (n) => {
  const page = Number.parseInt(n, 10)
  if (Number.isInteger(page) && page >= 1 && page <= props.pagesCount) {
    pageNumber.value = page
  }
})
</script>

<template>
  <p class="text-center">
    <b-button sm primary :disabled="pageNumber <= 1" @click="--requestedPageNumber">&lt;</b-button>
    <label>
      {{ $t('pdfNavigationPage') }}
      <input type="number" min="1" :max="pagesCount" v-model="requestedPageNumber" @blur="requestedPageNumber = pageNumber" />
      {{ $t('pdfNavigationPageOver', pagesCount) }}
    </label>
    <b-button sm primary :disabled="pageNumber >= pagesCount" @click="++requestedPageNumber">&gt;</b-button>
  </p>
</template>

<style scoped>
/* https://www.w3schools.com/howto/howto_css_hide_arrow_number.asp */
input {
  -moz-appearance: textfield;
}
input::-webkit-outer-spin-button, input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
</style>
