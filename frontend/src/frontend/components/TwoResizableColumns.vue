<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import { onMounted, onBeforeUnmount } from 'vue'
import SplitGrid from 'split-grid'


const props = withDefaults(defineProps<{
  leftWidth?: string,
  rightWidth?: string,
}>(), {
  leftWidth: '1fr',
  rightWidth: '1fr',
})

const initialStyle = computed(() => ({
  gridTemplateColumns: `${props.leftWidth} 10px ${props.rightWidth}`,
}))

const style = ref({})

watch(
  initialStyle,
  (value) => {
    style.value = value
  },
  {
    immediate: true,
  },
)

const gutter = ref<HTMLElement | null>(null)
var split = null
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
    <div class="overflow-x-auto"><slot name="left"></slot></div>
    <div class="gutter" ref="gutter"><slot name="gutter"><div class="handle"></div></slot></div>
    <div class="overflow-x-auto"><slot name="right"></slot></div>
  </div>
</template>

<style scoped>
.gutter {
  cursor: col-resize;
}
.gutter .handle {
  height: 100%;
  background-color: black;
  position: relative;
  margin-left: 4px;
  margin-right: 4px;
  width: 2px;
}
</style>
