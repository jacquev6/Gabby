<script setup lang="ts">
import type { Section } from '$adapted/types'
import TricolorLines from './TricolorLines.vue'
import MonocolorSection from './MonocolorSection.vue'


defineProps<{
  section: Section,
}>()
</script>

<template>
  <TricolorLines>
    <MonocolorSection :section>
      <template v-slot="{ token, tokenIndex }">
        <slot :token :tokenIndex></slot>
      </template>
    </MonocolorSection>
  </TricolorLines>
</template>
