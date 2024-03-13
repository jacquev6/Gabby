<script setup>
import { RouterLink } from 'vue-router'
import { ref } from 'vue'

import AboutModal from './AboutModal.vue'
import languageSelector from './opinion/language-selector.vue'


const about = ref(null)
</script>

<template>
  <nav class="navbar navbar-expand-sm bg-body-tertiary">
    <div class="container-fluid">
      <router-link to="/" class="navbar-brand"><img src="/logo-cartable-fantastique.png" alt="Logo Cartable Fantastique" width="28" height="28"> MALIN</router-link>
      <slot></slot>
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
</template>
