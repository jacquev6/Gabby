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

export function makeRange(formats: Record<string, Format>, quillModel: QuillModel, quillRange: SelectionRange): SelectionRange {
  const ops = JSON.parse(JSON.stringify(quillModel)) as QuillModel

  let quillIndex = quillRange.index
  let index = 0
  let quillLength = quillRange.length
  let length = 0

  // let model = makeModel(formats, quillModel)

  // console.clear()
  // console.log('Init:', quillIndex, quillLength, JSON.stringify(ops), index, length, model, '[' + model.slice(index, index + length) + ']')

  // Skip ops before quillIndex
  while (true) {
    const opLength = 'attributes' in ops[0] ? ops[0].insert.length : 1
    if (quillIndex >= opLength) {
      quillIndex -= opLength
      index += makeModelPart(formats, ops[0]).length
      // console.log('Skipping', JSON.stringify(ops[0]))
      ops.shift()
    } else {
      break
    }
  }

  // console.log('Starts in:', quillIndex, quillLength, JSON.stringify(ops), index, length, '[' + model.slice(index, index + length) + ']')

  // Range starts at the start of, or in, ops[0]
  if ('attributes' in ops[0]) {
    if (Object.keys(ops[0].attributes).length === 0) {
      // It's a plain text op, we can start in the middle of it
      index += quillIndex
    } else {
      // It's a formatted text op, we need to start at the beginning (lengthening the range by the left)
      if (quillLength > 0) {
        quillLength += quillIndex
        quillIndex = 0
      }
    }
  } else {
    // It's an embed op, of length 1
    quillLength += quillIndex
    quillIndex = 0
  }

  if (quillLength === 0) {
    return {index, length}
  }

  // console.log('C', quillIndex, quillLength, JSON.stringify(ops), index, length, '[' + model.slice(index, index + length) + ']')

  // Accumulate ops until quillLength
  while (quillLength > 0) {
    const opLength = 'attributes' in ops[0] ? ops[0].insert.length : 1
    if (quillIndex + quillLength > opLength) {
      if ('attributes' in ops[0]) {
        if (Object.keys(ops[0].attributes).length === 0) {
          // Plain text op: include its suffix
          length += opLength - quillIndex
        } else {
          console.assert(quillIndex === 0)
          length += makeModelPart(formats, ops[0]).length
        }
      } else {
        // Embed op: include it
        length += makeModelPart(formats, ops[0]).length
      }
      quillLength -= opLength - quillIndex
      quillIndex = 0
      // console.log('Including', JSON.stringify(ops[0]), 'to', length)
      ops.shift()
    } else {
      break
    }
  }

  // console.log('Stops in', quillIndex, quillLength, JSON.stringify(ops), index, length, '[' + model.slice(index, index + length) + ']')

  // Range stops at the start of, or in, ops[0]
  if (quillLength > 0) {
    if ('attributes' in ops[0]) {
      if (Object.keys(ops[0].attributes).length === 0) {
        // It's a plain text op, we can stop in the middle of it
        length += quillLength
      } else {
        // It's a formatted text op, we need to stop at the end (lengthening the range by the right)
        length += makeModelPart(formats, ops[0]).length
      }
    } else {
      // It's an embed op, of length 1
      length += makeModelPart(formats, ops[0]).length
    }
  }

  // console.log('E', quillIndex, quillLength, JSON.stringify(ops), index, length, '[' + model.slice(index, index + length) + ']')

  return {index, length}
}
</script>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'

import Quill, { type Model as QuillModel, type SelectionRange } from './Quill.vue'

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
      @selectionChange="range => emit('selectionChange', makeRange(formats, quillModel, range))"
    />
  </div>
</template>
