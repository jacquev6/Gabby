<script setup lang="ts">
import { BLabeledInput } from '../opinion/bootstrap'


const model = defineModel<{
  placeholder: string,
}>({
  required: true,
  default: {
    placeholder: '...',
  },
})
</script>

<template>
  <b-labeled-input :label="$t('placeholderText')" type="text" v-model="model.placeholder" />
</template>
