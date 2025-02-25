<script setup lang="ts">
import { reactive, computed, watch } from 'vue'

import type { Exercise } from '$adapted/types'
import TricolorSection from './TricolorSection.vue'
import MonocolorSection from './MonocolorSection.vue'


const props = withDefaults(defineProps<{
  projectId: string
  exerciseId: string
  exercise: Exercise
  pageletIndex: number
  isPreview?: boolean
}>(), {
  isPreview: false,
})

// @todo Make this key depend on when the exercise (or its adaptation ) was last modified
const storageKey = computed(() => `exerciseAnswers/v2/project-${props.projectId}/exercise-${props.exerciseId}`)

const pagelet = computed(() => {
  console.assert(props.pageletIndex >= 0 && props.pageletIndex < props.exercise.pagelets.length)
  return props.exercise.pagelets[props.pageletIndex]
})

const models = reactive<
  {
    instructions: {[index: string]: any/* @todo Type */},
    wording: {[index: string]: any/* @todo Type */},
  }[]
>([])
function reinitModels() {
  models.splice(0, models.length, ...props.exercise.pagelets.map(() => ({instructions: {}, wording: {}})))
}
watch(() => props.exercise, reinitModels, {deep: true, immediate: true})
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
          models.splice(0, models.length, ...parsedStoredModels)
          console.log('Loaded models from', storageKey.value, models)
        }
      }
    }
  },
  {immediate: true},
)

defineExpose({
  reinitModels,
  disabledReinitModels: computed(() => models.every(pagelet => Object.keys(pagelet.wording).length === 0)),
})
</script>

<template>
  <div style="position: relative; font-family: Arial, sans-serif;">
    <MonocolorSection :paragraphs="pagelet.instructions.paragraphs" :centered="true" :first="true" v-model="models[pageletIndex].instructions" />
    <div style="padding: 6px">
      <TricolorSection :paragraphs="pagelet.wording.paragraphs" :centered="false" :first="false" v-model="models[pageletIndex].wording" />
    </div>
  </div>
</template>
