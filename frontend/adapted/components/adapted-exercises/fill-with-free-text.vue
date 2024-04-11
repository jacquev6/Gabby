<script setup>
import { reactive, computed, watch } from 'vue'
import chroma from 'chroma-js'


const props = defineProps({
  exercise: {
    type: Object,
    required: true
  },
})

const placeholder = {}

const lines = computed(() => props.exercise.wording.split('\n').filter(line => line !== '').map(line => {
  const textParts = line.trim().split(props.exercise.adaptation.placeholder).map(part => part.trim())
  const parts = []
  for (const textPart of textParts) {
    if (parts.length !== 0) {
      parts.push(placeholder)
    }
    parts.push(textPart)
  }
  return parts
}))
</script>

<template>
  <template v-for="line in lines">
    <p>
      <template v-for="part in line">
        <template v-if="part === placeholder">
          <wbr/> <input type="text" /> <wbr />
        </template>
        <template v-else>
          <span>{{ part }}</span>
        </template>
      </template>
    </p>
  </template>
</template>
