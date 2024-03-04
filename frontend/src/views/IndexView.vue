<script setup>
import { ref, reactive, shallowRef } from 'vue'
import { computedAsync } from '@vueuse/core'

import { usePdfsStore } from '../stores/pdfs'
import { useApiStore } from '../stores/api'
import BInput from '../components/BootstrapInput.vue'
import { BRow, BCol, BButton } from '../components/bootstrap'
import Loading from '../components/Loading.vue'
import PdfPreview from '../components/PdfPreview.vue'


const pdfs = usePdfsStore()
const loadingPdf = ref(false)
const lastPdfOpened = shallowRef(null)  // Don't interfere with '.document': it must remain an actual 'PDFDocumentProxy' for '.getPage' to work

async function loadPdf(source) {
  loadingPdf.value = true
  lastPdfOpened.value = null
  try {
    lastPdfOpened.value = await pdfs.open(source)
  } finally {
    loadingPdf.value = false
  }
}

const mode = ref(null)
const textbookAttributes = reactive({title: '', publisher: '', year: null, isbn: ''})
const creatingTextbook = ref(false)
const textbooksCreated = ref(0)
async function createTextbook() {
  creatingTextbook.value = true
  try {
    const pdfFile = await api.client.post(
      'pdfFile',
      {sha256: lastPdfOpened.value.info.sha256, bytesCount: 0, pagesCount: lastPdfOpened.value.document.numPages},
      {namings: [], sections: []},
    )
    const pdfFileNaming = await api.client.post(
      'pdfFileNaming',
      {name: lastPdfOpened.value.info.name},
      {pdfFile},
    )
    const textbook = await api.client.post(
      'textbook',
      textbookAttributes,
      {exercises: [], sections: []}
    )
    await api.client.post(
      'section',
      {pdfFileStartPage: 1, pagesCount: lastPdfOpened.value.document.numPages, textbookStartPage: 1},
      {pdfFile, textbook},
    )
  } finally {
    creatingTextbook.value = false
    mode.value = null
    ++textbooksCreated.value
  }
}


const api = useApiStore()
const loadingTextbooks = ref(false)
const textbooks = computedAsync(
  async () => {
    textbooksCreated.value  // Dependency to force reactivity
    return await api.client.get_all('textbooks', {include: 'sections.pdfFile.namings'})
  },
  [],
  loadingTextbooks,
)
</script>

<template>
  <b-row>
    <b-col>
      <h1>Ouvrir un PDF</h1>
      <loading :loading="loadingPdf">
        <BInput :label="$t('inputFile')" type="file" accept=".pdf" @change="(e) => loadPdf(e.target.files[0])" />
        <p>(Ou ouvrir le <a href="#" @click.prevent="loadPdf({url: '/test.pdf'})">PDF de test</a>)</p>
      </loading>
      <h1>PDFs ouverts</h1>
      <ul v-if="pdfs.known.length">
        <li v-for="info in pdfs.known">
          <a href="#" @click.prevent="pdfs.getDocument(info.sha256).then((document) => lastPdfOpened = {info, document})">{{ info.name }}</a>
          ({{ info.size }} octets)
          <b-button sm secondary @click="pdfs.close(info.sha256)">Fermer</b-button>
        </li>
      </ul>
      <p v-else>Aucun PDF ouvert actuellement.</p>
      <template v-if="lastPdfOpened">
        <h1>PDF sélectionné <b-button sm secondary @click="lastPdfOpened = null">Désélectionner</b-button></h1>
        <b-row>
          <b-col>
            <template v-if="api.cache.get('pdfFile', lastPdfOpened.info.sha256)?.relationships.sections">
              <p>Il contient :</p>
              <ul>
                <li v-for="section in api.cache.get('pdfFile', lastPdfOpened.info.sha256).relationships.sections">
                  aux pages {{  section.attributes.pdfFileStartPage }} à {{ section.attributes.pdfFileStartPage + section.attributes.pagesCount - 1 }},
                  <router-link :to="{name: 'textbook-page', params: {textbookId: section.relationships.textbook.id, page: section.attributes.textbookStartPage }}">
                    les pages {{ section.attributes.textbookStartPage }} à {{ section.attributes.textbookStartPage + section.attributes.pagesCount - 1 }}
                    de {{ section.relationships.textbook.attributes.title }}, {{ section.relationships.textbook.attributes.publisher }}, {{ section.relationships.textbook.attributes.year }}
                  </router-link>
                </li>
              </ul>
              <p>@todo(Feature, now) Créer un nouveau manuel (pour les PDFs contenant (des extraits de) plusieurs manuels)</p>
              <p>@todo(Feature, soon) Associer un manuel existant (pour les manuels répartis sur plusieurs PDFs)</p>
            </template>
            <template v-else>
              <p>Il ne correspond à aucun manuel existant.</p>
              <template v-if="mode === 'create-textbook'">
                <loading :loading="creatingTextbook">
                  <BInput label="Titre" v-model="textbookAttributes.title"/>
                  <BInput label="Éditeur" v-model="textbookAttributes.publisher"/>
                  <BInput label="Année" type="number" v-model="textbookAttributes.year"/>
                  <BInput label="ISBN" v-model="textbookAttributes.isbn"/>
                  <p class="d-grid"><b-button primary @click="createTextbook">Enregistrer</b-button></p>
                </loading>
              </template>
              <template v-else>
                <p class="d-grid"><b-button primary @click="mode = 'create-textbook'">Nouveau manuel</b-button></p>
              </template>
            </template>
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
                sont dans {{ pdfs.getInfo(section.relationships.pdfFile.attributes.sha256)?.name ?? ' un PDF précédent nommé ' + section.relationships.pdfFile.relationships.namings[0].attributes.name }}
              </li>
            </ul>
          </li>
        </ul>
      </template>
      <p v-else>Aucun manuel existant.</p>
    </b-col>
  </b-row>
</template>
