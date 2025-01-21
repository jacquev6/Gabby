<script lang="ts">
import type { Textbook, InCache, Exists } from '$frontend/stores/api'


export interface Model {
  title: string
  publisher: string
  year: number | null
  isbn: string
}

export function makeModel(): Model {
  return {
    title: '',
    publisher: '',
    year: null,
    isbn: '',
  }
}

export function assignModelFrom(model: Model, textbook: Textbook & InCache & Exists) {
  model.title = textbook.attributes.title
  model.publisher = textbook.attributes.publisher || ''
  model.year = textbook.attributes.year
  model.isbn = textbook.attributes.isbn || ''
}

export function resetModel(model: Model) {
  Object.assign(model, makeModel())
}

// @todo Add 'create' and 'save' functions (cf. ExerciseFieldsForm)
</script>

<script setup lang="ts">
import { computed } from 'vue'

import { BLabeledInput, BLabeledNumberInput } from './opinion/bootstrap'


const model = defineModel<Model>({required: true})

const saveDisabled = computed(() => model.value.title === '')

defineExpose({
  saveDisabled,
})
</script>

<template>
  <BLabeledInput :label="$t('textbookTitle')" v-model="model.title"/>
  <BLabeledInput :label="$t('textbookPublisher')" v-model="model.publisher"/>
  <BLabeledNumberInput :label="$t('textbookYear')" v-model="model.year"/>
  <BLabeledInput :label="$t('textbookIsbn')" v-model="model.isbn"/>
</template>
