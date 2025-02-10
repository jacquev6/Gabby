<script setup lang="ts">
import { ref } from 'vue'

import { BLabeledCheckbox } from '../../../../components/opinion/bootstrap'
import FloatingColorPicker from '$frontend/components/FloatingColorPicker.vue'
import { allColorsForSelectableEffect, type Settings } from './MultipleChoicesTools.vue'


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

  <p>{{ $t('effects') }}</p>
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
