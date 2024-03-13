<script setup>
import { ref, reactive, watch, computed } from 'vue'
import { useRouter } from 'vue-router'
import { computedAsync } from '@vueuse/core'

import { useApiStore } from '../../stores/api'
import { usePdfsStore } from '../../stores/pdfs'
import NavBarred from '../../components/NavBarred.vue'
import { BBusy, BRow, BCol, BButton } from '../../components/opinion/bootstrap'
import PdfRenderer from '../../components/PdfRenderer.vue'
import ExerciseForm from '../../components/ExerciseForm.vue'
import TextPicker from '../../components/TextPicker.vue'
import SectionEditor from '../../components/SectionEditor.vue'


const props = defineProps({
  projectId: {type: String, required: true},
  textbookId: {type: String, required: true},
  page: {type: Number, required: true},
})

// @todo(Feature, now) Set title according to props
// @todo(Feature, now) Set navbar according to props

const router = useRouter()
const api = useApiStore()
const pdfs = usePdfsStore()

const sectionEditor = ref(null)

const projectLoading = ref(false)
const project = computedAsync(
  async () => {
    return await api.client.getOne('project', props.projectId)
  },
  null,
  projectLoading,
)

const textbookLoading = ref(false)
const textbook = computedAsync(
  async () => {
    const textbook = await api.client.getOne('textbook', props.textbookId, {include: 'sections.pdfFile.namings'})
    if (textbook.relationships.project.id === props.projectId) {
      return textbook
    } else {
      return null
    }
  },
  null,
  textbookLoading,
)

// @todo(Feature, soon) Get the number of pages from the textbook itself
const textbookPagesCount = computed(() => {
  let c = 1
  for (const section of textbook.value?.relationships?.sections || []) {
    c = Math.max(c, section.attributes.textbookStartPage + section.attributes.pagesCount - 1)
  }
  return c
})

