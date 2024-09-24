<script setup lang="ts" generic="T">
import { label as makeLabel, value as makeValue, type Option } from './Select.vue'

defineOptions({
  inheritAttrs: false
})

defineProps<{
  label: string,
  options: (string | Option<T>)[],
}>()

const model = defineModel<T>()

const id = `input-${ Math.floor(Math.random() * 4000000000) }`
</script>

<template>
  <div class="mb-3">
    <p class="form-label">{{ label }}</p>
    <div class="form-check" v-for="option, index in options">
      <input class="form-check-input" type="radio" :id="`${id}-${index}`" v-model="model" :value="makeValue(option)" />
      <label class="form-check-label" :for="`${id}-${index}`">{{ makeLabel(option) }}</label>
    </div>
  </div>
</template>
