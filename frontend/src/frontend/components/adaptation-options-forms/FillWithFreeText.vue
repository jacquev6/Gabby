<script setup lang="ts">
import { BLabeledInput } from '../opinion/bootstrap'
import type { FillWithFreeTextAdaptationOptions } from '$frontend/types/api'


const model = defineModel<FillWithFreeTextAdaptationOptions>({
  required: true,
  default: ((): FillWithFreeTextAdaptationOptions => ({
    placeholder: '...',
  }))(),
})
</script>

<template>
  <b-labeled-input :label="$t('placeholderText')" type="text" v-model="model.placeholder" />
</template>
