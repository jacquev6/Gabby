<script setup>
import { ref, reactive, computed } from 'vue'

import { useApiStore } from '../../stores/api'
import { BBusy, BRow, BCol, BButton } from '../../components/opinion/bootstrap'
import ExerciseForm from './exercise-form-with-injection.vue'


const props = defineProps({
  project: {type: Object, required: true},
  textbook: {type: Object, required: true},
  pdf: {required: true},
  section: {type: Object, required: true},
  page: {type: Number, required: true},
})

const api = useApiStore()

const creatingExercise = ref(false)

const needsBoundingRectangle = ref(false)
const currentExercise = reactive({})
const extractionEvents = reactive([])

function switchToListMode() {
  needsBoundingRectangle.value = false
  currentExercise.id = null
  extractionEvents.splice(0)
  currentExercise.attributes = {}
}

function switchToCreateMode(incrementNumber) {
  needsBoundingRectangle.value = true
  currentExercise.id = null
  extractionEvents.splice(0)

  const number = (() => {
    const prevNumber = currentExercise.attributes.number
    if (incrementNumber && Number.isInteger(+prevNumber)) {
      const number = (+prevNumber + 1).toString()
      extractionEvents.push({kind: 'ExerciseNumberSetAutomatically', value: number})
      return number
    } else {
      return ''
    }
  })()

  currentExercise.attributes = {
    number,
    instructions: '',
    example: '',
    clue: '',
    wording: '',
  }
}

const exerciseForm = ref(null)
function textSelected(text, point, textItems, rectangle) {
  if (needsBoundingRectangle.value) {
    extractionEvents.push({
      kind: "BoundingRectangleSelectedInPdf",
      pdf: {
        name: props.section.relationships.pdfFile.relationships.namings[0].attributes.name,
        sha256: props.section.relationships.pdfFile.id,
        page: props.pdf.page.pageNumber,
        rectangle,
      },
    })
    needsBoundingRectangle.value = false
  } else {
    extractionEvents.push({
      kind: "TextSelectedInPdf",
      pdf: {
        name: props.section.relationships.pdfFile.relationships.namings[0].attributes.name,
        sha256: props.section.relationships.pdfFile.id,
        page: props.pdf.page.pageNumber,
        rectangle,
      },
      value: text,
      textItems,
    })
    exerciseForm.value?.textSelected(text, point)
  }
}

async function createExercise() {
  creatingExercise.value = true
  const exercise = await api.client.post(
    'exercise',
    {...currentExercise.attributes, textbookPage: props.page},
    {
      project: {type: 'project', id: props.project.id},
      textbook: {type: 'textbook', id: props.textbook.id},
    },
  )
  for (const event of extractionEvents) {
    await api.client.post(
      'extractionEvent',
      {event: JSON.stringify(event)},
      {exercise: {type: 'exercise', id: exercise.id}},
    )
  }
  switchToCreateMode(true)
  creatingExercise.value = false
}

switchToListMode()
switchToCreateMode()

const visualizationUrl = computed(() => {
  const data = {exercises: {a: {...currentExercise.attributes, adaptation: {type: 'selectWords', colors: 3}}}}
  return `/adapted?data=${JSON.stringify(data)}&exerciseId=a`
})

defineExpose({
  textSelected,
})
</script>

<template>
  <b-row>
    <b-col>
      <h1>{{ $t('edition') }}</h1>
      <b-busy :busy="creatingExercise">
        <div style="position: relative">
          <ExerciseForm
            ref="exerciseForm"
            :fixedNumber="false"
            v-model="currentExercise.attributes"
            @extractionEvent="(event) => extractionEvents.push(event)"
          />
          <div v-if="needsBoundingRectangle" style="position: absolute; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.8);" class="text-center">
            <div style="position: absolute; left: 25%; top: 25%; width: 50%; height: 50%; background-color: white">
              <p>Merci de commencer par dessiner un rectangle autour de l'exercice entier.</p>
              <b-button sm secondary @click="needsBoundingRectangle = false">Passer cette étape</b-button>
            </div>
          </div>
        </div>
        <div class="mb-3">
          <router-link class="btn btn-secondary" :to="{name: 'project-textbook-page-list-exercises'}">{{ $t('cancel') }}</router-link>
          <b-button primary type="text" @click="createExercise" :disabled="currentExercise.attributes.number === ''">{{ $t('save.next') }}</b-button>
        </div>
      </b-busy>
    </b-col>
    <b-col>
      <h1>{{ $t('visualization') }}</h1>
      <iframe :src="visualizationUrl" style="width: 100%; height: 100%"></iframe>
    </b-col>
  </b-row>
</template>
