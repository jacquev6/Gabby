<script setup lang="ts">
import { BLabeledInput } from '../opinion/bootstrap'
import type { FillWithFreeTextOptions } from '$frontend/types/api'


const model = defineModel<{
  placeholder: string,
}>({
  required: true,
  default: ((): FillWithFreeTextOptions => ({
    placeholder: '...',
  }))(),
})
</script>

<template>
  <b-labeled-input :label="$t('placeholderText')" type="text" v-model="model.placeholder" />
</template>
