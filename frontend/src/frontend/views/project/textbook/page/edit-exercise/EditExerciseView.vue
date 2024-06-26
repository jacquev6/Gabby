<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { computedAsync } from '@vueuse/core'

import { useApiStore } from '$frontend/stores/api'
import { BButton, BBusy } from '$frontend/components/opinion/bootstrap'
import ExerciseForm from '$frontend/components/ExerciseForm.vue'
import TwoResizableColumns from '$frontend/components/TwoResizableColumns.vue'
import ExerciseTools from '../ExerciseTools.vue'
import type { Project, Textbook, Section, Exercise } from '$frontend/types/api'
import AdaptedExercise from '../AdaptedExercise.vue'


const props = defineProps<{
  project: Project,
  textbook: Textbook,
  pdf: any/* @todo Type */,
  section: Section,
  page: number,
  exerciseId: string
}>()

const router = useRouter()
const api = useApiStore()

const exerciseLoading = ref(false)
const exercise = computedAsync(
  async () => {
    await new Promise((resolve) => resolve(null))  // @todo Understand why removing this line duplicates the request
    return await api.client.getOne<Exercise>('exercise', props.exerciseId, {include: 'adaptation'})
  },
  undefined,
  exerciseLoading,
)

const exerciseForm = ref<typeof ExerciseForm | null>(null)

function saved() {
  router.push({name: 'project-textbook-page-list-exercises'})
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
          @saved="saved"
          v-slot="{ disabled, save }"
        >
          <RouterLink class="btn btn-secondary" :to="{name: 'project-textbook-page-list-exercises'}">{{ $t('cancel') }}</RouterLink>
          <BButton primary :disabled @click="save" data-cy="save-exercise">{{ $t('save') }}</BButton>
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
