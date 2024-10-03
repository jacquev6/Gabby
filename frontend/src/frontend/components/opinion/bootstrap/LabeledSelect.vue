<script setup lang="ts" generic="T">
import BSelect, { type Option } from './Select.vue'

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
    <label class="form-label" :for="id">{{ label }}</label>
    <BSelect class="form-control" :id="id" v-model="model" :options v-bind="$attrs"/>
  </div>
</template>
