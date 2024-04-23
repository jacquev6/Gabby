<script setup lang="ts">
import { ref, computed, watch } from 'vue'

import { BBusy, BLabeledInput, BLabeledTextarea } from './opinion/bootstrap'
import { useApiStore } from '../stores/api'
import type { Project } from '../types/api'


const props = defineProps<{
  project?: Project,
}>()

const emit = defineEmits<{
  created: [project: Project],
  saved: [],
}>()

const api = useApiStore()

const title = ref('')
const description = ref('')

watch(
  () => props.project,
  () => {
    if (props.project !== undefined) {
      console.assert(props.project.attributes !== undefined)

      title.value = props.project.attributes.title ?? ''
      description.value = props.project.attributes.description ?? ''
    }
  },
  {immediate: true},
)

const disabled = computed(() => !title.value)
const busy = ref(false)

async function create() {
  busy.value = true
  const project = await api.client.post<Project>(
    'project',
    {title: title.value, description: description.value},
    {},
  )

  title.value = ''
  description.value = ''

  busy.value = false

  emit('created', project)
}

async function save() {
  console.assert(props.project !== undefined)

  busy.value = true
  await api.client.patch(
    'project',
    props.project.id,
    {
      title: title.value,
      description: description.value,
    },
    {},
  )

  busy.value = false

  emit('saved')
}
</script>

<template>
  <b-busy :busy>
    <b-labeled-input v-model="title" :label="$t('projectTitle')" />
    <b-labeled-textarea v-model="description" :label="$t('projectDescription')" />
    <slot :disabled :create :save></slot>
  </b-busy>
</template>
