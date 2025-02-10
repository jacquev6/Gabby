<script lang="ts">
import { InlineBlot } from '$frontend/components/Quill.vue'
import { basicBlots } from '$frontend/components/WysiwygEditor.vue'
import { Choices2Blot } from './MultipleChoicesTools.vue'
import { SelBlot } from './SelectableEffectTools.vue'


class ManualItemBlot extends InlineBlot {
  static override blotName = 'manual-item'
  static override tagName = 'manual-item-blot'
}

export const wysiwygBlots = [
  ...basicBlots,
  SelBlot,
  Choices2Blot,
  ManualItemBlot,
]

export const wysiwygContagiousFormats = ['choices2']

export const wysiwygCompatibleFormats = [['bold', 'italic']]

export interface Settings {
  itemized: {
    items: {
      isLetters: boolean
      isWords: boolean
      isPunctuation: boolean
      isSentences: boolean
      isManual: boolean
      isSeparated: boolean
      separator: string
    }
    effects: {
      isSelectable: boolean
      selectable: {
        colorsCount: number
        allColors: string[]
      }
      isBoxed: boolean
      hasMcqBeside: boolean
      hasMcqBelow: boolean
    }
  }
}
</script>

<script setup lang="ts">
import { computed, reactive, watch } from 'vue'
import MultipleChoicesTools from './MultipleChoicesTools.vue'
import ItemsTools from './ItemsTools.vue'
import SelectableEffectTools, { allColorsForSelectableEffect } from './SelectableEffectTools.vue'
import BoxedEffectTools from './BoxedEffectTools.vue'
import { cleanupModel, type Model } from './ExerciseFieldsForm.vue'
import ExerciseFieldsForm from './ExerciseFieldsForm.vue'
import type { Textbook } from '$frontend/stores/api'
import UndoRedoTool from './UndoRedoTool.vue'
import { BButton, BLabeledCheckbox } from '$frontend/components/opinion/bootstrap'
import DistributionToggles from './DistributionToggles.vue'
import ExerciseToolsColumnSection from './ExerciseToolsColumnSection.vue'
import OptionalInput from '$frontend/components/OptionalInput.vue'
import deepEqual from 'deep-equal'


defineProps<{
  textbook: Textbook
  fields: InstanceType<typeof ExerciseFieldsForm> | null
  resetUndoRedo: number
}>()

const model = defineModel<Model>({required: true})

// Keep the 'style' section below consistent with the length of this array
const defaultColorsForSelectableEffect = [
  allColorsForSelectableEffect[0],
  allColorsForSelectableEffect[3],
  allColorsForSelectableEffect[6],
  allColorsForSelectableEffect[7],
  allColorsForSelectableEffect[10],
]

// Keep settings in memory even when they are not used, so that they are not reset when used again.
const settings = reactive<Settings>({
  itemized: {
    items: {
      isLetters: false,
      isWords: false,
      isPunctuation: false,
      isSentences: false,
      isManual: false,
      isSeparated: false,
      separator: '',
    },
    effects: {
      isSelectable: false,
      selectable: {
        colorsCount: 2,
        allColors: [...defaultColorsForSelectableEffect],
      },
      isBoxed: false,
      hasMcqBeside: false,
      hasMcqBelow: false,
    },
  },
})

const items = computed(() => {
  if (settings.itemized.items.isLetters) {
    return {kind: 'characters' as const, letters: true}
  } else if (settings.itemized.items.isWords || settings.itemized.items.isPunctuation) {
    return {kind: 'tokens' as const, words: settings.itemized.items.isWords, punctuation: settings.itemized.items.isPunctuation}
  } else if (settings.itemized.items.isSentences) {
    return {kind: 'sentences' as const}
  } else if (settings.itemized.items.isManual) {
    return {kind: 'manual' as const}
  } else if (settings.itemized.items.isSeparated && settings.itemized.items.separator !== '') {
    return {kind: 'separated' as const, separator: settings.itemized.items.separator}
  } else {
    return null
  }
})

const hasItems = computed(() => items.value !== null)

const fillWithFreeTextPlaceholder = computed({
  get() {
    if (model.value.adaptation.placeholder_for_fill_with_free_text !== null) {
      return model.value.adaptation.placeholder_for_fill_with_free_text
    } else {
      return ''
    }
  },
  set(value: string) {
    if (value === '') {
      model.value.adaptation.placeholder_for_fill_with_free_text = null
    } else {
      model.value.adaptation.placeholder_for_fill_with_free_text = value
    }
  },
})

