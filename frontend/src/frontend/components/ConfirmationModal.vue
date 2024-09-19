<script setup lang="ts">
import { ref } from 'vue'

import { BModal, BButton } from './opinion/bootstrap'


const modal = ref<InstanceType<typeof BModal> | null>(null)

let resolve: ((value: boolean) => void) | null = null

async function show() {
  console.assert(modal.value !== null)
  console.assert(resolve === null)

  const promise = new Promise<boolean>(r => {
    resolve = r
  })
  modal.value.show()
  const confirmed = await promise

  resolve = null
  return confirmed
}

function confirm() {
  console.assert(modal.value !== null)
  console.assert(resolve !== null)

  modal.value.hide()
  resolve(true)
}

function cancel() {
  console.assert(modal.value !== null)
  console.assert(resolve !== null)

  modal.value.hide()
  resolve(false)
}

defineExpose({
  show,
})
</script>

<template>
  <BModal ref="modal" :close="false" backdrop="static" :keyboard="false" :fade="false">
    <template #header>
      <h1>{{ $t('confirmTitle') }}</h1>
    </template>
    <template #body>
      <slot></slot>
    </template>
    <template #footer>
      <BButton lg secondary @click="cancel">{{ $t('confirmNo') }}</BButton>
      <BButton lg primary @click="confirm">{{ $t('confirmYes') }}</BButton>
    </template>
  </BModal>
</template>
