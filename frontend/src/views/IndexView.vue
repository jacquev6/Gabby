<script setup>
import { ref, reactive } from 'vue'

import { usePdfsStore } from '../stores/pdfs'
import { useApiStore } from '../stores/api'
import BInput from '../components/BootstrapInput.vue'
import { BRow, BCol } from '../components/bootstrap'


const pdfs = usePdfsStore()
const loadingPdf = ref(false)
const lastPdfOpened = ref(null)

async function loadPdf(source) {
  loadingPdf.value = true
  lastPdfOpened.value = null
  try {
    lastPdfOpened.value = (await pdfs.load(source)).sha256
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
    const response = await api.client.get('textbooks', {include: 'sections.pdfFile.namings'})
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
      <div v-if="loadingPdf" class="spinner-border" role="status"><span class="visually-hidden">Loading...</span></div>
      <div v-else>
        <BInput :label="$t('inputFile')" type="file" accept=".pdf" @change="(e) => loadPdf(e.target.files[0])" />
        <p>(Ou ouvrir le <a href="#" @click.prevent="loadPdf('/test.pdf')">PDF de test</a>)</p>
      </div>
      <template v-if="lastPdfOpened">
        <h1>PDF ouvert</h1>
        <b-row>
          <b-col>
            <template v-if="api.cache.get('pdfFile', lastPdfOpened)?.relationships.sections">
              <p>Il contient :</p>
              <ul>
                <li v-for="section in api.cache.get('pdfFile', lastPdfOpened).relationships.sections">
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
            <p class="text-center">
              @todo(Feature, now) Display a preview of the PDF<br>
              <button class="btn btn-primary btn-sm">&lt;</button>
              <label>{{ $t('Page') }} <input class="number-no-spin" type="number" min="1" /> {{ $t('pageOver', 42) }}</label>
              <button class="btn btn-primary btn-sm" >&gt;</button>
            </p>
            <canvas class="img img-fluid" height="2970" width="2100" style="border: 1px solid black"></canvas>
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
