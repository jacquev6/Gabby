<script setup>
import { ref, computed } from 'vue'
import { BBusy, BLabeledInput, BButton } from '../../components/opinion/bootstrap'
import { useApiStore } from '../../stores/api'
import { usePdfsStore } from '../../stores/pdfs'


const props = defineProps({
  projectId: {type: String, required: true},
})

const emit = defineEmits([
  'loadedPdf',  // (pdf: Object) => void
  'unloadedPdf',  // () => void
  'created',  // (textbookId: string) => void
])

const pdfs = usePdfsStore()
const api = useApiStore()

const pdf = ref(null)
const loadingPdf = ref(false)
async function loadPdf(source) {
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
  creating.value = true
  const results = await api.client.batch(
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
  <b-busy :busy="creating">
    <b-busy :busy="loadingPdf">
      <b-labeled-input :label="$t('inputFile')" type="file" accept=".pdf" @change="(e) => loadPdf(e.target.files[0])" />
    </b-busy>
    <b-labeled-input :label="$t('textbookTitle')" v-model="title"/>
    <b-labeled-input :label="$t('textbookPublisher')" v-model="publisher"/>
    <b-labeled-input :label="$t('textbookYear')" type="number" v-model="year"/>
    <b-labeled-input :label="$t('textbookIsbn')" v-model="isbn"/>
    <b-button secondary @click="emit('unloadedPdf')">{{ $t('cancel') }}</b-button>
    <b-button primary @click="create" :disabled="disabled">{{ $t('createTextbook') }}</b-button>
  </b-busy>
</template>
