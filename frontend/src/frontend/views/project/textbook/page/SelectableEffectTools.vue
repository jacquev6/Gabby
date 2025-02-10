<script lang="ts">
import { InlineBlot } from '$frontend/components/Quill.vue'

// Colors provided by the client, in display order
export const allColorsForSelectableEffect = [
  '#ffff00',  // yellow
  '#ffcf4c',  // orange
  '#ff8084',  // red
  '#ffc0cb',  // pink
  '#d49cff',  // purple
  '#8177ff',  // dark blue
  '#bbbbff',  // light blue
  '#bbffbb',  // light green
  '#68e495',  // dark green
  '#632f2b',  // brown
  '#bbbbbb',  // grey
  '#000000',  // black
]


export class SelBlot extends InlineBlot {
  static override blotName = 'sel'
  static override tagName = 'sel-blot'

  static override create(s: number) {
    let node = super.create()
    node.setAttribute('data-sel', s.toString())
    return node
  }

  static override formats(node: HTMLElement) {
    const data = node.getAttribute('data-sel')
    console.assert(data !== null)
    return Number.parseInt(data)
  }
}
</script>

<script setup lang="ts">
import { ref } from 'vue'

import { BLabeledCheckbox } from '../../../../components/opinion/bootstrap'
import FloatingColorPicker from '$frontend/components/FloatingColorPicker.vue'
import { type Settings } from './ExerciseToolsColumn.vue'


defineProps<{
  settings: Settings
}>()

const colorPickers = ref<InstanceType<typeof FloatingColorPicker>[]>([])
</script>

<template>
  <FloatingColorPicker
    v-for="i in settings.itemized.effects.selectable.allColors.length"
    ref="colorPickers"
    v-model="settings.itemized.effects.selectable.allColors[i - 1]"
    :colors="allColorsForSelectableEffect"
    backdropCovers1="#left-col-2"
    backdropCovers2="#gutter-2"
  />

  <BLabeledCheckbox :label="$t('effectsSelectable')" v-model="settings.itemized.effects.isSelectable" />
  <span class="maybe-usable-colors-container">
    <span v-for="i in settings.itemized.effects.selectable.allColors.length" :class="settings.itemized.effects.isSelectable && i - 1 < settings.itemized.effects.selectable.colorsCount ? 'usable-colors-container' : 'unusable-colors-container'">
      <span
        class="usable-colors-button"
        :style="{backgroundColor: settings.itemized.effects.selectable.allColors[i - 1]}"
        :data-cy-colors="i"
        @click="settings.itemized.effects.isSelectable = true; settings.itemized.effects.selectable.colorsCount = i"
        @contextmenu.prevent="(event) => colorPickers[i - 1].show(event.target as HTMLElement)"
      ></span>
    </span>
  </span>
</template>

<style scoped>
span.maybe-usable-colors-container {
  display: block flow-root;
  line-height: 0;
}

span.usable-colors-container {
  display: inline flow-root;
  background-color: var(--bs-primary);
}

span.unusable-colors-container {
  display: inline flow-root;
  background-color: var(--bs-secondary);
}

span.usable-colors-button {
  display: inline flow-root;
  margin: 0.25em;
  width: 1.25em;
  height: 1.25em;
  cursor: pointer;
}
</style>
