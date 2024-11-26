<script lang="ts">
import { BoldBlot, ItalicBlot } from './Quill.vue'


export function escapeForTag(text: string) {
  return text.replaceAll('\\', '\\\\').replaceAll('|', '\\|').replaceAll('{', '\\{').replaceAll('}', '\\}')
}

export const basicFormats = {
  bold: {
    kind: 'text' as const,
    make: (text: string) => `{bold|${escapeForTag(text)}}`,
    blot: BoldBlot,
  },
  italic: {
    kind: 'text' as const,
    make: (text: string) => `{italic|${escapeForTag(text)}}`,
    blot: ItalicBlot,
  },
}

export type Format = {
  kind: 'text'
  make: (text: string, value: unknown) => string
  blot: typeof BoldBlot
} | {
  kind: 'embed'
  make: (value: unknown) => string
  blot: typeof BoldBlot
}
</script>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'

import Quill, { type Model, type SelectionRange } from './Quill.vue'

const props = defineProps<{
  label: string
  formats: Record<string, Format>
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
  {immediate: true},
)

const blots = computed(() => Object.values(props.formats).map(format => format.blot))

defineExpose({
  // Could we automate these? They all forward to 'quill.value'.
  toggle(format: string, value: unknown = true) {
    console.assert(quill.value !== null)
    quill.value.toggle(format, value)
  },
  focus() {
    console.assert(quill.value !== null)
    quill.value.focus()
  },
  // Warning, these two functions should translate from Wysiwyg selection range to Quill selection range.
  // It just so happens that their errors compensate each other and that they are currently always used together.
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
      @focus="emit('focus')"
      @blur="emit('blur')"
      @selectionChange="range => emit('selectionChange', range)"
    />
  </div>
</template>
