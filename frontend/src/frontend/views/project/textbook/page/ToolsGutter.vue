<script setup lang="ts">
import { computed, useSlots } from 'vue'

const slots = useSlots()

const slotNames = computed(() => Object.keys(slots))
</script>

<template>
  <h1>{{ $t('tools') }}</h1>
  <hr/>
  <template v-for="slotName in slotNames" :name="slotName" :x="42">
    <div @mousedown="e => e.stopPropagation()" @touchstart="e => e.stopPropagation()" style="cursor: initial">
      <slot :name="slotName"></slot>
    </div>
    <hr/>
  </template>
</template>
