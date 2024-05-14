<script setup lang="ts">
import { ref } from 'vue'

defineOptions({
  // Disable attribute inheritance to apply all fallthrough attributes to the textarea
  // https://vuejs.org/guide/components/attrs#disabling-attribute-inheritance
  inheritAttrs: false
})

defineProps<{
  label: string,
}>()

const model = defineModel<string>({default: ''})

const id = `textarea-${ Math.floor(Math.random() * 4000000000) }`

const textarea = ref<HTMLTextAreaElement | null>(null)

defineExpose({
  focus: () => textarea.value?.focus(),
  setSelectionRange: (start: number, end: number) => textarea.value?.setSelectionRange(start, end),
  textarea,
})
</script>

<template>
  <div class="mb-3">
    <label class="form-label" :for="id">{{ label }}</label>
    <textarea class="form-control" :id="id" ref="textarea" v-model="model" v-bind="$attrs" :rows="model.split('\n').length + 1"></textarea>
  </div>
</template>
