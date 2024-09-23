<script setup lang="ts" generic="T">
export interface Option<T> {
  value: T
  label: string
}

defineProps<{
  options: (string | Option<T>)[],
}>()

const model = defineModel<T>()

function value(option: string | Option<T>) {
  if (typeof option === 'string') {
    return option
  } else {
    return option.value
  }
}

function label(option: string | Option<T>) {
  if (typeof option === 'string') {
    return option
  } else {
    return option.label
  }
}
</script>

<template>
  <select v-model="model" class="form-select">
    <template v-for="option in options" :key="value(option)">
      <option :value="value(option)">{{ label(option) }}</option>
    </template>
  </select>
</template>
