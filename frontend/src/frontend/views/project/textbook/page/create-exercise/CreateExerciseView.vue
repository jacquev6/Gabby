<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

import { BButton } from '../../../../../components/opinion/bootstrap'
import ExerciseForm from '../../../../../components/ExerciseForm.vue'
import TwoResizableColumns from '../../../../../components/TwoResizableColumns.vue'


const props = defineProps({
  project: {type: Object, required: true},
  textbook: {type: Object, required: true},
  pdf: {required: true},
  section: {required: true},
  page: {type: Number, required: true},
})

const router = useRouter()

const exerciseForm = ref(null)

const number = ref('')
const automaticNumber = ref(false)
function created(exercise, suggestedNumber) {
  number.value = suggestedNumber
  automaticNumber.value = true
}

function changePage(page) {
  router.push({name: 'project-textbook-page-create-exercise', params: {projectId: props.project.id, textbookId: props.textbook.id, page}})
}

defineExpose({
  changePage,
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
        :number
        :automaticNumber
        :editMode="false"
        @created="created"
        v-slot="{ disabled, create }"
      >
        <RouterLink class="btn btn-secondary" :to="{name: 'project-textbook-page-list-exercises'}">{{ $t('cancel') }}</RouterLink>
        <BButton primary :disabled @click="create">{{ $t('save.next') }}</BButton>
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
