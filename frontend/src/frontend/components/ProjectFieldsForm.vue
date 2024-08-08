<script lang="ts">
import type { Project, InCache, Exists } from '$frontend/stores/api'


export interface Model {
  title: string
  description: string
}

export function makeModel(): Model {
  return {
    title: '',
    description: '',
  }
}

export function assignModelFrom(model: Model, project: Project & InCache & Exists) {
  model.title = project.attributes.title
  model.description = project.attributes.description
  
}

export function resetModel(model: Model) {
  Object.assign(model, makeModel())
}

// @todo Add 'create' and 'save' functions (cf. ExerciseFieldsForm)
</script>

<script setup lang="ts">
import { computed } from 'vue'

import { BLabeledInput, BLabeledTextarea } from './opinion/bootstrap'


const model = defineModel<Model>({required: true})

const saveDisabled = computed(() => model.value.title === '')

defineExpose({
  saveDisabled,
})
</script>

<template>
  <BLabeledInput :label="$t('projectTitle')" v-model="model.title" />
  <BLabeledTextarea :label="$t('projectDescription')" v-model="model.description" />
</template>
