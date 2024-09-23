<script lang="ts">
function sum(a: number[]) {
  return a.reduce((a, b) => a + b, 0)
}

function gridTemplateToPixels(totalWidth: number, gridTemplate: string) {
  const parts = gridTemplate.split(' ')

  let pxSum = 0
  let frSum = 0
  for (const part of parts) {
    if (part.endsWith('px')) {
      pxSum += Number.parseFloat(part.slice(0, -2))
    } else {
      console.assert(part.endsWith('fr'))
      frSum += Number.parseFloat(part.slice(0, -2))
    }
  }

  const frWidth = (totalWidth - pxSum) / frSum

  return parts.map(part => {
    if (part.endsWith('px')) {
      return Number.parseFloat(part.slice(0, -2))
    } else {
      console.assert(part.endsWith('fr'))
      return frWidth * Number.parseFloat(part.slice(0, -2))
    }
  })
}
</script>

<script setup lang="ts">
import { computed, reactive, ref, watch } from 'vue'
import { useSlots } from 'vue'
import SplitGrid, { type SplitInstance } from 'split-grid'


const gutterMargin = 4  // Keep in sync with <style>
const handleWidth = 2  // Keep in sync with <style>
const uncollapseButtonWidth = 20

const props = withDefaults(defineProps<{
  widths?: Record<string, string>
  collapsed?: Record<string, boolean>
}>(), {
  // @ts-ignore/* @todo Understand and fix typing issue */
  widths: {},
  // @ts-ignore/* @todo Understand and fix typing issue */
  collapsed: {},
})

type Slot = {
  index: number
  name: string
  uncollapsedWidth: string
  collapsed: boolean
}

const slots: Slot[] = reactive(Object.keys(useSlots()).map((name, index) => {
  const uncollapsedWidth = props.widths[name] ?? '1fr'
  console.assert(uncollapsedWidth.endsWith('fr'))
  const collapsed = props.collapsed[name]

  return {
    index,
    name,
    uncollapsedWidth,
    collapsed,
  }
}))

type FalseGutter = {
  collapsedSlots: Slot[]
  width(): string
  style(): Record<string, string>
}

function makeLeftFalseGutter(collapsedSlotsCount: number) {
  const collapsedSlots = []
  for (let index = 0; index !== collapsedSlotsCount; index++) {
    collapsedSlots.push(slots[index])
  }

  return {
    collapsedSlots,
    _widths() {
      const ws = []
      for (const _slot of this.collapsedSlots) {
        ws.push(uncollapseButtonWidth + gutterMargin)
        ws.push(handleWidth + gutterMargin)
      }
      ws[ws.length - 1] += gutterMargin
      return ws
    },
    width() {
      return `${sum(this._widths())}px`
    },
    style() {
      return {
        gridTemplateColumns: this._widths().map(w => `${w}px`).join(' '),
      }
    },
  }
}

function makeRightFalseGutter(collapsedSlotsCount: number) {
  const collapsedSlots = []
  for (let i = 0; i !== collapsedSlotsCount; i++) {
    const index = slots.length - collapsedSlotsCount + i
    collapsedSlots.push(slots[index])
  }

  return {
    collapsedSlots,
    _widths() {
      const ws = []
      for (const _slot of this.collapsedSlots) {
        ws.push(handleWidth + gutterMargin)
        ws.push(uncollapseButtonWidth + gutterMargin)
      }
      ws[ws.length - 1] += gutterMargin
      return ws
    },
    width() {
      return `${sum(this._widths())}px`
    },
    style() {
      return {
        gridTemplateColumns: this._widths().map(w => `${w}px`).join(' '),
      }
    },
  }
}

type ActiveColumn = {
  kind: 'gutter',
  collapsedSlots: Slot[]
  width(): string
  style(): Record<string, string>
} | {
  kind: 'slot'
  slot: Slot
  width(): string
}

function makeGutterActiveColumn() {
  return {
    kind: 'gutter' as const,
    isFirst: false,
    isLast: false,
    collapsedSlots: [],
    _widths() {
      if (this.collapsedSlots.length === 0) {
        return [handleWidth + 2 * gutterMargin]
      } else {
        const ws = []
        for (const _slot of this.collapsedSlots) {
          ws.push(handleWidth + gutterMargin)
          ws.push(uncollapseButtonWidth + gutterMargin)
        }
        ws.push(handleWidth + 2 * gutterMargin)
        return ws
      }
    },
    width() {
      return `${sum(this._widths())}px`
    },
    style() {
      return {
        gridTemplateColumns: this._widths().map(w => `${w}px`).join(' '),
      }
    },
  }
}

