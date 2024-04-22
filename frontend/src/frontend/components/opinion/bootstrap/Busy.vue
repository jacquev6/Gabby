<script setup>
import { ref, computed, watch } from 'vue'


const props = defineProps({
  busy: {
    type: Boolean,
    required: true,
  },
  showWhileBusy: {
    type: String,
    default: 'always',
  },
  size: {
    type: String,
    default: '2rem',
  },
})

const hasEverBeenNotBusy = ref(false)
watch(() => props.busy, (busy) => {
  if (!busy) {
    hasEverBeenNotBusy.value = true
  }
})

const show = computed(() => {
  if (props.showWhileBusy === 'always') {
    return true
  } else if (props.showWhileBusy === 'afterNotBusy') {
    return hasEverBeenNotBusy.value
  } else {
    console.assert(props.showWhileBusy === 'never')
    return !props.busy
  }
})

const style = computed(() => {
  if (props.busy) {
    return {
      'min-height': props.size,
    }
  } else {
    return {}
  }
})
</script>

<template>
  <div style="position: relative" :style="style">
    <template v-if="show">
      <slot v-bind="$attrs"></slot>
    </template>
    <div v-if="busy" class="busy d-flex justify-content-center align-items-center" style="position: absolute; top: 0; left: 0; height: 100%; width: 100%; background: rgba(0, 0, 0, 0.5)">
      <div class="spinner-border" :style="{width: size, height: size}" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
  </div>
</template>
