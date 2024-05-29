<script setup lang="ts">
import type { Section } from '$adapted/types'
import TricolorLines from './TricolorLines.vue'
import MonocolorSection from './MonocolorSection.vue'


defineProps<{
  section: Section,
}>()

const models = defineModel<{
  [index: string]: any/* @todo Type */
}>({
  required: true,
})
</script>

<template>
  <TricolorLines>
    <MonocolorSection :section v-model="models">
      <template v-slot="{ token, tokenIndex }">
        <slot :token :tokenIndex></slot>
      </template>
    </MonocolorSection>
  </TricolorLines>
</template>
