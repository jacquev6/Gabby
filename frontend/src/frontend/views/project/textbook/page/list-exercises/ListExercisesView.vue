<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

import { BBusy, BButton } from '$frontend/components/opinion/bootstrap'
import ExercisesList from './ExercisesList.vue'
import type { Exercise, Project, Textbook } from '$frontend/stores/api'
import type { ExerciseCreationHistory } from '../ExerciseCreationHistory'


const props = defineProps<{
  project: Project,
  textbook: Textbook,
  pdf: unknown,  // Unused
  section: unknown,  // Unused
  page: number,
  exerciseCreationHistory: ExerciseCreationHistory,
}>()

const router = useRouter()

props.exerciseCreationHistory.reset()

const deletingExercise = ref(false)
async function deleteExercise(exercise: Exercise) {
  deletingExercise.value = true
  await exercise.delete()
  await exercisesList.value?.exercises.refresh()
  deletingExercise.value = false
}

function changePage(page: number) {
  router.push({name: 'project-textbook-page-list-exercises', params: {projectId: props.project.id, textbookId: props.textbook.id, page}})
}

const exercisesList = ref<typeof ExercisesList | null>(null)

const highlightedRectangles = computed(() => {
  const rectangles = exercisesList.value?.exercises.items.filter((exercise: Exercise) => exercise.exists).map((exercise: Required<Exercise>) => exercise.attributes.boundingRectangle).filter((rectangle: any/* @todo Type */) => rectangle !== null)
  if (rectangles?.length > 0) {
    return rectangles
  } else {
    return null
  }
})

defineExpose({
  changePage,
  highlightedRectangles,
})
</script>

<template>
  <h1>{{ $t('existingExercises') }}</h1>
  <p>
    <RouterLink class="btn btn-primary" :to="{name: 'project-textbook-page-create-exercise'}" data-cy="new-exercise">
      {{ $t('create') }}
    </RouterLink>
  </p>
  <ExercisesList ref="exercisesList" :textbook :page >
    <template v-slot="{exercise}">
      <BBusy tag="span" :busy="exercise.loading">
        <RouterLink class="btn btn-primary btn-sm" :to="{name: 'project-textbook-page-edit-exercise', params: {exerciseId: exercise.id}}">{{ $t('edit') }}</RouterLink>
        <BButton secondary sm @click="deleteExercise(exercise)">{{ $t('delete') }}</BButton>
      </BBusy>
    </template>
  </ExercisesList>
</template>
