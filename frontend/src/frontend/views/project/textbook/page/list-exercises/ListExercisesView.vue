<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

import { BBusy, BButton } from '$frontend/components/opinion/bootstrap'
import ExercisesList from './ExercisesList.vue'
import type { Exercise, Project, Textbook } from '$frontend/stores/api'
import type { ExerciseCreationHistory } from '../ExerciseCreationHistory'
import type { List, InCache, Exists } from '$frontend/stores/api'
import type { Rectangle } from '../RectanglesHighlighter.vue'


const props = defineProps<{
  project: Project,
  textbook: Textbook,
  pdf: unknown,  // Unused
  section: unknown,  // Unused
  page: number,
  exercises: List<'exercise'>
  exerciseCreationHistory: ExerciseCreationHistory,
}>()

const router = useRouter()

props.exerciseCreationHistory.reset()

const deletingExercise = ref(false)
async function deleteExercise(exercise: Exercise) {
  deletingExercise.value = true
  await exercise.delete()
  await props.exercises.refresh()
  deletingExercise.value = false
}

function changePage(page: number) {
  router.push({name: 'project-textbook-page-list-exercises', params: {projectId: props.project.id, textbookId: props.textbook.id, page}})
}

const greyRectangles = computed(() => {
  const rectangles = props.exercises.items
    .filter((exercise): exercise is Exercise & InCache & Exists => exercise.inCache && exercise.exists)
    .map(exercise => exercise.attributes.boundingRectangle)
    .filter((x): x is Rectangle => x !== null)

  if (rectangles.length > 0) {
    return rectangles
  } else {
    return []
  }
})

defineExpose({
  changePage,
  surroundedRectangles: [],
  greyRectangles,
})
</script>

<template>
  <h1>{{ $t('existingExercises') }}</h1>
  <p style="margin-left: 5em">
    <RouterLink class="btn btn-primary btn-lg" :to="{name: 'project-textbook-page-create-exercise'}" data-cy="new-exercise">
      {{ $t('create') }}
    </RouterLink>
  </p>
  <ExercisesList :exercises >
    <template v-slot="{exercise}">
      <BBusy tag="span" :busy="exercise.loading">
        <RouterLink class="btn btn-primary btn-sm" :to="{name: 'project-textbook-page-edit-exercise', params: {exerciseId: exercise.id}}">{{ $t('edit') }}</RouterLink>
        <BButton secondary sm @click="deleteExercise(exercise)">{{ $t('delete') }}</BButton>
      </BBusy>
    </template>
  </ExercisesList>
</template>
