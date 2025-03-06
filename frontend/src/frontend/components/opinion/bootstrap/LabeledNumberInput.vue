<script setup lang="ts">
import { computed } from 'vue'

defineOptions({
  inheritAttrs: false
})

defineProps<{
  label: string
}>()

const model = defineModel<number | null>({required: true})

const internalModel = computed({
  get() {
    if (model.value === null) {
      return ''
    } else {
      return model.value
    }
  },
  set(value: number | '') {
    if (typeof value === 'number') {
      model.value = value
    } else {
      console.assert(value === '', 'Expected empty string')
      model.value = null
    }
  }
})

const id = `input-${ Math.floor(Math.random() * 4000000000) }`
</script>

<template>
  <div class="mb-3">
    <label class="form-label" :for="id">{{ label }}</label>
    <input ref="inputElement" class="form-control" :id type="number" v-model="internalModel" v-bind="$attrs" />
  </div>
</template>
