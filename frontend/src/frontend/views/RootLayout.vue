<script setup>
import { ref, computed } from 'vue'
import { useI18n } from 'vue-i18n'

import Navbar from '../components/Navbar.vue'


const i18n = useI18n()

const component = ref(null)

const title = computed(() => {
  if (component.value) {
    if (component.value.title === undefined) {
      console.error('component.value.title is undefined')
      return i18n.t('thisIsABug')
    } else {
      console.assert(component.value.title !== null)
      return ['MALIN', ...component.value.title].join(' - ')
    }
  } else {
    return 'MALIN'
  }
})

const breadcrumbs = computed(() => {
  const home = {title: i18n.t('home'), to: '/'}
  if (component.value) {
    if (component.value.breadcrumbs === undefined) {
      console.error('component.value.breadcrumbs is undefined')
      return [{title: i18n.t('thisIsABug')}]
    } else {
      console.assert(component.value.breadcrumbs !== null)
      return [home, ...component.value.breadcrumbs]
    }
  } else {
    return [home]
  }
})

const componentHandlesScrolling = computed(() => component.value?.handlesScrolling ?? false)

const class_ = computed(() => ({
  'h-100': componentHandlesScrolling.value,
  'overflow-y-hidden': componentHandlesScrolling.value,
  'overflow-y-auto': !componentHandlesScrolling.value,
}))
</script>

<template>
  <div class="vh-100 d-flex flex-column overflow-y-hidden">
    <Navbar :title :breadcrumbs></Navbar>
    <div class="flex-fill container-fluid" :class="class_">
      <RouterView v-slot="{ Component }">
        <component :is="Component" ref="component" />
      </RouterView>
    </div>
  </div>
</template>