watch(
  model,
  model => {
    if (model.adaptation.items === null) {
      settings.itemized.items.isLetters = false
      settings.itemized.items.isWords = false
      settings.itemized.items.isPunctuation = false
      settings.itemized.items.isSentences = false
      settings.itemized.items.isManual = false
      settings.itemized.items.isSeparated = false
      settings.itemized.items.separator = ''
    } else if (model.adaptation.items.kind === 'characters') {
      settings.itemized.items.isLetters = model.adaptation.items.letters
      settings.itemized.items.isWords = false
      settings.itemized.items.isPunctuation = false
      settings.itemized.items.isSentences = false
      settings.itemized.items.isManual = false
      settings.itemized.items.isSeparated = false
      settings.itemized.items.separator = ''
    } else if (model.adaptation.items.kind === 'tokens') {
      settings.itemized.items.isLetters = false
      settings.itemized.items.isWords = model.adaptation.items.words
      settings.itemized.items.isPunctuation = model.adaptation.items.punctuation
      settings.itemized.items.isSentences = false
      settings.itemized.items.isManual = false
      settings.itemized.items.isSeparated = false
      settings.itemized.items.separator = ''
    } else if (model.adaptation.items.kind === 'manual') {
      settings.itemized.items.isLetters = false
      settings.itemized.items.isWords = false
      settings.itemized.items.isPunctuation = false
      settings.itemized.items.isSentences = false
      settings.itemized.items.isManual = true
      settings.itemized.items.isSeparated = false
      settings.itemized.items.separator = ''
    } else if (model.adaptation.items.kind === 'sentences') {
      settings.itemized.items.isLetters = false
      settings.itemized.items.isWords = false
      settings.itemized.items.isPunctuation = false
      settings.itemized.items.isSentences = true
      settings.itemized.items.isManual = false
      settings.itemized.items.isSeparated = false
      settings.itemized.items.separator = ''
    } else if (model.adaptation.items.kind === 'separated') {
      settings.itemized.items.isLetters = false
      settings.itemized.items.isWords = false
      settings.itemized.items.isPunctuation = false
      settings.itemized.items.isSentences = false
      settings.itemized.items.isManual = false
      settings.itemized.items.isSeparated = true
      settings.itemized.items.separator = model.adaptation.items.separator
    } else {
      console.assert(false, ((items: never) => items)(model.adaptation.items))
    }

    if (model.adaptation.items_are_selectable === null) {
      settings.itemized.effects.isSelectable = false
      settings.itemized.effects.selectable.colorsCount = 2
      settings.itemized.effects.selectable.allColors.splice(0, settings.itemized.effects.selectable.allColors.length, ...defaultColorsForSelectableEffect)
    } else {
      settings.itemized.effects.isSelectable = true
      settings.itemized.effects.selectable.colorsCount = model.adaptation.items_are_selectable.colors.length
      settings.itemized.effects.selectable.allColors.splice(
        0,
        model.adaptation.items_are_selectable.colors.length,
        ...model.adaptation.items_are_selectable.colors
      )
    }
    settings.itemized.effects.isBoxed = model.adaptation.items_are_boxed
    settings.itemized.effects.hasMcqBeside = model.adaptation.items_have_mcq_beside
    settings.itemized.effects.hasMcqBelow = model.adaptation.items_have_mcq_below
  },
  {
    deep: true,
    immediate: true,
  },
)

watch(
  settings,
  () => {
    let isBoxed = settings.itemized.effects.isBoxed
    let selectable = (() => {
      if (settings.itemized.effects.isSelectable) {
        return  {
          colors: settings.itemized.effects.selectable.allColors.slice(0, settings.itemized.effects.selectable.colorsCount),
        }
      } else {
        return null
      }
    })()
    let hasMcqBeside = settings.itemized.effects.hasMcqBeside
    let hasMcqBelow = settings.itemized.effects.hasMcqBelow

    const items = (() => {
      if (isBoxed || selectable !== null || hasMcqBeside || hasMcqBelow) {
        if (settings.itemized.items.isLetters) {
          return {kind: 'characters' as const, letters: true}
        } else if (settings.itemized.items.isWords || settings.itemized.items.isPunctuation) {
          return {kind: 'tokens' as const, words: settings.itemized.items.isWords, punctuation: settings.itemized.items.isPunctuation}
        } else if (settings.itemized.items.isSentences) {
          return {kind: 'sentences' as const}
        } else if (settings.itemized.items.isManual) {
          return {kind: 'manual' as const}
        } else if (settings.itemized.items.isSeparated && settings.itemized.items.separator !== '') {
          return {kind: 'separated' as const, separator: settings.itemized.items.separator}
        } else {
          return null
        }
      } else {
        return null
      }
    })()

    if (items === null) {
      isBoxed = false
      selectable = null
      hasMcqBeside = false
      hasMcqBelow = false
    }

    // Break the infinite 'watch' loop by setting the model only if the value has actually changed.
    let hasChanged = false
    if (!deepEqual(items, model.value.adaptation.items)) {
      hasChanged = true
      model.value.adaptation.items = items
    }
    if (!deepEqual(selectable, model.value.adaptation.items_are_selectable)) {
      hasChanged = true
      model.value.adaptation.items_are_selectable = selectable
    }
    if (isBoxed !== model.value.adaptation.items_are_boxed) {
      hasChanged = true
      model.value.adaptation.items_are_boxed = isBoxed
    }
    if (hasMcqBeside !== model.value.adaptation.items_have_mcq_beside) {
      hasChanged = true
      model.value.adaptation.items_have_mcq_beside = hasMcqBeside
    }
    if (hasMcqBelow !== model.value.adaptation.items_have_mcq_below) {
      hasChanged = true
      model.value.adaptation.items_have_mcq_below = hasMcqBelow
    }

    if (hasChanged) {
      cleanupModel(model.value)
    }
  },
  {
    deep: true,
  },
)
</script>

