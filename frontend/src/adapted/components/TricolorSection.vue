<script setup lang="ts">
import { ref } from 'vue'
import type { Paragraph } from '$adapted/types'
import TricolorLines from './TricolorLines.vue'
import MonocolorSection from './MonocolorSection.vue'


defineProps<{
  paragraphs: Paragraph[],
  centered: boolean
  first: boolean
}>()

const model = defineModel<Record<string, any/* @todo Type */>>({
  required: true,
})

const tricolorLines = ref<InstanceType<typeof TricolorLines> | null>(null)
</script>

<template>
  <TricolorLines ref="tricolorLines">
    <MonocolorSection :paragraphs :centered :first v-model="model" @layoutChanged="tricolorLines?.recolor()" />
  </TricolorLines>
</template>
