<script setup lang="ts">
defineOptions({
  // Disable attribute inheritance to apply all fallthrough attributes to the textarea
  // https://vuejs.org/guide/components/attrs#disabling-attribute-inheritance
  inheritAttrs: false
})

defineProps<{
  label: string,
}>()

const model = defineModel<boolean>({default: false})

const id = `checkbox-${ Math.floor(Math.random() * 4000000000) }`
</script>

<template>
  <div class="form-check">
    <label class="form-check-label" :for="id">{{ label }}</label>
    <input class="form-check-input" :id="id" type="checkbox" v-model="model" v-bind="$attrs" />
  </div>
</template>
