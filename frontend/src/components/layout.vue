<script setup>
import { ref, computed } from 'vue'
import { useHead } from '@unhead/vue'

import AboutModal from './AboutModal.vue'
import languageSelector from './opinion/language-selector.vue'


const props = defineProps({
  title: {type: String, required: true},
  breadcrumbs: {type: Array, default: []},
})

useHead({
  title: computed(() => props.title)  // 'useHead' does not react to props directly,
})

const about = ref(null)
</script>

<template>
  <div class="container-fluid">
    <nav class="navbar navbar-expand-sm bg-body-tertiary">
      <div class="container-fluid">
        <router-link to="/" class="navbar-brand"><img src="/logo-cartable-fantastique.png" alt="Logo Cartable Fantastique" width="28" height="28"> MALIN</router-link>
        <nav v-if="breadcrumbs.length" style="--bs-breadcrumb-divider: '>'" aria-label="breadcrumb">
          <!-- @todo Fix vertical alignment of the breadcrumbs -->
          <ol class="breadcrumb">
            <template v-for="(breadcrumb, index) in breadcrumbs" :key="index">
              <template v-for="active in [index === breadcrumbs.length - 1]">
                <li class="breadcrumb-item" :class="{active}">
                  <template v-if="active">{{ breadcrumb.title }}</template>
                  <router-link v-else :to="breadcrumb.to">{{ breadcrumb.title }}</router-link>
                </li>
              </template>
            </template>
          </ol>
        </nav>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbar-collapse" aria-controls="navbar-collapse" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
        <div class="collapse navbar-collapse" id="navbar-collapse">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item"><a href="/doc/" class="nav-link">{{ $t('help') }}</a></li>
            <li class="nav-item"><a href="#" class="nav-link" @click.prevent="about.show()">{{ $t('about') }}</a></li>
            <li><language-selector class="w-auto" /></li>
          </ul>
        </div>
      </div>
    </nav>
    <about-modal ref="about"/>
    <slot></slot>
  </div>
</template>
