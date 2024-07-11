<script setup lang="ts">
import { watch } from 'vue'

import type { Paragraph } from '$adapted/types'
import MultipleChoicesInput from './MultipleChoicesInput.vue'
import SelectableText from './SelectableText.vue'
import SelectedText from './SelectedText.vue'
import FreeTextInput from './FreeTextInput.vue'


defineProps<{
  paragraphs: Paragraph[],
  paragraphIndexOffset: number,
}>()

const models = defineModel<{
  [index: string]: any/* @todo Type */
}>({
  required: true,
})

const emit = defineEmits<{
  layoutChanged: []
}>()

watch(models, () => emit('layoutChanged'), { deep: true })
</script>

<template>
  <p v-for="(paragraph, paragraphIndex) in paragraphs">
    <template v-for="(sentence, sentenceIndex) in paragraph.sentences">
      <template v-for="(token, tokenIndex) in sentence.tokens">
        <template v-for="modelKey in [`${paragraphIndex + paragraphIndexOffset}-${sentenceIndex}-${tokenIndex}`]">
          <span>
            <template v-if="token.type === 'plainText'">{{ token.text }}</template>
            <template v-else-if="token.type === 'whitespace'"><wbr /> <wbr /></template>
            <template v-else-if="token.type === 'boxedText'"><span class="boxed">{{ token.text }}</span></template>
            <template v-else-if="token.type === 'freeTextInput'">
              <FreeTextInput v-model="models[modelKey]" />
            </template>
            <template v-else-if="token.type === 'selectableText'">
              <SelectableText :colors="token.colors" v-model="models[modelKey]">{{ token.text }}</SelectableText>
            </template>
            <template v-else-if="token.type === 'selectedText'">
              <SelectedText :colors="token.colors" :color="token.color">{{ token.text }}</SelectedText>
            </template>
            <template v-else-if="token.type === 'selectedClicks'">
              <SelectedText :colors="token.colors" :color="token.color">{{ token.color }} {{ $t('nClicks', token.color) }}</SelectedText>
            </template>
            <template v-else-if="token.type === 'multipleChoicesInput'">
              <MultipleChoicesInput :choices="token.choices" v-model="models[modelKey]" />
            </template>
            <template v-else>
              <span>{{ $t('thisIsABug') }} {{ ((t: never) => t)(token) }}</span>
            </template>
          </span>
        </template>
      </template>
      <span> </span>
    </template>
  </p>
</template>

<style scoped>
p {
  line-height: 2.5em;
}

span.boxed {
  margin: 0;
  padding: 0 0.4em;
  border: 2px solid black;
}
</style>
