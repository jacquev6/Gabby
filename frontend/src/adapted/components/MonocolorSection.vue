<script setup lang="ts">
import type { Exercise } from '$adapted/types'


defineProps<{
  section: Exercise['wording'],
}>()
</script>

<template>
  <p v-for="paragraph in section.paragraphs">
    <template v-for="sentence in paragraph.sentences">
      <template v-for="(token, tokenIndex) in sentence.tokens">
        <span><slot :token :tokenIndex></slot></span>
      </template>
      <span> </span>
    </template>
  </p>
</template>
