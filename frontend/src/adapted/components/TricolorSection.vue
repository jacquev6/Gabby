<script setup lang="ts">
import { ref } from 'vue'
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

const tricolorLines = ref<typeof TricolorLines | null>(null)
</script>

<template>
  <TricolorLines ref="tricolorLines">
    <MonocolorSection :paragraphs :paragraphIndexOffset v-model="model" @layoutChanged="tricolorLines?.recolor()">
      <template v-slot="{ token, tokenIndex }">
        <slot :token :tokenIndex></slot>
      </template>
    </MonocolorSection>
  </TricolorLines>
</template>
