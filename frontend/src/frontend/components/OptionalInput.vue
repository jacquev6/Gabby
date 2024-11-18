<script setup lang="ts">
import { ref, computed } from 'vue'
import { nextTick } from 'vue'

import { BLabeledInput } from './opinion/bootstrap'


defineProps<{
  label: string,
}>()

const model = defineModel<string>({required: true})

const forced = ref(false)

const inputElement = ref<InstanceType<typeof BLabeledInput> | null>(null)

function force() {
  forced.value = true
  nextTick(() => inputElement.value?.focus())
}

function unforce() {
  forced.value = false
}

const expanded = computed(() => model.value !== '' || forced.value)

defineExpose({
  expanded,
  focus: () => inputElement.value?.focus(),
  setSelectionRange: (start: number, end: number) => inputElement.value?.setSelectionRange(start, end),
  inputElement: inputElement.value?.inputElement,
})
</script>

<template>
  <BLabeledInput v-if="expanded" ref="inputElement" :label v-model="model" @focus="force" @blur="unforce" />
  <p v-else @click="force">{{ label }} <button class="btn btn-sm btn-primary">+</button></p>
</template>
