<script setup lang="ts">
import { ref, computed } from 'vue'
import { nextTick } from 'vue'

import { BLabeledTextarea } from './opinion/bootstrap'


const props = defineProps<{
  label: string,
  enforceTrailingLineEnd: boolean,
}>()

const model = defineModel<string>({required: true})

const forced = ref(false)

const textArea = ref<InstanceType<typeof BLabeledTextarea> | null>(null)

function force() {
  forced.value = true
  nextTick(() => textArea.value?.focus())
}

function unforce() {
  forced.value = false
}

const emptyModel = computed(() => props.enforceTrailingLineEnd ? '\n' : '')

const expanded = computed(() => model.value !== emptyModel.value || forced.value)

defineExpose({
  expanded,
  focus: () => textArea.value?.focus(),
  setSelectionRange: (start: number, end: number) => textArea.value?.setSelectionRange(start, end),
  textarea: textArea.value?.textarea,
})
</script>

<template>
  <BLabeledTextarea v-if="expanded" ref="textArea" :label :enforceTrailingLineEnd v-model="model" @focus="force" @blur="unforce" />
  <p v-else @click="force">{{ label }} <button class="btn btn-sm btn-primary">+</button></p>
</template>
