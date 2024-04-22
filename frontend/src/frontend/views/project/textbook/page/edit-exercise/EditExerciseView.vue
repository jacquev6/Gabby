<script setup>
import { ref, reactive, computed, watch } from 'vue'
import { useRouter } from 'vue-router'
import { computedAsync } from '@vueuse/core'

import { useApiStore } from '../../../../../stores/api'
import { BButton } from '../../../../../components/opinion/bootstrap'
import ExerciseForm from '../../../../../components/ExerciseForm.vue'
import TwoResizableColumns from '../../../../../components/TwoResizableColumns.vue'


const props = defineProps({
  project: {type: Object, required: true},
  textbook: {type: Object, required: true},
  pdf: {required: true},
  section: {required: true},
  page: {type: Number, required: true},
  exerciseId: {type: String, required: true},
})

const router = useRouter()
const api = useApiStore()

const exerciseLoading = ref(false)
const exercise = computedAsync(
  async () => {
    return await api.client.getOne('exercise', props.exerciseId, {include: 'adapted'})
  },
  null,
  exerciseLoading,
)

const exerciseForm = ref(null)

function saved() {
  router.push({name: 'project-textbook-page-list-exercises'})
}

defineExpose({
  // @todo Allow editing the bounding rectangle
  textSelected: computed(() => exerciseForm.value?.textSelected),
  highlightedRectangles: computed(() => exerciseForm.value?.highlightedRectangles),
})
</script>

<template>
  <TwoResizableColumns>
    <template #left>
      <h1>{{ $t('edition') }}</h1>
      <ExerciseForm
        ref="exerciseForm"
        :project
        :textbook
        :textbookPage="page"
        :section
        :pdf
        :number="exercise?.attributes.number || ''"
        :automaticNumber="false"
        :editMode="true"
        :exercise
        @saved="saved"
        v-slot="{ disabled, save }"
      >
        <RouterLink class="btn btn-secondary" :to="{name: 'project-textbook-page-list-exercises'}">{{ $t('cancel') }}</RouterLink>
        <BButton primary :disabled @click="save">{{ $t('save') }}</BButton>
      </ExerciseForm>
    </template>
    <template #right>
      <div class="h-100 d-flex flex-column">
        <h1>{{ $t('adaptation') }}</h1>
        <iframe class="flex-fill w-100" :src="exerciseForm?.adaptationUrl"></iframe>
      </div>
    </template>
  </TwoResizableColumns>
</template>
