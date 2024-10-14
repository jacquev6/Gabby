<script lang="ts">
import { BoldBlot, ItalicBlot } from './Quill.vue'


export const basicFormats = {
  bold: {
    kind: 'text' as const,
    make: (text: string) => `{bold|${text}}`,
    blot: BoldBlot,
  },
  italic: {
    kind: 'text' as const,
    make: (text: string) => `{italic|${text}}`,
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

export function makeModel(formats: Record<string, Format>, quillModel: QuillModel): string {
  let model = ''
  for (const delta of quillModel) {
    model += makeModelPart(formats, delta)
  }
  console.assert(model.endsWith('\n'))  // The Quill model always ends with a line end. (Unlike 'props.delta')
  return model
}

function makeModelPart(formats: Record<string, Format>, delta: QuillModel[number]): string {
  if ('attributes' in delta) {
    console.assert(typeof delta.insert === 'string')
    const keys = Object.keys(delta.attributes ?? {})
    if (keys.length === 0) {
      return delta.insert
    } else {
      console.assert(keys.length === 1)
      console.assert(delta.attributes !== undefined)
      const format = formats[keys[0]]
      console.assert(format !== undefined)
      console.assert(format.kind === 'text')
      return format.make(delta.insert, delta.attributes[keys[0]])
    }
  } else {
    console.assert(typeof(delta.insert) === 'object')
    const keys = Object.keys(delta.insert ?? {})
    console.assert(keys.length === 1)
    const format = formats[keys[0]]
    console.assert(format !== undefined)
    console.assert(format.kind === 'embed')
    return format.make(delta.insert[keys[0]])
  }
}
</script>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'

import Quill, { type Model as QuillModel } from './Quill.vue'

const props = defineProps<{
  label: string
  formats: Record<string, Format>
  delta: QuillModel
}>()

const model = defineModel<string>({required: true})

const emit = defineEmits<{
  focus: []
  blur: []
  selectionChange: [{index: number, length: number}]
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

const deltaWithAdditionalLineEnd = computed((): QuillModel => {
  if (props.delta.length === 0) {
    return [{insert: '\n', attributes: {}}]
  } else {
    const lastOp = props.delta[props.delta.length - 1]
    if ('attributes' in lastOp && Object.keys(lastOp.attributes).length === 0) {
      return [...props.delta.slice(0, -1), {insert: lastOp.insert + '\n', attributes: {}}]
    } else {
      return [...props.delta, {insert: '\n', attributes: {}}]
    }
  }
})

const quillModel = ref<QuillModel>([])
const quill = ref<InstanceType<typeof Quill> | null>(null)

watch(
  deltaWithAdditionalLineEnd,
  delta => {
    if (JSON.stringify(quillModel.value) !== JSON.stringify(delta)) {
      quillModel.value = delta
    }
  },
  {immediate: true},
)

watch(quillModel, quillModel => {
  const expectedModel = makeModel(props.formats, quillModel)
  if (modelWithAdditionalLineEnd.value !== expectedModel) {
    modelWithAdditionalLineEnd.value = expectedModel
  }
})

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
    <Quill
      ref="quill"
      v-model="quillModel"
      :blots
      @focus="emit('focus')"
      @blur="emit('blur')"
    />
  </div>
</template>
