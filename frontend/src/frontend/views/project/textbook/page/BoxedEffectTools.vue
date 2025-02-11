<script setup lang="ts">
import { BLabeledCheckbox } from '../../../../components/opinion/bootstrap'
import type { Model } from './ExerciseFieldsForm.vue'

const model = defineModel<Model>({required: true})
</script>

<template>
  <BLabeledCheckbox :label="$t('effectsBoxed')" v-model="model.adaptationSettings.itemized.effects.isBoxed" />
</template>
