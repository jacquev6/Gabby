<script setup>
const props = defineProps({
  options: {
    type: Array,
    required: true,
  },
})

const model = defineModel()

function value(option) {
  if (option.value) {
    return option.value
  } else {
    return option
  }
}

function label(option) {
  if (option.label) {
    return option.label
  } else {
    return option
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
