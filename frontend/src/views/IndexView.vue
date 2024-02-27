<script setup>
import { ref, reactive, shallowRef } from 'vue'

import { usePdfsStore } from '../stores/pdfs'
import { useApiStore } from '../stores/api'
import BInput from '../components/BootstrapInput.vue'
import { BRow, BCol } from '../components/bootstrap'
import Loading from '../components/Loading.vue'
import PdfPreview from '../components/PdfPreview.vue'


const pdfs = usePdfsStore()
const loadingPdf = ref(false)
const lastPdfOpened = shallowRef(null)  // Don't interfere with '.document': it must remain an actual 'PDFDocumentProxy' for '.getPage' to work

async function loadPdf(source) {
  loadingPdf.value = true
  lastPdfOpened.value = null
  try {
    lastPdfOpened.value = await pdfs.load(source)
  } finally {
    loadingPdf.value = false
  }
}

function formatPdfSource(source) {
  if (typeof source === 'string') {
    return source
  } else {
    return source.name
  }
}


const api = useApiStore()
const loadingTextbooks = ref(false)
const textbooks = reactive([])

async function loadTextbooks() {
  loadingTextbooks.value = true
  try {
    textbooks.splice(0, textbooks.length)
    const response = await api.client.get_all('textbooks', {include: 'sections.pdfFile.namings'})
    textbooks.push(...response)
  } finally {
    loadingTextbooks.value = false
  }
}
loadTextbooks()
</script>

<template>
  <b-row>
    <b-col>
      <h1>Ouvrir un PDF</h1>
      <loading :loading="loadingPdf">
        <BInput :label="$t('inputFile')" type="file" accept=".pdf" @change="(e) => loadPdf(e.target.files[0])" />
        <p>(Ou ouvrir le <a href="#" @click.prevent="loadPdf('/test.pdf')">PDF de test</a>)</p>
      </loading>
      <template v-if="lastPdfOpened">
        <h1>PDF ouvert</h1>
        <b-row>
          <b-col>
            <template v-if="api.cache.get('pdfFile', lastPdfOpened.sha256)?.relationships.sections">
              <p>Il contient :</p>
              <ul>
                <li v-for="section in api.cache.get('pdfFile', lastPdfOpened.sha256).relationships.sections">
                  <router-link :to="{name: 'textbook-page', params: {textbookId: section.relationships.textbook.id, page: section.attributes.textbookStartPage }}">
                    les pages {{ section.attributes.textbookStartPage }} à {{ section.attributes.textbookStartPage + section.attributes.pagesCount - 1 }}
                    de {{ section.relationships.textbook.attributes.title }}, {{ section.relationships.textbook.attributes.publisher }}, {{ section.relationships.textbook.attributes.year }}
                  </router-link>
                </li>
              </ul>
            </template>
            <template v-else>
              <p>Il ne correspond à aucun manuel existant.</p>
            </template>
            <p>@todo(Feature, now) Créer un nouveau manuel (pour les PDFs contenant (des extraits de) plusieurs manuels)</p>
            <p>@todo(Feature, soon) Associer un manuel existant (pour les manuels répartis sur plusieurs PDFs)</p>
          </b-col>
          <b-col>
            <pdf-preview :pdf="lastPdfOpened.document" />
          </b-col>
        </b-row>
      </template>
    </b-col>
    <b-col :w="4">
      <h1>Manuels existants</h1>
      <li v-if="loadingTextbooks" class="spinner-border" role="status"><span class="visually-hidden">Loading...</span></li>
      <template v-else-if="textbooks.length">
        <ul>
          <li v-for="textbook in textbooks">
            {{ textbook.attributes.title }}, {{ textbook.attributes.publisher }}, {{ textbook.attributes.year }}, dont
            <ul v-if="textbook.relationships.sections">
              <li v-for="section in textbook.relationships.sections">
                <router-link :to="{name: 'textbook-page', params: {textbookId: textbook.id, page: section.attributes.textbookStartPage }}">
                  les pages {{ section.attributes.textbookStartPage }} à {{ section.attributes.textbookStartPage + section.attributes.pagesCount - 1 }}
                </router-link>
                sont dans {{ pdfs.getSource(section.relationships.pdfFile.attributes.sha256) ? formatPdfSource(pdfs.getSource(section.relationships.pdfFile.attributes.sha256)) : ' un PDF précédent nommé ' + section.relationships.pdfFile.relationships.namings[0].attributes.name }}
              </li>
            </ul>
          </li>
        </ul>
      </template>
      <p v-else>Aucun manuel existant.</p>
    </b-col>
  </b-row>
</template>
