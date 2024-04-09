<script setup>
import { ref, reactive, watch, nextTick, computed, onMounted, onBeforeUnmount } from 'vue'

import { tokenize } from './tokenize'


const props = defineProps({
  text: {
    type: String,
    required: true,
  }
})

const tokens = computed(() => tokenize(props.text))

const paragraph = ref(null)

const lines = reactive([])

const colors = ['red', 'green', 'blue']

const style = computed(() => {
  return tokens.value.map((_, i) => {
    return {
      color: colors[lines[i] % colors.length],
    }
  })
})

function computeLines() {
  console.assert(paragraph.value !== null)

  lines.splice(0)

  var currentLine = -1
  var previousOffset = null
  for (let index = 0; index < tokens.value.length; index++) {
    const offset = paragraph.value.children[index].offsetLeft
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
