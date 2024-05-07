<script setup lang="ts">
import { BLabeledInput } from '../opinion/bootstrap'


const model = defineModel<{
  colors: number,
}>({
  required: true,
  default: {
    colors: 1,
  },
})
</script>

<template>
  <b-labeled-input :label="$t('colorsCount')" type="number" min="1" v-model="model.colors" />
</template>
