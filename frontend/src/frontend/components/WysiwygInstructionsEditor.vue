<script setup lang="ts">
import { ref, watch } from 'vue'

import Quill, { type Model as QuillModel, ChoiceBlot } from './Quill.vue'


const model = defineModel<string>({required: true})

const quillModel = ref<QuillModel>([])
const quill = ref<InstanceType<typeof Quill> | null>(null)

// @todo Consider using a writable 'computed' instead of this two-way 'watch' (https://vuejs.org/api/reactivity-core.html#computed)
watch(
  model,
  model => {
    const expectedQuillModel = makeQuillModel(model)
    if (JSON.stringify(quillModel.value) !== JSON.stringify(expectedQuillModel)) {
      quillModel.value = expectedQuillModel
    }
  },
  {immediate: true}
)

watch(quillModel, quillModel => {
  const expectedModel = makeModel(quillModel)
  if (model.value !== expectedModel) {
    model.value = expectedModel
  }
})

function makeQuillModel(model: string): QuillModel {
  // @todo Get AST from server? Use .adapted? Remove this awful substring-based parsing!
  const quillModel: QuillModel = []
  while (model !== '') {
    const indexOfNextChoice = model.indexOf('{choice|')
    if (indexOfNextChoice !== -1) {
      const indexOfNextChoiceEnd = model.indexOf('}', indexOfNextChoice)
      if(indexOfNextChoiceEnd !== -1) {
        quillModel.push({insert: model.substring(0, indexOfNextChoice)})
        quillModel.push({insert: model.substring(indexOfNextChoice + 8, indexOfNextChoiceEnd), attributes: {choice: true}})
        model = model.substring(indexOfNextChoiceEnd + 1)
      } else {
        quillModel.push({insert: model})
        model = ''
      }
    } else {
      quillModel.push({insert: model})
      model = ''
    }
  }
  return quillModel
}

function makeModel(quillModel: QuillModel): string {
  let model = ''
  for (const delta of quillModel) {
    if (delta.attributes?.choice) {
      model += `{choice|${delta.insert}}`
    } else {
      model += delta.insert
    }
  }
  return model
}

// This variable is required: passing ':blots="[ChoiceBlot]"' to the 'Quill' component
// changes its 'props.blots' on every update, triggering unwanted re-computations.
const blots = [ChoiceBlot]

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
})
</script>

<template>
  <Quill ref="quill" v-model="quillModel" :blots />
</template>
