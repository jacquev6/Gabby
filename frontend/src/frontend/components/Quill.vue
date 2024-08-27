<script lang="ts">
import type AttributeMap from 'quill-delta/dist/AttributeMap'
import Quill, { Parchment } from 'quill/core'
import Block from 'quill/blots/block'
import Break from 'quill/blots/break'
import Cursor from 'quill/blots/cursor'
import Inline from 'quill/blots/inline'
import Scroll from 'quill/blots/scroll'
import TextBlot from 'quill/blots/text'
import Keyboard from 'quill/modules/keyboard'


// Monkey-patching Quill to remove some default bindings, until I learn how to do it properly.
delete Keyboard.DEFAULTS.bindings.bold
delete Keyboard.DEFAULTS.bindings.italic

// Partial of node_modules/quill-delta/dist/Op.d.ts, more readable than using TypeScript's 'Omit',
// but slightly more fragile in the unlikely case quill-delta changes its interface. OK.
interface InsertOp {
  insert: string
  attributes?: AttributeMap
}

export type Model = InsertOp[]

function makeMinimalRegistry() {
  const registry = new Parchment.Registry()
  registry.register(Block)
  registry.register(Break)
  registry.register(Cursor)
  registry.register(Inline)
  registry.register(Scroll)
  registry.register(TextBlot)
  return registry
}

export type Blot = typeof Inline

function makeRegistryWithBlots(blots: Blot[]) {
  const registry = makeMinimalRegistry()
  for (const blot of blots) {
    registry.register(blot)
  }
  return registry
}

export const InlineBlot = Quill.import('blots/inline') as Blot

export class BoldBlot extends InlineBlot {
  static override blotName = 'bold'
  static override tagName = 'bold-blot'
}

export class ItalicBlot extends InlineBlot {
  static override blotName = 'italic'
  static override tagName = 'italic-blot'
}
</script>

<script setup lang="ts">
import { ref, watch, computed } from 'vue'
import 'quill/dist/quill.core.css'  // Removing this CSS causes a bug on Firefox:
// spaces added at the end of the editor are ignored, resulting in space-less text.
// This is because this CSS adds a 'white-space: pre' style or similar.
// We don't want the typographical styling from Quill, but we do want to avoid similar bugs.
// Adding this 'white-space: pre' style ourselves would prevent this very bug, but we don't know
// about other bugs. Quill is designed to be used with its CSS. So we do import the css,
// and re-style the typography.


const props = defineProps<{
  blots: Blot[]
}>()

const emit = defineEmits<{
  focus: []
  blur: []
}>()

const registry = computed(() => makeRegistryWithBlots(props.blots))

const model = defineModel<Model>({required: true})

const container = ref<HTMLDivElement | null>(null)

function getContents(quill: Quill): Model {
  return quill.getContents().ops.map(op => {
    console.assert(typeof op.insert === 'string')
    return {insert: op.insert, attributes: op.attributes}
  })
}

const hasFocus = ref(false)
const currentFormat = ref<Record<string, unknown>>({})

const quill = computed(() => {
  if (container.value === null) {
    return null
  } else {
    const quill = new Quill(
      container.value,
      {
        registry: registry.value,
        modules: {history: {maxStack: 0, userOnly: true}},  // https://github.com/slab/quill/issues/691#issuecomment-797861431
      },
    )
    quill.on('text-change', (_delta: unknown, _oldDelta: unknown, source: string) => {
      if (source === 'user') {
        model.value = getContents(quill)
      }
    })
    quill.on('selection-change', (range: object | null, _oldRange: object | null, _source: string) => {
      const hadFocus = hasFocus.value
      hasFocus.value = range !== null
      if (hasFocus.value) {
        currentFormat.value = quill.getFormat()
        if (!hadFocus) {
          emit('focus')
        }
      } else {
        currentFormat.value = {}
        if (hadFocus) {
          emit('blur')
        }
      }
    })
    return quill
  }
})

watch([quill, model], ([quill, model]) => {
  if (quill !== null && JSON.stringify(getContents(quill)) !== JSON.stringify(model)) {
    quill.setContents(model)
  }
})

function toggle(formatting: string, value: unknown = true) {
  console.assert(quill.value !== null)

  currentFormat.value = {}

  // Clear formatting of the caret, in case selection is empty.
  // Incidentally, this also clears the formatting of the selected range in whole.
  const previousFormat = quill.value.getFormat()
  for (const f of Object.keys(previousFormat)) {
    quill.value.format(f, false, 'user')
  }

  // Clear any formatting of (any part of) the selected range.
  const {index, length} = quill.value.getSelection(true)
  quill.value.removeFormat(index, length)

  // Toggle the requested formatting, either for the caret, or for the selected range.
  if (previousFormat[formatting] !== value) {
    quill.value.format(formatting, value, 'user')
    currentFormat.value = {[formatting]: value}
  }
}

defineExpose({
  toggle,
  hasFocus,
  currentFormat,
  focus() {
    console.assert(quill.value !== null)
    quill.value.focus()
  },
  getSelection() {
    console.assert(quill.value !== null)
    return quill.value.getSelection(true)
  },
  setSelection(index: number, length: number) {
    console.assert(quill.value !== null)
    quill.value.setSelection(index, length)
  },
  getLength() {
    console.assert(quill.value !== null)
    return quill.value.getLength()
  },
})
</script>

<template>
  <div ref="container"></div>
</template>

<style>
div.ql-editor bold-blot {
  font-weight: bold;
}

div.ql-editor italic-blot {
  font-style: italic;
}

/* Fight against 'quill/dist/quill.core.css' to achieve formatting close to Bootstrap's.
We'll soon benefit from learning more about customizing Bootstrap's SCSSs. */
div.ql-editor {
  border: var(--bs-border-width) solid var(--bs-border-color);
  border-radius: var(--bs-border-radius);
  padding: .375rem .75rem;
  font-size: 1rem;
  line-height: 1.5;
  font-family: var(--bs-body-font-family);
  transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out;
}

div.ql-editor:focus {
  color: var(--bs-body-color);
  background-color: var(--bs-body-bg);
  border-color: #86b7fe;
  outline: 0;
  box-shadow: 0 0 0 .25rem rgba(13,110,253,.25);
}
</style>
