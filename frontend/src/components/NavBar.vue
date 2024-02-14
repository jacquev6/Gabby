<script setup>
import { RouterLink } from 'vue-router'

import AboutModal from '../components/AboutModal.vue'
</script>

<template>
  <nav class="navbar navbar-expand-sm bg-body-tertiary">
    <div class="container-fluid">
      <router-link to="/" class="navbar-brand"><img src="/logo-cartable-fantastique.png" alt="Logo Cartable Fantastique" width="28" height="28"> MALIN</router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbar-collapse" aria-controls="navbar-collapse" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
      <div class="collapse navbar-collapse" id="navbar-collapse">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item"><router-link to="/help" class="nav-link">{{ $t('help') }}</router-link></li>
          <li class="nav-item"><a href="#" class="nav-link" data-bs-toggle="modal" data-bs-target="#about-modal">{{ $t('about') }}</a></li>
        </ul>
        <div class="d-flex">
          <select v-model="$i18n.locale"><option v-for="locale in $i18n.availableLocales" :key="locale" :value="locale">{{ {'en': '🇺🇸 English', 'fr': '🇫🇷 Français'}[locale] }}</option></select>
        </div>
      </div>
    </div>
  </nav>
  <about-modal id="about-modal" />
</template>
