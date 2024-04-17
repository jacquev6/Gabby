<script setup>
import { ref, computed } from 'vue'
import { computedAsync } from '@vueuse/core'

import { useApiStore } from '../../stores/api'
import { usePdfsStore } from '../../stores/pdfs'
import { BBusy, BRow, BCol, BButton } from '../../components/opinion/bootstrap'
import PdfNavigationControls from '../../components/pdf-navigation-controls.vue'
import PdfNotLoaded from './pdf-not-loaded.vue'
import PdfRenderer from '../../components/pdf-renderer.vue'
import SectionEditor from './section-editor.vue'
import TextPicker from './text-picker.vue'
import RectanglesHighlighter from './rectangles-highlighter.vue'


const props = defineProps({
  projectId: {type: String, required: true},
  textbookId: {type: String, required: true},
  page: {type: Number, required: true},
})

const api = useApiStore()
const pdfs = usePdfsStore()

const component = ref(null)
const sectionEditor = ref(null)
const pdfRenderer = ref(null)
const textPicker = ref(null)

const projectLoading = ref(false)
const project = computedAsync(
  async () => {
    return await api.client.getOne('project', props.projectId)
  },
  null,
  projectLoading,
)

const projectTitle = computed(() => {
  if (project.value?.inCache && project.value?.exists) {
    return project.value.attributes.title
  } else {
    return null
  }
})

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

const textbookTitle = computed(() => {
  if (textbook.value?.inCache && textbook.value?.exists) {
    return textbook.value.attributes.title
  } else {
    return null
  }
})

const sections = computed(() => textbook.value?.relationships.sections || [])

// @todo(Feature, soon) Get the number of pages from the textbook itself
const textbookPagesCount = computed(() => {
  let c = 1
  for (const section of sections.value) {
    c = Math.max(c, section.attributes.textbookStartPage + section.attributes.pagesCount - 1)
  }
  return c
})

const section = computed(() => {
  for (const section of sections.value) {
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

defineExpose({
  title: computed(() => {
    if (projectTitle.value && textbookTitle.value) {
      return ['MALIN', projectTitle.value, textbookTitle.value, `Page ${props.page}`]
    } else {
      return ['MALIN']
    }
  }),
  breadcrumbs: computed(() => {
    if (projectTitle.value && textbookTitle.value) {
      return [
        {title: projectTitle.value, to: {name: 'project', params: {projectId: props.projectId}}},
        {title: textbookTitle.value},
      ]
    } else {
      return []
    }
  }),
})
</script>

<template>
  <b-busy size="11rem" :busy="projectLoading || textbookLoading">
    <template v-if="!project?.exists">
      <h1>{{ $t('projectNotFound') }}</h1>
    </template>
    <template v-else-if="!textbook?.exists">
      <h1>{{ $t('textbookNotFound') }}</h1>
    </template>
    <template v-else>
      <b-row>
        <b-col :w="4">
          <pdf-navigation-controls :page @update:page="component?.changePage" :disabled="!component?.changePage" :pagesCount="textbookPagesCount">
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
                  <rectangles-highlighter
                    v-if="component?.highlightedRectangles && pdfRenderer?.transform"
                    class="img img-fluid" style="position: absolute; top: 0; left: 0"
                    :width="pdfRenderer.width" :height="pdfRenderer.height" :transform="pdfRenderer.transform"
                    :rectangles="component.highlightedRectangles"
                  />
                  <text-picker
                    v-if="component?.textSelected && pdfRenderer?.transform"
                    class="img img-fluid" style="position: absolute; top: 0; left: 0"
                    :width="pdfRenderer.width" :height="pdfRenderer.height" :transform="pdfRenderer.transform"
                    :textContent="pdf.textContent"
                    @text-selected="component.textSelected"
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
          <router-view :project :textbook :page :pdf :section v-slot="{ Component }">
            <component :is="Component" ref="component"></component>
          </router-view>
        </b-col>
      </b-row>
    </template>
  </b-busy>
</template>
