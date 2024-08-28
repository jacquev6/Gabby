<script setup lang="ts">
import { computed, reactive, ref, toRaw, watch } from 'vue'
import { computedAsync } from '@vueuse/core'
import type { PDFPageProxy, TextItem } from 'pdfjs-dist/types/src/display/api'

import { usePdfsStore, type InfoDoc } from '$frontend/stores/pdfs'
import { BBusy, BLabeledInput, BRow, BCol } from '$frontend/components/opinion/bootstrap'
import PdfRenderer from '$frontend/components/PdfRenderer.vue'
import PdfNavigationControls from '../components/PdfNavigationControls.vue'
import RectanglesHighlighter from './project/textbook/page/RectanglesHighlighter.vue'


type PDFObjects = PDFPageProxy['commonObjs']

const pdfs = usePdfsStore()

const pdfOpener = ref<InstanceType<typeof BLabeledInput> | null>(null)
const loadingPdf = ref(false)
const pdf = ref<InfoDoc | null>(null)

async function previewKnownPdf(sha256: string) {
  loadingPdf.value = true
  pdf.value = {info: pdfs.getInfo(sha256)!, document: (await pdfs.getDocument(sha256))!}
  loadingPdf.value = false
}

async function loadPdf(event: Event) {
  loadingPdf.value = true
  console.assert(event.target !== null)
  const input = event.target as HTMLInputElement
  if (input.files !== null && input.files.length !== 0) {
    pdf.value = await pdfs.open(input.files[0])
  }
  loadingPdf.value = false
}

const loadingCommonCommonObjects = ref(false)
const commonCommonObjects_ = computedAsync(
  async () => {
    if (pdf.value === null) {
      return null
    } else {
      const doc = toRaw(pdf.value.document)
      const commonObjects = (await doc.getPage(1)).commonObjs
      for (let pageIndex = 1; pageIndex !== pdf.value.document.numPages; ++pageIndex) {
        const page = await doc.getPage(pageIndex + 1)
        if (page.commonObjs !== commonObjects) {
          return null
        }
      }
      return commonObjects
    }
  },
  null,
  loadingCommonCommonObjects,
)
const commonObjectsHaveChanged = ref(0)
const commonCommonObjects = computed(() => {
  if (commonCommonObjects_.value === null) {
    return null
  } else {
    // 'commonObjs' starts empty, and is populated when pages are rendered.
    // Keys even depend on the order in which pages are rendered.
    // So we artificially populate it by rendering all pages in the 'watch' below.
    commonObjectsHaveChanged.value  // Trigger reactivity
    return {commonObjs: commonCommonObjects_.value}
  }
})
const fonts_ = reactive<Record<string, {pages: number[], charsCount: number}>>({})
const progress = ref(0)
// Render all pages to populate 'commonCommonObjects'. In a 'watch' instead of the 'computedAsync'
// for 'commonCommonObjects_' to be able to report progress, as this is a quite long opperation.
const sentinel = ref(0)
watch(
  [pdf, commonCommonObjects_],
  async ([pdf, commonObjs]) => {
    if (pdf === null || commonObjs === null) {
      progress.value = 1
    } else {
      ++sentinel.value
      const expectedSentinel = sentinel.value
      Object.keys(fonts_).forEach(key => delete fonts_[key])
      commonObjectsHaveChanged.value = 0
      const canvasContext = document.createElement('canvas').getContext('2d')
      const doc = toRaw(pdf.document)
      console.assert(canvasContext !== null)
      for (let pageIndex = 0; pageIndex !== doc.numPages; ++pageIndex) {
        // const t0 = performance.now()
        const page = await doc.getPage(pageIndex + 1)
        // const t1 = performance.now()
        await page.render({canvasContext, viewport: page.getViewport()}).promise
        // const t2 = performance.now()
        ++commonObjectsHaveChanged.value
        const textContent = await page.getTextContent()
        // const t3 = performance.now()
        const items = textContent.items as TextItem[]
        for (const {str, fontName: fontId} of items) {
          const {name: fontName} = await new Promise<{name: string}>(resolve => commonObjs.get(fontId, resolve))
          if (sentinel.value !== expectedSentinel) {
            return
          }
          fonts_[fontName] = fonts_[fontName] || {pages: [], charsCount: 0}
          if (fonts_[fontName].pages[fonts_[fontName].pages.length - 1] !== pageIndex + 1) {
            fonts_[fontName].pages.push(pageIndex + 1)
          }
          fonts_[fontName].charsCount += str.length
        }
        progress.value = pageIndex + 1
        // const t4 = performance.now()
        // const totalDuration = t4 - t0
        // if (totalDuration > 1000) {
        //   const getPart = Math.round(100 * (t1 - t0) / totalDuration)
        //   const renderPart = Math.round(100 * (t2 - t1) / totalDuration)
        //   const getContentPart = Math.round(100 * (t3 - t2) / totalDuration)
        //   const accumulatePart = Math.round(100 * (t4 - t3) / totalDuration)
        //   console.log(`Page ${pageIndex + 1}: ${totalDuration}ms - get: ${getPart}%, render: ${renderPart}%, get content: ${getContentPart}%, accumulate: ${accumulatePart}%`)
        // }
      }
    }
  }
)

