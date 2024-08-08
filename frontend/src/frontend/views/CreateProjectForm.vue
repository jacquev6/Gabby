<script setup lang="ts">
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'

import { BButton, BBusy } from '$frontend/components/opinion/bootstrap'
import ProjectFieldsForm from '$frontend/components/ProjectFieldsForm.vue'
import { useApiStore } from '$frontend/stores/api'
import type { List } from '$frontend/stores/api'
import { makeModel, resetModel } from '$frontend/components/ProjectFieldsForm.vue'


const props = defineProps<{
  projects: List<'project'>
}>()

const router = useRouter()
const api = useApiStore()

const fields = ref<InstanceType<typeof ProjectFieldsForm> | null>(null)

const model = reactive(makeModel())

const busy = ref(false)
async function create() {
  busy.value = true
  const project = await api.client.createOne(
    'project',
    {title: model.title, description: model.description},
    {},
  )
  busy.value = false

  resetModel(model)

  /* no await */ props.projects.refresh()

  router.push({name: 'project', params: {projectId: project.id}})
}
</script>

<template>
  <BBusy :busy>
    <ProjectFieldsForm ref="fields" v-model="model" />
    <BButton primary :disabled="fields === null || fields.saveDisabled" @click="create" data-cy="create-project">{{ $t('createProject' )}}</BButton>
  </BBusy>
</template>
