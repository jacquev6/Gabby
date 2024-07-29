<script setup lang="ts">
import { BLabeledInput, BLabeledCheckbox } from './opinion/bootstrap'

import type { Model } from './ExerciseFieldsForm.vue'


defineProps<{
  wysiwyg: boolean
}>()

const model = defineModel<Model>({required: true})

const addingChoices = defineModel<boolean>('addingChoices', {required: true})
</script>

<template>
  <template v-if="model.adaptationType === '-'">
  </template>
  <template v-else-if="model.adaptationType === 'fillWithFreeTextAdaptation'">
    <BLabeledInput :label="$t('placeholderText')" type="text" v-model="model.fillWithFreeTextAdaptationOptions.placeholder" />
  </template>
  <template v-else-if="model.adaptationType === 'selectThingsAdaptation'">
    <BLabeledInput :label="$t('colorsCount')" type="number" min="1" v-model="model.selectThingsAdaptationOptions.colors" />
    <p class="alert alert-secondary">
      <i18n-t keypath="useSel1ToSelN" v-if="model.selectThingsAdaptationOptions.colors > 1">
        <template v-slot:first>
          <code>{sel1|<em>text</em>}</code>
        </template>
        <template v-slot:last>
          <code>{sel{{ model.selectThingsAdaptationOptions.colors }}|<em>text</em>}</code>
        </template>
      </i18n-t>
      <i18n-t keypath="useSel1" v-else>
        <template v-slot:first>
          <code>{sel1|<em>text</em>}</code>
        </template>
      </i18n-t>
    </p>
    <BLabeledCheckbox :label="$t('includePunctuation')" v-model="model.selectThingsAdaptationOptions.punctuation" />
  </template>
  <template v-else-if="model.adaptationType === 'multipleChoicesInInstructionsAdaptation'">
    <div v-if="wysiwyg" class="mb-3">
      <input id="add-choices" type="checkbox" class="btn-check" v-model="addingChoices">
      <label class="btn btn-primary" for="add-choices">Add choices</label>
    </div>
    <p v-else class="alert alert-secondary">
      <i18n-t keypath="useChoice">
        <template v-slot:choice>
          <code>{choice|<em>text</em>}</code>
        </template>
      </i18n-t>
    </p>
    <BLabeledInput :label="$t('placeholderText')" type="text" v-model="model.multipleChoicesInInstructionsAdaptationOptions.placeholder" />
  </template>
  <template v-else-if="model.adaptationType === 'multipleChoicesInWordingAdaptation'">
    <p class="alert alert-secondary">
      <i18n-t keypath="useChoices">
        <template v-slot:choices>
          <code>{choices|<em>text</em>|<em>text</em>|<em>...</em>}</code>
        </template>
      </i18n-t>
    </p>
  </template>
  <template v-else>
    <span>{{ ((t: never) => t)(model.adaptationType) }}</span>
  </template>
</template>
