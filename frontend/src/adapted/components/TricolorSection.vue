<script setup lang="ts">
import type { Section } from '../types'
import TricolorLines from './TricolorLines.vue'
import MonocolorSection from './MonocolorSection.vue'


defineProps<{
  section: Section,
}>()
</script>

<template>
  <TricolorLines>
    <MonocolorSection :section>
      <template v-slot="{ token }">
        <slot :token></slot>
      </template>
    </MonocolorSection>
  </TricolorLines>
</template>
