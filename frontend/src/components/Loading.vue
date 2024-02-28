<script setup>
import { computed } from 'vue'


const props = defineProps({
  loading: {
    type: Boolean,
    required: true,
  },
  size: {
    type: String,
    default: '2rem',
  },
})

const style = computed(() => {
  if (props.loading) {
    return {
      'min-height': props.size,
    }
  } else {
    return {
    }
  }
})
</script>

<template>
  <div style="position: relative" :style="style">
    <slot v-bind="$attrs"></slot>
    <div v-if="loading" class="d-flex justify-content-center align-items-center" style="position: absolute; top: 0; left: 0; height: 100%; width: 100%; background: rgba(0, 0, 0, 0.5)">
      <div class="spinner-border" :style="{width: size, height: size}" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
  </div>
</template>