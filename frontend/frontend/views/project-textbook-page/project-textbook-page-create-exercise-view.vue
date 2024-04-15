<script setup>
import { ref, computed } from 'vue'

import { BRow, BCol, BButton } from '../../components/opinion/bootstrap'
import ExerciseForm from '../../components/exercise-form.vue'


const props = defineProps({
  project: {type: Object, required: true},
  textbook: {type: Object, required: true},
  page: {type: Number, required: true},
  pdf: {required: true},
  section: {required: true},
})

const exerciseForm = ref(null)

const number = ref('')
const automaticNumber = ref(false)
function created(exercise, suggestedNumber) {
  number.value = suggestedNumber
  automaticNumber.value = true
}

defineExpose({
  textSelected: computed(() => exerciseForm.value?.textSelected),
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
        :number
        :automaticNumber
        :fixedNumber="false"
        @created="created"
        v-slot="{ disabled, create }"
      >
        <router-link class="btn btn-secondary" :to="{name: 'project-textbook-page-list-exercises'}">{{ $t('cancel') }}</router-link>
        <b-button primary :disabled @click="create">{{ $t('save.next') }}</b-button>
      </exercise-form>
    </b-col>
    <b-col>
      <h1>{{ $t('adaptation') }}</h1>
      <iframe :src="exerciseForm?.adaptationUrl" style="width: 100%; height: 100%"></iframe>
    </b-col>
  </b-row>
</template>
