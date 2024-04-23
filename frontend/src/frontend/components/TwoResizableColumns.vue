<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import { onMounted, onBeforeUnmount } from 'vue'
import SplitGrid, { type SplitInstance } from 'split-grid'


const gutterMargin = 4  // Keep in sync with <style>
const gutterWidth = 2  // Keep in sync with <style>

const props = withDefaults(defineProps<{
  leftWidth?: string,
  gutterWidth?: string,
  rightWidth?: string,
}>(), {
  leftWidth: '1fr',
  gutterWidth: `${gutterMargin + gutterWidth + gutterMargin}px`,
  rightWidth: '1fr',
})

const initialStyle = computed(() => ({
  gridTemplateColumns: `${props.leftWidth} ${props.gutterWidth} ${props.rightWidth}`,
}))

const style = ref(initialStyle.value)

watch(initialStyle, (value) => { style.value = value })

const gutter = ref<HTMLElement | null>(null)
var split : SplitInstance | null = null
onMounted(() => {
  console.assert(gutter.value !== null)
  console.assert(split === null)
  split = SplitGrid({
    columnGutters: [
      {
        track: 1,
        element: gutter.value,
      },
    ],
    columnMinSizes: [100, 0, 100],
    snapOffset: 0,
    writeStyle: (_, __, s) => {style.value.gridTemplateColumns = s},
  });
})

onBeforeUnmount(() => {
  console.assert(gutter.value !== null)
  console.assert(split !== null)
  split.destroy()
  split = null
})
</script>

<template>
  <div class="d-grid" :style>
    <div class="overflow-hidden"><slot name="left"></slot></div>
    <div class="overflow-hidden gutter" ref="gutter"><slot name="gutter"><div class="handle"></div></slot></div>
    <div class="overflow-hidden"><slot name="right"></slot></div>
  </div>
</template>

<style scoped>
.gutter {
  cursor: col-resize;
}
</style>

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
