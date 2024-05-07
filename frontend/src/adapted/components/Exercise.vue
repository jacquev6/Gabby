<script setup lang="ts">
import { computed, inject } from 'vue'

import type { Settings, Exercise } from '../types'
import SelectableWord from './SelectableWord.vue'
import TricolorSection from './TricolorSection.vue'
import MonocolorSection from './MonocolorSection.vue'


defineProps<{
  exercise: Exercise,
}>()

const settings = inject('settings') as Settings

const section = computed(() => settings.tricolorWording ? TricolorSection : MonocolorSection)
</script>

<template>
  <p>{{ exercise.instructions }}</p>
  <component :is="section" :section="exercise.wording">
    <template v-slot="{ token }">
      <template v-if="false"></template>
      <template v-else-if="token.type === 'plainWord'" :token="token">{{ token.text }}</template>
      <template v-else-if="token.type === 'whitespace'" :token="token"><wbr /> <wbr /></template>
      <template v-else-if="token.type === 'punctuation'" :token="token">{{ token.text }}</template>
      <template v-else-if="token.type === 'freeTextInput'" :token="token">
        <input type="text" />
      </template>
      <template v-else-if="token.type === 'selectableWord'">
        <SelectableWord :colors="1">{{ token.text }}</SelectableWord>
      </template>
      <template v-else>
        <span>{{ ((t: never) => t)(token) }}</span>
      </template>
    </template>
  </component>
</template>
