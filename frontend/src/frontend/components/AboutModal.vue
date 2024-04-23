<script setup lang="ts">
import { ref } from 'vue'

import { BModal, BButton } from './opinion/bootstrap'


const gabbyVersion = import.meta.env.VITE_OPINION_APP_VERSION
const userAgent = JSON.stringify((window.navigator as any/* Chromium-specific */).userAgentData || window.navigator.userAgent)

const windowWidth = ref(window.innerWidth)
const windowHeight = ref(window.innerHeight)
function onResize() {
  windowWidth.value = window.innerWidth
  windowHeight.value = window.innerHeight
}
onResize()
window.addEventListener('resize', onResize)

const modal = ref<typeof BModal | null>(null)
function show() {
  modal.value?.show()
}

function hide() {
  modal.value?.hide()
}

defineExpose({show, hide})
</script>

<template>
  <BModal ref="modal">
    <template #header>
      <h1>{{ $t('about') }}</h1>
    </template>
    <template #body>
      <div class="container-fluid">
        <div class="row">
          <div class="col">
            <p>{{ $t('french-only') }} Bienvenue sur la démo de l'interface d'adaptation de manuels scolaires pour le projet MALIN et le Cartable Fantastique.</p>

            <p>
              Une aide est disponible via un lien dans le cartouche de navigation à coté du lien "À propos".
              Elle contient également un historique des versions et une description des évolutions prévues.
            </p>

            <p>
              Faites-moi part de vos remarques, posez-moi vos questions et rapportez-moi les bugs et comportements contre-intuitifs.
              Je rebouclerai avec Caroline si j'ai besoin de clarifier les priorités.
              Merci de joindre à vos messages les informations figurant dans la colone de droite et, si ça vous semble judicieux, des captures d'écran et le PDF que vous utilisez.
            </p>
            <p>Merci d'avance&nbsp;!</p>
            <p class="text-end">Vincent Jacques</p>
          </div>
          <div class="col-4">
            <p>
              E-mail: <a href="mailto:vincent@vincent-jacques.net">vincent@vincent-jacques.net</a><br />
              GitHub: <a href="https://github.com/jacquev6/Gabby">@jacquev6/Gabby</a>
            </p>
            <p>Information à joindre à tout rapport de bug ou question&nbsp;:</p>
            <pre>
Gabby version: {{ gabbyVersion }}
Locale: {{ $i18n.locale }}
User agent: {{ userAgent }}
Window size: {{ windowWidth }}x{{ windowHeight }}
            </pre>
          </div>
        </div>
      </div>
    </template>
    <template #footer>
      <BButton secondary @click="hide">{{ $t('close') }}</BButton>
    </template>
  </BModal>
</template>
