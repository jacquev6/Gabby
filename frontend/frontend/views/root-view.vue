<script setup>
import { ref, computed } from 'vue'

import Navbar from '../components/navbar.vue'


const component = ref(null)

const thisIsABug = 'You should not be seeing this; this is a bug. Please let Vincent Jacques know about it.'

const title = computed(() => (component.value?.title || [thisIsABug]).join(' - '))

const breadcrumbs = computed(
  () => component.value?.breadcrumbs || [{title: thisIsABug}]
)
</script>

<template>
  <div class="container-fluid">
    <navbar :title :breadcrumbs></navbar>
    <router-view v-slot="{ Component }">
      <component :is="Component" ref="component" />
    </router-view>
  </div>
</template>
