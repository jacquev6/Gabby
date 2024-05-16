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
  <p class="alert alert-secondary" v-if="model.colors > 1">
    <i18n-t keypath="useSel1ToSelN">
      <template v-slot:first>
        <code>{sel1|<em>text</em>}</code>
      </template>
      <template v-slot:last>
        <code>{sel{{ model.colors }}|<em>text</em>}</code>
      </template>
    </i18n-t>
  </p>
  <BLabeledCheckbox :label="$t('includePunctuation')" v-model="model.punctuation" />
</template>
