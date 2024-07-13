<script setup lang="ts">
import { computed } from 'vue'

import { useI18n } from 'vue-i18n'

import PasswordResetModal from '$frontend/components/PasswordResetModal.vue'
import Navbar from '$frontend/components/Navbar.vue'
import bc from '$frontend/components/breadcrumbs'


defineProps<{
  emailAddress: string,
  token: string,
}>()

const i18n = useI18n()

const title = computed(() => ['MALIN', i18n.t('resetPasswordTitle')].join(' - '))
const breadcrumbs = computed(() => bc.last(i18n.t('home')))
</script>

<template>
  <div class="vh-100 d-flex flex-column overflow-hidden">
    <Navbar :title :breadcrumbs></Navbar>
    <PasswordResetModal :emailAddress :token />
  </div>
</template>
