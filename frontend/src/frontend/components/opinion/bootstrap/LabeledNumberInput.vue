<script setup lang="ts">
import { ref } from 'vue'

defineOptions({
  inheritAttrs: false
})

defineProps<{
  label: string
}>()

const model = defineModel<number | null>()

const id = `input-${ Math.floor(Math.random() * 4000000000) }`

const inputElement = ref<HTMLInputElement | null>(null)

defineExpose({
  focus: () => inputElement.value?.focus(),
  setSelectionRange: (start: number, end: number) => inputElement.value?.setSelectionRange(start, end),
  inputElement,
})
</script>

<template>
  <div class="mb-3">
    <label class="form-label" :for="id">{{ label }}</label>
    <input ref="inputElement" class="form-control" :id type="number" v-model="model" v-bind="$attrs" />
  </div>
</template>
