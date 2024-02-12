<script setup>
import { ref, watch, nextTick } from 'vue'

import BTextArea from './BootstrapTextArea.vue';

const props = defineProps({
  label: { type: String, required: true },
})

const model = defineModel({ type: String })

const force = ref(false)

watch(model, () => { force.value = false })

const textarea = ref(null)

function activate() {
  force.value = true
  nextTick(() => textarea.value.focus())
}
</script>

<template>
  <BTextArea v-if="model || force" ref="textarea" :label="label" v-model="model" :rows="model.split('\n').length + 1" />
  <p v-else @click="activate">{{ label }} <button class="btn btn-sm btn-primary">+</button></p>
</template>
