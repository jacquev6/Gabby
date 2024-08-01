<script setup lang="ts">
import { ref, watch } from 'vue'

import Quill, { type Model as QuillModel, ChoiceBlot } from './Quill.vue'


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
    if (makeModel(quillModel.value) !== makeModel(delta)) {
      console.log('delta -> quillModel', makeModel(quillModel.value), '->', makeModel(delta))
      quillModel.value = delta
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
