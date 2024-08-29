<script setup lang="ts">
interface Option {
  value: string
  label: string
}

defineProps<{
  options: (string | Option)[],
}>()

const model = defineModel<string>()

function value(option: string | Option) {
  if (typeof option === 'string') {
    return option
  } else {
    return option.value
  }
}

function label(option: string | Option) {
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
