<script setup lang="ts">
defineOptions({
  inheritAttrs: false
})

defineProps<{
  label: string,
}>()

const model = defineModel<unknown>()

const id = `input-${ Math.floor(Math.random() * 4000000000) }`
</script>

<template>
  <div class="mb-3">
    <label class="form-label" :for="id">{{ label }}</label>
    <input class="form-control" :id="id" v-model="model" v-bind="$attrs"/>
  </div>
</template>
