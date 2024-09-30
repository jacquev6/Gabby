<script lang="ts">
import { computed, type Ref } from 'vue'


export function useExercisePagelets(
  paragraphsCountPerPagelet: Ref<number>,
  totalParagraphsCount: Ref<number>,
  pageletIndex: Ref<number>,
) {
  const degenerate = computed(() => totalParagraphsCount.value === 0)

  return {
    firstWordingParagraph: computed(() => {
      if (degenerate.value) {
        return null
      } else {
        return pageletIndex.value * paragraphsCountPerPagelet.value!
      }
    }),
    lastWordingParagraph: computed(() => {
      if (degenerate.value) {
        return null
      } else {
        return (pageletIndex.value + 1) * paragraphsCountPerPagelet.value!
      }
    }),
    pageletsCount: computed(() => {
      if (degenerate.value) {
        return 1
      } else {
        console.assert(paragraphsCountPerPagelet.value! > 0)
        return Math.ceil(totalParagraphsCount.value / paragraphsCountPerPagelet.value!)
      }
    })
  }
}
</script>

<script setup lang="ts">
import { reactive, watch } from 'vue'

import type { Settings, Exercise } from '$adapted/types'
import TricolorSection from './TricolorSection.vue'
import MonocolorSection from './MonocolorSection.vue'


const props = withDefaults(defineProps<{
  projectId: string,
  exerciseId: string,
  exercise: Exercise,
  settings: Settings,
  firstWordingParagraph?: number | null,
  lastWordingParagraph?: number | null,
  isPreview?: boolean,
}>(), {
  isPreview: false,
  firstWordingParagraph: null,
  lastWordingParagraph: null,
})

// @todo Make this key depend on when the exercise (or its adaptation ) was last modified
const storageKey = computed(() => `exerciseAnswers/project-${props.projectId}/exercise-${props.exerciseId}`)

const models = reactive<{
  wording: {[index: string]: any/* @todo Type */},
  instructions: {[index: string]: any/* @todo Type */},
  example: {[index: string]: any/* @todo Type */},
  clue: {[index: string]: any/* @todo Type */},
}>({
  wording: {},
  instructions: {},
  example: {},
  clue: {},
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

const wordingParagraphs = computed(() => {
  if (props.firstWordingParagraph === null || props.lastWordingParagraph === null) {
    return props.exercise.wording.paragraphs
  } else {
    return props.exercise.wording.paragraphs.slice(
      props.firstWordingParagraph,
      props.lastWordingParagraph,
    )}
})

const wordingParagraphIndexOffset = computed(() => {
  if (props.firstWordingParagraph === null) {
    return 0
  } else {
    return props.firstWordingParagraph
  }
})

defineExpose({
  reinitModels,
  disabledReinitModels: computed(() => Object.keys(models.wording).length === 0),
})
</script>

<template>
  <div style="position: relative; font-family: Arial, sans-serif;">
    <MonocolorSection :paragraphs="exercise.instructions.paragraphs" :paragraphIndexOffset="0" :centered="settings.centeredInstructions" :first="true" v-model="models.instructions" />
    <MonocolorSection :paragraphs="exercise.example.paragraphs" :paragraphIndexOffset="0" :centered="settings.centeredInstructions" v-model="models.example" />
    <MonocolorSection :paragraphs="exercise.clue.paragraphs" :paragraphIndexOffset="0" :centered="settings.centeredInstructions" v-model="models.clue" />
    <div style="padding: 6px">
      <TricolorSection v-if="settings.tricolorWording" :paragraphs="wordingParagraphs" :paragraphIndexOffset="wordingParagraphIndexOffset" v-model="models.wording" />
      <MonocolorSection v-else :paragraphs="wordingParagraphs" :paragraphIndexOffset="wordingParagraphIndexOffset" v-model="models.wording" />
    </div>
  </div>
</template>
