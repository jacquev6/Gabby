<script setup lang="ts">
import { ref, computed } from 'vue'
import { useHead } from '@unhead/vue'
import type { RouteLocationRaw } from 'vue-router'

import AboutModal from './AboutModal.vue'
import LanguageSelector from './opinion/LanguageSelector.vue'


const props = defineProps<{
  title: string,
  breadcrumbs: {title: string, to: RouteLocationRaw}[],
}>()

useHead({
  title: computed(() => props.title)  // 'useHead' does not react to props directly,
})

const about = ref<typeof AboutModal | null>(null)
</script>

<template>
  <nav class="navbar navbar-expand-sm bg-body-tertiary">
    <div class="container-fluid">
      <RouterLink to="/" class="navbar-brand"><img src="/logo-cartable-fantastique.png" alt="Logo Cartable Fantastique" width="28" height="28"> MALIN</RouterLink>
      <nav v-if="breadcrumbs.length" style="--bs-breadcrumb-divider: '>'" aria-label="breadcrumb">
        <!-- @todo Fix vertical alignment of the breadcrumbs -->
        <ol class="breadcrumb">
          <template v-for="(breadcrumb, index) in breadcrumbs" :key="index">
            <template v-for="active in [index === breadcrumbs.length - 1]">
              <li class="breadcrumb-item" :class="{active}">
                <template v-if="active">{{ breadcrumb.title }}</template>
                <RouterLink v-else :to="breadcrumb.to">{{ breadcrumb.title }}</RouterLink>
              </li>
            </template>
          </template>
        </ol>
      </nav>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbar-collapse" aria-controls="navbar-collapse" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
      <div class="collapse navbar-collapse" id="navbar-collapse">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item"><a href="/doc/" class="nav-link">{{ $t('help') }}</a></li>
          <li class="nav-item"><a href="#" class="nav-link" @click.prevent="about?.show()">{{ $t('about') }}</a></li>
          <li><LanguageSelector class="w-auto" /></li>
        </ul>
      </div>
    </div>
  </nav>
  <AboutModal ref="about"/>
</template>
