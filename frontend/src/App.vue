<script setup>
import { ref, watch, onMounted } from 'vue'
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle.min.js'

import PdfPicker from './components/PdfPicker.vue'
import FloatingModal from './components/FloatingModal.vue'

const windowHeight = ref(null)
function onResize() {
  windowHeight.value = window.innerHeight
}
onResize()
window.addEventListener('resize', onResize);

const pdf = ref('/test.pdf')
const pdfName = ref(null)
const pageNumber = ref(1)
const pagesCount = ref(null)

function pdfLoaded(name, numPages) {
  pdfName.value = name
  pagesCount.value = numPages
  pageNumber.value = 1
}

watch(pageNumber, () => {
  if (pageNumber.value < 1) {
    pageNumber.value = 1
  } else if (pageNumber.value > pagesCount.value) {
    pageNumber.value = pagesCount.value
  }
})

const selectedText = ref(null)
const showTextSelectionMenu = ref(false)
const textSelectionMenuReference = ref({x: 0, y: 0})

function textSelected(text, point) {
  selectedText.value = text
  showTextSelectionMenu.value = true
  textSelectionMenuReference.value = {x: point.clientX, y: point.clientY}
}

// @todo Use a single 'reactive' object instead of several 'ref's
const sections = {
  // French vocabulary used here to avoid a translation roundtrip from the specs in French
  consignes: ref(''),
  exemple: ref(''),
  indice: ref(''),
  énoncé: ref(''),
}

const wording = ref('')
const directives = ref('')

const modal = ref(null)
onMounted(() => {
  (new bootstrap.Modal(modal.value)).show()
})
</script>

<template>
  <PdfPicker style="float: left" :pdf="pdf" :page="pageNumber" :targetHeight="windowHeight" @text-selected="textSelected" @pdf-loaded="pdfLoaded" />

  <FloatingModal
    v-if="showTextSelectionMenu"
    :title="$t('selectedText')"
    :reference="textSelectionMenuReference"
    @dismissed="showTextSelectionMenu=false"
  >
    <pre>{{ selectedText }}</pre>
    <hr/>
    <p>{{ $t('addTo') }}</p>
    <template v-for="(_, section, index) in sections">
      <template v-if="index !== 0">&nbsp;</template>
      <button class="btn btn-primary" @click="sections[section].value += selectedText; showTextSelectionMenu=false">{{ $t(section) }}</button>
    </template>
  </FloatingModal>

  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand"><img src="/favicon.ico" alt="Logo" width="30" height="24" class="d-inline-block align-text-top">Gabby</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0"></ul>
        <form>
          <select class="form-control" v-model="$i18n.locale">
            <option v-for="locale in $i18n.availableLocales" :key="locale" :value="locale">{{ {'en': '🇺🇸 English (US)', 'fr': '🇫🇷 Français'}[locale] }}</option>
          </select>
        </form>
      </div>
    </div>
  </nav>

  <div class="container-fluid">
    <div class="row">
      <div class="col">
        <h2>{{ $t('edition') }}</h2>
        <form>
          <div class="mb-3">
            <label class="form-label">{{ $t('inputFile') }}</label>
            <input class="form-control" type="file" @change="(e) => { pdf = e.target.files[0] }" />
          </div>

          <div class="mb-3">
            <label class="form-label">Page (sur {{ pagesCount }})</label>
            <input class="form-control" type="number" v-model="pageNumber" />
          </div>

          <div v-for="(content, section) in sections" class="mb-3">
            <label class="form-label">{{ $t(section) }}</label>
            <textarea class="form-control" rows="3" v-model="sections[section].value"></textarea>
          </div>
        </form>
      </div>
      <div class="col">
        <h2>{{ $t('visualization') }}</h2>
        <p>({{ $t('not-yet-implemented') }})</p>
        <p v-for="(content) in sections" class="mb-3">{{ content.value }}</p>
      </div>
    </div>
  </div>

  <div ref="modal" class="modal">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <h3 class="modal-title">Bienvenue&nbsp;!</h3>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <p>Bienvenue sur la démo de <em>Gabby</em>, l'interface d'adaptation de manuels scolaires pour le projet MALIN et le Cartable Fantastique.</p>
          <p>
            Le développement de <em>Gabby</em> vient de commencer, donc rien n'est définitif.
            Cette démo est là pour vous permettre de me donner aussi tôt que vous le souhaitez votre avis sur l'interface.
            Pour l'instant c'est une coquille vide ; il y a encore énormément à faire, dont beaucoup sera invisible.
          </p>
          <p>
            Cliquez partout, essayez tout ce que vous voulez !
            Gardez à l'esprit que rien n'est enregistré.
            Faites-moi part de vos remarques, posez-moi vos questions et rapportez-moi les bugs et comportements contre-intuitifs.
            Je rebouclerai avec Caroline si j'ai besoin de clarifier les priorités.
            Si vous trouvez des problèmes spécifiques à un PDF, il serait pratique que vous me l'envoyiez si vous le pouvez.
            Il est également pratique pour moi que vous me disiez quel navigateur web vous utilisez et que vous joigniez des captures d'écran à votre prose.
          </p>

          <p>Merci d'avance, <a href="mailto:vincent@vincent-jacques.net">Vincent Jacques &lt;vincent@vincent-jacques.net&gt;</a></p>
        </div>
      </div>
    </div>
  </div>
</template>
