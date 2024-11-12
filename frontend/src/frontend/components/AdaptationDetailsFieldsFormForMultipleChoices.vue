<script setup lang="ts">
import type { Model } from './ExerciseFieldsForm.vue'
import { BButton } from './opinion/bootstrap'


defineProps<{
  wysiwyg: boolean
}>()

const model = defineModel<Model>({required: true})
</script>

<template>
  <template v-if="wysiwyg">
    <BButton primary sm @click="model.inProgress = {kind: 'multipleChoicesCreation'}">{{ $t('multipleChoicesButton') }}</BButton>
  </template>
</template>
