<script setup lang="ts">
import { useFloating, arrow, shift } from '@floating-ui/vue'
import { computed, ref, watch } from 'vue'


const emit = defineEmits<{
  shown: []
  hidden: []
}>()

const inDom = ref(false)
const floatingReference = ref<HTMLElement | null>(null)
const floatingContainer = ref<HTMLElement | null>(null)
const floatingArrow = ref<HTMLElement | null>(null)
const floatingContent = ref<HTMLElement | null>(null)

function show(ref: HTMLElement) {
  inDom.value = true
  floatingReference.value = ref
}

function hide() {
  inDom.value = false
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

defineExpose({show, hide})
</script>

<template>
  <Teleport to="body">
    <template v-if="inDom">
      <div
        class="floating-backdrop"
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
  z-index: 1000;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: #00000022;
}

div.floating-container {
  z-index: 1001;
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
