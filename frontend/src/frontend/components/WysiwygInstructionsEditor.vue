<script setup lang="ts">
import { ref, computed, watch } from 'vue'

import Quill, { type Model as QuillModel, BoldBlot, ChoiceBlot, ItalicBlot } from './Quill.vue'


const props = defineProps<{
  delta: QuillModel
}>()

const model = defineModel<string>({required: true})

const quillModel = ref<QuillModel>([])
const quill = ref<InstanceType<typeof Quill> | null>(null)

// @todo Consider using a writable 'computed' instead of this two-way 'watch' (https://vuejs.org/api/reactivity-core.html#computed)
watch(
  () => props.delta,
  delta => {
    if (homogenizeDelta(quillModel.value) !== homogenizeDelta(delta)) {
      quillModel.value = delta
    }
  },
  {immediate: true},
)

function homogenizeDelta(delta: QuillModel): string {
  return JSON.stringify(delta.map(op => {
    const {insert, attributes} = op
    if (attributes === undefined || Object.keys(attributes).length === 0) {
      return {insert, attributes: {}}
    } else {
      return {insert, attributes}
    }
  }))
}

watch(quillModel, quillModel => {
  const expectedModel = makeModel(quillModel)
  if (model.value !== expectedModel) {
    model.value = expectedModel
  }
})

function makeModel(quillModel: QuillModel): string {
  let model = ''
  for (const delta of quillModel) {
    if (delta.attributes?.choice) {
      model += `{choice|${delta.insert}}`
    } else if (delta.attributes?.bold) {
      model += `{bold|${delta.insert}}`
    } else if (delta.attributes?.italic) {
      model += `{italic|${delta.insert}}`
    } else {
      model += delta.insert
    }
  }
  return model
}

// This variable is required: passing ':blots="[ChoiceBlot]"' to the 'Quill' component
// changes its 'props.blots' on every update, triggering unwanted re-computations.
const blots = [ChoiceBlot, BoldBlot, ItalicBlot]

defineExpose({
  // Could we automate these? They all forward to 'quill.value'.
  toggle(format: string) {
    console.assert(quill.value !== null)
    quill.value.toggle(format)
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
})
</script>

<template>
  <Quill ref="quill" v-model="quillModel" :blots />
</template>
