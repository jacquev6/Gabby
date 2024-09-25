<script lang="ts">
export interface Option<T> {
  value: T
  label: string
  disabled?: boolean
}

export function value<T>(option: string | Option<T>) {
  if (typeof option === 'string') {
    return option
  } else {
    return option.value
  }
}

export function label<T>(option: string | Option<T>) {
  if (typeof option === 'string') {
    return option
  } else {
    return option.label
  }
}

export function disabled<T>(option: string | Option<T>) {
  if (typeof option === 'string') {
    return false
  } else {
    return option.disabled
  }
}
</script>

<script setup lang="ts" generic="T">
defineProps<{
  options: (string | Option<T>)[],
}>()

const model = defineModel<T>()
</script>

<template>
  <select v-model="model" class="form-select">
    <template v-for="option in options" :key="value(option)">
      <option :value="value(option)">{{ label(option) }}</option>
    </template>
  </select>
</template>
