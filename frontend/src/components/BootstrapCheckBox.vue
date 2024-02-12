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

const model = defineModel({ type: Boolean })

const id = self.crypto.randomUUID()
</script>

<template>
  <div class="form-check">
    <label class="form-check-label" :for="id">{{ label }}</label>
    <input class="form-check-input" :id="id" type="checkbox" v-model="model" v-bind="$attrs" />
  </div>
</template>
