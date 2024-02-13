<script setup>
import { ref } from 'vue'

import BTextArea from './BootstrapTextArea.vue';


const model = defineModel({ type: String })

const textArea = ref(null)

defineExpose({
  focus: () => textArea.value.focus(),
  setSelectionRange: (start, end) => textArea.value.setSelectionRange(start, end),
})
</script>

<template>
  <BTextArea ref="textArea" v-model="model" :rows="model.split('\n').length + 1"><slot></slot></BTextArea>
</template>
