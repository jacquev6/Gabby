<script setup>
import { ref } from 'vue'

defineOptions({
  // Disable attribute inheritance to apply all fallthrough attributes to the textarea
  // https://vuejs.org/guide/components/attrs#disabling-attribute-inheritance
  inheritAttrs: false
})

const props = defineProps({
  label: { type: String, required: true },
})

const model = defineModel({ type: String })

const id = `textarea-${ Math.floor(Math.random() * 4000000000) }`

const textarea = ref(null)

defineExpose({
  focus: () => textarea.value.focus(),
  setSelectionRange: (start, end) => textarea.value.setSelectionRange(start, end),
})
</script>

<template>
  <div class="mb-3">
    <label class="form-label" :for="id">{{ label }}</label>
    <textarea class="form-control" :id="id" ref="textarea" v-model="model" v-bind="$attrs"></textarea>
  </div>
</template>
