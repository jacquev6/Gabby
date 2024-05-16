<script setup lang="ts">
import type { Exercise } from '$adapted/types'


defineProps<{
  section: Exercise['wording'],
}>()
</script>

<template>
  <p v-for="(paragraph, paragraphIndex) in section.paragraphs">
    <template v-for="(sentence, sentenceIndex) in paragraph.sentences">
      <template v-for="(token, tokenIndex) in sentence.tokens">
        <span><slot :token :tokenIndex="`${paragraphIndex}-${sentenceIndex}-${tokenIndex}`"></slot></span>
      </template>
      <span> </span>
    </template>
  </p>
</template>

<style scoped>
p {
  line-height: 2.5em;
}
</style>
