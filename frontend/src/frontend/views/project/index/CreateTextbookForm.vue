<script setup lang="ts">
import { ref, computed } from 'vue'

import { BBusy, BLabeledInput, BButton } from '../../../components/opinion/bootstrap'
import { useApiStore } from '../../../stores/api'
import { usePdfsStore, type InfoDoc } from '../../../stores/pdfs'


const props = defineProps<{
  projectId: string,
}>()

const emit = defineEmits<{
  loadedPdf: [pdf: any/* @todo Type */],
  unloadedPdf: [],
  created: [textbookId: string],
}>()

const pdfs = usePdfsStore()
const api = useApiStore()

const pdf = ref<InfoDoc | null>(null)
const loadingPdf = ref(false)
async function loadPdf(source: File) {
  loadingPdf.value = true
  pdf.value = await pdfs.open(source)
  emit('loadedPdf', pdf.value)
  loadingPdf.value = false
}
const title = ref('')
const publisher = ref('')
const year = ref('')
const isbn = ref('')
const disabled = computed(() => !pdf.value || !title.value)
const creating = ref(false)
async function create() {
  console.assert(pdf.value !== null)

  creating.value = true
  const results = await (api.client.batch as any/* @todo Type */)(
    [
      'add', 'pdfFile', 'pdf',
      {sha256: pdf.value.info.sha256, bytesCount: 0, pagesCount: pdf.value.document.numPages},
      {},
    ],
    [
      'add', 'pdfFileNaming', null,
      {name: pdf.value.info.name},
      {pdfFile: {type: 'pdfFile', lid: 'pdf'}},
    ],
    [
      'add', 'textbook', 'tb',
      {title: title.value, publisher: publisher.value || undefined, year: year.value || undefined, isbn: isbn.value || undefined},
      {project: {type: 'project', id: props.projectId}}
    ],
    [
      'add', 'section', null,
      {pdfFileStartPage: 1, pagesCount: pdf.value.document.numPages, textbookStartPage: 1},
      {pdfFile: {type: 'pdfFile', lid: 'pdf'}, textbook: {type: 'textbook', lid: 'tb'}},
    ],
  )
  creating.value = false
  emit('created', results[2].id)
}
</script>

<template>
  <BBusy :busy="creating">
    <BBusy :busy="loadingPdf">
      <BLabeledInput :label="$t('inputFile')" type="file" accept=".pdf" @change="(e: any/* @todo Type */) => loadPdf(e.target.files[0])" />
    </BBusy>
    <BLabeledInput :label="$t('textbookTitle')" v-model="title"/>
    <BLabeledInput :label="$t('textbookPublisher')" v-model="publisher"/>
    <BLabeledInput :label="$t('textbookYear')" type="number" v-model="year"/>
    <BLabeledInput :label="$t('textbookIsbn')" v-model="isbn"/>
    <BButton secondary @click="emit('unloadedPdf')">{{ $t('cancel') }}</BButton>
    <BButton primary @click="create" :disabled="disabled">{{ $t('createTextbook') }}</BButton>
  </BBusy>
</template>
