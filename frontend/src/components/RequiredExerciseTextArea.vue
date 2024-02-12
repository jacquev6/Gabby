<script setup>
const model = defineModel({ type: String })

const id = self.crypto.randomUUID()
</script>

<template>
  <div class="mb-3">
    <label class="form-label" :for="id"><slot></slot></label>
    <textarea class="form-control" :id="id" v-model="model" :rows="model.split('\n').length + 1"></textarea>
  </div>
</template>
