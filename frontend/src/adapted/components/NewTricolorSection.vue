<script setup lang="ts">
import { ref } from 'vue'
import type { NewParagraph as Paragraph } from '$adapted/types'
import TricolorLines from './TricolorLines.vue'
import MonocolorSection from './NewMonocolorSection.vue'


defineProps<{
  paragraphs: Paragraph[],
}>()

const model = defineModel<Record<string, any/* @todo Type */>>({
  required: true,
})

const tricolorLines = ref<InstanceType<typeof TricolorLines> | null>(null)
</script>

<template>
  <TricolorLines ref="tricolorLines">
    <MonocolorSection :paragraphs v-model="model" @layoutChanged="tricolorLines?.recolor()">
      <template v-slot="{ token, tokenIndex }">
        <slot :token :tokenIndex></slot>
      </template>
    </MonocolorSection>
  </TricolorLines>
</template>
