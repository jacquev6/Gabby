<script setup>
import { ref } from 'vue'


const gabbyVersion = import.meta.env.VITE_GABBY_VERSION
const userAgent = JSON.stringify(window.navigator.userAgentData || window.navigator.userAgent)

const windowWidth = ref(null)
const windowHeight = ref(null)
function onResize() {
  windowWidth.value = window.innerWidth
  windowHeight.value = window.innerHeight
}
onResize()
window.addEventListener('resize', onResize)
</script>

<template>
  <div class="modal fade">
    <div class="modal-dialog modal-xl">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title">{{ $t('about') }}</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="container-fluid">
            <div class="row">
              <div class="col">
                <p>{{ $t('french-only') }} Bienvenue sur la démo de l'interface d'adaptation de manuels scolaires pour le projet MALIN et le Cartable Fantastique.</p>

                <p>
                  Une aide est maintenant disponible via un lien dans le cartouche de navigation à coté du lien "À propos".
                  Elle contient également un historique des versions.
                </p>

                <p>Restrictions actuelles :</p>
                <ul>
                  <li>Les changements ne sont enregistrés que de façon temporaires et peuvent être perdus à tout moment.</li>
                  <li>Les numéros d'exercises sont forcément numériques pour l'instant. Donc pas de "Défis langue" pour l'instant.</li>
                </ul>
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
        </div>
      </div>
    </div>
  </div>
</template>
