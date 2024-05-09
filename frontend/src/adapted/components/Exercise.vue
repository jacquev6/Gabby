<script setup lang="ts">
import { computed, reactive, watch } from 'vue'

import { BButton } from '../../frontend/components/opinion/bootstrap'
import type { Settings, Exercise } from '../types'
import SelectableWord from './SelectableWord.vue'
import TricolorSection from './TricolorSection.vue'
import MonocolorSection from './MonocolorSection.vue'


const props = withDefaults(
  defineProps<{
    projectId: string,
    exerciseId: string,
    exercise: Exercise,
    settings?: Settings,
    isPreview?: boolean,
  }>(),
  {
    settings: {
      tricolorWording: true,
    },
    isPreview: false,
  },
)

const section = computed(() => props.settings.tricolorWording ? TricolorSection : MonocolorSection)

// @todo Make this key depend on when the exercise (or its adaptation ) was last modified
const storageKey = computed(() => `exerciseAnswers/project-${props.projectId}/exercise-${props.exerciseId}`)

const models = reactive<{[index: string]: any}>({})
function reinitModels() {
  Object.keys(models).forEach((key: string) => delete models[key]);
}
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
  <p>{{ exercise.instructions }}</p>
  <component :is="section" :section="exercise.wording">
    <template v-slot="{ token, tokenIndex }">
      <template v-if="false"></template>
      <template v-else-if="token.type === 'plainText'" :token="token">{{ token.text }}</template>
      <template v-else-if="token.type === 'whitespace'" :token="token"><wbr /> <wbr /></template>
      <template v-else-if="token.type === 'freeTextInput'" :token="token">
        <input type="text" v-model="models[tokenIndex]" />
      </template>
      <template v-else-if="token.type === 'selectableText'">
        <SelectableWord :colors="token.colors" v-model="models[tokenIndex]">{{ token.text }}</SelectableWord>
      </template>
      <template v-else>
        <span>{{ ((t: never) => t)(token) }}</span>
      </template>
    </template>
  </component>
  <p><BButton secondary sm @click="reinitModels" :disabled="Object.keys(models).length === 0">Effacer les réponses</BButton></p>
</template>
