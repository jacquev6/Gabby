<script setup lang="ts">
import { computed, ref } from 'vue'

import { BLabeledCheckbox } from '../../../../components/opinion/bootstrap'
import type { Textbook } from '$frontend/stores/api'
import { type Model, cleanupModel, disableItemizedEffects } from './ExerciseFieldsForm.vue'


defineProps<{
  textbook: Textbook
}>()

const model = defineModel<Model>({required: true})

const isLetters = computed({
  get() {
    return model.value.adaptationSettings.itemized.items.isLetters
  },
  set(value: boolean) {
    model.value.adaptationSettings.itemized.items.isLetters = value
    if (value) {
      model.value.adaptationSettings.itemized.items.isWords = false
      model.value.adaptationSettings.itemized.items.isPunctuation = false
      model.value.adaptationSettings.itemized.items.isSentences = false
      model.value.adaptationSettings.itemized.items.isManual = false
      model.value.adaptationSettings.itemized.items.isSeparated = false
    } else {
      disableItemizedEffects(model.value)
    }
  },
})

const isWords = computed({
  get() {
    return model.value.adaptationSettings.itemized.items.isWords
  },
  set(value: boolean) {
    model.value.adaptationSettings.itemized.items.isWords = value
    if (value) {
      model.value.adaptationSettings.itemized.items.isLetters = false
      // Keep model.value.adaptationSettings.itemized.items.isPunctuation unchanged
      model.value.adaptationSettings.itemized.items.isSentences = false
      model.value.adaptationSettings.itemized.items.isManual = false
      model.value.adaptationSettings.itemized.items.isSeparated = false
    } else if (!model.value.adaptationSettings.itemized.items.isPunctuation) {
      disableItemizedEffects(model.value)
    }
  },
})

const isPunctuation = computed({
  get() {
    return model.value.adaptationSettings.itemized.items.isPunctuation
  },
  set(value: boolean) {
    model.value.adaptationSettings.itemized.items.isPunctuation = value
    if (value) {
      model.value.adaptationSettings.itemized.items.isLetters = false
      // Keep model.value.adaptationSettings.itemized.items.isWords unchanged
      model.value.adaptationSettings.itemized.items.isSentences = false
      model.value.adaptationSettings.itemized.items.isManual = false
      model.value.adaptationSettings.itemized.items.isSeparated = false
    } else if (!model.value.adaptationSettings.itemized.items.isWords) {
      disableItemizedEffects(model.value)
    }
  },
})

const isSentences = computed({
  get() {
    return model.value.adaptationSettings.itemized.items.isSentences
  },
  set(value: boolean) {
    model.value.adaptationSettings.itemized.items.isSentences = value
    if (value) {
      model.value.adaptationSettings.itemized.items.isLetters = false
      model.value.adaptationSettings.itemized.items.isWords = false
      model.value.adaptationSettings.itemized.items.isPunctuation = false
      model.value.adaptationSettings.itemized.items.isManual = false
      model.value.adaptationSettings.itemized.items.isSeparated = false
    } else {
      disableItemizedEffects(model.value)
    }
  },
})

const isManual = computed({
  get() {
    return model.value.adaptationSettings.itemized.items.isManual
  },
  set(value: boolean) {
    model.value.adaptationSettings.itemized.items.isManual = value
    if (value) {
      model.value.adaptationSettings.itemized.items.isLetters = false
      model.value.adaptationSettings.itemized.items.isWords = false
      model.value.adaptationSettings.itemized.items.isPunctuation = false
      model.value.adaptationSettings.itemized.items.isSentences = false
      model.value.adaptationSettings.itemized.items.isSeparated = false
    } else {
      disableItemizedEffects(model.value)
      cleanupModel(model.value)
    }
  },
})

const isSeparated = computed({
  get() {
    return model.value.adaptationSettings.itemized.items.isSeparated
  },
  set(value: boolean) {
    model.value.adaptationSettings.itemized.items.isSeparated = value
    if (value) {
      model.value.adaptationSettings.itemized.items.isLetters = false
      model.value.adaptationSettings.itemized.items.isWords = false
      model.value.adaptationSettings.itemized.items.isPunctuation = false
      model.value.adaptationSettings.itemized.items.isSentences = false
      model.value.adaptationSettings.itemized.items.isManual = false
    } else {
      disableItemizedEffects(model.value)
    }
  },
})

const separatorFocused = ref(false)
const separatorsHovered = ref(false)
</script>

<template>
  <div class="mb-3">
    <p class="form-label">{{ $t('items') }}</p>
    <BLabeledCheckbox v-model="isLetters" :label="$t('itemsLetters')" />
    <BLabeledCheckbox v-model="isWords" :label="$t('itemsWords')" />
    <BLabeledCheckbox v-model="isPunctuation" :label="$t('itemsPunctuation')" />
    <BLabeledCheckbox v-model="isSentences" :label="$t('itemsSentences')" />
    <BLabeledCheckbox v-model="isSeparated" :label="$t('itemsSeparated')">
      <span style="position: relative; display: inline-block">
        <input
          v-model="model.adaptationSettings.itemized.items.separator"
          style="width: 2em"
          @focus="separatorFocused = true"
          @click="isSeparated = true"
          @blur="separatorFocused = false"
        />
        <div
          v-if="(separatorFocused || separatorsHovered) && textbook.inCache && textbook.exists"
          @pointerenter="separatorsHovered = true"
          @pointerleave="separatorsHovered = false"
          style="position: absolute; width: 2em; border: 1px solid grey; background: white; user-select: none;"
        >
          <p
            v-for="value in textbook.attributes.suggestedItemsSeparators"
            class="separatorSuggestion"
            @click="model.adaptationSettings.itemized.items.separator = value; separatorsHovered = false"
          >
            {{ value }}
          </p>
        </div>
      </span>
    </BLabeledCheckbox>
    <BLabeledCheckbox v-model="isManual" :label="$t('itemsManual')" />
  </div>
</template>
