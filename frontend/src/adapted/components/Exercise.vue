<script setup lang="ts">
import { computed, reactive, watch } from 'vue'

import { BButton } from '$frontend/components/opinion/bootstrap'
import type { Settings, Exercise } from '$adapted/types'
import TricolorSection from './TricolorSection.vue'
import MonocolorSection from './MonocolorSection.vue'


const props = withDefaults(defineProps<{
  projectId: string,
  exerciseId: string,
  exercise: Exercise,
  settings: Settings,
  isPreview?: boolean,
}>(), {
  isPreview: false,
})

// @todo Make this key depend on when the exercise (or its adaptation ) was last modified
const storageKey = computed(() => `exerciseAnswers/project-${props.projectId}/exercise-${props.exerciseId}`)

const models = reactive<{
  wording: {[index: string]: any/* @todo Type */},
  instructions: {[index: string]: any/* @todo Type */},
}>({
  wording: {},
  instructions: {},
})
function reinitModels() {
  for (const m of Object.values(models)) {
    Object.keys(m).forEach((key: string) => delete m[key])
  }
}
watch(() => props.exercise, reinitModels, {deep: true})
watch(
  models,
  () => {
    if (!props.isPreview) {
      localStorage.setItem(storageKey.value, JSON.stringify(models))
      console.log('Saved models to', storageKey.value)
    }
  },
  {deep: true},
)
watch(
  storageKey,
  () => {
    if (!props.isPreview) {
      const storedModels = localStorage.getItem(storageKey.value)
      if (storedModels) {
        const parsedStoredModels = JSON.parse(storedModels)
        if (typeof parsedStoredModels === 'object') {
          reinitModels()
          Object.assign(models, parsedStoredModels)
          console.log('Loaded models from', storageKey.value, models)
        }
      }
    }
  },
  {immediate: true},
)
</script>

<template>
  <MonocolorSection :section="exercise.instructions" v-model="models.instructions" />
  <hr />
  <TricolorSection v-if="settings.tricolorWording" :section="exercise.wording" v-model="models.wording" />
  <MonocolorSection v-else :section="exercise.wording" v-model="models.wording" />
  <hr />
  <p><BButton
    data-cy="erase-responses"
    secondary sm
    @click="reinitModels"
    :disabled="Object.keys(models).length === 0"
  >
    {{ $t('eraseAnswers') }}
  </BButton></p>
</template>
