<script setup lang="ts">
import { computed, ref, watch } from 'vue'
import deepCopy from 'deep-copy'
import deepEqual from 'deep-equal'

import { BBusy } from '$frontend/components/opinion/bootstrap'
import TwoResizableColumns from '$frontend/components/TwoResizableColumns.vue'
import type { Exists, InCache, Textbook, ParsedExercise } from '$frontend/stores/api'
import { type Model, getParsed } from './ExerciseFieldsForm.vue'
import AdaptedExercise from './AdaptedExercise.vue'
import ExerciseFieldsForm from './ExerciseFieldsForm.vue'
import ExerciseToolsColumn from './ExerciseToolsColumn.vue'


defineProps<{
  mode: 'edit' | 'create'
  projectId: string
  textbook: Textbook
  displayedPage: number
  busy: boolean
}>()

const model = defineModel<Model>({required: true})

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
        <ExerciseToolsColumn v-model="model" :fields :textbook :resetUndoRedo="doResetUndoRedo" />
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
