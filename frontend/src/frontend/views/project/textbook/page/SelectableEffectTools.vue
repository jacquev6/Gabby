<script lang="ts">
import { InlineBlot } from '$frontend/components/Quill.vue'
import { allColorsForSelectableEffect, cleanupModel } from './ExerciseFieldsForm.vue'


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
import { ref, watch } from 'vue'

import { BLabeledCheckbox } from '../../../../components/opinion/bootstrap'
import FloatingColorPicker from '$frontend/components/FloatingColorPicker.vue'
import type { Model } from './ExerciseFieldsForm.vue'


defineProps<{
  disabled: boolean
}>()

const model = defineModel<Model>({required: true})

const colorPickers = ref<InstanceType<typeof FloatingColorPicker>[]>([])

watch(
  [
    () => model.value.adaptationSettings.itemized.effects.isSelectable,
    () => model.value.adaptationSettings.itemized.effects.selectable.colorsCount,
  ],
  () => {
    cleanupModel(model.value)
  },
)
</script>

<template>
  <FloatingColorPicker
    v-for="i in model.adaptationSettings.itemized.effects.selectable.allColors.length"
    ref="colorPickers"
    v-model="model.adaptationSettings.itemized.effects.selectable.allColors[i - 1]"
    :colors="allColorsForSelectableEffect"
    backdropCovers1="#left-col-2"
    backdropCovers2="#gutter-2"
  />

  <BLabeledCheckbox :label="$t('effectsSelectable')" v-model="model.adaptationSettings.itemized.effects.isSelectable" :disabled />
  <span class="maybe-usable-colors-container">
    <span v-for="i in model.adaptationSettings.itemized.effects.selectable.allColors.length" :class="model.adaptationSettings.itemized.effects.isSelectable && i - 1 < model.adaptationSettings.itemized.effects.selectable.colorsCount ? 'usable-colors-container' : 'unusable-colors-container'">
      <span
        class="usable-colors-button"
        :style="{backgroundColor: model.adaptationSettings.itemized.effects.selectable.allColors[i - 1], cursor: disabled ? 'default' : 'pointer'}"
        :data-cy-colors="i"
        @click="model.adaptationSettings.itemized.effects.isSelectable = true; model.adaptationSettings.itemized.effects.selectable.colorsCount = i"
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
}
</style>
