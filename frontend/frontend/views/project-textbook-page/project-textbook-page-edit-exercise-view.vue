<script setup>
import { ref, reactive, computed, watch } from 'vue'
import { useRouter } from 'vue-router'
import { computedAsync } from '@vueuse/core'

import { useApiStore } from '../../stores/api'
import { BBusy, BRow, BCol, BButton } from '../../components/opinion/bootstrap'
import ExerciseForm from '../../components/exercise-form.vue'


const props = defineProps({
  project: {type: Object, required: true},
  textbook: {type: Object, required: true},
  page: {type: Number, required: true},
  pdf: {required: true},
  section: {type: Object, required: true},
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

// const updatingExercise = ref(false)

// const currentExercise = reactive({})
// const extractionEvents = reactive([])

// function switchToListMode() {
//   currentExercise.id = null
//   extractionEvents.splice(0)
//   currentExercise.attributes = {}
// }

// function switchToEditMode(e) {
//   currentExercise.id = e.id
//   extractionEvents.splice(0)
//   currentExercise.attributes = e.attributes
// }

const exerciseForm = ref(null)
// function textSelected(text, point, textItems, rectangle) {
//   extractionEvents.push({
//     kind: "TextSelectedInPdf",
//     pdf: {
//       name: props.section.relationships.pdfFile.relationships.namings[0].attributes.name,
//       sha256: props.section.relationships.pdfFile.id,
//       page: props.pdf.page.pageNumber,
//       rectangle,
//     },
//     value: text,
//     textItems,
//   })
//   exerciseForm.value?.textSelected(text, point)
// }

// async function updateExercise() {
//   updatingExercise.value = true
//   await api.client.patch(
//     'exercise',
//     currentExercise.id,
//     {
//       instructions: currentExercise.attributes.instructions,
//       example: currentExercise.attributes.example,
//       clue: currentExercise.attributes.clue,
//       wording: currentExercise.attributes.wording,
//     },
//     {},
//   )
//   for (const event of extractionEvents) {
//     await api.client.post(
//       'extractionEvent',
//       {event: JSON.stringify(event)},
//       {exercise: {type: 'exercise', id: currentExercise.id}},
//     )
//   }
//   router.push({name: 'project-textbook-page-list-exercises'})
//   updatingExercise.value = false
// }

// switchToListMode()
// watch(exercise, () => {
//   if (exercise.value) {
//     switchToEditMode(exercise.value)
//   }
// })

function saved() {
  router.push({name: 'project-textbook-page-list-exercises'})
}

defineExpose({
  textSelected: computed(() => exerciseForm.value?.textSelected),
})
</script>

<template>
  <b-row>
    <b-col>
      <h1>{{ $t('edition') }}</h1>
      <exercise-form
        ref="exerciseForm"
        :project
        :textbook
        :textbookPage="page"
        :section
        :pdf
        :number="exercise?.attributes.number || ''"
        :automaticNumber="false"
        :fixedNumber="true"
        :exercise
        @saved="saved"
        v-slot="{ disabled, save }"
      >
        <router-link class="btn btn-secondary" :to="{name: 'project-textbook-page-list-exercises'}">{{ $t('cancel') }}</router-link>
        <b-button primary :disabled @click="save">{{ $t('save') }}</b-button>
      </exercise-form>
    </b-col>
    <b-col>
      <h1>{{ $t('adaptation') }}</h1>
      <iframe :src="exerciseForm?.adaptationUrl" style="width: 100%; height: 100%"></iframe>
    </b-col>
  </b-row>
</template>
