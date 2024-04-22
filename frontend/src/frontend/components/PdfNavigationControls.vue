<script setup>
import { ref, watch } from 'vue'

import { BButton } from './opinion/bootstrap'


const props = defineProps({
  pagesCount: {type: Number, required: true},
  disabled: {type: Boolean, default: false},
})

const pageNumber = defineModel('page', {type: Number, default: 1})

const requestedPageNumber = ref(1)
watch(requestedPageNumber, (n) => {
  const page = Number.parseInt(n, 10)
  if (Number.isInteger(page) && page >= 1 && page <= props.pagesCount) {
    pageNumber.value = page
  }
})

watch(
  pageNumber,
  (n) => {
    requestedPageNumber.value = n
  },
  {immediate: true},
)
</script>

<template>
  <p class="text-center">
    <b-button sm primary :disabled="disabled || pageNumber <= 1" @click="--requestedPageNumber">&lt;</b-button>
    <label>
      {{ $t('pdfNavigationPage') }}
      <input type="number" min="1" :max="pagesCount" size="4" :disabled v-model="requestedPageNumber" @blur="requestedPageNumber = pageNumber" />
      {{ $t('pdfNavigationPageOver', pagesCount) }}
    </label>
    <b-button sm primary :disabled="disabled || pageNumber >= pagesCount" @click="++requestedPageNumber">&gt;</b-button>
    <slot></slot>
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
