<script setup lang="ts">
import { ref } from 'vue'
import AdaptationDetailsFieldsForm from '$frontend/components/AdaptationDetailsFieldsForm.vue'
import { type Model } from '$frontend/components/ExerciseFieldsForm.vue'
import ExerciseFieldsForm from '$frontend/components/ExerciseFieldsForm.vue'
import type { Textbook } from '$frontend/stores/api'
import ToolsGutter from './ToolsGutter.vue'
import UndoRedoTool from './UndoRedoTool.vue'
import BasicFormattingTools from './BasicFormattingTools.vue'
import { BButton, BLabeledCheckbox } from '$frontend/components/opinion/bootstrap'
import DistributionToggles from './DistributionToggles.vue'


defineProps<{
  textbook: Textbook
  fields: InstanceType<typeof ExerciseFieldsForm> | null
  resetUndoRedo: number
}>()

const model = defineModel<Model>({required: true})

const adaptationDetails = ref<InstanceType<typeof AdaptationDetailsFieldsForm> | null>(null)

const toolSlotNames = [
  'undoRedo',
  'adaptationDetails',
  'basicFormatting',
  'distribution',
]
</script>

<template>
  <div class="h-100 overflow-hidden d-flex flex-row position-relative" id="gutter-2">
    <div class="handle"></div>
    <div class="h-100 overflow-auto flex-fill" data-cy="gutter-2">
      <div style="position: relative">
        <div>
          <ToolsGutter :slotNames="toolSlotNames">
            <template #undoRedo>
              <UndoRedoTool v-model="model" :reset="resetUndoRedo" />
            </template>
            <template #adaptationDetails>
              <AdaptationDetailsFieldsForm ref="adaptationDetails" v-if="fields !== null" v-model="model" :textbook :fields/>
            </template>
            <template #basicFormatting>
              <BasicFormattingTools v-if="fields !== null && adaptationDetails !== null" v-model="model" :fields :adaptationDetails />
            </template>
            <template #distribution>
              <div class="mb-3">
                <p class="form-label">{{ $t('exerciseDistribution') }}</p>
                <DistributionToggles v-model="model.adaptation.wording_paragraphs_per_pagelet" />
                <BLabeledCheckbox v-model="model.adaptation.single_item_per_paragraph" :label="$t('singleItemPerParagraph')" />
              </div>
            </template>
          </ToolsGutter>
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
