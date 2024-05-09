<script setup lang="ts">
import { BLabeledInput, BLabeledCheckbox } from '../opinion/bootstrap'
import type { SelectThingsOptions } from '$frontend/types/api'


const model = defineModel<SelectThingsOptions>({
  required: true,
  default: ((): SelectThingsOptions => ({
    colors: 1,
    words: true,
    punctuation: true,
  }))(),
})
</script>

<template>
  <BLabeledInput :label="$t('colorsCount')" type="number" min="1" v-model="model.colors" />
  <BLabeledCheckbox :label="$t('includePunctuation')" v-model="model.punctuation" />
</template>
