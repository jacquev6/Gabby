<script lang="ts">
import type AttributeMap from 'quill-delta/dist/AttributeMap'


// Partial of node_modules/quill-delta/dist/Op.d.ts, more readable than using TypeScript's 'Omit',
// but slightly more fragile in the unlikely case quill-delta changes its interface. OK.
interface InsertOp {
  insert: string
  attributes?: AttributeMap
}

export type Model = InsertOp[]

export type Format = 'bold' | 'italic' | 'choice'
</script>

<script setup lang="ts">
import { ref, shallowRef, watch } from 'vue'
import { onMounted } from 'vue'
import Quill from 'quill/core'
import 'quill/dist/quill.core.css'  // Removing this CSS causes a bug on Firefox:
// spaces added at the end of the editor are ignored, resulting in space-less text.
// This is because this CSS adds a 'white-space: pre' style or similar.
// We don't want the typographical styling from Quill, but we do want to avoid similar bugs.
// Adding this 'white-space: pre' style ourselves would prevent this very bug, but we don't know
// about other bugs. Quill is designed to be used with its CSS. So we do import the css,
// and re-style the typography.


// @todo Avoid registering blots globally: https://quilljs.com/docs/configuration#formats
// seems to indicate that 'formats' and 'registry' can be passed at instanciation time.

const InlineBlot = Quill.import('blots/inline') as any/* @todo Type. Maybe see https://github.com/slab/quill/issues/1233 */

class BoldBlot extends InlineBlot {
  static blotName = 'bold'
  static tagName = 'bold-blot'
}

if (Quill.imports['formats/bold'] === undefined) {
  Quill.register(BoldBlot)
}

class ItalicBlot extends InlineBlot {
  static blotName = 'italic'
  static tagName = 'italic-blot'
}

if (Quill.imports['formats/italic'] === undefined) {
  Quill.register(ItalicBlot)
}

class ChoiceBlot extends InlineBlot {
  static blotName = 'choice'
  static tagName = 'choice-blot'
}

if (Quill.imports['formats/choice'] === undefined) {
  Quill.register(ChoiceBlot)
}

const model = defineModel<Model>({required: true})

const container = ref<HTMLDivElement | null>(null)
let quill = shallowRef<Quill | null>(null)

function getContents(quill: Quill): Model {
  return quill.getContents().ops.map(op => {
    console.assert(typeof op.insert === 'string')
    return {insert: op.insert, attributes: op.attributes}
  })
}

watch([quill, model], ([quill, model]) => {
  if (quill !== null && JSON.stringify(getContents(quill)) !== JSON.stringify(model)) {
    quill.setContents(model)
  }
})

onMounted(() => {
  console.assert(container.value !== null)
  quill.value = new Quill(
    container.value,
    {
      modules: {history: {maxStack: 0, userOnly: true}},  // https://github.com/slab/quill/issues/691#issuecomment-797861431
    },
  )
  quill.value.on('text-change', (_1: unknown, _2: unknown, source: string) => {
    if (source === 'user') {
      console.assert(quill.value !== null)
      model.value = getContents(quill.value)
    }
  })
})

function toggle(format: Format) {
  console.assert(quill.value !== null)
  console.assert(Quill.imports[`formats/${format}`] !== undefined)
  if (quill.value.getFormat()[format]) {
    quill.value.format(format, false, 'user')
  } else {
    quill.value.format(format, true, 'user')
  }
}

defineExpose({
  toggle,
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

div.ql-editor choice-blot {
  margin: 0;
  padding: 0 0.4em;
  border: 2px solid black;
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
