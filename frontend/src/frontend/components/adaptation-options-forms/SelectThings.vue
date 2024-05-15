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
  <p class="alert alert-secondary" v-if="model.colors > 1">{{ $t('useSel1ToSelN') }} <code>{sel1|text}</code> to <code>{sel{{ model.colors }}|text}</code></p>
  <BLabeledCheckbox :label="$t('includePunctuation')" v-model="model.punctuation" />
</template>