function makeSlotActiveColumn(slot: Slot) {
  return {
    kind: 'slot' as const,
    slot,
    width() {
      return slot.uncollapsedWidth
    },
  }
}

const layout = computed(() => {
  const layout = {
    leftFalseGutter: null as FalseGutter | null,
    activeColumns: [] as ActiveColumn[],
    rightFalseGutter: null as FalseGutter | null,
  }

  let collapsedOnTheLeft = 0
  while (slots[collapsedOnTheLeft].collapsed) {
    ++collapsedOnTheLeft
  }
  if (collapsedOnTheLeft > 0) {
    layout.leftFalseGutter = makeLeftFalseGutter(collapsedOnTheLeft)
  }

  let collapsedOnTheRight = 0
  while (slots[slots.length - collapsedOnTheRight - 1].collapsed) {
    ++collapsedOnTheRight
  }
  if (collapsedOnTheRight > 0) {
    layout.rightFalseGutter = makeRightFalseGutter(collapsedOnTheRight)
  }

  for (let i = collapsedOnTheLeft; i < slots.length - collapsedOnTheRight; i++) {
    const slot = slots[i]
    if (slot.collapsed) {
      if (layout.activeColumns.length === 0 || layout.activeColumns[layout.activeColumns.length - 1].kind !== 'gutter') {
        layout.activeColumns.push(makeGutterActiveColumn())
      }
      const previousColumn = layout.activeColumns[layout.activeColumns.length - 1]
      console.assert(previousColumn.kind === 'gutter')
      previousColumn.collapsedSlots.push(slot)
    } else {
      if (layout.activeColumns.length > 0 && layout.activeColumns[layout.activeColumns.length - 1].kind !== 'gutter') {
        layout.activeColumns.push(makeGutterActiveColumn())
      }
      layout.activeColumns.push(makeSlotActiveColumn(slot))
    }
  }

  return layout
})

const rootStyle = computed(() => {
  const ws = []
  if (layout.value.leftFalseGutter !== null) {
    ws.push(layout.value.leftFalseGutter.width())
  }
  ws.push('1fr')
  if (layout.value.rightFalseGutter !== null) {
    ws.push(layout.value.rightFalseGutter.width())
  }

  return {
    gridTemplateColumns: ws.join(' '),
  }
})

const forcedSplitStyle = ref<string | null>(null)
const splitStyle = computed(() => {
  if (forcedSplitStyle.value !== null) {
    return {
      gridTemplateColumns: forcedSplitStyle.value
    }
  } else {
    return {
      gridTemplateColumns: layout.value.activeColumns.map(c => c.width()).join(' '),
    }
  }
})

const splitElement = ref<HTMLDivElement | null>(null)
const activeGutterElements = ref<HTMLDivElement[]>([])
var split = ref<SplitInstance | null>(null)
const collapsingSlot = ref<Slot | null>(null)

watch(
  activeGutterElements,
  (gutters) => {
    const columnGutters = gutters.map((element, index) => {
      return {
        track: 2 * index + 1,
        element,
      }
    })

    // console.log('Making SplitGrid with', columnGutters)
    if (split.value !== null) {
      split.value.destroy()
    }
    const snapOffset = 50
    console.assert(snapOffset > gutterMargin)
    const columnMinSizes = {} as Record<number, number>
    if (layout.value.leftFalseGutter === null) {
      columnMinSizes[0] = uncollapseButtonWidth + gutterMargin
    }
    if (layout.value.rightFalseGutter === null) {
      columnMinSizes[gutters.length * 2] = uncollapseButtonWidth + gutterMargin
    }
    split.value = SplitGrid({
      columnGutters,
      minSize: uncollapseButtonWidth,
      columnMinSizes,
      snapOffset,
      onDragStart() {
        console.assert(collapsingSlot.value === null)
        console.assert(forcedSplitStyle.value === null)
      },
      onDrag(_direction, track, gridTemplateStyle) {
        console.assert(splitElement.value !== null)
        const sizesInPixels = gridTemplateToPixels(splitElement.value.clientWidth, gridTemplateStyle)
        console.assert(sizesInPixels.length === layout.value.activeColumns.length)
        collapsingSlot.value = null
        forcedSplitStyle.value = gridTemplateStyle
        for (const columnIndex of [track - 1, track + 1]) {
          if (sizesInPixels[columnIndex] < uncollapseButtonWidth + snapOffset) {
            const column = layout.value.activeColumns[columnIndex]
            console.assert(column.kind === 'slot')
            collapsingSlot.value = column.slot
          }
        }
      },
      onDragEnd() {
        console.assert(forcedSplitStyle.value !== null)
        console.assert(splitElement.value !== null)

        const parts = forcedSplitStyle.value.split(' ')
        const columns = [...layout.value.activeColumns]
        console.assert(parts.length === columns.length)
        for (let index = 0; index < parts.length; index += 2) {
          const column = columns[index]
          console.assert(column.kind === 'slot')
          if (column.slot === collapsingSlot.value) {
            column.slot.collapsed = true
          } else {
            column.slot.uncollapsedWidth = parts[index]
          }
        }

        collapsingSlot.value = null
        forcedSplitStyle.value = null
      },
    });
  },
  { deep: true },
)

