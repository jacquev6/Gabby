<script setup lang="ts">
import { BLabeledCheckbox } from '../../../../components/opinion/bootstrap'
import type { Settings } from './MultipleChoicesTools.vue'


defineProps<{
  settings: Settings
}>()
</script>

<template>
  <BLabeledCheckbox :label="$t('effectsBoxed')" v-model="settings.itemized.effects.isBoxed" />
</template>
