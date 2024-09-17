<script lang="ts">
import { computed, type Ref } from 'vue'

import { useApiStore } from '$frontend/stores/api'


const api = useApiStore()

export function useProjectTextbookPageData(
  projectId: Ref<string>,
  textbookId: Ref<string>,
  page: Ref<number>,
  displayedPage: Ref<number>,
) {
  const project = computed(() => api.auto.getOne('project', projectId.value))

  const textbook = computed(() => api.auto.getOne('textbook', textbookId.value, {include: ['sections.pdfFile.namings']}))

  const exercisesOnPage = computed(() => api.auto.getAll('exercise', {filters: {textbook: textbookId.value, textbookPage: page.value.toString()}}))

  const exercisesOnDisplayedPage = computed(() => api.auto.getAll('exercise', {filters: {textbook: textbookId.value, textbookPage: displayedPage.value.toString()}}))

  return {
    project,
    textbook,
    exercisesOnPage,
    exercisesOnDisplayedPage,
  }
}
</script>

<script setup lang="ts">
import { computedAsync } from '@vueuse/core'
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'

import { BBusy, BButton } from '$/frontend/components/opinion/bootstrap'
import { useGloballyBusyStore } from '$frontend/stores/globallyBusy'
import { usePdfsStore } from '$/frontend/stores/pdfs'
import bc, { type Breadcrumbs } from '$frontend/components/breadcrumbs'
import PdfNotLoaded from './PdfNotLoaded.vue'
import PdfRenderer from '$frontend/components/PdfRenderer.vue'
import ProjectLayout from '../../ProjectLayout.vue'
import SectionEditor from './SectionEditor.vue'
import TwoResizableColumns from '$frontend/components/TwoResizableColumns.vue'
import type { Project, Textbook } from '$frontend/stores/api'
import PdfNavigationControls from '$frontend/components/PdfNavigationControls.vue'


const props = defineProps<{
  project: Project
  textbook: Textbook
  page: number
  title: string[]
  breadcrumbs: Breadcrumbs
}>()

const displayedPage = defineModel<number>('displayedPage', {required: true})

const i18n = useI18n()
const globallyBusy = useGloballyBusyStore()
const pdfs = usePdfsStore()

globallyBusy.register('loading textbook', computed(() => props.textbook.loading))

const textbookBelongsToProject = computed(() => 
  props.textbook.inCache && props.textbook.exists && props.textbook.relationships.project === props.project
)

const title = computed(() => {
  if (props.textbook.loading) {
    return []
  } else if (props.textbook.inCache && props.textbook.exists && textbookBelongsToProject.value) {
    return [props.textbook.attributes.title, `Page ${props.page}`, ...props.title]
  } else {
    return [i18n.t('textbookNotFound')]
  }
})

const breadcrumbs = computed(() => {
  if (props.textbook.loading) {
    return bc.empty
  } else if (props.textbook.inCache && props.textbook.exists) {
    return bc.prepend(
      `${props.textbook.attributes.title}, page ${props.page}`,
      {name: 'project-textbook-page'},
      props.breadcrumbs,
    )
  } else {
    return bc.last(i18n.t('textbookNotFound'))
  }
})

// @todo(Feature, soon) Get the number of pages from the textbook itself
const textbookPagesCount = computed(() => {
  let c = 1
  if (props.textbook.inCache && props.textbook.exists) {
    for (const section of props.textbook.relationships.sections) {
      if(section.inCache && section.exists) {
        c = Math.max(c, section.attributes.textbookStartPage + section.attributes.pagesCount - 1)
      }
    }
  }
  return c
})

const sectionEditor = ref<InstanceType<typeof SectionEditor> | null>(null)

const section = computed(() => {
  if (props.textbook.inCache && props.textbook.exists) {
    for (const section of props.textbook.relationships.sections) {
      if(section.inCache && section.exists) {
        if (displayedPage.value >= section.attributes.textbookStartPage && displayedPage.value < section.attributes.textbookStartPage + section.attributes.pagesCount) {
          return section
        }
      }
    }
  }
  return null
})

const pdfRenderer = ref<InstanceType<typeof PdfRenderer> | null>(null)

const pdfLoading = ref(false)
const pdf = computedAsync(
  async () => {
    if (section.value) {
      const pageNumber = section.value.attributes.pdfFileStartPage + displayedPage.value - section.value.attributes.textbookStartPage
      if (pdfs.getInfo(section.value.relationships.pdfFile.id)) {
        const document = await pdfs.getDocument(section.value.relationships.pdfFile.id)
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
</script>

<template>
  <ProjectLayout
    :project
    :title :breadcrumbs :slotHandlesScrolling="true"
    #="{ project }"
  >
    <template v-if="textbook.inCache">
      <template v-if="textbook.exists && textbookBelongsToProject">
        <TwoResizableColumns saveKey="projectTextbookPage-1" rightWidth="2fr" :snap="250" class="h-100 overflow-hidden">
          <template #left>
            <div class="h-100 overflow-hidden d-flex flex-column">
              <PdfNavigationControls v-model:page="displayedPage" :pagesCount="textbookPagesCount">
                <BButton secondary sm :disabled="section === null" @click="console.assert(section !== null); sectionEditor?.show(section.id)">&#9881;</BButton>
              </PdfNavigationControls>
              <SectionEditor ref="sectionEditor" />
              <template v-if="section?.inCache && section.exists">
                <BBusy size="7rem" :busy="pdfLoading" showWhileBusy="afterNotBusy" class="flex-fill overflow-auto" data-cy="pdf-container">
                  <template v-if="pdf !== null">
                    <div style="border: 1px solid black">
                      <!--
                        @todo Fix the PdfRenderer. Form the console logs:
                        - it renders each page twice
                        - it fails an assertion when one changes the displayed page several times quickly
                      -->
                      <PdfRenderer
                        ref="pdfRenderer"
                        :page="pdf.page"
                        class="img w-100"
                      />
                      <template v-if="pdfRenderer">
                        <slot
                          name="pdfOverlay"
                          :project :textbook
                          :pdfFile="section.relationships.pdfFile" :pdf
                          :width="pdfRenderer.width" :height="pdfRenderer.height" :transform="pdfRenderer.transform"
                        ></slot>
                      </template>
                    </div>
                  </template>
                  <template v-else>
                    <PdfNotLoaded :name="
                      section.relationships.pdfFile.inCache
                      && section.relationships.pdfFile.exists
                      && section.relationships.pdfFile.relationships.namings.length > 0
                      && section.relationships.pdfFile.relationships.namings[0].inCache
                      && section.relationships.pdfFile.relationships.namings[0].exists
                      ? section.relationships.pdfFile.relationships.namings[0].attributes.name : ''" />
                  </template>
                </BBusy>
              </template>
              <template v-else>
                <p>{{ $t('pageNoKnown') }}</p>
              </template>
            </div>
          </template>
          <template #right>
            <div class="h-100 overflow-auto" data-cy="right-col-1">
              <slot :project :textbook :pdf></slot>
            </div>
          </template>
        </TwoResizableColumns>
      </template>
      <template v-else>
        <h1>{{ i18n.t('textbookNotFound') }}</h1>
      </template>
    </template>
  </ProjectLayout>
</template>
