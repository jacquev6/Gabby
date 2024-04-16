<script setup>
import { ref, reactive, computed, watch } from 'vue'
import { useRouter } from 'vue-router'
import { computedAsync } from '@vueuse/core'

import { useApiStore } from '../../stores/api'
import { BRow, BCol, BButton } from '../../components/opinion/bootstrap'
import ExerciseForm from '../../components/exercise-form.vue'


const props = defineProps({
  project: {type: Object, required: true},
  textbook: {type: Object, required: true},
  page: {type: Number, required: true},
  pdf: {required: true},
  section: {type: Object, required: true},
  exerciseId: {type: String, required: true},
})

const router = useRouter()
const api = useApiStore()

const exerciseLoading = ref(false)
const exercise = computedAsync(
  async () => {
    return await api.client.getOne('exercise', props.exerciseId, {include: 'adapted'})
  },
  null,
  exerciseLoading,
)

const exerciseForm = ref(null)

function saved() {
  router.push({name: 'project-textbook-page-list-exercises'})
}

defineExpose({
  // @todo Allow editing the bounding rectangle
  textSelected: computed(() => exerciseForm.value?.textSelected),
  highlightedRectangles: computed(() => exerciseForm.value?.highlightedRectangles),
})
</script>

<template>
  <b-row>
    <b-col>
      <h1>{{ $t('edition') }}</h1>
      <exercise-form
        ref="exerciseForm"
        :project
        :textbook
        :textbookPage="page"
        :section
        :pdf
        :number="exercise?.attributes.number || ''"
        :automaticNumber="false"
        :fixedNumber="true"
        :exercise
        @saved="saved"
        v-slot="{ disabled, save }"
      >
        <router-link class="btn btn-secondary" :to="{name: 'project-textbook-page-list-exercises'}">{{ $t('cancel') }}</router-link>
        <b-button primary :disabled @click="save">{{ $t('save') }}</b-button>
      </exercise-form>
    </b-col>
    <b-col>
      <h1>{{ $t('adaptation') }}</h1>
      <iframe :src="exerciseForm?.adaptationUrl" style="width: 100%; height: 100%"></iframe>
    </b-col>
  </b-row>
</template>
