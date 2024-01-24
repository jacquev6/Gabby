<script setup>
import { ref, reactive, watch } from 'vue'

import AboutModal from './components/AboutModal.vue'
import ExerciseForm from './components/ExerciseForm.vue'
import PdfPicker from './components/PdfPicker.vue'


const pdfMaxWidth = ref(null)
const pdfMaxHeight = ref(null)
function onResize() {
  pdfMaxWidth.value = window.innerWidth * 0.4
  pdfMaxHeight.value = window.innerHeight
}
onResize()
window.addEventListener('resize', onResize);

const pdf = ref('/test.pdf')
const pdfName = ref(null)
const pdfSha1 = ref(null)
const pdfPageNumber = ref(null)
const pdfPagesCount = ref(null)

function pdfDisplayed(name, sha1, pagesCount, pageNumber) {
  pdfName.value = name
  pdfSha1.value = sha1
  pdfPagesCount.value = pagesCount
  pdfPageNumber.value = pageNumber
}

// The PdfPicker doesn't rely on this clamping logic:
// this is just to avoid a flash when the user selects an out-of-range page number.
watch(pdfPageNumber, () => {
  if (pdfPageNumber.value < 1) {
    pdfPageNumber.value = 1
  } else if (pdfPageNumber.value > pdfPagesCount.value) {
    pdfPageNumber.value = pdfPagesCount.value
  }
})

const exercisesOnPage = reactive([])
const mode = ref(null)
const exerciseForm = ref(null)
const fields = ['instructions', 'example', 'clue', 'wording']
const currentExercise = reactive({})

async function switchToListMode() {
  currentExercise.attributes = {}
  currentExercise.id = null
  mode.value = 'list'

  exercisesOnPage.splice(0, exercisesOnPage.length)
  var next = `/api/exercises?filter[pdfPage]=${pdfPageNumber.value}&filter[pdfSha1]=${pdfSha1.value}&sort=number`
  while (next) {
    const r = await (await fetch(next)).json()
    exercisesOnPage.splice(exercisesOnPage.length, 0, ...r.data)
    next = r.links.next
  }
}

function switchToCreateMode(number) {
  currentExercise.attributes = {
    number,
    instructions: '',
    example: '',
    clue: '',
    wording: '',
  }
  currentExercise.id = null
  mode.value = 'create'
}

function switchToEditMode(e) {
  currentExercise.id = e.id
  currentExercise.attributes = e.attributes
  mode.value = 'edit'
}

watch([pdfSha1, pdfPageNumber], switchToListMode)

function textSelected(text, point) {
  exerciseForm.value?.textSelected(text, point)
}

async function createExercise() {
  await fetch(
    '/api/exercises',
    {
      method: 'POST',
      headers: {
        'content-type': 'application/vnd.api+json',
      },
      body: JSON.stringify({
        data: {
          type: 'exercise',
          id: null,
          attributes: {
            pdfSha1: pdfSha1.value,
            pdfPage: pdfPageNumber.value,
            ...currentExercise.attributes,
          },
        }
      }),
    },
  )
}

async function updateExercise() {
  await fetch(
    `/api/exercises/${currentExercise.id}`,
      {
      method: 'PATCH',
      headers: {
        'content-type': 'application/vnd.api+json',
      },
      body: JSON.stringify({
        data: {
          type: 'exercise',
          id: currentExercise.id,
          attributes: {
            pdfSha1: pdfSha1.value,
            pdfPage: pdfPageNumber.value,
            ...currentExercise.attributes,
          },
        }
      }),
    },
  )
}

async function deleteExercise(exercise) {
  await fetch(
    `/api/exercises/${exercise.id}`,
    {
      method: 'DELETE',
    },
  )
}
</script>

<template>
  <PdfPicker
    style="float: left"
    :pdf="pdf"
    :page="pdfPageNumber"
    :maxWidth="pdfMaxWidth"
    :maxHeight="pdfMaxHeight"
    @displayed="pdfDisplayed"
    @text-selected="textSelected"
  />

  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand"><img src="/favicon.ico" alt="Logo" width="30" height="24" class="d-inline-block align-text-top">Gabby</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0"></ul>
        <div class="d-flex">
          <button type="button" class="btn btn-secondary" data-bs-toggle="modal" data-bs-target="#aboutModal">{{ $t('about') }}</button>
          <select v-model="$i18n.locale">
            <option v-for="locale in $i18n.availableLocales" :key="locale" :value="locale">{{ {'en': '🇺🇸 English (US)', 'fr': '🇫🇷 Français'}[locale] }}</option>
          </select>
        </div>
      </div>
    </div>
  </nav>

  <div class="container-fluid">
    <div class="row">
      <div class="col">
        <h2>{{ $t('edition') }}</h2>
        <div class="mb-3">
          <label class="form-label">{{ $t('inputFile') }}</label>
          <input class="form-control" type="file" :disabled="mode !== 'list'" @change="(e) => { pdf = e.target.files[0] }" />
        </div>

        <div class="mb-3">
          <label class="form-label">{{ $t('pageOver', {count : pdfPagesCount}) }}</label>
          <input class="form-control" type="number" :disabled="mode !== 'list'" v-model="pdfPageNumber" />
        </div>

        <template v-if="mode === 'list'">
          <template v-if="exercisesOnPage.length">
            <p>{{ $t('existingExercises') }}</p>
            <ul>
              <li v-for="exercise in exercisesOnPage">
                {{ exercise.attributes.number }} <button class="btn btn-primary" @click="switchToEditMode(exercise)">{{ $t('edit') }}</button> <button class="btn btn-secondary" @click="deleteExercise(exercise).then(switchToListMode)">{{ $t('delete') }}</button></li>
            </ul>
          </template>
          <p><button class="btn btn-primary" @click="switchToCreateMode(null)">{{ $t('create') }}</button></p>
        </template>
        <template v-else-if="mode !== null">
          <div class="mb-3">
            <label class="form-label">{{ $t('exerciseNumber') }}</label>
            <input class="form-control" type="number" v-model="currentExercise.attributes.number" :disabled="mode === 'edit'"/>
          </div>
          <ExerciseForm
            ref="exerciseForm"
            :fields="fields"
            :pdfSha1="pdfSha1"
            :pdfPage="pdfPageNumber"
            v-model="currentExercise.attributes"
          />
          <div v-if="mode === 'create'" class="mb-3">
            <button class="btn btn-secondary" type="text" @click="switchToListMode()">{{ $t('cancel') }}</button>
            <button class="btn btn-primary" type="text" @click="createExercise().then(() => switchToCreateMode(currentExercise.attributes.number + 1))" :disabled="currentExercise.attributes.number === null">{{ $t('save.next') }}</button>
          </div>
          <div v-else-if="mode === 'edit'" class="mb-3">
            <button class="btn btn-secondary" type="text" @click="switchToListMode()">{{ $t('cancel') }}</button>
            <button class="btn btn-primary" type="text" @click="updateExercise().then(switchToListMode)">{{ $t('save') }}</button>
          </div>
        </template>
      </div>
      <div class="col">
        <h2>{{ $t('visualization') }}</h2>
        <template v-if="mode === 'create' || mode === 'edit'">
          <p>({{ $t('not-yet-implemented') }})</p>
          <template  v-for="field in fields">
            <p>{{ $t(field) }}:</p>
            <p>{{ currentExercise.attributes[field] }}</p>
          </template>
        </template>
      </div>
    </div>
  </div>

  <AboutModal id="aboutModal" />
</template>
