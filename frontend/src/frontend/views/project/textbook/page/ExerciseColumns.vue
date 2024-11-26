<script setup lang="ts">
import { computed, ref, watch } from 'vue'
import deepCopy from 'deep-copy'
import deepEqual from 'deep-equal'
import { useI18n } from 'vue-i18n'

import { BBusy, BButton, BLabeledRadios } from '$frontend/components/opinion/bootstrap'
import TwoResizableColumns from '$frontend/components/TwoResizableColumns.vue'
import type { Exists, InCache, ParsedExercise } from '$frontend/stores/api'
import { type Model, getParsed } from '$frontend/components/ExerciseFieldsForm.vue'
import AdaptedExercise from './AdaptedExercise.vue'
import ExerciseFieldsForm from '$frontend/components/ExerciseFieldsForm.vue'
import UndoRedoTool from './UndoRedoTool.vue'
import ToolsGutter from './ToolsGutter.vue'
import BasicFormattingTools from './BasicFormattingTools.vue'
import AdaptationDetailsFieldsForm from '$frontend/components/AdaptationDetailsFieldsForm.vue'


defineProps<{
  mode: 'edit' | 'create'
  projectId: string
  displayedPage: number
  busy: boolean
}>()

const model = defineModel<Model>({required: true})

const i18n = useI18n()

const fields = ref<InstanceType<typeof ExerciseFieldsForm> | null>(null)

const parsedExercise = ref<ParsedExercise & InCache & Exists | null>(null)
const parsedExerciseIsLoading = ref(false)
const parsedExerciseNeedsLoading = ref(true)
watch(model, () => { parsedExerciseNeedsLoading.value = true }, {deep: true})
watch(parsedExerciseNeedsLoading, async () => {
  while (parsedExerciseNeedsLoading.value) {
    const modelBefore = deepCopy(model.value)
    parsedExerciseIsLoading.value = true
    const parsed = await getParsed(model.value)
    if (deepEqual(model.value, modelBefore)) {
      parsedExercise.value = parsed
      parsedExerciseIsLoading.value = false
      parsedExerciseNeedsLoading.value = false
    }
  }
}, {immediate: true})

const adaptedExercise = computed(() => {
  if (parsedExercise.value === null) {
    return null
  } else {
    return parsedExercise.value.attributes.adapted
  }
})

const toolSlotNames = [
  'undoRedo',
  'adaptationDetails',
  'basicFormatting',
  'repartition',
]

const wordingParagraphsPerPageletOptions = computed(() => [1, 2, 3, 4, 5].map(value => ({
  label: i18n.t('exerciseLinesPerPage', {lines: value}),
  value,
})))

const doResetUndoRedo = ref(0)
function resetUndoRedo() {
  doResetUndoRedo.value++
}

defineExpose({
  parsedExercise,
  fields,
  resetUndoRedo,
})
</script>

<template>
  <TwoResizableColumns saveKey="projectTextbookPage-2" :snap="150" class="h-100" gutterWidth="200px">
    <template #left>
      <div class="h-100 overflow-auto position-relative" id="left-col-2" data-cy="left-col-2">
        <h1>{{ $t('edition') }}</h1>
        <BBusy :busy>
          <ExerciseFieldsForm ref="fields"
            v-model="model" :displayedPage
            :fixedNumber="mode === 'edit'"
          >
            <template #overlay>
              <slot name="exerciseFieldsOverlay"></slot>
            </template>
          </ExerciseFieldsForm>
          <slot name="exerciseFieldsButtons"></slot>
        </BBusy>
      </div>
    </template>

    <template #gutter>
      <slot name="gutter">
        <div class="h-100 overflow-hidden d-flex flex-row position-relative" id="gutter-2">
          <div class="handle"></div>
          <div class="h-100 overflow-auto flex-fill" data-cy="gutter-2">
            <div style="position: relative">
              <div>
                <ToolsGutter :slotNames="toolSlotNames">
                  <template #undoRedo>
                    <UndoRedoTool v-model="model" :reset="doResetUndoRedo" />
                  </template>
                  <template #adaptationDetails>
                    <AdaptationDetailsFieldsForm v-if="fields !== null" v-model="model" :fields/>
                  </template>
                  <template #basicFormatting>
                    <BasicFormattingTools v-if="fields !== null" v-model="model" :fields />
                  </template>
                  <template #repartition>
                    <BLabeledRadios :label="$t('exerciseRepartition')" v-model="model.wordingParagraphsPerPagelet" :options="wordingParagraphsPerPageletOptions" />
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
      </slot>
    </template>

    <template #right>
      <div class="h-100 overflow-auto position-relative" data-cy="right-col-2" id="right-col-2">
        <h1>{{ $t('adaptation') }}</h1>
        <BBusy :busy="parsedExerciseIsLoading">
          <AdaptedExercise
            v-if="adaptedExercise !== null"
            :projectId="projectId"
            exerciseId="unused @todo Compute storageKey in an independent composable, and let AdaptedExercise load and save iif the key is not null"
            :exercise="adaptedExercise"
          />
        </BBusy>
      </div>
    </template>
  </TwoResizableColumns>
</template>
