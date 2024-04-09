<script setup>
import { ref, reactive, computed, watch } from 'vue'
import { useRouter } from 'vue-router'
import { computedAsync } from '@vueuse/core'

import { useApiStore } from '../../stores/api'
import { usePdfsStore } from '../../stores/pdfs'
import { BBusy, BRow, BCol, BButton } from '../../components/opinion/bootstrap'
import PdfRenderer from '../../components/pdf-renderer.vue'
import PdfNavigationControls from '../../components/pdf-navigation-controls.vue'
import ExerciseForm from './exercise-form-with-injection.vue'
import TextPicker from './text-picker.vue'
import SectionEditor from './section-editor.vue'
import PdfNotLoaded from './pdf-not-loaded.vue'


const props = defineProps({
  project: {type: Object, required: true},
  textbook: {type: Object, required: true},
  page: {type: Number, required: true},
  exerciseId: {type: String, required: true},
})

const router = useRouter()
const api = useApiStore()
const pdfs = usePdfsStore()

const sectionEditor = ref(null)

const exerciseLoading = ref(false)
const exercise = computedAsync(
  async () => {
    return await api.client.getOne('exercise', props.exerciseId)
  },
  null,
  exerciseLoading,
)

// @todo(Feature, soon) Get the number of pages from the textbook itself
const textbookPagesCount = computed(() => {
  let c = 1
  for (const section of props.textbook.relationships.sections) {
    c = Math.max(c, section.attributes.textbookStartPage + section.attributes.pagesCount - 1)
  }
  return c
})

const section = computed(() => {
  for (const section of props.textbook.relationships.sections) {
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

const updatingExercise = ref(false)

const currentExercise = reactive({})
const extractionEvents = reactive([])

function switchToListMode() {
  currentExercise.id = null
  extractionEvents.splice(0)
  currentExercise.attributes = {}
}

function switchToEditMode(e) {
  currentExercise.id = e.id
  extractionEvents.splice(0)
  currentExercise.attributes = e.attributes
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

async function updateExercise() {
  updatingExercise.value = true
  await api.client.patch(
    'exercise',
    currentExercise.id,
    {
      instructions: currentExercise.attributes.instructions,
      example: currentExercise.attributes.example,
      clue: currentExercise.attributes.clue,
      wording: currentExercise.attributes.wording,
    },
    {},
  )
  for (const event of extractionEvents) {
    await api.client.post(
      'extractionEvent',
      {event: JSON.stringify(event)},
      {exercise: {type: 'exercise', id: currentExercise.id}},
    )
  }
  router.push({name: 'project-textbook-page-list-exercises'})
  updatingExercise.value = false
}

switchToListMode()
watch(exercise, () => {
  if (exercise.value) {
    switchToEditMode(exercise.value)
  }
})

const visualizationUrl = computed(() => {
  if (currentExercise.id) {
    const data = {exercises: {a: {...currentExercise.attributes, adaptation: {type: 'selectWords', colors: 3}}}}
    return `/adapted?data=${JSON.stringify(data)}&exerciseId=a`
  } else {
    return null
  }
})
</script>

<template>
  <b-busy size="7rem" :busy="exerciseLoading">
    <b-row>
      <b-col>
        <pdf-navigation-controls :page :pagesCount="textbookPagesCount" disabled>
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
                  v-if="pdfRenderer"
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
        <b-busy :busy="updatingExercise">
          <ExerciseForm
            v-if="currentExercise.id"
            ref="exerciseForm"
            :fixedNumber="true"
            v-model="currentExercise.attributes"
            @extractionEvent="(event) => extractionEvents.push(event)"
          />
          <div class="mb-3">
            <router-link class="btn btn-secondary" :to="{name: 'project-textbook-page-list-exercises'}">{{ $t('cancel') }}</router-link>
            <b-button primary type="text" @click="updateExercise">{{ $t('save') }}</b-button>
          </div>
        </b-busy>
      </b-col>
      <b-col>
        <h1>{{ $t('visualization') }}</h1>
        <iframe :src="visualizationUrl" style="width: 100%; height: 100%"></iframe>
      </b-col>
    </b-row>
  </b-busy>
</template>
