<script setup>
import { ref, reactive, watch } from 'vue'

import AboutModal from './components/AboutModal.vue'
import ExerciseForm from './components/ExerciseForm.vue'
import PdfPicker from './components/PdfPicker.vue'


// @todo Handle API failures and slow-downs

const pdf = ref('/test.pdf')
const pdfName = ref(null)
const pdfSha256 = ref(null)
const pdfPageNumber = ref(null)
const pdfPagesCount = ref(null)
const pdfException = ref(null)

function pdfDisplayed(name, sha256, pagesCount, pageNumber) {
  pdfName.value = name
  pdfSha256.value = sha256
  pdfPagesCount.value = pagesCount
  // @todo This is not a great idea because when the user presses "up" a few times in the page selector,
  // we could end up changing the page back to an unwanted, intermediate, page.
  pdfPageNumber.value = pageNumber
  pdfException.value = null
}

function pdfLoadingFailed(e) {
  pdfName.value = null
  pdfSha256.value = null
  exercisesOnPage.splice(0, exercisesOnPage.length)
  pdfException.value = e
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
const mode = ref('list')
const exerciseForm = ref(null)
const currentExercise = reactive({})

async function switchToListMode() {
  currentExercise.attributes = {}
  currentExercise.id = null
  mode.value = 'list'

  exercisesOnPage.splice(0, exercisesOnPage.length)
  var next = `/api/exercises?filter[pdfPage]=${pdfPageNumber.value}&filter[pdfSha256]=${pdfSha256.value}&sort=number`
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

watch([pdfSha256, pdfPageNumber], switchToListMode)

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
            pdfSha256: pdfSha256.value,
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
            pdfSha256: pdfSha256.value,
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

function ellipsis(s) {
  return s.length > 25 ? s.slice(0, 25) + '…' : s
}
</script>

<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-4">
        <div class="row">
          <div class="col">
            <div class="mb-3">
              <!-- @todo Display a "loading" animation when loading a new PDF or navigating to another page, until the page is displayed, and the list of existing exercices is retrieved -->
              <label class="form-label">{{ $t('inputFile') }}</label>
              <input class="form-control" type="file" accept=".pdf" :disabled="mode !== 'list'" @change="(e) => { pdf = e.target.files[0] }" />
            </div>
          </div>
          <div class="col-3">
            <div class="mb-3">
              <label class="form-label">{{ $t('pageOver', {count : pdfPagesCount}) }}</label>
              <!-- @todo Debounce changes in pdfPageNumber: don't start a render for intermediate pages when the user presses "up" a few times in this field -->
              <input class="form-control" type="number" :disabled="pdfSha256 === null || mode !== 'list'" v-model="pdfPageNumber" />
            </div>
          </div>
        </div>
        <PdfPicker
          :pdf="pdf"
          :page="pdfPageNumber"
          :disabled="mode === 'list'"
          @loading-failed="pdfLoadingFailed"
          @displayed="pdfDisplayed"
          @text-selected="textSelected"
        />
      </div>

      <div class="col">
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
          <div class="container-fluid">
            <a class="navbar-brand"><img src="/logo-cartable-fantastique.png" alt="Logo Cartable Fantastique" width="30" height="24" class="d-inline-block align-text-top">MALIN</a>
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
        <div class="row">
          <div class="col">
            <h2>{{ $t('edition') }}</h2>
            <template v-if="pdfException !== null">
              <p>{{ $t('error.pdf') }}</p>
              <pre>{{ pdfException }}</pre>
            </template>
            <template v-else-if="mode === 'list'">
              <template v-if="exercisesOnPage.length">
                <p>{{ $t('existingExercises') }}</p>
                <ul>
                  <li v-for="exercise in exercisesOnPage">
                    <strong>{{ exercise.attributes.number }}</strong> {{ ellipsis(exercise.attributes.instructions) }}
                    <button class="btn btn-primary btn-sm" @click="switchToEditMode(exercise)">{{ $t('edit') }}
                    </button> <button class="btn btn-secondary btn-sm" @click="deleteExercise(exercise).then(switchToListMode)">{{ $t('delete') }}</button></li>
                </ul>
              </template>
              <div class="d-grid gap-2">
                <button class="btn btn-primary" @click="switchToCreateMode('')">{{ $t('create') }}</button>
              </div>
            </template>
            <template v-else>
              <ExerciseForm
                ref="exerciseForm"
                :pdfSha256="pdfSha256"
                :pdfPage="pdfPageNumber"
                :fixedNumber="mode === 'edit'"
                v-model="currentExercise.attributes"
              />
              <div v-if="mode === 'create'" class="mb-3">
                <button class="btn btn-secondary" type="text" @click="switchToListMode()">{{ $t('cancel') }}
                <!-- @todo How do I keep a space between buttons more explicitly than that? -->
                </button> <button class="btn btn-primary" type="text" @click="createExercise().then(() => switchToCreateMode(currentExercise.attributes.number + 1))" :disabled="currentExercise.attributes.number === ''">{{ $t('save.next') }}</button>
              </div>
              <div v-else-if="mode === 'edit'" class="mb-3">
                <button class="btn btn-secondary" type="text" @click="switchToListMode()">{{ $t('cancel') }}
                </button> <button class="btn btn-primary" type="text" @click="updateExercise().then(switchToListMode)">{{ $t('save') }}</button>
              </div>
            </template>
          </div>
          <div class="col">
            <h2>{{ $t('visualization') }}</h2>
            <template v-if="mode !== 'list'">
              <!-- @todo Retrieve from the back-end -->
              <p>({{ $t('not-yet-implemented') }})</p>
              <p>{{ $t('instructions') }}:</p>
              <p>{{ currentExercise.attributes.instructions }}</p>
              <p>{{ $t('example') }}:</p>
              <p>{{ currentExercise.attributes.example }}</p>
              <p>{{ $t('clue') }}:</p>
              <p>{{ currentExercise.attributes.clue }}</p>
              <p>{{ $t('wording') }}:</p>
              <p>{{ currentExercise.attributes.wording }}</p>
            </template>
          </div>
        </div>
      </div>
    </div>
  </div>

  <AboutModal id="aboutModal" />
</template>
