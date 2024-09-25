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

const models = defineModel<Record<string, any/* @todo Type */>>({
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
            <template v-else-if="token.type === 'whitespace'"><wbr />&nbsp;<wbr /></template>
            <template v-else-if="token.type === 'boxedText'"><span class="boxed">{{ token.text }}</span></template>
            <template v-else-if="token.type === 'boldText'"><b>{{ token.text }}</b></template>
            <template v-else-if="token.type === 'italicText'"><i>{{ token.text }}</i></template>
            <template v-else-if="token.type === 'freeTextInput'">
              <FreeTextInput v-model="models[modelKey]" />
            </template>
            <template v-else-if="token.type === 'selectableText'">
              <SelectableText :colors="token.colors" :boxed="token.boxed" v-model="models[modelKey]">{{ token.text }}</SelectableText>
            </template>
            <template v-else-if="token.type === 'selectedText'">
              <SelectedText :color="token.color" :boxed="false">{{ token.text }}</SelectedText>
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
  /* CSS provided by client. I think we'll run into issues with sizes specified in px, but let's go with it for now. */
  font-family: Arial;
  font-size: 32px;
  line-height: 112px;
}

span.boxed {
  margin: 0;
  padding: 0 0.4em;
  border: 2px solid black;
}
</style>
