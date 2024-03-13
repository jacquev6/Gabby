<script setup>
import { ref, computed } from 'vue'

import { useApiStore } from '../../stores/api'
import { BButton, BBusy, BLabeledInput, BLabeledTextarea } from '../../components/opinion/bootstrap'


const props = defineProps({
  project: {type: Object, required: true},
})

const api = useApiStore()

const editing = ref(false)
const title = ref(null)
const description = ref(null)
function startEditing() {
  title.value = props.project.attributes.title
  description.value = props.project.attributes.description
  editing.value = true
}

// @todo Factorize with create-project-form.vue
const disabled = computed(() => !title.value)
const saving = ref(false)
async function save() {
  saving.value = true
  await api.client.patch('project', props.project.id, {title: title.value, description: description.value}, {})
  saving.value = false
  editing.value = false
}
</script>

<template>
  <template v-if="editing">
    <h1>Project</h1>
    <b-busy :busy="saving">
      <b-labeled-input :label="$t('projectTitle')" v-model="title" />
      <b-labeled-textarea :label="$t('projectDescription')" v-model="description" />
      <b-button sm secondary @click="editing = false">{{ $t('cancel') }}</b-button>
      <b-button sm primary @click="save" :disabled="disabled">{{ $t('saveProject') }}</b-button>
    </b-busy>
  </template>
  <template v-else>
    <h1>{{ $t('projectHeader', {title: project.attributes.title}) }} <b-button sm secondary @click="startEditing">{{ $t('edit') }}</b-button></h1>
    <p>{{ project.attributes.description }}</p>
  </template>
</template>
