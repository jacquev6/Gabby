<script setup lang="ts">
import { computed, reactive, watch } from 'vue'

import { BButton } from '$frontend/components/opinion/bootstrap'
import type { Settings, Exercise } from '$adapted/types'
import SelectableText from './SelectableText.vue'
import SelectedText from './SelectedText.vue'
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

const section = computed(() => props.settings.tricolorWording ? TricolorSection : MonocolorSection)

// @todo Make this key depend on when the exercise (or its adaptation ) was last modified
const storageKey = computed(() => `exerciseAnswers/project-${props.projectId}/exercise-${props.exerciseId}`)

const models = reactive<{[index: string]: any/* @todo Type */}>({})
function reinitModels() {
  Object.keys(models).forEach((key: string) => delete models[key]);
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
  <MonocolorSection :section="exercise.instructions">
    <template v-slot="{ token }">
      <template v-if="false"></template>
      <template v-else-if="token.type === 'plainText'">{{ token.text }}</template>
      <template v-else-if="token.type === 'whitespace'"><wbr /> <wbr /></template>
      <template v-else-if="token.type === 'freeTextInput'"><input type="text" /></template>
      <template v-else-if="token.type === 'selectableText'">{{ token.text }}</template>
      <template v-else-if="token.type === 'selectedText'">
        <SelectedText :colors="token.colors" :color="token.color">{{ token.text }}</SelectedText>
      </template>
      <template v-else-if="token.type === 'selectedClicks'">
        <SelectedText :colors="token.colors" :color="token.color">{{ token.color }} {{ $t('nClicks', token.color) }}</SelectedText>
      </template>
      <template v-else>
        <span>{{ ((t: never) => t)(token) }}</span>
      </template>
    </template>
  </MonocolorSection>
  <hr />
  <component :is="section" :section="exercise.wording">
    <template v-slot="{ token, tokenIndex }">
      <template v-if="false"></template>
      <template v-else-if="token.type === 'plainText'">{{ token.text }}</template>
      <template v-else-if="token.type === 'whitespace'"><wbr /> <wbr /></template>
      <template v-else-if="token.type === 'freeTextInput'">
        <input type="text" v-model="models[tokenIndex]" />
      </template>
      <template v-else-if="token.type === 'selectableText'">
        <SelectableText :colors="token.colors" v-model="models[tokenIndex]">{{ token.text }}</SelectableText>
      </template>
      <template v-else-if="token.type === 'selectedText'">{{ token.text }}</template>
      <template v-else-if="token.type === 'selectedClicks'">{{ token.color }} {{ $t('nClicks', token.color) }}</template>
      <template v-else>
        <span>{{ ((t: never) => t)(token) }}</span>
      </template>
    </template>
  </component>
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
