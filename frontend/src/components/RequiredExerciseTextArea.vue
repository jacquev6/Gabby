<script setup>
import BTextArea from './BootstrapTextArea.vue';

const model = defineModel({ type: String })
</script>

<template>
  <BTextArea v-model="model" :rows="model.split('\n').length + 1"><slot></slot></BTextArea>
</template>
