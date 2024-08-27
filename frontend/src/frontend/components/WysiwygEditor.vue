<script lang="ts">
import { BoldBlot, ItalicBlot } from './Quill.vue'


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
</script>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'

import Quill, { type Model as QuillModel } from './Quill.vue'


export interface Format {
  make: (text: string, value: unknown) => string
  blot: typeof BoldBlot
}

const props = defineProps<{
  label: string
  formats: Record<string, Format>
  delta: QuillModel
}>()

const model = defineModel<string>({required: true})

const emit = defineEmits<{
  focus: []
  blur: []
}>()

// We do not detect if the model (or delta) has a trailing line end.
// We just add one for Quill and remove it for the model.
// This will match the behavior of 'textarea' elements.
const modelWithAdditionalLineEnd = computed({
  get() {
    return model.value + '\n'
  },
  set(value) {
    console.assert(value.endsWith('\n'))
    model.value = value.slice(0, -1)
  },
})

const deltaWithAdditionalLineEnd = computed(() => {
  if (props.delta.length === 0) {
    return [{insert: '\n'}]
  } else {
    const lastOp = props.delta[props.delta.length - 1]
    if (Object.keys(lastOp.attributes ?? {}).length === 0) {
      return [...props.delta.slice(0, -1), {insert: lastOp.insert + '\n'}]
    } else {
      return [...props.delta, {insert: '\n'}]
    }
  }
})

const quillModel = ref<QuillModel>([])
const quill = ref<InstanceType<typeof Quill> | null>(null)

watch(
  deltaWithAdditionalLineEnd,
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
  if (modelWithAdditionalLineEnd.value !== expectedModel) {
    modelWithAdditionalLineEnd.value = expectedModel
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
      console.assert(delta.attributes !== undefined)
      const format = props.formats[keys[0]]
      model += format.make(delta.insert, delta.attributes[keys[0]])
    }
  }
  console.assert(model.endsWith('\n'))  // The Quill model always ends with a line end. (Unlike 'props.delta')
  return model
}

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
    <Quill ref="quill" v-model="quillModel" :blots @focus="emit('focus')" @blur="emit('blur')" />
  </div>
</template>
