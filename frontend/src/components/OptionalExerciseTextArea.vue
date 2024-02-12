<script setup>
import { ref, watch, nextTick } from 'vue'

const model = defineModel({ type: String })

const id = self.crypto.randomUUID()

const force = ref(false)

watch(model, () => { force.value = false })

const textarea = ref(null)

function activate() {
  force.value = true
  nextTick(() => textarea.value.focus())
}
</script>

<template>
  <div class="mb-3">
    <label class="form-label" :for="id"><slot></slot> <button class="btn btn-sm btn-primary" v-if="!model && !force" href="#" @click.prevent="activate">+</button></label>
    <textarea class="form-control" :id="id" ref="textarea" v-if="model || force" v-model="model" :rows="model.split('\n').length + 1"></textarea>
  </div>
</template>
