<script setup lang="ts">
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'

import { BBusy, BButton, BLabeledInput } from '$frontend/components/opinion/bootstrap'
import TextbookFieldsForm from '$frontend/components/TextbookFieldsForm.vue'
import { usePdfsStore, type InfoDoc } from '$frontend/stores/pdfs'
import { useApiStore } from '$frontend/stores/api'
import type { Project, InCache, Exists, Textbook } from '$frontend/stores/api'
import { makeModel, resetModel } from '$frontend/components/TextbookFieldsForm.vue'


const props = defineProps<{
  project: Project & InCache & Exists,
}>()

const pdfs = usePdfsStore()
const api = useApiStore()
const router = useRouter()

const fields = ref<InstanceType<typeof TextbookFieldsForm> | null>(null)

const model = reactive(makeModel())

const pdfOpener = ref<InstanceType<typeof BLabeledInput> | null>(null)
const loadingPdf = ref(false)
const pdf = ref<InfoDoc | null>(null)
async function loadPdf(event: Event) {
  loadingPdf.value = true
  console.assert(event.target !== null)
  const target = event.target as HTMLInputElement
  console.assert(target.files !== null)
  pdf.value = await pdfs.open(target.files[0])
  loadingPdf.value = false
}

const busy = ref(false)
async function create() {
  busy.value = true
  const operations: any/* @todo Type */[] = [
    [
      'add', 'textbook', 'tb',
      {title: model.title, publisher: model.publisher || undefined, year: model.year || undefined, isbn: model.isbn || undefined},
      {project: {type: 'project', id: props.project.id}},
    ],
  ]
  if(pdf.value !== null) {
    operations.push([
      'add', 'pdfFile', 'pdf',
      {sha256: pdf.value.info.sha256, bytesCount: 0, pagesCount: pdf.value.document.numPages},
      {},
    ])
    operations.push([
      'add', 'pdfFileNaming', null,
      {name: pdf.value.info.name},
      {pdfFile: {type: 'pdfFile', lid: 'pdf'}},
    ])
    operations.push([
      'add', 'section', null,
      {pdfFileStartPage: 1, pagesCount: pdf.value.document.numPages, textbookStartPage: 1},
      {pdfFile: {type: 'pdfFile', lid: 'pdf'}, textbook: {type: 'textbook', lid: 'tb'}},
    ])
  }
  console.log(operations)
  const results = await api.client.batch(...operations)
  const textbook = results[0] as Textbook & InCache & Exists
  busy.value = false

  reset()

  /* no await */ props.project.refresh()

  router.push({name: 'project-textbook-page', params: {textbookId: textbook.id, page: 1}})
}

function reset() {
  console.assert(pdfOpener.value !== null)
  pdfOpener.value.clear()
  pdf.value = null
  resetModel(model)
}

defineExpose({
  pdfToPreview: pdf,
})
</script>

<template>
  <BBusy :busy>
    <BBusy :busy="loadingPdf">
      <BLabeledInput ref="pdfOpener" :label="$t('inputFile')" type="file" accept=".pdf" @change="loadPdf" />
    </BBusy>
    <TextbookFieldsForm
      ref="fields"
      v-model="model"
    />
    <BButton secondary @click="reset">{{ $t('cancel') }}</BButton>
    <BButton primary @click="create" :disabled="fields === null || fields.saveDisabled || pdf === null">{{ $t('createTextbook') }}</BButton>
  </BBusy>
</template>
