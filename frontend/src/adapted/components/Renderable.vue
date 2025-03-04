<script setup lang="ts">
import { computed } from 'vue'

import type { Paragraph } from '$adapted/types'

import FreeTextInput from './FreeTextInput.vue'
import MultipleChoicesInput from './MultipleChoicesInput.vue'
import Renderable from './Renderable.vue'
import SelectableText from './SelectableText.vue'


const props = defineProps<{
  node: Paragraph['contents'][number]
  modelKey: number[]
  nested: boolean
}>()

const models = defineModel<Record<string, any/* @todo Type */>>({
  required: true,
})

const modelKey = computed(() => `model-${props.modelKey.join('-')}`)

const tricolorable = computed(() => !props.nested)
</script>

<template>
  <template v-if="node.kind === 'whitespace'">
    <span
      :class="{bold: node.bold, italic: node.italic, highlighted: !!node.highlighted}"
      :style="!!node.highlighted ? {background: node.highlighted} : {}"
    >&nbsp;&nbsp;<wbr /></span>
  </template>
  <template v-else-if="node.kind === 'text'">
    <span
      :class="{bold: node.bold, italic: node.italic, highlighted: !!node.highlighted, tricolorable}"
      :style="!!node.highlighted ? {background: node.highlighted} : {}"
    >
      {{ node.text }}
    </span>
  </template>
  <template v-else-if="node.kind === 'passiveSequence'">
    <span :class="{boxed: node.boxed}">
      <Renderable v-for="(sub, index) in node.contents" :node="sub" v-model="models" :modelKey="[...props.modelKey, index]" :nested />
    </span>
  </template>
  <template v-else-if="node.kind === 'freeTextInput'">
    <FreeTextInput :class="{tricolorable}" v-model="models[modelKey]" />
  </template>
  <template v-else-if="node.kind === 'multipleChoicesInput'">
    <MultipleChoicesInput
      :class="{tricolorable}"
      v-model="models[modelKey]"
      :choices="node.choices"
      placeholder="...."
      :showArrowBefore="!!node.show_arrow_before"
      :showChoicesByDefault="!!node.show_choices_by_default"
    />
  </template>
  <template v-else-if="node.kind === 'selectableInput'">
    <SelectableText
      v-model="models[modelKey]"
      :boxed="!!node.boxed"
      :colors="node.colors"
    >
      <Renderable v-for="(sub, index) in node.contents" :node="sub" v-model="models" :modelKey="[...props.modelKey, index]" :nested />
    </SelectableText>
  </template>
  <template v-else-if="node.kind === 'sequence'">
    <template v-if="node.vertical">
      <span style="display: inline-block; vertical-align: top;">
        <p v-for="(sub, index) in node.contents"><Renderable :node="sub" v-model="models" :modelKey="[...props.modelKey, index]" :nested /></p>
      </span>
    </template>
    <template v-else>
      <Renderable v-for="(sub, index) in node.contents" :node="sub" v-model="models" :modelKey="[...props.modelKey, index]" :nested />
    </template>
  </template>
  <template v-else>
    <span>{{ $t('thisIsABug') }} {{ ((content: never) => content)(node) }}</span>
  </template>
</template>

<style scoped>
p {
  font-size: 32px;
  line-height: 3;
  margin: 0px;
}

span.italic {
  font-style: italic;
}

span.bold {
  font-weight: bold;
}

span.boxed {
  padding: 4px;
  border: 2px solid black;
}

span.highlighted {
  padding-top: 4px;
  padding-bottom: 4px;
}

span.highlighted:last-child, span.highlighted:has(+ :not(.highlighted)) {
  padding-right: 4px;
}

span.highlighted:first-child, :not(span.highlighted) + span.highlighted {
  padding-left: 4px;
}
</style>
