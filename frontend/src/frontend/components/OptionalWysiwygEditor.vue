<script setup lang="ts">
import { ref, computed } from 'vue'
import { nextTick } from 'vue'

import WysiwygEditor, { type Format } from './WysiwygEditor.vue'
import { type Model as QuillModel } from './Quill.vue'


defineProps<{
  label: string,
  formats: Record<string, Format>
  delta: QuillModel
}>()

const model = defineModel<string>({required: true})

const forced = ref(false)

const editor = ref<InstanceType<typeof WysiwygEditor> | null>(null)

function force() {
  forced.value = true
  nextTick(() => editor.value?.focus())  // @todo Fix
}

function unforce() {
  forced.value = false
}

const expanded = computed(() => model.value !== '' || forced.value)

defineExpose({
  expanded,
  toggle(format: string, value: unknown = true) {
    console.assert(editor.value !== null)
    editor.value.toggle(format, value)
  },
  focus: () => editor.value?.focus(),
  setSelection(index: number, length: number) {
    editor.value?.setSelection(index, length)
  },
  getLength() {
    return editor.value?.getLength() ?? 0
  },
  hasFocus: computed(() => editor.value !== null && editor.value.hasFocus),
  currentFormat: computed(() => editor.value === null ? {} : editor.value.currentFormat),
})
</script>

<template>
  <WysiwygEditor
    v-if="expanded"
    ref="editor"
    :label
    :formats
    :delta
    v-model="model"
    @focus="force"
    @blur="unforce"
  />
  <p v-else @click="force">{{ label }} <button class="btn btn-sm btn-primary">+</button></p>
</template>
