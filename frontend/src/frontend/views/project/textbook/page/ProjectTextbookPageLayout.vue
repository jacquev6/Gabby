<script setup lang="ts">
import { ref, computed } from 'vue'
import { computedAsync } from '@vueuse/core'

import { usePdfsStore } from '../../../../stores/pdfs'
import { BBusy, BRow, BCol, BButton } from '../../../../components/opinion/bootstrap'
import PdfNavigationControls from '../../../../components/PdfNavigationControls.vue'
import PdfNotLoaded from './PdfNotLoaded.vue'
import PdfRenderer from '../../../../components/PdfRenderer.vue'
import SectionEditor from './SectionEditor.vue'
import TextPicker from './TextPicker.vue'
import RectanglesHighlighter from './RectanglesHighlighter.vue'


const props = defineProps<{
  project: Object,
  refreshProject: Function,
  textbook: Object,
  refreshTextbook: Function,
  page: Number,
}>()

const pdfs = usePdfsStore()

const component = ref(null)
const sectionEditor = ref(null)
const pdfRenderer = ref(null)

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

defineExpose({
  title: computed(() => [`Page ${props.page}`]),
  breadcrumbs: computed(() => []),
})
</script>

<template>
  <BRow>
    <BCol :w="4">
      <PdfNavigationControls :page @update:page="component?.changePage" :disabled="!component?.changePage" :pagesCount="textbookPagesCount">
        <BButton secondary sm :disabled="!section" @click="sectionEditor.show(section.id)">&#9881;</BButton>
      </PdfNavigationControls>
      <SectionEditor ref="sectionEditor" />
      <template v-if="section">
        <BBusy size="7rem" :busy="pdfLoading">
          <template v-if="pdf?.page">
            <div style="border: 1px solid black">
              <PdfRenderer
                ref="pdfRenderer"
                :page="pdf.page"
                class="img img-fluid"
              />
              <RectanglesHighlighter
                v-if="component?.highlightedRectangles && pdfRenderer?.transform"
                class="img img-fluid" style="position: absolute; top: 0; left: 0"
                :width="pdfRenderer.width" :height="pdfRenderer.height" :transform="pdfRenderer.transform"
                :rectangles="component.highlightedRectangles"
              />
              <TextPicker
                v-if="component?.textSelected && pdfRenderer?.transform"
                class="img img-fluid" style="position: absolute; top: 0; left: 0"
                :width="pdfRenderer.width" :height="pdfRenderer.height" :transform="pdfRenderer.transform"
                :textContent="pdf.textContent"
                @text-selected="component.textSelected"
              />
            </div>
          </template>
          <template v-else>
            <PdfNotLoaded :name="section.relationships.pdfFile.relationships.namings[0].attributes.name" />
          </template>
        </BBusy>
      </template>
      <template v-else>
        <p>{{ $t('pageNoKnown') }}</p>
      </template>
    </BCol>
    <BCol>
      <RouterView :project :textbook :pdf :section :page v-slot="{ Component }">
        <component :is="Component" ref="component"></component>
      </RouterView>
    </BCol>
  </BRow>
</template>
