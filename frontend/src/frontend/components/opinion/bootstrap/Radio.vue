<script setup lang="ts" generic="T">

defineProps<{
  label: string
  value: T
  disabled?: boolean
}>()

const model = defineModel<T>()

const id = `input-${ Math.floor(Math.random() * 4000000000) }`
</script>

<template>
  <div class="form-check">
    <input class="form-check-input" type="radio" :id="id" v-model="model" :value :disabled />
    <label class="form-check-label" :for="id">{{ label }}</label>
  </div>
</template>
