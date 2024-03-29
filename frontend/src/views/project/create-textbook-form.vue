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
  try {
    await api.client.post(
      'pdfFile',
      {sha256: pdf.value.info.sha256, bytesCount: 0, pagesCount: pdf.value.document.numPages},
      {namings: [], sections: []},
    )
  } catch (e) {
    if (e?.cause?.errors?.[0].code === 'unique') {  // @todo Make the server idempotent so that there is no error at all
      // The PDF file already exists
    } else {
      throw e
    }
  }
  try {
    await api.client.post(
      'pdfFileNaming',
      {name: pdf.value.info.name},
      {pdfFile: {type: 'pdfFile', id: pdf.value.info.sha256}},
    )
  } catch (e) {
    if (e?.cause?.status === 500) {  // @todo Don't 500, make the server idempotent :-/
      // The naming already exists
    } else {
      throw e
    }
  }
  const textbook = await api.client.post(
    'textbook',
    {title: title.value, publisher: publisher.value || undefined, year: year.value || undefined, isbn: isbn.value || undefined},
    {project: {type: 'project', id: props.projectId}, exercises: [], sections: []}
  )
  await api.client.post(
    'section',
    {pdfFileStartPage: 1, pagesCount: pdf.value.document.numPages, textbookStartPage: 1},
    {pdfFile: {type: 'pdfFile', id: pdf.value.info.sha256}, textbook},
  )
  creating.value = false
  emit('created', textbook.id)
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