<template>
  <div class="h-100 overflow-hidden d-flex flex-row position-relative" id="gutter-2">
    <div class="handle"></div>
    <div class="h-100 overflow-auto flex-fill" data-cy="gutter-2">
      <div style="position: relative">
        <div>
          <h1>{{ $t('tools') }}</h1>
          <ExerciseToolsColumnSection>
            <UndoRedoTool v-model="model" :reset="resetUndoRedo" />
          </ExerciseToolsColumnSection>
          <ExerciseToolsColumnSection>
            <MultipleChoicesTools v-if="fields !== null" v-model="model" :textbook :fields :settings :hasItems />
          </ExerciseToolsColumnSection>
          <ExerciseToolsColumnSection>
            <OptionalInput v-model="fillWithFreeTextPlaceholder" :label="$t('placeholderForFreeText')" />
          </ExerciseToolsColumnSection>
          <ExerciseToolsColumnSection>
            <ItemsTools v-if="fields !== null" v-model="model" :textbook :settings />
          </ExerciseToolsColumnSection>
          <ExerciseToolsColumnSection>
            <SelectableEffectTools v-if="fields !== null" :settings :disabled="!hasItems" />
          </ExerciseToolsColumnSection>
          <ExerciseToolsColumnSection>
            <template v-if="fields !== null">
              <p>
                <BButton
                  sm secondary
                  :disabled="fields.focusedWysiwygField == null"
                  :class="{active: fields.currentWysiwygFormat.bold}"
                  @click="fields.toggle('bold')"
                  data-cy="format-bold"
                ><img :style="{height: '1.25em'}" src="/bold.svg" /></BButton>
                <BButton
                  sm secondary
                  :disabled="fields.focusedWysiwygField == null"
                  :class="{active: fields.currentWysiwygFormat.italic}"
                  @click="fields.toggle('italic')"
                  data-cy="format-italic"
                ><img :style="{height: '1.25em'}" src="/italic.svg" /></BButton>
              </p>

              <p v-if="model.adaptation.items !== null && model.adaptation.items_are_selectable !== null">
                <template v-for="i in model.adaptation.items_are_selectable.colors.length">
                  <BButton
                    class="format-color"
                    sm secondary
                    :disabled="fields.focusedWysiwygField === null || fields.focusedWysiwygField === 'wording'"
                    :class="{active: fields.currentWysiwygFormat.sel === i}"
                    @click="fields.toggle('sel', i)"
                    :style="{lineHeight: 0, padding: '2px'}"
                    :data-cy="`format-color-${i}`"
                  >
                    <span :style="{backgroundColor: model.adaptation.items_are_selectable.colors[i - 1]}"></span>
                  </BButton>
                  <wbr />
                </template>
              </p>

              <p v-if="settings.itemized.items.isManual">
                <BButton
                  sm secondary
                  :disabled="fields.focusedWysiwygField !== 'wording'"
                  :class="{active: fields.currentWysiwygFormat['manual-item']}"
                  @click="fields.toggle('manual-item')"
                  data-cy="format-manual-item"
                >{{ $t('manualItemButton') }}</BButton>
              </p>
            </template>

            <BLabeledCheckbox v-model="model.adaptation.single_item_per_paragraph" :label="$t('singleItemPerParagraph')" :disabled="!hasItems" />
            <BoxedEffectTools v-if="fields !== null" :settings :disabled="!hasItems" />
          </ExerciseToolsColumnSection>
          <ExerciseToolsColumnSection>
            <div class="mb-3">
              <p class="form-label">{{ $t('exerciseDistribution') }}</p>
              <DistributionToggles v-model="model.adaptation.wording_paragraphs_per_pagelet" />
            </div>
          </ExerciseToolsColumnSection>
        </div>

        <div
          v-if="model.inProgress.kind === 'multipleChoicesCreation'"
          style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.5); cursor: initial;"
          @mousedown="e => e.stopPropagation()" @touchstart="e => e.stopPropagation()"
        >
          <div style="position: absolute; top: 50px; left: 10%; width: 80%; background-color: white; padding: 1em;">
            {{ $t('multipleChoicesInstructions') }}
            <BButton secondary sm @click="model.inProgress = {kind: 'nothing'}">{{ $t('choicesSettingsCancel') }}</BButton>
          </div>
        </div>
      </div>
    </div>
    <div class="handle"></div>
  </div>
</template>

<style scoped>
button.format-color > span {
  display: inline flow-root;
  margin: 0.25em;
  width: 1.25em;
  height: 1.25em;
  cursor: pointer;
}
</style>