const fonts = computed(() => Object.fromEntries(Object.entries(fonts_)
  .sort(([_leftFontName, left], [_rightFontName, right]) => {
    return right.charsCount - left.charsCount
  })
))

function formatPdfObjects(objs: PDFObjects) {
  return Array.from(objs).map(([key, value]) => `${key}: ${JSON.stringify(value)}`).join('\n')
}

const pageNumber = ref(1)
watch(pdf, () => { pageNumber.value = 1 })
const loadingPage = ref(false)
const pdfPage = computedAsync(
  () => {
    if (pdf.value === null) {
      return null
    } else {
      return toRaw(pdf.value.document).getPage(pageNumber.value)
    }
  },
  null,
  loadingPage,
)

const pdfRenderer = ref<InstanceType<typeof PdfRenderer> | null>(null)
const highlightFont = ref('-')
const highlightedRectangles = computedAsync(
  async () => {
    if (pdfPage.value === null || commonCommonObjects.value === null || highlightFont.value === '-') {
      return []
    } else {
      const commonObjs = commonCommonObjects.value.commonObjs
      const font = highlightFont.value
      const textContent = await pdfPage.value.getTextContent()
      const items = textContent.items as TextItem[]
      return items
        .filter(({fontName}) => {
          return commonObjs.get(fontName).name === font
        })
        .map(({width, height, transform}) => ({
          start: {x: transform[4], y: transform[5]},
          stop: {x: transform[4] + width, y: transform[5] + height}
        }))
    }
  },
  [],
)
</script>

<template>
  <div class="container-fluid">
    <h1>PDFs currently opened</h1>
    <ul>
      <li v-for="pdf in pdfs.known">
        {{ pdf.sha256 }} ({{ pdf.name }}) <button @click="previewKnownPdf(pdf.sha256)">Preview</button> <button @click="pdfs.close(pdf.sha256)">Close</button>
      </li>
    </ul>
    <h1>Open a new PDF</h1>
    <BBusy :busy="loadingPdf">
      <BLabeledInput ref="pdfOpener" :label="$t('inputFile')" type="file" accept=".pdf" @change="loadPdf" />
    </BBusy>
    <template  v-if="pdf !== null">
      <h1>Last opened PDF</h1>
      <BBusy :busy="loadingCommonCommonObjects">
        <h2>Document<template v-if="progress !== pdf.document.numPages"> (loading: {{ progress }}/{{ pdf.document.numPages }})</template></h2>
        <template v-if="commonCommonObjects === null">
          <p class="alert">Common objects are not common to all pages.</p>
        </template>
        <template v-else>
          <p>Common objects:</p>
          <pre>{{ formatPdfObjects(commonCommonObjects.commonObjs) }}</pre>
          <p>{{ Object.keys(fonts).length }} fonts in common objects:</p>
          <ul>
            <li v-for="font, fontName of fonts">{{ fontName }}: {{ font.charsCount }} characters on {{ font.pages.length }} pages</li>
          </ul>
        </template>
        <h2>Pages</h2>
        <BRow>
          <BCol :w="4">
            <PdfNavigationControls :pagesCount="pdf.document.numPages" v-model:page="pageNumber" :disabled="false" />
            <div
              v-if="pdfPage !== null"
              style="position: relative; border: 1px solid black"
            >
              <PdfRenderer
                ref="pdfRenderer"
                class="img img-fluid"
                :page="pdfPage"
                @rendered="commonObjectsHaveChanged++"
              />
              <RectanglesHighlighter
                v-if="pdfRenderer !== null"
                class="img w-100" style="position: absolute; top: 0; left: 0"
                :width="pdfRenderer.width" :height="pdfRenderer.height" :transform="pdfRenderer.transform"
                :greyRectangles="[]" :surroundedRectangles="highlightedRectangles"
              />
            </div>
          </BCol>
          <BCol :w="8" v-if="pdfPage !== null">
            <p>
              <label>Hightlight font:
                <select v-model="highlightFont">
                  <option value="-">-</option>
                  <option v-for="_font, fontName in fonts" :value="fontName">{{ fontName }}</option>
                </select>: {{ highlightedRectangles.length }} items
              </label>
            </p>
            <p>Page objects:</p>
            <pre>{{ formatPdfObjects(pdfPage.objs) }}</pre>
          </BCol>
        </BRow>
      </BBusy>
    </template>
  </div>
</template>

<style scoped>
pre {
  max-height: 20em;
  max-width: 100%;
  border: solid black 1px;
  padding: 2px;
  overflow: scroll;
}
</style>
