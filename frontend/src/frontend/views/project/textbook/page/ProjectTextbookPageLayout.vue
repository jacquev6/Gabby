<script setup lang="ts">
import { ref, computed } from 'vue'
import { computedAsync } from '@vueuse/core'

import { usePdfsStore } from '$frontend/stores/pdfs'
import { BBusy, BButton } from '$frontend/components/opinion/bootstrap'
import PdfNavigationControls from '$frontend/components/PdfNavigationControls.vue'
import PdfNotLoaded from './PdfNotLoaded.vue'
import PdfRenderer from '$frontend/components/PdfRenderer.vue'
import SectionEditor from './SectionEditor.vue'
import TextPicker from './TextPicker.vue'
import RectanglesHighlighter from './RectanglesHighlighter.vue'
import TwoResizableColumns from '$frontend/components/TwoResizableColumns.vue'
import { useApiStore, type Project, type Textbook } from '$frontend/stores/api'
import { makeExerciseCreationHistory } from './ExerciseCreationHistory'
import type { Rectangle } from './RectanglesHighlighter.vue'


const props = defineProps<{
  project: Project,
  refreshProject(): void,
  textbook: Textbook,
  refreshTextbook(): void,
  page: number,
}>()

const pdfs = usePdfsStore()
const api = useApiStore()

const component = ref<{
  changePage?: any/* @todo Type */,
  greyRectangles: Rectangle[],
  surroundedRectangles: Rectangle[],
  textSelected?: any/* @todo Type */,
  handlesScrolling: boolean,
} | null>(null)
const sectionEditor = ref<typeof SectionEditor | null>(null)
const pdfRenderer = ref<typeof PdfRenderer | null>(null)

// @todo(Feature, soon) Get the number of pages from the textbook itself
const textbookPagesCount = computed(() => {
  console.assert(props.textbook.relationships !== undefined)

  let c = 1
  for (const section of props.textbook.relationships.sections) {
    console.assert(section.attributes !== undefined)
    c = Math.max(c, section.attributes.textbookStartPage + section.attributes.pagesCount - 1)
  }
  return c
})

const section = computed(() => {
  console.assert(props.textbook.relationships !== undefined)

  for (const section of props.textbook.relationships.sections) {
    console.assert(section.attributes !== undefined)
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
      const pageNumber = section.value.attributes!.pdfFileStartPage + props.page - section.value.attributes!.textbookStartPage
      if (pdfs.getInfo(section.value.relationships!.pdfFile.id)) {
        const document = await pdfs.getDocument(section.value.relationships!.pdfFile.id)
        // WARNING: no reactivity to dependencies accessed after this first await (https://vueuse.org/core/computedAsync/#caveats)
        const page = await document?.getPage(pageNumber)
        const textContent = []
        if (page) {
          for (const item of (await page.getTextContent()).items) {
            console.assert('str' in item)

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

const exercises = computed(() => api.auto.getAll(
  'exercise',
  {filters: {'textbook': props.textbook.id, 'textbookPage': props.page.toString()}}
))

const componentHandlesScrolling = computed(() => component.value?.handlesScrolling ?? false)

const class_ = computed(() => componentHandlesScrolling.value ? 'overflow-hidden' : 'overflow-auto')

const exerciseCreationHistory = makeExerciseCreationHistory()

defineExpose({
  title: computed(() => [`Page ${props.page}`]),
  breadcrumbs: computed(() => []),
  handlesScrolling: true,
})
</script>

<template>
  <TwoResizableColumns saveKey="projectTextbookPage-1" rightWidth="2fr" :snap="250" class="h-100 overflow-hidden">
    <template #left>
      <div class="h-100 overflow-hidden d-flex flex-column">
        <PdfNavigationControls :page @update:page="component?.changePage" :disabled="!component?.changePage" :pagesCount="textbookPagesCount">
          <BButton secondary sm :disabled="!section" @click="sectionEditor!.show(section!.id)">&#9881;</BButton>
        </PdfNavigationControls>
        <SectionEditor ref="sectionEditor" />
        <template v-if="section">
          <BBusy size="7rem" :busy="pdfLoading" class="flex-fill overflow-auto" data-cy="pdf-container">
            <template v-if="pdf?.page">
              <div style="border: 1px solid black">
                <PdfRenderer
                  ref="pdfRenderer"
                  :page="pdf.page"
                  class="img w-100"
                />
                <RectanglesHighlighter
                  v-if="pdfRenderer?.transform && component"
                  class="img w-100" style="position: absolute; top: 0; left: 0"
                  :width="pdfRenderer.width" :height="pdfRenderer.height" :transform="pdfRenderer.transform"
                  :greyRectangles="component.greyRectangles" :surroundedRectangles="component.surroundedRectangles"
                />
                <TextPicker
                  v-if="pdfRenderer?.transform && component?.textSelected"
                  class="img w-100" style="position: absolute; top: 0; left: 0"
                  :width="pdfRenderer.width" :height="pdfRenderer.height" :transform="pdfRenderer.transform"
                  :textContent="pdf.textContent"
                  @text-selected="component?.textSelected"
                />
              </div>
            </template>
            <template v-else>
              <PdfNotLoaded :name="section.relationships!.pdfFile.relationships!.namings[0].attributes!.name" />
            </template>
          </BBusy>
        </template>
        <template v-else>
          <p>{{ $t('pageNoKnown') }}</p>
        </template>
      </div>
    </template>
    <template #right>
      <div class="h-100" :class="class_" data-cy="right-col-1">
        <RouterView v-slot="{ Component }">
          <component :is="Component" ref="component" :project :textbook :pdf :section :page :exercises :exerciseCreationHistory></component>
        </RouterView>
      </div>
    </template>
  </TwoResizableColumns>
</template>
