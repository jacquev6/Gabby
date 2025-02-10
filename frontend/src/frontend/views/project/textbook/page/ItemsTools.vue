<script setup lang="ts">
import { computed, ref } from 'vue'

import { BLabeledCheckbox } from '../../../../components/opinion/bootstrap'
import type { Textbook } from '$frontend/stores/api'
import type { Settings } from './MultipleChoicesTools.vue'


const props = defineProps<{
  textbook: Textbook
  settings: Settings
}>()

const isLettersProxy = computed({
  get() {
    return props.settings.itemized.items.isLetters
  },
  set(value: boolean) {
    props.settings.itemized.items.isLetters = value
    if (value) {
      props.settings.itemized.items.isWords = false
      props.settings.itemized.items.isPunctuation = false
      props.settings.itemized.items.isSentences = false
      props.settings.itemized.items.isManual = false
      props.settings.itemized.items.isSeparated = false
    }
  },
})

const isWordsProxy = computed({
  get() {
    return props.settings.itemized.items.isWords
  },
  set(value: boolean) {
    props.settings.itemized.items.isWords = value
    if (value) {
      props.settings.itemized.items.isLetters = false
      props.settings.itemized.items.isSentences = false
      props.settings.itemized.items.isManual = false
      props.settings.itemized.items.isSeparated = false
    }
  },
})

const isPunctuationProxy = computed({
  get() {
    return props.settings.itemized.items.isPunctuation
  },
  set(value: boolean) {
    props.settings.itemized.items.isPunctuation = value
    if (value) {
      props.settings.itemized.items.isLetters = false
      props.settings.itemized.items.isSentences = false
      props.settings.itemized.items.isManual = false
      props.settings.itemized.items.isSeparated = false
    }
  },
})

const isSentencesProxy = computed({
  get() {
    return props.settings.itemized.items.isSentences
  },
  set(value: boolean) {
    props.settings.itemized.items.isSentences = value
    if (value) {
      props.settings.itemized.items.isLetters = false
      props.settings.itemized.items.isWords = false
      props.settings.itemized.items.isPunctuation = false
      props.settings.itemized.items.isManual = false
      props.settings.itemized.items.isSeparated = false
    }
  },
})

const isManualProxy = computed({
  get() {
    return props.settings.itemized.items.isManual
  },
  set(value: boolean) {
    props.settings.itemized.items.isManual = value
    if (value) {
      props.settings.itemized.items.isLetters = false
      props.settings.itemized.items.isWords = false
      props.settings.itemized.items.isPunctuation = false
      props.settings.itemized.items.isSentences = false
      props.settings.itemized.items.isSeparated = false
    }
  },
})

const isSeparatedProxy = computed({
  get() {
    return props.settings.itemized.items.isSeparated
  },
  set(value: boolean) {
    props.settings.itemized.items.isSeparated = value
    if (value) {
      props.settings.itemized.items.isLetters = false
      props.settings.itemized.items.isWords = false
      props.settings.itemized.items.isPunctuation = false
      props.settings.itemized.items.isSentences = false
      props.settings.itemized.items.isManual = false
    }
  },
})

const separatorFocused = ref(false)
const separatorsHovered = ref(false)
</script>

<template>
  <div class="mb-3">
    <p class="form-label">{{ $t('items') }}</p>
    <BLabeledCheckbox v-model="isLettersProxy" :label="$t('itemsLetters')" />
    <BLabeledCheckbox v-model="isWordsProxy" :label="$t('itemsWords')" />
    <BLabeledCheckbox v-model="isPunctuationProxy" :label="$t('itemsPunctuation')" />
    <BLabeledCheckbox v-model="isSentencesProxy" :label="$t('itemsSentences')" />
    <BLabeledCheckbox v-model="isManualProxy" :label="$t('itemsManual')" />
    <BLabeledCheckbox v-model="isSeparatedProxy" :label="$t('itemsSeparated')">
      <span style="position: relative; display: inline-block">
        <input
          v-model="settings.itemized.items.separator"
          style="width: 2em"
          @focus="separatorFocused = true"
          @click="isSeparatedProxy = true"
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
            @click="settings.itemized.items.separator = value; separatorsHovered = false"
          >
            {{ value }}
          </p>
        </div>
      </span>
    </BLabeledCheckbox>
  </div>
</template>
