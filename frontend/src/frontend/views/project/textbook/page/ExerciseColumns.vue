<script setup lang="ts">
import { computed, ref, watch } from 'vue'
import deepCopy from 'deep-copy'
import deepEqual from 'deep-equal'

import { BBusy } from '$frontend/components/opinion/bootstrap'
import TwoResizableColumns from '$frontend/components/TwoResizableColumns.vue'
import type { Exists, InCache, ParsedExercise } from '$frontend/stores/api'
import { type Model, getParsed } from '$frontend/components/ExerciseFieldsForm.vue'
import AdaptedExercise from './AdaptedExercise.vue'


defineProps<{
  projectId: string
}>()

const model = defineModel<Model>({required: true})

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

const deltas = computed(() => {
  if (parsedExercise.value === null) {
    return null
  } else {
    return parsedExercise.value.attributes.delta
  }
})

defineExpose({
  parsedExercise,
  deltas,
})
</script>

<template>
  <TwoResizableColumns saveKey="projectTextbookPage-2" :snap="150" class="h-100" gutterWidth="200px">
    <template #left>
      <slot name="left"></slot>
    </template>

    <template #gutter>
      <slot name="gutter"></slot>
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
