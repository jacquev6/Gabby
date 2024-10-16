<script setup lang="ts">
import type { Model } from './ExerciseFieldsForm.vue'
import { BButton } from './opinion/bootstrap'


defineProps<{
  wysiwyg: boolean
}>()

const model = defineModel<Model>({required: true})
</script>

<template>
  <template v-if="wysiwyg">
    <BButton primary sm @click="model.awaiting.multipleChoices = {globalSelection: true, confirmation: false, editing: false, editionWatch() {}, range: null, settings: null}">Multiple choices</BButton>
  </template>
  <template v-else>
    <p class="alert alert-secondary">
      <i18n-t keypath="useChoices">
        <template v-slot:choices>
          <code>{choices|<em>text</em>|<em>text</em>|<em>...</em>}</code>
        </template>
      </i18n-t>
    </p>
  </template>
</template>
