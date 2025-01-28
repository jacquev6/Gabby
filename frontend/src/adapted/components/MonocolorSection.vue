<script setup lang="ts">
import { computed, watch } from 'vue'
import { nextTick } from 'vue'

import type { Paragraph } from '$adapted/types'
import MultipleChoicesInput from './MultipleChoicesInput.vue'
import SelectableText from './SelectableText.vue'
import SelectedText from './SelectedText.vue'
import FreeTextInput from './FreeTextInput.vue'


const props = withDefaults(defineProps<{
  paragraphs: Paragraph[]
  centered?: boolean
  first?: boolean
}>(), {
  centered: false,
  first: false,
})

const models = defineModel<Record<string, any/* @todo Type */>>({
  required: true,
})

const emit = defineEmits<{
  layoutChanged: []
}>()

watch(models, () => nextTick(() => emit('layoutChanged')), { deep: true })

const style = computed(() => ({
  textAlign: props.centered ? 'center' as const : 'left' as const,
}))
</script>

<template>
  <p v-for="(paragraph, paragraphIndex) in paragraphs" :style :class="{first: first && paragraphIndex === 0}">
    <template v-for="(token, tokenIndex) in paragraph.tokens">
      <template v-for="modelKey in [`${paragraphIndex}-${tokenIndex}`]">
        <template v-if="token.type === 'plainText'">
          <span class="tricolorable">{{ token.text }}</span>
        </template>
        <template v-else-if="token.type === 'whitespace'">
          <span>&nbsp;&nbsp;<wbr /></span>
        </template>
        <template v-else-if="token.type === 'boxedText'">
          <span class="tricolorable boxed">{{ token.text }}</span>
        </template>
        <template v-else-if="token.type === 'passiveFormattedText'">
          <span class="tricolorable" :class="{passiveBold: token.bold, passiveItalic: token.italic}">{{ token.text }}</span>
        </template>
        <template v-else-if="token.type === 'freeTextInput'">
          <FreeTextInput class="tricolorable" v-model="models[modelKey]" />
        </template>
        <template v-else-if="token.type === 'selectableText'">
          <SelectableText class="tricolorable" :colors="token.colors" :boxed="token.boxed" v-model="models[modelKey]">{{ token.text }}</SelectableText>
        </template>
        <template v-else-if="token.type === 'selectable'">
          <SelectableText :colors="token.colors" :boxed="token.boxed" v-model="models[modelKey]">
            <template v-for="subToken in token.contents">
              <template v-if="subToken.type === 'plainText'">
                <span class="tricolorable">{{ subToken.text }}</span>
              </template>
              <template v-else-if="subToken.type === 'whitespace'">
                <span>&nbsp;&nbsp;<wbr /></span>
              </template>
              <template v-else-if="subToken.type === 'boxedText'">
                <span class="tricolorable boxed">{{ subToken.text }}</span>
              </template>
              <template v-else-if="subToken.type === 'passiveFormattedText'">
                <span class="tricolorable" :class="{passiveBold: subToken.bold, passiveItalic: subToken.italic}">{{ subToken.text }}</span>
              </template>
              <template v-else-if="subToken.type === 'freeTextInput'">
                <FreeTextInput class="tricolorable" v-model="models[modelKey]" />
              </template>
              <template v-else-if="subToken.type === 'selectedText'">
                <SelectedText class="tricolorable" :color="subToken.color" :boxed="false">{{ subToken.text }}</SelectedText>
              </template>
              <template v-else-if="subToken.type === 'multipleChoicesInput'">
                <MultipleChoicesInput class="tricolorable" :showArrowBefore="subToken.show_arrow_before" :choices="subToken.choices" placeholder="...." :showChoicesByDefault="subToken.show_choices_by_default" v-model="models[modelKey]" />
              </template>
              <template v-else>
                <span>{{ $t('thisIsABug') }} {{ ((t: never) => t)(subToken) }}</span>
              </template>
            </template>
          </SelectableText>
        </template>
        <template v-else-if="token.type === 'boxed'">
          <span class="boxed">
            <template v-for="subToken in token.contents">
              <template v-if="subToken.type === 'plainText'">
                <span class="tricolorable">{{ subToken.text }}</span>
              </template>
              <template v-else-if="subToken.type === 'whitespace'">
                <span>&nbsp;&nbsp;<wbr /></span>
              </template>
              <template v-else-if="subToken.type === 'boxedText'">
                <span class="tricolorable boxed">{{ subToken.text }}</span>
              </template>
              <template v-else-if="subToken.type === 'passiveFormattedText'">
                <span class="tricolorable" :class="{passiveBold: subToken.bold, passiveItalic: subToken.italic}">{{ subToken.text }}</span>
              </template>
              <template v-else-if="subToken.type === 'freeTextInput'">
                <FreeTextInput class="tricolorable" v-model="models[modelKey]" />
              </template>
              <template v-else-if="subToken.type === 'selectedText'">
                <SelectedText class="tricolorable" :color="subToken.color" :boxed="false">{{ subToken.text }}</SelectedText>
              </template>
              <template v-else-if="subToken.type === 'multipleChoicesInput'">
                <MultipleChoicesInput class="tricolorable" :showArrowBefore="subToken.show_arrow_before" :choices="subToken.choices" placeholder="...." :showChoicesByDefault="subToken.show_choices_by_default" v-model="models[modelKey]" />
              </template>
              <template v-else>
                <span>{{ $t('thisIsABug') }} {{ ((t: never) => t)(subToken) }}</span>
              </template>
            </template>
          </span>
        </template>
        <template v-else-if="token.type === 'selectedText'">
          <SelectedText class="tricolorable" :color="token.color" :boxed="false">{{ token.text }}</SelectedText>
        </template>
        <template v-else-if="token.type === 'multipleChoicesInput'">
          <MultipleChoicesInput class="tricolorable" :showArrowBefore="token.show_arrow_before" :choices="token.choices" placeholder="...." :showChoicesByDefault="token.show_choices_by_default" v-model="models[modelKey]" />
        </template>
        <template v-else>
          <span>{{ $t('thisIsABug') }} {{ ((t: never) => t)(token) }}</span>
        </template>
      </template>
    </template>
  </p>
</template>

<style scoped>
p {
  font-size: 32px;
  line-height: 3;
  margin: 0px;
}

p.first {
  margin-top: -24px;
}

span.boxed {
  padding: 4px 0;
  outline: 2px solid black;
}

span.passiveItalic {
  font-style: italic;
}

span.passiveBold {
  font-weight: bold;
}
</style>
