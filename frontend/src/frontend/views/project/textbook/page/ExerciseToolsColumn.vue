<script lang="ts">
import { InlineBlot } from '$frontend/components/Quill.vue'
import { basicBlots } from '$frontend/components/WysiwygEditor.vue'
import { Choices2Blot } from './MultipleChoicesTools.vue'
import { SelBlot } from './SelectableEffectTools.vue'


class ManualItemBlot extends InlineBlot {
  static override blotName = 'manual-item'
  static override tagName = 'manual-item-blot'
}

class McqPlaceholderBlot extends InlineBlot {
  static override blotName = 'mcq-placeholder'
  static override tagName = 'mcq-placeholder-blot'
}

export const wysiwygBlots = [
  ...basicBlots,
  SelBlot,
  Choices2Blot,
  ManualItemBlot,
  McqPlaceholderBlot,
]

export const wysiwygContagiousFormats = ['choices2']

export const wysiwygCompatibleFormats = [['bold', 'italic']]
</script>

<script setup lang="ts">
import { computed, ref } from 'vue'
import MultipleChoicesTools from './MultipleChoicesTools.vue'
import ItemsTools from './ItemsTools.vue'
import SelectableEffectTools from './SelectableEffectTools.vue'
import BoxedEffectTools from './BoxedEffectTools.vue'
import { type Model, makeItems } from './ExerciseFieldsForm.vue'
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

const items = computed(() => makeItems(model.value.adaptationSettings))
const hasItems = computed(() => items.value !== null)

const fillWithFreeTextPlaceholder = computed({
  get() {
    if (model.value.adaptationSettings.placeholderForFillWithFreeText !== null) {
      return model.value.adaptationSettings.placeholderForFillWithFreeText
    } else {
      return ''
    }
  },
  set(value: string) {
    if (value === '') {
      model.value.adaptationSettings.placeholderForFillWithFreeText = null
    } else {
      model.value.adaptationSettings.placeholderForFillWithFreeText = value
    }
  },
})

const selfRef = ref<HTMLDivElement | null>(null)
</script>

<template>
  <div ref="selfRef" class="h-100 overflow-hidden d-flex flex-row position-relative" id="gutter-2">
    <div class="handle"></div>
    <div class="h-100 overflow-auto flex-fill" data-cy="gutter-2">
      <div style="position: relative">
        <div>
          <h1>{{ $t('tools') }}</h1>
          <ExerciseToolsColumnSection>
            <UndoRedoTool v-model="model" :reset="resetUndoRedo" />
          </ExerciseToolsColumnSection>
          <ExerciseToolsColumnSection>
            <MultipleChoicesTools v-if="fields !== null && selfRef !== null /* See comment on SelectableEffectTools */" v-model="model" :textbook :fields :hasItems />
          </ExerciseToolsColumnSection>
          <ExerciseToolsColumnSection>
            <OptionalInput v-model="fillWithFreeTextPlaceholder" :label="$t('placeholderForFreeText')" />
          </ExerciseToolsColumnSection>
          <ExerciseToolsColumnSection>
            <ItemsTools v-model="model" :textbook />
          </ExerciseToolsColumnSection>
          <ExerciseToolsColumnSection>
            <SelectableEffectTools v-if="selfRef !== null /* Because SelectableEffectTools refers to #left-col-2 and #gutter-2 (bad design, @todo Fix) */" v-model="model" :disabled="!hasItems" />
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

              <p v-if="hasItems && model.adaptationSettings.itemized.effects.isSelectable">
                <template v-for="i in model.adaptationSettings.itemized.effects.selectable.colorsCount">
                  <BButton
                    class="format-color"
                    sm secondary
                    :disabled="fields.focusedWysiwygField === null || fields.focusedWysiwygField === 'wording'"
                    :class="{active: fields.currentWysiwygFormat.sel === i}"
                    @click="fields.toggle('sel', i)"
                    :style="{lineHeight: 0, padding: '2px'}"
                    :data-cy="`format-color-${i}`"
                  >
                    <span :style="{backgroundColor: model.adaptationSettings.itemized.effects.selectable.allColors[i - 1]}"></span>
                  </BButton>
                  <wbr />
                </template>
              </p>

              <p v-if="model.adaptationSettings.itemized.items.isManual">
                <BButton
                  sm secondary
                  :disabled="fields.focusedWysiwygField !== 'wording'"
                  :class="{active: fields.currentWysiwygFormat['manual-item']}"
                  @click="fields.toggle('manual-item')"
                  data-cy="format-manual-item"
                >{{ $t('manualItemButton') }}</BButton>
              </p>

              <p v-if="model.adaptationSettings.itemized.effects.repeatedWithMcq">
                <BButton
                  sm secondary
                  :disabled="fields.focusedWysiwygField !== 'wording'"
                  :class="{active: fields.currentWysiwygFormat['mcq-placeholder']}"
                  @click="fields.toggle('mcq-placeholder')"
                  data-cy="format-mcq-placeholder"
                >{{ $t('mcqPlaceholderItemButton') }}</BButton>
              </p>
            </template>

            <BLabeledCheckbox v-model="model.adaptationSettings.singleItemPerParagraph" :label="$t('singleItemPerParagraph')" :disabled="!hasItems" />
            <BoxedEffectTools v-if="fields !== null" v-model="model" :disabled="!hasItems" />
          </ExerciseToolsColumnSection>
          <ExerciseToolsColumnSection>
            <div class="mb-3">
              <p class="form-label">{{ $t('exerciseDistribution') }}</p>
              <DistributionToggles v-model="model.adaptationSettings.wordingParagraphsPerPagelet" />
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

<style>
div.ql-editor manual-item-blot {
  margin: 0;
  padding: 0 0.4em;
  border: 2px dotted black;
}

div.ql-editor mcq-placeholder-blot {
  background-color: #ffff00;
}
</style>
