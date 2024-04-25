<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import { onMounted, onBeforeUnmount } from 'vue'
import SplitGrid, { type SplitInstance } from 'split-grid'

import { BButton } from './opinion/bootstrap'


const gutterMargin = 4  // Keep in sync with <style>
const gutterWidth = 2  // Keep in sync with <style>

const props = withDefaults(defineProps<{
  leftWidth?: string,
  gutterWidth?: string,
  rightWidth?: string,
  snap?: false | number,
}>(), {
  leftWidth: '1fr',
  snap: false,
  gutterWidth: `${gutterMargin + gutterWidth + gutterMargin}px`,
  rightWidth: '1fr',
})

const initialGridTemplateColumns = computed(() => `${props.leftWidth} ${props.gutterWidth} ${props.rightWidth}`)

const gridTemplateColumns = ref(initialGridTemplateColumns.value)

watch(initialGridTemplateColumns, (value) => { gridTemplateColumns.value = value })

const gutter = ref<HTMLElement | null>(null)
var split = ref<SplitInstance | null>(null)
const active = computed(() => split.value !== null)

function activate() {
  console.assert(gutter.value !== null)
  console.assert(split.value === null)

  displayLeftButton.value = false
  displayRightButton.value = false
  gridTemplateColumns.value = initialGridTemplateColumns.value

  split.value = SplitGrid({
    columnGutters: [
      {
        track: 1,
        element: gutter.value,
      },
    ],
    minSize: 0,
    snapOffset: props.snap === false ? 0 : props.snap,
    writeStyle,
    onDragEnd,
  });
}

function deactivate() {
  console.assert(gutter.value !== null)
  console.assert(split.value !== null)

  split.value.destroy()
  split.value = null
}

function deactivateIfActive() {
  if (active.value) {
    deactivate()
  }
}

onMounted(activate)
onBeforeUnmount(deactivateIfActive)

const gutterStyle = computed(() => active.value ? {cursor: 'col-resize'} : {})

const displayLeftButton = ref(false)
const displayRightButton = ref(false)

function writeStyle(_: unknown, __: unknown, s: string) {
  // console.log('style:', s)
  displayLeftButton.value = false
  displayRightButton.value = false
  if (props.snap !== false) {
    const parts = s.split(' ')
    console.assert(parts.length === 3)
    console.assert(parts[0].endsWith('fr'))
    console.assert(parts[2].endsWith('fr'))
    const leftWidth = Math.abs(Number.parseFloat(parts[0].slice(0, -2)))
    const rightWidth = Math.abs(Number.parseFloat(parts[2].slice(0, -2)))
    // console.log(parts[0].slice(0, -2), parts[2].slice(0, -2), leftWidth, rightWidth)

    if (leftWidth <= 1e-6) {
      // console.log('snap left')
      displayLeftButton.value = true
      s = `20px ${props.gutterWidth} 1fr`
    } else if (rightWidth <= 1e-6) {
      // console.log('snap right')
      displayRightButton.value = true
      s = `1fr ${props.gutterWidth} 20px`
    }
  }
  gridTemplateColumns.value = s
}

function onDragEnd() {
  if (displayLeftButton.value || displayRightButton.value) {
    deactivate()
  }
}
</script>

<template>
  <div class="d-grid" :style="{gridTemplateColumns}">
    <div class="overflow-hidden">
      <div v-if="displayLeftButton">
        <BButton secondary @click="activate">&gt;<br/>&gt;</BButton>
      </div>
      <div class="h-100 overflow-hidden" :class="{'d-none': displayLeftButton}"><slot name="left"></slot></div>
    </div>
    <div class="overflow-hidden gutter" :style="gutterStyle" ref="gutter"><slot name="gutter"><div class="handle"></div></slot></div>
    <div class="overflow-hidden">
      <div v-if="displayRightButton">
        <BButton secondary @click="activate">&lt;<br/>&lt;</BButton>
      </div>
      <div class="h-100 overflow-hidden" :class="{'d-none': displayRightButton}"><slot name="right"></slot></div>
    </div>
  </div>
</template>

<style>
.gutter .handle {
  height: 100%;
  background-color: black;
  position: relative;
  margin-left: 4px;  /* Keep equal to gutterMargin*/
  margin-right: 4px;  /* Keep equal to gutterMargin*/
  min-width: 2px;  /* Keep equal to gutterWidth*/
}
</style>
