<script setup lang="ts">
import { onMounted } from 'vue'

import { BLabeledInput } from '../opinion/bootstrap'


const model = defineModel<any/* @todo Type */>({required: true})

onMounted(() => {
  const newModel = {
    placeholder: model.value.placeholder ?? '...',
  }
  Object.keys(model.value).forEach(key => delete model.value[key])
  Object.assign(model.value, newModel)
})
</script>

<template>
  <b-labeled-input :label="$t('placeholderText')" type="text" v-model="model.placeholder" />
</template>
