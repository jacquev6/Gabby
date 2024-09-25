<script setup lang="ts">
import { computed, reactive, ref, watch } from 'vue'

import { BLabeledCheckbox, BRadio } from './opinion/bootstrap'
import type { Model } from './ExerciseFieldsForm.vue'
import { defaultColors as defaultColorsForSelectableEffect } from './AdaptationDetailsFieldsForm.vue'
import FloatingColorPicker from './FloatingColorPicker.vue'


const model = defineModel<Model>({required: true})

const colorPickers = ref<InstanceType<typeof FloatingColorPicker>[]>([])

// Keep settings in memory even when "selectable" is unchecked, so that re-checking it doesn't reset the settings.
const selectableEffectSettings = reactive({
  colors: [defaultColorsForSelectableEffect[0]],
})
watch(
  model,
  () => {
    if (model.value.itemsAndEffectsAttempt1AdaptationOptions.effects.selectable !== null) {
      Object.assign(selectableEffectSettings, model.value.itemsAndEffectsAttempt1AdaptationOptions.effects.selectable)
    }
  },
  {immediate: true},
)

const hasSelectableEffect = computed({
  get() {
    return model.value.itemsAndEffectsAttempt1AdaptationOptions.effects.selectable !== null
  },
  set(value) {
    if (value) {
      model.value.itemsAndEffectsAttempt1AdaptationOptions.effects.selectable = selectableEffectSettings
    } else {
      model.value.itemsAndEffectsAttempt1AdaptationOptions.effects.selectable = null
    }
  },
})

const allColorsForSelectableEffect = reactive([...defaultColorsForSelectableEffect])
const colorsProxyForSelectableEffect = allColorsForSelectableEffect.map((_color, i) => computed({
  get() {
    if (i < selectableEffectSettings.colors.length) {
      return selectableEffectSettings.colors[i]
    } else {
      return allColorsForSelectableEffect[i]
    }
  },
  set(value) {
    allColorsForSelectableEffect[i] = value
    if (model.value.itemsAndEffectsAttempt1AdaptationOptions.effects.selectable !== null && i < model.value.itemsAndEffectsAttempt1AdaptationOptions.effects.selectable.colors.length) {
      model.value.itemsAndEffectsAttempt1AdaptationOptions.effects.selectable.colors[i] = value
    }
  },
}))

const colorsCountForSelectableEffect = computed({
  get() {
    return selectableEffectSettings.colors.length
  },
  set(value) {
    hasSelectableEffect.value = true
    const prev = selectableEffectSettings.colors.length
    if (value > prev) {
      for (let k = prev; k !== value; ++k) {
        selectableEffectSettings.colors.push(allColorsForSelectableEffect[k])
      }
    } else {
      selectableEffectSettings.colors.length = value
    }
  },
})

const wordsItemsSettings = reactive({
  kind: 'words' as const,
  punctuation: false,
})
watch(
  model,
  () => {
    if (model.value.itemsAndEffectsAttempt1AdaptationOptions.items.kind === 'words') {
      Object.assign(wordsItemsSettings, model.value.itemsAndEffectsAttempt1AdaptationOptions.items)
      model.value.itemsAndEffectsAttempt1AdaptationOptions.items = wordsItemsSettings
    }
  },
  {immediate: true},
)

const itemsKind = computed({
  get() {
    return model.value.itemsAndEffectsAttempt1AdaptationOptions.items.kind
  },
  set(kind) {
    switch (kind) {
      case 'words':
        model.value.itemsAndEffectsAttempt1AdaptationOptions.items = {kind, punctuation: false}
        break
      case 'sentences':
        model.value.itemsAndEffectsAttempt1AdaptationOptions.items = {kind}
        break
      case 'manual':
        model.value.itemsAndEffectsAttempt1AdaptationOptions.items = {kind}
        break
    }
  },
})
</script>

<template>
  <FloatingColorPicker
    v-for="i in colorsProxyForSelectableEffect.length"
    ref="colorPickers"
    v-model="colorsProxyForSelectableEffect[i - 1].value"
    :default="defaultColorsForSelectableEffect[i - 1]"
  />

  <div class="mb-3">
    <p class="form-label">{{ $t('items') }}</p>
    <BRadio v-model="itemsKind" :label="$t('itemsWords')" value="words" />
    <BLabeledCheckbox :label="$t('itemsPunctuation')" v-model="wordsItemsSettings.punctuation" :disabled="itemsKind !== 'words'" />
    <BRadio v-model="itemsKind" :label="$t('itemsSentences')" value="sentences" disabled />
    <BRadio v-model="itemsKind" :label="$t('itemsManual')" value="manual" disabled />
  </div>
  <p>{{ $t('effects') }}</p>
  <BLabeledCheckbox :label="$t('effectsSelectable')" v-model="hasSelectableEffect" />
  <span class="maybe-usable-colors-container">
    <span v-for="i in colorsProxyForSelectableEffect.length" :class="i - 1 < colorsCountForSelectableEffect ? 'usable-colors-container' : 'unusable-colors-container'">
      <span
        class="usable-colors-button"
        :style="{backgroundColor: colorsProxyForSelectableEffect[i - 1].value}"
        :data-cy-colors="i"
        @click="colorsCountForSelectableEffect = i"
        @contextmenu.prevent="(event) => colorPickers[i - 1].show(event.target as HTMLElement)"
      ></span>
    </span>
  </span>
  <BLabeledCheckbox :label="$t('effectsBoxed')" v-model="model.itemsAndEffectsAttempt1AdaptationOptions.effects.boxed" />
  <!-- <p>{{ model.itemsAndEffectsAttempt1AdaptationOptions }}</p> -->
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
