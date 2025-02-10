<script setup lang="ts">
import { computed, ref } from 'vue'
import AdaptationDetailsFieldsForm1 from './MultipleChoicesTools.vue'
import AdaptationDetailsFieldsForm2 from './ItemsAndEffectsTools.vue'
import { type Model } from './ExerciseFieldsForm.vue'
import ExerciseFieldsForm from './ExerciseFieldsForm.vue'
import type { Textbook } from '$frontend/stores/api'
import UndoRedoTool from './UndoRedoTool.vue'
import { BButton, BLabeledCheckbox } from '$frontend/components/opinion/bootstrap'
import DistributionToggles from './DistributionToggles.vue'
import ExerciseToolsColumnSection from './ExerciseToolsColumnSection.vue'
import OptionalInput from '$frontend/components/OptionalInput.vue'


defineProps<{
  textbook: Textbook
  fields: InstanceType<typeof ExerciseFieldsForm> | null
  resetUndoRedo: number
}>()

const model = defineModel<Model>({required: true})

const adaptationDetails = ref<InstanceType<typeof AdaptationDetailsFieldsForm1> | null>(null)

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
            <AdaptationDetailsFieldsForm1 ref="adaptationDetails" v-if="fields !== null" v-model="model" :textbook :fields />
          </ExerciseToolsColumnSection>
          <ExerciseToolsColumnSection>
            <OptionalInput v-model="fillWithFreeTextPlaceholder" :label="$t('placeholderForFreeText')" />
          </ExerciseToolsColumnSection>
          <ExerciseToolsColumnSection>
            <AdaptationDetailsFieldsForm2 v-if="adaptationDetails !== null && fields !== null" v-model="model" :textbook :fields :settings="adaptationDetails.settings" />
          </ExerciseToolsColumnSection>
          <ExerciseToolsColumnSection>
            <template v-if="fields !== null && adaptationDetails !== null">
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

              <p v-if="adaptationDetails !== null && adaptationDetails.settings.itemized.items.isManual">
                <BButton
                  sm secondary
                  :disabled="fields.focusedWysiwygField !== 'wording'"
                  :class="{active: fields.currentWysiwygFormat['manual-item']}"
                  @click="fields.toggle('manual-item')"
                  data-cy="format-manual-item"
                >{{ $t('manualItemButton') }}</BButton>
              </p>
            </template>
          </ExerciseToolsColumnSection>
          <ExerciseToolsColumnSection>
            <div class="mb-3">
              <p class="form-label">{{ $t('exerciseDistribution') }}</p>
              <DistributionToggles v-model="model.adaptation.wording_paragraphs_per_pagelet" />
              <BLabeledCheckbox v-model="model.adaptation.single_item_per_paragraph" :label="$t('singleItemPerParagraph')" />
            </div>
          </ExerciseToolsColumnSection>
          <hr />
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
