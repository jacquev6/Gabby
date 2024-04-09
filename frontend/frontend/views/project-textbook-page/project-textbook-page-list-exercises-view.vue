<script setup>
import { ref, reactive, computed } from 'vue'
import { useRouter } from 'vue-router'
import { computedAsync } from '@vueuse/core'

import { useApiStore } from '../../stores/api'
import { usePdfsStore } from '../../stores/pdfs'
import { BBusy, BRow, BCol, BButton } from '../../components/opinion/bootstrap'
import PdfRenderer from '../../components/pdf-renderer.vue'
import PdfNavigationControls from '../../components/pdf-navigation-controls.vue'
import SectionEditor from './section-editor.vue'
import ExercisesList from './exercises-list.vue'
import PdfNotLoaded from './pdf-not-loaded.vue'


const props = defineProps({
  project: {type: Object, required: true},
  textbook: {type: Object, required: true},
  page: {type: Number, required: true},
})

const router = useRouter()
const api = useApiStore()
const pdfs = usePdfsStore()

const sectionEditor = ref(null)

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

const deletingExercise = ref(false)
const refreshCounter = ref(1)

const needsBoundingRectangle = ref(false)
const currentExercise = reactive({})
const extractionEvents = reactive([])

function switchToListMode() {
  needsBoundingRectangle.value = false
  currentExercise.id = null
  extractionEvents.splice(0)
  currentExercise.attributes = {}
  ++refreshCounter.value
}

async function deleteExercise(exercise) {
  deletingExercise.value = true
  await api.client.delete('exercise', exercise.id)
  deletingExercise.value = false
  switchToListMode()
}

switchToListMode()

function changePage(page) {
  console.assert(Number.isInteger(page) && page >= 1 && page <= textbookPagesCount.value)
  router.push({name: 'project-textbook-page-list-exercises', params: {projectId: props.project.id, textbookId: props.textbook.id, page}})
}
</script>

<template>
  <b-row>
    <b-col>
      <pdf-navigation-controls :page @update:page="changePage" :pagesCount="textbookPagesCount">
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
      <b-busy :busy="deletingExercise">
        <exercises-list :textbook :page >
          <template v-slot="{exercise}">
            <router-link class="btn btn-primary btn-sm" :to="{name: 'project-textbook-page-edit-exercise', params: {exerciseId: exercise.id}}">{{ $t('edit') }}</router-link>
            <b-button secondary sm @click="deleteExercise(exercise)">{{ $t('delete') }}</b-button>
          </template>
        </exercises-list>
        <p class="d-grid">
          <router-link class="btn btn-primary" :to="{name: 'project-textbook-page-create-exercise'}">
            {{ $t('create') }}
          </router-link>
        </p>
      </b-busy>
    </b-col>
    <b-col>
      <h1>{{ $t('visualization') }}</h1>
    </b-col>
  </b-row>
</template>
