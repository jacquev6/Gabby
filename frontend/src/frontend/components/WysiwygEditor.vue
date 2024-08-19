<script lang="ts">
import { ChoiceBlot, BoldBlot, ItalicBlot } from './Quill.vue'


export const basicFormats = {
  bold: {
    make: (text: string) => `{bold|${text}}`,
    blot: BoldBlot,
  },
  italic: {
    make: (text: string) => `{italic|${text}}`,
    blot: ItalicBlot,
  },
}

export const instructionsFormats = {
  ...basicFormats,
  choice: {
    make: (text: string) => `{choice|${text}}`,
    blot: ChoiceBlot,
  },
}
</script>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'

import Quill, { type Model as QuillModel } from './Quill.vue'


export interface Format {
  make: (text: string) => string
  blot: typeof BoldBlot
}

const props = defineProps<{
  label: string
  formats: Record<string, Format>
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
    const keys = Object.keys(delta.attributes ?? {})
    if (keys.length === 0) {
      model += delta.insert
    } else {
      console.assert(keys.length === 1)
      const format = props.formats[keys[0]]
      model += format.make(delta.insert)
    }
  }
  return model
}

const blots = computed(() => Object.values(props.formats).map(format => format.blot))

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
  <div class="mb-3">
    <label class="form-label" @click="quill?.focus()">{{ label }}</label>
    <Quill ref="quill" v-model="quillModel" :blots />
  </div>
</template>