function uncollapse(slot: Slot) {
  slot.collapsed = false
  // @todo Take width from previous and next visible slots only if possible, instead of all visible slots. If they are too small, take from all visible slots.
}
</script>

<template>
  <div class="root" :style="rootStyle">
    <div v-if="layout.leftFalseGutter !== null" class="false-gutter" :style="layout.leftFalseGutter.style()">
      <template v-for="slot in layout.leftFalseGutter.collapsedSlots">
        <div class="uncollapse" @click="uncollapse(slot)"></div>
        <div class="handle"></div>
      </template>
    </div>
    <div ref="splitElement" class="split" :style="splitStyle">
      <template v-for="column in layout.activeColumns">
        <template v-if="column.kind === 'slot'">
          <template  v-if="column.slot === collapsingSlot">
            <div class="column" :class="column.slot.index === 0 ? 'firstCollapsingColumn' : column.slot.index === slots.length - 1 ? 'lastCollapsingColumn' : 'middleCollapsingColumn'">
              <div class="uncollapse"></div>
            </div>
          </template>
          <template v-else>
            <div class="column">
              <slot :name="column.slot.name"></slot>
            </div>
          </template>
        </template>
        <template v-else-if="column.kind === 'gutter'">
          <div ref="activeGutterElements" class="gutter" :style="column.style()">
            <div class="handle"></div>
            <template v-for="slot in column.collapsedSlots">
              <div
                class="uncollapse"
                @mousedown="e => e.stopPropagation()"
                @touchstart="e => e.stopPropagation()"
                @click="uncollapse(slot)"
              ></div>
              <div class="handle"></div>
            </template>
          </div>
        </template>
      </template>
    </div>
    <div v-if="layout.rightFalseGutter !== null" class="false-gutter" :style="layout.rightFalseGutter.style()">
      <template v-for="slot in layout.rightFalseGutter.collapsedSlots">
        <div class="handle"></div>
        <div class="uncollapse" @click="uncollapse(slot)"></div>
      </template>
    </div>
  </div>
</template>

<style scoped>
.root {
  display: grid;
}

.split {
  display: grid;
}

.column {
  overflow: hidden;
  background-color: green;
}

.gutter {
  cursor: col-resize;
  display: grid;
  background-color: yellow;
}

.false-gutter {
  display: grid;
  background-color: orange;
}

.handle {
  height: 100%;
  background-color: black;
  position: relative;
  margin-left: 4px;  /* Keep equal to gutterMargin */
  margin-right: 4px;  /* Keep equal to gutterMargin */
  min-width: 2px;  /* Keep equal to handleWidth */
}

/* @todo Use actual buttons */
div.uncollapse {
  height: 100%;
  background-color: blue;
  position: relative;
  margin-left: 4px;  /* Keep equal to gutterMargin */
  margin-right: 4px;  /* Keep equal to gutterMargin */
  min-width: 20px;  /* Keep equal to uncollapseButtonWidth */
  cursor: pointer;
}

.firstCollapsingColumn div.uncollapse {
  margin-right: 0;
}

.middleCollapsingColumn div.uncollapse {
  margin: 0;
}

.lastCollapsingColumn div.uncollapse {
  margin-left: 0;
}
</style>
