<script setup lang="ts" generic="T">
import { label as makeLabel, value as makeValue, disabled as makeDisabled, type Option } from './Select.vue'
import Radio from './Radio.vue'

defineOptions({
  inheritAttrs: false
})

defineProps<{
  label: string,
  options: (string | Option<T>)[],
}>()

const model = defineModel<T>()
</script>

<template>
  <div class="mb-3">
    <p class="form-label">{{ label }}</p>
    <Radio v-for="option in options" v-model="model" :label="makeLabel(option)" :value="makeValue(option)" :disabled="makeDisabled(option)" />
  </div>
</template>
