<script setup lang="ts">
import { useFloating, arrow, shift } from '@floating-ui/vue'
import { computed, ref, watch } from 'vue'
import { useElementBounding } from '@vueuse/core'

import closeWithKeyboard from './closeWithKeyboard'


const props = defineProps<{
  backdropCovers1: string
  backdropCovers2: string
}>()

const emit = defineEmits<{
  shown: []
  hidden: []
}>()

const inDom = ref(false)
const floatingReference = ref<HTMLElement | null>(null)
const floatingContainer = ref<HTMLElement | null>(null)
const floatingArrow = ref<HTMLElement | null>(null)
const floatingContent = ref<HTMLElement | null>(null)

let cancelClosingOnEscape: (() => void) | null = null

function show(ref: HTMLElement) {
  inDom.value = true
  floatingReference.value = ref
  console.assert(cancelClosingOnEscape === null)
  cancelClosingOnEscape = closeWithKeyboard(hide, {withEscape: true, withEnter: true})
}

function hide() {
  inDom.value = false
  console.assert(cancelClosingOnEscape !== null)
  cancelClosingOnEscape()
  cancelClosingOnEscape = null
}

watch(floatingContent, floatingContent => {
  if (floatingContent === null) {
    emit('hidden')
  } else {
    // This hard-coded duration is fragile, but Vue's nextTick is not enough. Not sure why.
    setTimeout(
      () => {
        if (document.activeElement instanceof HTMLElement) {
          document.activeElement.blur()
        }
      },
      100,
    )
    emit('shown')
  }
})

const {floatingStyles, middlewareData} = useFloating(
  floatingReference,
  floatingContainer,
  {
    middleware: [
      shift(),
      arrow({element: floatingArrow}),
    ],
    placement: 'bottom',
  },
)

const floatingArrowStyles = computed(() => {
  const arrow = middlewareData.value.arrow
  if (arrow === undefined) {
    return {}
  } else {
    console.assert(arrow.x !== undefined)
    return {
      left: `${arrow.x}px`,
    }
  }
})


const backdropCovers1 = computed(() => {
  const element = document.querySelector(props.backdropCovers1)
  console.assert(element !== null)
  return element as HTMLElement
})

const backdropCoversBoundingRect1 = useElementBounding(backdropCovers1)

const backdropCovers2 = computed(() => {
  const element = document.querySelector(props.backdropCovers2)
  console.assert(element !== null)
  return element as HTMLElement
})

const backdropCoversBoundingRect2 = useElementBounding(backdropCovers2)

const backdropStyles = computed(() => {
  const boundingRects = [backdropCoversBoundingRect1, backdropCoversBoundingRect2]
  boundingRects.forEach(rect => rect.update())

  const top = Math.min(...boundingRects.map(rect => rect.top.value))
  const bottom = Math.max(...boundingRects.map(rect => rect.bottom.value))
  const left = Math.min(...boundingRects.map(rect => rect.left.value))
  const right = Math.max(...boundingRects.map(rect => rect.right.value))

  const styles = {
    top: `${top}px`,
    bottom: `${window.innerHeight - bottom}px`,
    left: `${left}px`,
    right: `${window.innerWidth - right}px`,
  }

  return styles
})

defineExpose({show, hide})
</script>

<template>
  <Teleport to="body">
    <template v-if="inDom">
      <div
        class="floating-backdrop"
        :style="backdropStyles"
        @click="hide" @contextmenu.prevent="hide"
      ></div>
      <div
        ref="floatingContainer"
        class="floating-container"
        :style="floatingStyles"
      >
        <div
          ref="floatingArrow"
          class="floating-arrow"
          :style="floatingArrowStyles"
        ></div>
        <div
          ref="floatingContent"
          class="floating-content"
        >
          <slot></slot>
        </div>
      </div>
    </template>
  </Teleport>
</template>

<style scoped>
span.default-color {
  display: inline flow-root;
  width: 1.25em;
  height: 1.25em;
}

div.floating-backdrop {
  position: fixed;
  z-index: 10;
  background: #00000022;
}

div.floating-container {
  z-index: 11;
}

div.floating-content {
  border: 2px solid #777;
  background: white;
  position: relative;
  top: 10px;
  padding: 2px;
}

div.floating-arrow {
  position: absolute;
  /* CSS Triangle trick: https://css-tricks.com/snippets/css/css-triangle/ */
  width: 0;
  height: 0;
  border-left: 0.75em solid transparent;
  border-right: 0.75em solid transparent;
  border-bottom: 0.75em solid #777;
}
</style>
