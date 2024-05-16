<script setup lang="ts">
import { ref } from 'vue'

import ProjectForm from '$frontend/components/ProjectForm.vue'
import { BButton } from '$frontend/components/opinion/bootstrap'
import type { Project } from '$frontend/types/api'


defineProps<{
  project: Project,
}>()

const editing = ref(false)
</script>

<template>
  <template v-if="editing">
    <h1>{{ $t('project') }}</h1>
    <ProjectForm :project v-slot="{ disabled, save }" @saved="editing = false">
      <BButton secondary @click="editing = false">{{ $t('cancel') }}</BButton>
      <BButton primary @click="save" :disabled="disabled">{{ $t('saveProject') }}</BButton>
    </ProjectForm>
  </template>
  <template v-else>
    <h1>{{ $t('projectHeader', {title: project.attributes?.title}) }} <BButton sm secondary @click="editing = true">{{ $t('edit') }}</BButton></h1>
    <p>{{ project.attributes?.description }}</p>
  </template>
</template>
