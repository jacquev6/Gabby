<script lang="ts">
import { useDebouncedRefHistory } from '@vueuse/core'
</script>

<script setup lang="ts">
import { useMagicKeys } from '@vueuse/core'
import { ref, watch } from 'vue'
import deepCopy from 'deep-copy'
import deepEqual from 'deep-equal'


import { BButton } from '$/frontend/components/opinion/bootstrap'
import type { Model } from '$/frontend/components/ExerciseFieldsForm.vue'


const props = defineProps<{
  reset: number  // @todo Find a better way to trigger reset
}>()

const model = defineModel<Model>({required: true})

// I don't know why 'useDebouncedRefHistory' doesn't work with 'model' directly
// (its undo/redo methods don't seem to have any effect)
// This two-way watch is a workaround
const model_ = ref(deepCopy(model.value))
watch(
  model_,
  m => {
    if (!deepEqual(model.value, m)) {
      Object.assign(model.value, deepCopy(m))
    }
  },
  {deep: true},
)
watch(
  model,
  m => {
    if (!deepEqual(model_.value, m)) {
      Object.assign(model_.value, deepCopy(m))
    }
  },
  {deep: true},
)

// @todo Consider using 'useThrottledRefHistory' instead of 'useDebouncedRefHistory'
let history = useDebouncedRefHistory(model_, {deep: true, debounce: 1000})

watch(() => props.reset, () => {
  history = useDebouncedRefHistory(model_, {deep: true, debounce: 1000})
})

const { Ctrl_Z, Ctrl_Y } = useMagicKeys()
watch(Ctrl_Z, (v) => {
  if (v && history.canUndo.value) {
    history.undo()
  }
})
watch(Ctrl_Y, (v) => {
  if (v && history.canRedo.value) {
    history.redo()
  }
})
</script>

<template>
  <BButton primary sm @click="history.undo" :disabled="!history.canUndo.value" title="Ctrl+Z" :data-gab="history.undoStack.value.length">{{ $t('undo') }}</BButton>
  <BButton primary sm @click="history.redo" :disabled="!history.canRedo.value" title="Ctrl+Y" :data-gab="history.redoStack.value.length">{{ $t('redo') }}</BButton>
</template>
