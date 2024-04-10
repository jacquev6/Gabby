<script setup>
import { onMounted } from 'vue'

import { BLabeledInput } from '../opinion/bootstrap'


const model = defineModel({type: Object})

onMounted(() => {
  model.value.colors ??= 1
})
</script>

<template>
  <b-labeled-input label="Colors" type="number" min="1" v-model="model.colors" />
</template>
