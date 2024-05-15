<script setup lang="ts">
import BSelect from './Select.vue'

defineOptions({
  inheritAttrs: false
})

interface Option {
  value: string,
  label: string,
}

defineProps<{
  label: string,
  options: (string | Option)[],
}>()

const model = defineModel<string>()

const id = `input-${ Math.floor(Math.random() * 4000000000) }`
</script>

<template>
  <div class="mb-3">
    <label class="form-label" :for="id">{{ label }}</label>
    <BSelect class="form-control" :id="id" v-model="model" :options v-bind="$attrs"/>
  </div>
</template>
