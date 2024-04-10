<script setup>
import { onMounted } from 'vue'

import { BLabeledInput } from '../opinion/bootstrap'


const model = defineModel({type: Object})

onMounted(() => {
  const newModel = {
    placeholder: model.value.placeholder ?? '...',
  }
  Object.keys(model.value).forEach(key => delete model.value[key])
  Object.assign(model.value, newModel)
})
</script>

<template>
  <b-labeled-input label="Placeholder" type="text" v-model="model.placeholder" />
</template>
