<script setup lang="ts">
import { ref, watch } from 'vue'

import { BButton } from './opinion/bootstrap'


const props = withDefaults(defineProps<{
  pagesCount: number,
  disabled: boolean,
}>(), {
  disabled: false,
})

const pageNumber = defineModel<number>('page', {default: 1})
const requestedPageNumber = ref('1')

function resetRequestedPageNumber() {
  requestedPageNumber.value = pageNumber.value.toString()
}

watch(pageNumber, resetRequestedPageNumber, {immediate: true})

watch(requestedPageNumber, () => {
  const page = Number.parseInt(requestedPageNumber.value, 10)
  if (Number.isInteger(page) && page >= 1 && page <= props.pagesCount) {
    pageNumber.value = page
  }
})
</script>

<template>
  <p class="text-center">
    <BButton sm primary :disabled="disabled || pageNumber <= 1" @click="--pageNumber">&lt;</BButton>
    <label>
      {{ $t('pdfNavigationPage') }}
      <input type="number" min="1" :max="pagesCount" size="4" :disabled v-model="requestedPageNumber" @blur="resetRequestedPageNumber" />
      {{ $t('pdfNavigationPageOver', pagesCount) }}
    </label>
    <BButton sm primary :disabled="disabled || pageNumber >= pagesCount" @click="++pageNumber">&gt;</BButton>
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
