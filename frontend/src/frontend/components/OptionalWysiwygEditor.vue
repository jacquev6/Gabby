<script setup lang="ts">
import { ref, computed } from 'vue'
import { nextTick } from 'vue'

import WysiwygEditor from './WysiwygEditor.vue'
import { type Model, BoldBlot } from './Quill.vue'
import deepEqual from 'deep-equal'


defineProps<{
  label: string,
  blots: (typeof BoldBlot)[]
  compatibleFormats: string[][]
  contagiousFormats: string[]
}>()

const model = defineModel<Model>({required: true})

const forced = ref(false)

const editor = ref<InstanceType<typeof WysiwygEditor> | null>(null)

function force() {
  forced.value = true
  nextTick(() => editor.value?.focus())  // @todo Fix
}

function unforce() {
  forced.value = false
}

const expanded = computed(() => !deepEqual(model.value, [{insert: '\n', 'attributes': {}}]) || forced.value)

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
    :blots
    :compatibleFormats
    :contagiousFormats
    v-model="model"
    @focus="force"
    @blur="unforce"
  />
  <p v-else @click="force">{{ label }} <button class="btn btn-sm btn-primary">+</button></p>
</template>
