<script setup lang="ts">
import { computed } from 'vue'

import type { Paragraph } from '$adapted/types'

import FreeTextInput from './FreeTextInput.vue'
import MultipleChoicesInput from './MultipleChoicesInput.vue'
import Renderable from './Renderable.vue'
import SelectableText from './SelectableText.vue'


const props = withDefaults(defineProps<{
  node: Paragraph['contents'][number]
  modelKey: number[]
  inStack?: boolean
}>(), {
  inStack: false,
})

const models = defineModel<Record<string, any/* @todo Type */>>({
  required: true,
})

const modelKey = computed(() => `model-${props.modelKey.join('-')}`)

function downgradePassiveList(contents: (Paragraph['contents'][number] & {kind: 'multipleChoicesInput'})['choices'][number]) {
  console.assert(contents.length === 1)
  console.assert(contents[0].kind === 'text')
  return contents[0].text
}
</script>

<template>
  <template v-if="node.kind === 'whitespace'">
    <span>&nbsp;&nbsp;<wbr /></span>
  </template>
  <template v-else-if="node.kind === 'text'">
    <span
      class="tricolorable"
      :class="{bold: node.bold, italic: node.italic}"
      :style="node.highlighted !== null ? {background: node.highlighted} : {}"
    >
      {{ node.text }}
    </span>
  </template>
  <template v-else-if="node.kind === 'passiveSequence'">
    <span :class="{boxed: node.boxed}">
      <Renderable v-for="(sub, index) in node.contents" :node="sub" v-model="models" :modelKey="[...props.modelKey, index]" />
    </span>
  </template>
  <template v-else-if="node.kind === 'freeTextInput'">
    <FreeTextInput class="tricolorable" v-model="models[modelKey]" />
  </template>
  <template v-else-if="node.kind === 'multipleChoicesInput'">
    <MultipleChoicesInput
      :class="{tricolorable: !inStack}"
      v-model="models[modelKey]"
      :choices="node.choices.map(downgradePassiveList)"
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
      <Renderable v-for="(sub, index) in node.contents" :node="sub" v-model="models" :modelKey="[...props.modelKey, index]" />
    </SelectableText>
  </template>
  <template v-else-if="node.kind === 'sequence'">
    <template v-if="node.vertical">
      <span style="display: inline-block; vertical-align: top;">
        <p v-for="(sub, index) in node.contents"><Renderable :node="sub" v-model="models" :modelKey="[...props.modelKey, index]" :inStack="true" /></p>
      </span>
    </template>
    <template v-else>
      <Renderable v-for="(sub, index) in node.contents" :node="sub" v-model="models" :modelKey="[...props.modelKey, index]" />
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
  padding: 4px 0;
  outline: 2px solid black;
}
</style>
