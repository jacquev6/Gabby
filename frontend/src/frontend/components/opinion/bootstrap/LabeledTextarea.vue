<script setup lang="ts">
import { computed, ref } from 'vue'

defineOptions({
  // Disable attribute inheritance to apply all fallthrough attributes to the textarea
  // https://vuejs.org/guide/components/attrs#disabling-attribute-inheritance
  inheritAttrs: false
})

const props = withDefaults(defineProps<{
  label?: string
  maxRows?: number
  enforceTrailingLineEnd?: boolean
}>(), {
  maxRows: Infinity,
  enforceTrailingLineEnd: false,
})

const model = defineModel<string>({default: '\n'})

const modelWithoutTrailingLineEnd = computed({
  get() {
    if (props.enforceTrailingLineEnd) {
      console.assert(model.value.endsWith('\n'))
      return model.value.slice(0, -1)
    } else {
      return model.value
    }
  },
  set(value) {
    if (props.enforceTrailingLineEnd) {
      model.value = value + '\n'
    } else {
      model.value = value
    }
  },
})

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
    <label v-if="label !== undefined" class="form-label" :for="id">{{ label }}</label>
    <textarea class="form-control" :id="id" ref="textarea" v-model="modelWithoutTrailingLineEnd" v-bind="$attrs" :rows="Math.min(modelWithoutTrailingLineEnd.split('\n').length + 1, maxRows)"></textarea>
  </div>
</template>
