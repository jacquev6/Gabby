<script setup lang="ts">
import { computed } from 'vue'

import { BRow, BCol } from '$frontend/components/opinion/bootstrap'
import { useApiStore } from '$frontend/stores/api'
import RootLayout from './RootLayout.vue'
import ProjectsList from './ProjectsList.vue'
import bc from '$frontend/components/breadcrumbs'
import CreateProjectForm from './CreateProjectForm.vue'


const api = useApiStore()

const projects = computed(() => api.auto.getAll('project'))
</script>

<template>
  <RootLayout
    :title="[]" :breadcrumbs="bc.empty"
  >
    <BRow>
      <BCol>
        <h1>{{ $t('newProject') }}</h1>
        <CreateProjectForm :projects />
      </BCol>
      <BCol>
        <h1>{{ $t('existingProjects' )}}</h1>
        <ProjectsList :projects />
      </BCol>
    </BRow>
  </RootLayout>
</template>
