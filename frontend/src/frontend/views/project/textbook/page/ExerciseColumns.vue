<script setup lang="ts">
import TwoResizableColumns from '$frontend/components/TwoResizableColumns.vue'
import { type Model } from '$frontend/components/ExerciseFieldsForm.vue'


defineProps<{
  projectId: string
}>()

defineModel<Model>({required: true})
</script>

<template>
  <TwoResizableColumns saveKey="projectTextbookPage-2" :snap="150" class="h-100" gutterWidth="200px">
    <template #left>
      <slot name="left"></slot>
    </template>

    <template #gutter>
      <slot name="gutter"></slot>
    </template>

    <template #right>
      <slot name="right"></slot>
    </template>
  </TwoResizableColumns>
</template>
