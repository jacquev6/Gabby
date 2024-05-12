<script setup lang="ts">
import { BLabeledInput, BLabeledCheckbox } from '../opinion/bootstrap'
import type { SelectThingsAdaptationOptions } from '$frontend/types/api'


const model = defineModel<SelectThingsAdaptationOptions>({
  required: true,
  default: ((): SelectThingsAdaptationOptions => ({
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