const section = computed(() => {
  for (const section of textbook.value?.relationships?.sections || []) {
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
      const pageNumber = section.value.attributes.pdfFileStartPage + props.page - section.value.attributes.textbookStartPage
      if (pdfs.getInfo(section.value.relationships.pdfFile.id)) {
        const document = await pdfs.getDocument(section.value.relationships.pdfFile.id)
        // WARNING: no reactivity to dependencies accessed after this first await (https://vueuse.org/core/computedAsync/#caveats)
        const page = await document?.getPage(pageNumber)
        const textContent = []
        if (page) {
          for (const item of (await page.getTextContent()).items) {
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
          return {page, textContent}
        }
      }
    }
    return null
  },
  null,
  pdfLoading,
)

const pdfRenderer = ref(null)

const mode = ref('list')
const modeIsLoading = ref(false)
const refreshCounter = ref(1)

const loadingExercises = ref(false)
const exercisesOnPage = computedAsync(
  async () => {
    if (refreshCounter.value !== 0) {
      refreshCounter.value = 1
    }
    if (mode.value === 'list') {
      return await api.client.getAll('exercises', {filter: {'textbook': props.textbookId, 'textbook_page': props.page}})
    } else {
      return []
    }
  },
  [],
  loadingExercises,
)

const currentExercise = reactive({})
const extractionEvents = reactive([])

const disablePrevPage = computed(() => {
  return mode.value !== 'list' || props.page <= 1
})

const disableNextPage = computed(() => {
  return mode.value !== 'list' || props.page >= textbookPagesCount.value
})

const disableSetPage = computed(() => {
  return mode.value !== 'list'
})

function switchToListMode() {
  currentExercise.id = null
  extractionEvents.splice(0)
  currentExercise.attributes = {}
  mode.value = 'list'
  ++refreshCounter.value
}

function ellipsis(s) {
  return s.length > 25 ? s.slice(0, 25) + '…' : s
}

function switchToCreateMode(incrementNumber) {
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
  mode.value = 'create'
}

function switchToEditMode(e) {
  currentExercise.id = e.id
  extractionEvents.splice(0)
  currentExercise.attributes = e.attributes
  mode.value = 'edit'
}

const exerciseForm = ref(null)
function textSelected(text, point, textItems, rectangle) {
  extractionEvents.push({
    kind: "TextSelectedInPdf",
    pdf: {
      name: section.value.relationships.pdfFile.relationships.namings[0].attributes.name,
      sha256: section.value.relationships.pdfFile.id,
      page: pdf.value.page.pageNumber,
      rectangle,
    },
    value: text,
    textItems,
  })
  exerciseForm.value?.textSelected(text, point)
}

async function createExercise() {
  modeIsLoading.value = true
  const exercise = await api.client.post(
    'exercise',
    {...currentExercise.attributes, textbook_page: props.page},
    {
      project: {type: 'project', id: props.projectId},
      textbook: {type: 'textbook', id: props.textbookId},
      extractionEvents: [],
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
  modeIsLoading.value = false
}

async function updateExercise() {
  modeIsLoading.value = true
  await api.client.patch('exercise', currentExercise.id, currentExercise.attributes, {})
  for (const event of extractionEvents) {
    await api.client.post(
      'extractionEvent',
      {event: JSON.stringify(event)},
      {exercise: {type: 'exercise', id: currentExercise.id}},
    )
  }
  switchToListMode()
  modeIsLoading.value = false
}

async function deleteExercise(exercise) {
  modeIsLoading.value = true
  await api.client.delete('exercise', exercise.id)
  modeIsLoading.value = false
  switchToListMode()
}

// @todo(Project management, soon) Factorize with 'PdfPreview' component
const requestedPage = ref(props.page)
watch(() => props.page, (n) => {
  requestedPage.value = n
  switchToListMode()
}, {immediate: true})
watch(requestedPage, (requested) => {
  const page = Number.parseInt(requested, 10)
  if (Number.isInteger(page) && page >= 1 && page <= textbookPagesCount.value) {
    router.push({name: 'project-textbook-page', params: {projectId: props.projectId, textbookId: props.textbookId, page}})
  }
})
</script>

<template>
  <nav-barred>
    <template #navbar v-if="project?.exists && textbook?.exists">{{ project.attributes.title }} - {{ textbook.attributes.title }}</template>
    <b-busy size="7rem" :busy="projectLoading || textbookLoading">
      <template v-if="project?.exists">
        <template v-if="textbook?.exists">
          <b-row>
            <b-col>
              <p class="text-center">
                <router-link :to="{name: 'project-textbook-page', params: {projectId, textbookId, page: page - 1}}" custom v-slot="{ navigate }" >
                  <b-button primary sm :disabled="disablePrevPage" @click="navigate">&lt;</b-button>
                </router-link>
                <label>{{ $t('Page') }} <input class="number-no-spin" v-model="requestedPage" type="number" min="1" :max="textbookPagesCount" :disabled="disableSetPage" @blur="requestedPage = page"/> {{ $t('pageOver', textbookPagesCount) }}</label>
                <router-link :to="{name: 'project-textbook-page', params: {projectId, textbookId, page: page + 1}}" custom v-slot="{ navigate }" >
                  <b-button primary sm :disabled="disableNextPage" @click="navigate">&gt;</b-button>
                </router-link>
                <b-button secondary sm :disabled="!section" @click="sectionEditor.show(section.id)">&#9881;</b-button>
              </p>
              <section-editor ref="sectionEditor" />
              <template v-if="section">
                <b-busy size="7rem" :busy="pdfLoading">
                  <template v-if="pdf?.page">
                    <div style="border: 1px solid black">
                      <pdf-renderer
                        ref="pdfRenderer"
                        :page="pdf.page"
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
                    <p>@todo(Project management, later) Remove this button: <button @click="pdfs.open({url: '/test.pdf'})">Load test.pdf</button></p>
                  </template>
                </b-busy>
              </template>
              <template v-else>
                <p>Aucun PDF enregistré ne contient cette page.</p>
                <p>@todo(Feature, soon) Let user associate PDF to page from here</p>
              </template>
            </b-col>
            <b-col>
              <h1>{{ $t('edition') }}</h1>
              <b-busy :busy="modeIsLoading">
                <template v-if="mode === 'list'">
                  <b-busy :busy="loadingExercises">
                    <template v-if="exercisesOnPage.length">
                      <p>{{ $t('existingExercises') }}</p>
                      <ul>
                        <li v-for="exercise in exercisesOnPage">
                          <strong>{{ exercise.attributes.number }}</strong> {{ ellipsis(exercise.attributes.instructions) }}
                          <b-button primary sm @click="switchToEditMode(exercise)">{{ $t('edit') }}</b-button>
                          <b-button secondary sm @click="deleteExercise(exercise)">{{ $t('delete') }}</b-button>
                        </li>
                      </ul>
                    </template>
                    <p v-else>{{ $t('noExercises') }}</p>
                  </b-busy>
                  <p class="d-grid"><b-button primary @click="switchToCreateMode(false)">{{ $t('create') }}</b-button></p>
                </template>
                <template v-else>
                  <ExerciseForm
                    ref="exerciseForm"
                    :fixedNumber="mode === 'edit'"
                    v-model="currentExercise.attributes"
                    @extractionEvent="(event) => extractionEvents.push(event)"
                  />
                  <div class="mb-3">
                    <b-button secondary type="text" @click="switchToListMode">{{ $t('cancel') }}</b-button>
                    <template v-if="mode === 'create'">
                      <b-button primary type="text" @click="createExercise" :disabled="currentExercise.attributes.number === ''">{{ $t('save.next') }}</b-button>
                    </template>
                    <template v-else-if="mode === 'edit'">
                      <b-button primary type="text" @click="updateExercise">{{ $t('save') }}</b-button>
                    </template>
                  </div>
                </template>
              </b-busy>
            </b-col>
            <b-col>
              <h1>{{ $t('visualization') }}</h1>
              <p>({{ $t('not-yet-implemented') }})</p>
            </b-col>
          </b-row>
        </template>
        <template v-else>
          <h1>{{ $t('textbookNotFound') }}</h1>
        </template>
      </template>
      <template v-else>
        <h1>{{ $t('projectNotFound') }}</h1>
      </template>
    </b-busy>
  </nav-barred>
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
</style>../../stores/api../../stores/pdfs../../components/opinion/bootstrap
