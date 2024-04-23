<script setup lang="ts">
import { onMounted } from 'vue'

import { BLabeledInput } from '../opinion/bootstrap'


const model = defineModel<any/* @todo Type */>({required: true})

onMounted(() => {
  model.value.colors ??= 1
})
</script>

<template>
  <b-labeled-input :label="$t('colorsCount')" type="number" min="1" v-model="model.colors" />
</template>
