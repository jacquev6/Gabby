<script setup lang="ts" generic="T">
import { label as makeLabel, value as makeValue, disabled as makeDisabled, type Option } from './Select.vue'
import Checkbox from './LabeledCheckbox.vue'
import { computed } from 'vue'


defineOptions({
  inheritAttrs: false
})

const props = defineProps<{
  label: string,
  options: Option<T>[],
}>()

const model = defineModel<T | null>()

const checked = computed(() => props.options.map(option => {
  const optionValue = makeValue(option)
  return computed({
    get() {
      return model.value === optionValue
    },
    set(value: boolean) {
      if (value) {
          model.value = optionValue
      } else {
          model.value = null
      }
    }
  })
}))
</script>

<template>
  <div class="mb-3">
    <p class="form-label">{{ label }}</p>
    <Checkbox v-for="option, index in options" v-model="checked[index].value" :label="makeLabel(option)" :value="makeValue(option)" :disabled="makeDisabled(option)" />
  </div>
</template>
