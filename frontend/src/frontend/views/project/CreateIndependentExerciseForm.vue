<script setup lang="ts">
import { ref, reactive } from 'vue'

import { BBusy, BButton } from '$frontend/components/opinion/bootstrap'
import ExerciseFieldsForm from '$frontend/components/ExerciseFieldsForm.vue'
import type { Project, InCache, Exists } from '$frontend/stores/api'
import { makeModelNotInTextbook, resetModelNotInTextbook, create as createExercise, suggestNextNumber } from '$frontend/components/ExerciseFieldsForm.vue'


const props = defineProps<{
  project: Project & InCache & Exists
}>()

const fields = ref<InstanceType<typeof ExerciseFieldsForm> | null>(null)

const model = reactive(makeModelNotInTextbook())

const busy = ref(false)
async function create() {
  const suggestedNextNumber = suggestNextNumber(model.number)
  busy.value = true
  await createExercise(props.project, null, model)
  busy.value = false
  resetModelNotInTextbook(model)
  model.number = suggestedNextNumber
  /* no await */ props.project.refresh()
}
</script>

<template>
  <BBusy :busy>
    <ExerciseFieldsForm
      ref="fields"
      v-model="model"
      :fixedNumber="false" :wysiwyg="false" :deltas="{instructions: [], wording: [], example: [], clue: []}"
    />
    <BButton primary :disabled="fields === null || fields.saveDisabled" @click="create" data-cy="create-exercise">{{ $t('createExercise' )}}</BButton>
  </BBusy>
</template>
