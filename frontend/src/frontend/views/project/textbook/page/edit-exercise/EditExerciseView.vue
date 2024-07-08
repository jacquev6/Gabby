<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

import { useApiStore } from '$frontend/stores/api'
import { BButton, BBusy } from '$frontend/components/opinion/bootstrap'
import ExerciseForm from '$frontend/components/ExerciseForm.vue'
import TwoResizableColumns from '$frontend/components/TwoResizableColumns.vue'
import ExerciseTools from '../ExerciseTools.vue'
import type { Project, Textbook, Section } from '$frontend/stores/api'
import AdaptedExercise from '../AdaptedExercise.vue'
import type { ExerciseCreationHistory } from '../ExerciseCreationHistory'


const props = defineProps<{
  project: Project,
  textbook: Textbook,
  pdf: any/* @todo Type */,
  section: Section | null,
  page: number,
  exerciseId: string
  exerciseCreationHistory: ExerciseCreationHistory,
}>()

const router = useRouter()
const api = useApiStore()

const exercise = computed(() => api.auto.getOne('exercise', props.exerciseId, {include: ['adaptation']}))

const exerciseForm = ref<typeof ExerciseForm | null>(null)

function goToPrevious() {
  const exerciseId = props.exerciseCreationHistory.previous
  console.assert(exerciseId !== null)
  props.exerciseCreationHistory.rewind()
  router.push({
    name: 'project-textbook-page-edit-exercise',
    params: {projectId: props.project.id, textbookId: props.textbook.id, exerciseId},
  })
}

async function saveThenBack(save: () => Promise<void>) {
  await save()
  router.push({name: 'project-textbook-page-list-exercises'})
}

async function saveThenNext(save: () => Promise<void>) {
  await save()
  const exerciseId = props.exerciseCreationHistory.next
  props.exerciseCreationHistory.forward()
  if(exerciseId === null) {
    router.push({
      name: 'project-textbook-page-create-exercise',
      params: {projectId: props.project.id, textbookId: props.textbook.id},
    })
  } else {
    router.push({
      name: 'project-textbook-page-edit-exercise',
      params: {projectId: props.project.id, textbookId: props.textbook.id, exerciseId},
    })
  }
}

defineExpose({
  textSelected: computed(() => exerciseForm.value?.textSelected),
  highlightedRectangles: computed(() => exerciseForm.value?.highlightedRectangles),
  handlesScrolling: true,
})
</script>

<template>
  <TwoResizableColumns saveKey="projectTextbookPage-2" :snap="150" class="h-100" gutterWidth="200px">
    <template #left>
      <div class="h-100 overflow-auto" data-cy="left-col-2">
        <h1>{{ $t('edition') }}</h1>
        <ExerciseForm
          ref="exerciseForm"
          :project
          :textbook
          :textbookPage="page"
          :section
          :pdf
          :number="exercise?.attributes!.number || ''"
          :automaticNumber="false"
          :editMode="true"
          :exercise
          v-slot="{ disabled, save }"
        >
          <template v-if="exerciseCreationHistory.current === null">
            <p>
              <RouterLink class="btn btn-secondary" :to="{name: 'project-textbook-page-list-exercises'}">{{ $t('backToList') }}</RouterLink>
              <BButton primary :disabled @click="saveThenBack(save)" data-cy="save-then-back">{{ $t('saveThenBack') }}</BButton>
            </p>
          </template>
          <template v-else>
            <p>
              <BButton secondary :disabled="exerciseCreationHistory.previous === null" @click="goToPrevious">{{ $t('previous') }}</BButton>
              <BButton primary :disabled @click="saveThenNext(save)" data-cy="save-then-next">{{ $t('saveThenNext') }}</BButton>
            </p>
            <p>
              <RouterLink class="btn btn-secondary" :to="{name: 'project-textbook-page-list-exercises'}">{{ $t('backToList') }}</RouterLink>
              <BButton secondary :disabled @click="saveThenBack(save)" data-cy="save-then-back">{{ $t('saveThenBack') }}</BButton>
            </p>
          </template>
        </ExerciseForm>
      </div>
    </template>
    <template #gutter>
      <div class="h-100 overflow-hidden d-flex flex-row">
        <div class="handle"></div>
        <div class="h-100 overflow-auto flex-fill" data-cy="gutter-2">
          <ExerciseTools v-if="exerciseForm" :exerciseForm />
        </div>
        <div class="handle"></div>
      </div>
    </template>
    <template #right>
      <div class="h-100 overflow-auto" data-cy="right-col-2">
        <h1>{{ $t('adaptation') }}</h1>
        <BBusy :busy="!exerciseForm || exerciseForm.adaptedDataLoading">
          <AdaptedExercise
            v-if="exerciseForm?.adaptedData"
            :projectId="props.project.id"
            :exerciseId="props.exerciseId"
            :exercise="exerciseForm.adaptedData"
          />
          <p v-else>{{ $t('selectExerciseType') }}</p>
        </BBusy>
      </div>
    </template>
  </TwoResizableColumns>
</template>
