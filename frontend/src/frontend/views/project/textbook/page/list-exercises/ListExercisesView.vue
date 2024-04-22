<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

import { useApiStore } from '../../../../../stores/api'
import { BBusy, BRow, BCol, BButton } from '../../../../../components/opinion/bootstrap'
import ExercisesList from './ExercisesList.vue'


const props = defineProps({
  project: {type: Object, required: true},
  textbook: {type: Object, required: true},
  page: {type: Number, required: true},
})

const router = useRouter()
const api = useApiStore()

const deletingExercise = ref(false)
async function deleteExercise(exercise) {
  deletingExercise.value = true
  await api.client.delete('exercise', exercise.id)
  deletingExercise.value = false
}

function changePage(page) {
  router.push({name: 'project-textbook-page-list-exercises', params: {projectId: props.project.id, textbookId: props.textbook.id, page}})
}

const exercisesList = ref(null)

const highlightedRectangles = computed(() => {
  const rectangles = exercisesList.value?.exercises.map(exercise => exercise.attributes.boundingRectangle).filter(rectangle => rectangle !== null)
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
  <BRow>
    <BCol>
      <h1>{{ $t('edition') }}</h1>
      <BBusy :busy="deletingExercise">
        <ExercisesList ref="exercisesList" :textbook :page >
          <template v-slot="{exercise}">
            <RouterLink class="btn btn-primary btn-sm" :to="{name: 'project-textbook-page-edit-exercise', params: {exerciseId: exercise.id}}">{{ $t('edit') }}</RouterLink>
            <BButton secondary sm @click="deleteExercise(exercise)">{{ $t('delete') }}</BButton>
          </template>
        </ExercisesList>
        <p>
          <RouterLink class="btn btn-primary" :to="{name: 'project-textbook-page-create-exercise'}">
            {{ $t('create') }}
          </RouterLink>
        </p>
      </BBusy>
    </BCol>
  </BRow>
</template>
