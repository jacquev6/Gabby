<script setup lang="ts">
import { BLabeledInput } from '../opinion/bootstrap'
import type { MultipleChoicesAdaptationOptions } from '$frontend/types/api'


const model = defineModel<MultipleChoicesAdaptationOptions>({
  required: true,
  default: ((): MultipleChoicesAdaptationOptions => ({
    placeholder: '...',
  }))(),
})
</script>

<template>
  <p class="alert alert-secondary">
    <i18n-t keypath="useChoice">
      <template v-slot:choice>
        <code>{choice|<em>text</em>}</code>
      </template>
    </i18n-t>
  </p>
  <b-labeled-input :label="$t('placeholderText')" type="text" v-model="model.placeholder" />
</template>
