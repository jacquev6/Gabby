<script setup>
import { ref, onMounted } from 'vue'
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle.min.js'


const gabbyVersion = import.meta.env.VITE_GABBY_VERSION
const userAgent = window.navigator.userAgent

const windowWidth = ref(null)
const windowHeight = ref(null)
function onResize() {
  windowWidth.value = window.innerWidth
  windowHeight.value = window.innerHeight
}
onResize()
window.addEventListener('resize', onResize);

const aboutModal = ref(null)
onMounted(() => {
  bootstrap.Modal.getOrCreateInstance(`#${aboutModal.value.id}`).show()
})
</script>

<template>
  <div ref="aboutModal" class="modal fade">
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
                  Je viens de commencer le développement donc tout peut encore très facilement être modifié.
                  Cette démo est là pour vous permettre de me donner votre avis sur l'interface aussi tôt que vous le souhaitez.
                  Pour l'instant c'est une coquille vide ; il y a encore énormément à faire, dont beaucoup sera invisible.
                </p>
                <p>Cliquez partout, essayez tout ce que vous voulez&nbsp;!</p>
                <p>
                  Les changements que vous faites sont enregistrés, mais de façon temporaire : la base de données sera effacée à la prochaine version.
                  Notez aussi que ce que vous faites est visible et modifiable par tous les utilisateurs.
                </p>
                <p>Attention, les numéros d'exercises sont forcément numériques pour l'instant. Donc pas de "Défis langue" pour l'instant.</p>
                <p>
                  Faites-moi part de vos remarques, posez-moi vos questions et rapportez-moi les bugs et comportements contre-intuitifs.
                  Je rebouclerai avec Caroline si j'ai besoin de clarifier les priorités.
                  Merci de joindre à vos messages les informations figurant dans la colone de droite
                  et, si ça vous semble judicieux, des captures d'écran et le PDF que vous utilisez.
                </p>
                <p>Merci d'avance&nbsp;!</p>
                <p class="text-end">Vincent Jacques</p>
                <p>
                  E-mail: <a href="mailto:vincent@vincent-jacques.net">vincent@vincent-jacques.net</a><br />
                  GitHub: <a href="https://github.com/jacquev6/Gabby">@jacquev6/Gabby</a>
                </p>
              </div>
              <div class="col-4">
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
