<script setup>
import { ref } from 'vue'

import ProjectForm from '../../components/project-form.vue'
import { BButton } from '../../components/opinion/bootstrap'


const props = defineProps({
  project: {type: Object, required: true},
})

const editing = ref(false)
</script>

<template>
  <template v-if="editing">
    <h1>Project</h1>
    <project-form :project="project" v-slot="{ disabled, save }" @saved="editing = false">
      <b-button secondary @click="editing = false">{{ $t('cancel') }}</b-button>
      <b-button primary @click="save" :disabled="disabled">{{ $t('saveProject') }}</b-button>
    </project-form>
  </template>
  <template v-else>
    <h1>{{ $t('projectHeader', {title: project.attributes.title}) }} <b-button sm secondary @click="editing = true">{{ $t('edit') }}</b-button></h1>
    <p>{{ project.attributes.description }}</p>
  </template>
</template>
