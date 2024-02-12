<script setup>
import { ref } from 'vue'

defineOptions({
  // Disable attribute inheritance to apply all fallthrough attributes to the textarea
  // https://vuejs.org/guide/components/attrs#disabling-attribute-inheritance
  inheritAttrs: false
})

const props = defineProps({
  label: { type: String, required: true },
})

const model = defineModel({})

const id = self.crypto.randomUUID()
</script>

<template>
  <div class="mb-3">
    <label class="form-label" :for="id">{{ label }}</label>
    <input class="form-control" :id="id" v-model="model" v-bind="$attrs"/>
  </div>
</template>
