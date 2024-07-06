<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

import { BButton } from '$frontend/components/opinion/bootstrap'
import ExerciseForm from '$frontend/components/ExerciseForm.vue'
import TwoResizableColumns from '$frontend/components/TwoResizableColumns.vue'
import ExerciseTools from '../ExerciseTools.vue'
import type { Project, Textbook, Section, Exercise } from '$frontend/types/api'
import AdaptedExercise from '../AdaptedExercise.vue'
import type { ExerciseCreationHistory } from '../ExerciseCreationHistory'


type CreateExercise = () => Promise<{exercise: Exercise, suggestedNumber: string}>

const props = defineProps<{
  project: Project,
  textbook: Textbook,
  pdf: any/* @todo Type */,
  section: Section | null,
  page: number,
  exerciseCreationHistory: ExerciseCreationHistory,
}>()

const router = useRouter()

const exerciseForm = ref<typeof ExerciseForm | null>(null)

const number = ref(props.exerciseCreationHistory.suggestedNumber ?? '')
const automaticNumber = ref(false)
async function createThenNext(createExercise: CreateExercise) {
  const { exercise, suggestedNumber } = await createExercise()
  props.exerciseCreationHistory.push(exercise.id)
  props.exerciseCreationHistory.suggestedNumber = suggestedNumber
  number.value = suggestedNumber
  automaticNumber.value = true
}

function goToPrevious() {
  const exerciseId = props.exerciseCreationHistory.previous
  console.assert(exerciseId !== null)
  props.exerciseCreationHistory.rewind()
  router.push({
    name: 'project-textbook-page-edit-exercise',
    params: {projectId: props.project.id, textbookId: props.textbook.id, exerciseId},
  })
}

async function createThenBack(createExercise: CreateExercise) {
  await createExercise()
  router.push({name: 'project-textbook-page-list-exercises', params: {projectId: props.project.id, textbookId: props.textbook.id, page: props.page}})
}

function changePage(page: number) {
  router.push({name: 'project-textbook-page-create-exercise', params: {projectId: props.project.id, textbookId: props.textbook.id, page}})
}

defineExpose({
  changePage,
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
          :number
          :automaticNumber
          :editMode="false"
          v-slot="{ disabled, create }"
        >
          <p>
            <BButton secondary :disabled="exerciseCreationHistory.previous === null" @click="goToPrevious">{{ $t('previous') }}</BButton>
            <BButton primary :disabled @click="createThenNext(create)" data-cy="create-then-next">{{ $t('saveThenNext') }}</BButton>
          </p>
          <p>
            <RouterLink class="btn btn-secondary" :to="{name: 'project-textbook-page-list-exercises'}">{{ $t('backToList') }}</RouterLink>
            <BButton secondary :disabled @click="createThenBack(create)" data-cy="create-then-back">{{ $t('saveThenBack') }}</BButton>
          </p>
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
        <AdaptedExercise
          v-if="exerciseForm?.adaptedData"
          :projectId="props.project.id"
          exerciseId="unused @todo Compute storageKey in an independent composable, and let AdaptedExercise load and save iif the key is not null"
          :exercise="exerciseForm?.adaptedData"
        />
        <p v-else>{{ $t('selectExerciseType') }}</p>
      </div>
    </template>
  </TwoResizableColumns>
</template>
