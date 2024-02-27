<script setup>
import { ref, reactive, watch, computed } from 'vue'
import { useRouter } from 'vue-router'
import { computedAsync } from '@vueuse/core'
import { useApiStore } from '@/stores/api'
import { usePdfsStore } from '@/stores/pdfs'

import { BRow, BCol, BButton } from '../components/bootstrap'
import PdfRenderer from '../components/PdfRenderer.vue'
import Loading from '../components/Loading.vue'
import ExerciseForm from '../components/ExerciseForm.vue'
import TextPicker from '@/components/TextPicker.vue'


const props = defineProps({
  textbookId: {
    type: String,
    required: true,
  },
  page: {
    type: Number,
    required: true,
  },
})

// @todo(Feature, now) Set title according to props
// @todo(Feature, now) Set navbar according to props

const router = useRouter()
const api = useApiStore()
const pdfs = usePdfsStore()

const textbookLoading = ref(false)
const textbook = computedAsync(
  async () => {
    return await api.client.get_one('textbook', props.textbookId, {include: 'sections.pdfFile.namings'})
  },
  null,
  textbookLoading,
)

// @todo(Feature, soon) Get the number of pages from the textbook itself
const textbookPagesCount = computed(() => {
  let c = 1
  for (const section of textbook.value?.relationships.sections || []) {
    c = Math.max(c, section.attributes.textbookStartPage + section.attributes.pagesCount - 1)
  }
  return c
})

const section = computed(() => {
  for (const section of textbook.value?.relationships.sections || []) {
    if (props.page >= section.attributes.textbookStartPage && props.page < section.attributes.textbookStartPage + section.attributes.pagesCount) {
      return section
    }
  }
  return null
})

const pdfLoading = ref(false)
const pdf = computedAsync(
  async () => {
    if (section.value) {
      const page = section.value.attributes.pdfFileStartPage + props.page - section.value.attributes.textbookStartPage
      const pdf = await pdfs.get(section.value.relationships.pdfFile.id)
      const document = pdf?.document
      const textContent = []
      if (document) {
        // @todo(Project management, now) getPage in a single place (currently, here and in the PdfRenderer)
        const pdfPage = await document.getPage(page)
        for (const item of (await pdfPage.getTextContent()).items) {
          textContent.push({
            str: item.str,

            font: item.fontName,

            left: item.transform[4],
            width: item.width,
            right: item.transform[4] + item.width,
            bottom: item.transform[5],
            height: item.height,
            top: item.transform[5] + item.height,
          })
        }
      }
      return {document, page, textContent}
    } else {
      return null
    }
  },
  null,
  pdfLoading,
)

const pdfRenderer = ref(null)

const mode = ref('list')
const refreshCounter = ref(1)

const loadingExercises = ref(false)
const exercisesOnPage = computedAsync(
  async () => {
    if (refreshCounter.value !== 0) {
      refreshCounter.value = 1
    }
    if (mode.value === 'list') {
      return await api.client.get_all('exercises', {filter: {textbook: props.textbookId, page: props.page}})
    } else {
      return []
    }
  },
  [],
  loadingExercises,
)

const currentExercise = reactive({})

const disablePrevPage = computed(() => {
  return mode.value !== 'list' || props.page <= 1
})

const disableNextPage = computed(() => {
  return mode.value !== 'list' || props.page >= textbookPagesCount.value
})

const disableSetPage = computed(() => {
  return mode.value !== 'list'
})

async function switchToListMode() {
  currentExercise.attributes = {}
  currentExercise.id = null
  mode.value = 'list'
  ++refreshCounter.value
}

