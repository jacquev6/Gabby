<script setup lang="ts">
import type { Paragraph } from '$adapted/types'
import TricolorLines from './TricolorLines.vue'
import MonocolorSection from './MonocolorSection.vue'


defineProps<{
  paragraphs: Paragraph[],
  paragraphIndexOffset: number,
}>()

const model = defineModel<{
  [index: string]: any/* @todo Type */
}>({
  required: true,
})
</script>

<template>
  <TricolorLines>
    <MonocolorSection :paragraphs :paragraphIndexOffset v-model="model">
      <template v-slot="{ token, tokenIndex }">
        <slot :token :tokenIndex></slot>
      </template>
    </MonocolorSection>
  </TricolorLines>
</template>
