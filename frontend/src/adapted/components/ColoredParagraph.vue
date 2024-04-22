<script setup lang="ts">
import { ref, reactive, watch, nextTick, computed, onMounted, onBeforeUnmount } from 'vue'

import { tokenize } from './tokenize'


const assert: (condition: any, message?: string) => asserts condition = console.assert

const props = defineProps<{
  text: string,
}>()

const tokens = computed(() => tokenize(props.text))

const paragraph = ref<HTMLElement | null>(null)

const lines = reactive<number[]>([])

const colors = ['red', 'green', 'blue']

const style = computed(() => {
  return tokens.value.map((_, i) => {
    return {
      color: colors[lines[i] % colors.length],
    }
  })
})

function computeLines() {
  assert(paragraph.value !== null)

  lines.splice(0)

  var currentLine = -1
  var previousOffset = null
  for (let index = 0; index < tokens.value.length; index++) {
    const offset = (paragraph.value.children[index] as HTMLElement).offsetLeft
    if (previousOffset === null || offset < previousOffset) {
      currentLine++
    }
    lines.push(currentLine)
    previousOffset = offset
  }
}

watch(tokens, () => nextTick(computeLines))

onMounted(() => {
  window.addEventListener('resize', computeLines)
  computeLines()
})

onBeforeUnmount(() => {
  window.removeEventListener('resize', computeLines)
})
</script>

<!-- The two <wbr /> element work around Vue.js removing spaces despite 'whitespace: 'preserve' in its configuration -->
<template>
  <p ref="paragraph">
    <template v-for="(token, index) in tokens">
      <span :style="style[index]">
        <template v-if="token.kind === 'whitespace'">
          <wbr /> <wbr />
        </template>
        <template v-else>
          <slot :token :index>{{ token.text }}</slot>
        </template>
      </span>
    </template>
  </p>
</template>
