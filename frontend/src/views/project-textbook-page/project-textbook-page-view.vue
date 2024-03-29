<script setup>
import { ref, reactive, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { computedAsync } from '@vueuse/core'

import { useApiStore } from '../../stores/api'
import { usePdfsStore } from '../../stores/pdfs'
import Layout from '../../components/layout.vue'
import { BBusy, BRow, BCol, BButton } from '../../components/opinion/bootstrap'
import PdfRenderer from '../../components/pdf-renderer.vue'
import PdfNavigationControls from '../../components/pdf-navigation-controls.vue'
import ExerciseForm from './exercise-form-with-injection.vue'
import TextPicker from './text-picker.vue'
import SectionEditor from './section-editor.vue'
import ExercisesList from './exercises-list.vue'
import PdfNotLoaded from './pdf-not-loaded.vue'


const props = defineProps({
  projectId: {type: String, required: true},
  textbookId: {type: String, required: true},
  page: {type: Number, required: true},
})

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

const breadcrumbs = computed(() => {
  if (project.value?.exists && textbook.value?.exists) {
    return [
      {title: project.value.attributes.title, to: {name: 'project', params: {projectId: props.projectId}}},
      {title: textbook.value.attributes.title},
    ]
  } else {
    return []
  }
})

const title = computed(() => {
  if (project.value?.exists && textbook.value?.exists) {
    return `MALIN - ${project.value?.attributes.title} - ${textbook.value?.attributes.title} - Page ${props.page}`
  } else {
    return 'MALIN'
  }
})

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

const needsBoundingRectangle = ref(false)
const currentExercise = reactive({})
const extractionEvents = reactive([])

const navigationDisabled = computed(() => {
  return mode.value !== 'list'
})

function switchToListMode() {
  needsBoundingRectangle.value = false
  currentExercise.id = null
  extractionEvents.splice(0)
  currentExercise.attributes = {}
  mode.value = 'list'
  ++refreshCounter.value
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
  mode.value = 'create'
}

function switchToEditMode(e) {
  needsBoundingRectangle.value = false
  currentExercise.id = e.id
  extractionEvents.splice(0)
  currentExercise.attributes = e.attributes
  mode.value = 'edit'
}

const exerciseForm = ref(null)
function textSelected(text, point, textItems, rectangle) {
  if (needsBoundingRectangle.value) {
    extractionEvents.push({
      kind: "BoundingRectangleSelectedInPdf",
      pdf: {
        name: section.value.relationships.pdfFile.relationships.namings[0].attributes.name,
        sha256: section.value.relationships.pdfFile.id,
        page: pdf.value.page.pageNumber,
        rectangle,
      },
    })
    needsBoundingRectangle.value = false
  } else {
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

onMounted(switchToListMode)

function changePage(page) {
  console.assert(Number.isInteger(page) && page >= 1 && page <= textbookPagesCount.value)
  router.push({name: 'project-textbook-page', params: {projectId: props.projectId, textbookId: props.textbookId, page}})
}
</script>

<template>
  <layout :title="title" :breadcrumbs="breadcrumbs">
    <b-busy size="7rem" :busy="projectLoading || textbookLoading">
      <template v-if="project?.exists">
        <template v-if="textbook?.exists">
          <b-row>
            <b-col>
              <pdf-navigation-controls :page @update:page="changePage" :pagesCount="textbookPagesCount" :disabled="navigationDisabled">
                <b-button secondary sm :disabled="!section" @click="sectionEditor.show(section.id)">&#9881;</b-button>
              </pdf-navigation-controls>
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
                    <pdf-not-loaded :name="section.relationships.pdfFile.relationships.namings[0].attributes.name" />
                  </template>
                </b-busy>
              </template>
              <template v-else>
                <p>{{ $t('pageNoKnown') }}</p>
                <!-- @todo Let user associate PDF to page from here -->
              </template>
            </b-col>
            <b-col>
              <h1>{{ $t('edition') }}</h1>
              <b-busy :busy="modeIsLoading">
                <template v-if="mode === 'list'">
                  <exercises-list :textbook :page >
                    <template v-slot="{exercise}">
                      <b-button primary sm @click="switchToEditMode(exercise)">{{ $t('edit') }}</b-button>
                      <b-button secondary sm @click="deleteExercise(exercise)">{{ $t('delete') }}</b-button>
                    </template>
                  </exercises-list>
                  <p class="d-grid"><b-button primary @click="switchToCreateMode(false)">{{ $t('create') }}</b-button></p>
                </template>
                <template v-else>
                  <div style="position: relative">
                    <ExerciseForm
                      ref="exerciseForm"
                      :fixedNumber="mode === 'edit'"
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
  </layout>
</template>
