<script lang="ts">
import { BoldBlot, ItalicBlot } from './Quill.vue'

export const basicBlots = [BoldBlot, ItalicBlot]
</script>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'

import Quill, { type Model, type SelectionRange } from './Quill.vue'

defineProps<{
  label: string
  blots: (typeof BoldBlot)[]
  formatsNestingOrder: string[]
  compatibleFormats: string[][]
  contagiousFormats: string[]
}>()

const model = defineModel<Model>({required: true})

const emit = defineEmits<{
  focus: []
  blur: []
  selectionChange: [SelectionRange]
}>()

const quill = ref<InstanceType<typeof Quill> | null>(null)

watch(
  model,
  delta => {
    console.assert(delta.length > 0)
    const lastOp = delta[delta.length - 1]
    console.assert(typeof lastOp.insert === 'string')
    console.assert(lastOp.insert.endsWith('\n'))
  },
  {immediate: true, deep: true},
)

const quill_ = computed(() => {
  if (quill.value === null) {
    return null
  } else {
    return quill.value.quill
  }
})

defineExpose({
  quill: quill_,
  toggle(format: string, value: unknown = true) {
    console.assert(quill.value !== null)
    quill.value.toggle(format, value)
  },
  focus() {
    console.assert(quill.value !== null)
    quill.value.focus()
  },
  setSelection(index: number, length: number) {
    console.assert(quill.value !== null)
    quill.value.setSelection(index, length)
  },
  getLength() {
    console.assert(quill.value !== null)
    return quill.value.getLength()
  },
  hasFocus: computed(() => quill.value !== null && quill.value.hasFocus),
  currentFormat: computed(() => quill.value === null ? {} : quill.value.currentFormat),
})
</script>

<template>
  <div class="mb-3">
    <label class="form-label" @click="quill?.focus()">{{ label }}</label>
    <Quill
      ref="quill"
      v-model="model"
      :blots
      :formatsNestingOrder
      :compatibleFormats
      :contagiousFormats
      @focus="emit('focus')"
      @blur="emit('blur')"
      @selectionChange="range => emit('selectionChange', range)"
    />
  </div>
</template>