function ellipsis(s) {
  return s.length > 25 ? s.slice(0, 25) + '…' : s
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

const exerciseForm = ref(null)
function textSelected(text, point) {
  exerciseForm.value?.textSelected(text, point)
}

async function createExercise() {
  await api.client.post(
    'exercise',
    {page: props.page, ...currentExercise.attributes},
    {textbook: {type: 'textbook', id: props.textbookId}},
  )
}

async function updateExercise() {
  await api.client.patch('exercise', currentExercise.id, currentExercise.attributes, {})
}

async function deleteExercise(exercise) {
  await api.client.delete('exercise', exercise.id)
}

const requestedPage = ref(props.page)
watch(() => props.page, (n) => {
  requestedPage.value = n
  switchToListMode()
}, {immediate: true})
watch(requestedPage, (requested) => {
  const page = Number.parseInt(requested, 10)
  if (Number.isInteger(page) && page >= 1 && page <= textbookPagesCount.value) {
    router.push({name: 'textbook-page', params: {textbookId: props.textbookId, page}})
  }
})
</script>

<template>
  <loading size="7rem" :loading="textbookLoading">
    <b-row>
      <b-col>
        <p>@todo(Feature, now) Add a "settings" link that opens a dialog to edit the section and the number of pages in the textbook</p>
        <p class="text-center">
          <router-link :to="{name: 'textbook-page', params: {textbookId, page: page - 1}}" custom v-slot="{ navigate }" >
            <b-button sm primary :disabled="disablePrevPage" @click="navigate">&lt;</b-button>
          </router-link>
          <label>{{ $t('Page') }} <input class="number-no-spin" v-model="requestedPage" type="number" min="1" :max="textbookPagesCount" :disabled="disableSetPage" @blur="requestedPage = page"/> {{ $t('pageOver', textbookPagesCount) }}</label>
          <router-link :to="{name: 'textbook-page', params: {textbookId, page: page + 1}}" custom v-slot="{ navigate }" >
            <b-button sm primary :disabled="disableNextPage" @click="navigate">&gt;</b-button>
          </router-link>
        </p>
        <template v-if="section">
          <loading size="7rem" :loading="pdfLoading">
            <template v-if="pdf?.document">
              <div style="border: 1px solid black">
                <pdf-renderer
                  ref="pdfRenderer"
                  :pdf="pdf.document" :page="pdf.page"
                  class="img img-fluid"
                />
                <text-picker
                  v-if="mode !== 'list'"
                  class="img img-fluid" style="position: absolute; top: 0; left: 0"
                  :width="pdfRenderer.width" :height="pdfRenderer.height" :transform="pdfRenderer.transform"
                  :textContent="pdf.textContent"
                  @text-selected="textSelected"
                />
              </div>
            </template>
            <template v-else>
              <p>Le PDF contenant cette page ({{ section.relationships.pdfFile.relationships.namings[0].attributes.name }}) n'a pas encore été ouvert.</p>
              <p>@todo(Feature, soon) Display all names known for this PDF</p>
              <p>@todo(Feature, soon) Let user open PDF from here</p>
              <p>@todo(Project management, later) Remove this button: <button @click="pdfs.load('/test.pdf')">Load test.pdf</button></p>
            </template>
          </loading>
        </template>
        <template v-else>
          <p>Aucun PDF enregistré ne contient cette page.</p>
          <p>@todo(Feature, soon) Let user associate PDF to page from here</p>
        </template>
      </b-col>
      <b-col>
        <h1>{{ $t('edition') }}</h1>
        <template v-if="mode === 'list'">
          <loading :loading="loadingExercises">
            <template v-if="exercisesOnPage.length">
              <p>{{ $t('existingExercises') }}</p>
              <ul>
                <li v-for="exercise in exercisesOnPage">
                  <strong>{{ exercise.attributes.number }}</strong> {{ ellipsis(exercise.attributes.instructions) }}
                  <button class="btn btn-primary btn-sm" @click="switchToEditMode(exercise)">{{ $t('edit') }}</button>
                  <button class="btn btn-secondary btn-sm" @click="deleteExercise(exercise).then(switchToListMode)">{{ $t('delete') }}</button>
                </li>
              </ul>
            </template>
            <p v-else>{{ $t('noExercises') }}</p>
          </loading>
          <div class="d-grid gap-2">
            <button class="btn btn-primary" @click="switchToCreateMode('')">{{ $t('create') }}</button>
          </div>
        </template>
        <template v-else>
          <ExerciseForm
            ref="exerciseForm"
            :fixedNumber="mode === 'edit'"
            v-model="currentExercise.attributes"
          />
          <div v-if="mode === 'create'" class="mb-3">
            <button class="btn btn-secondary" type="text" @click="switchToListMode()">{{ $t('cancel') }}</button>
            <button class="btn btn-primary" type="text" @click="createExercise().then(() => switchToCreateMode(currentExercise.attributes.number + 1))" :disabled="currentExercise.attributes.number === ''">{{ $t('save.next') }}</button>
          </div>
          <div v-else-if="mode === 'edit'" class="mb-3">
            <button class="btn btn-secondary" type="text" @click="switchToListMode()">{{ $t('cancel') }}</button>
            <button class="btn btn-primary" type="text" @click="updateExercise().then(switchToListMode)">{{ $t('save') }}</button>
          </div>
        </template>
      </b-col>
      <b-col>
        <h1>{{ $t('visualization') }}</h1>
        <p>({{ $t('not-yet-implemented') }})</p>
        <template v-if="mode !== 'list'">
          <!-- @todo(Feature, later) Retrieve from the back-end -->
          <p>{{ $t('instructions') }}:</p>
          <p>{{ currentExercise.attributes.instructions }}</p>
          <p>{{ $t('example') }}:</p>
          <p>{{ currentExercise.attributes.example }}</p>
          <p>{{ $t('clue') }}:</p>
          <p>{{ currentExercise.attributes.clue }}</p>
          <p>{{ $t('wording') }}:</p>
          <p>{{ currentExercise.attributes.wording }}</p>
        </template>
      </b-col>
    </b-row>
  </loading>
</template>

<style>
/* https://www.w3schools.com/howto/howto_css_hide_arrow_number.asp */
input.number-no-spin {
  -moz-appearance: textfield;
}
input.number-no-spin::-webkit-outer-spin-button,
input.number-no-spin::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
</style>
