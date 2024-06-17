<script setup lang="ts">
import { ref, watch } from 'vue'

import { BModal, BButton, BRow, BCol, BLabeledInput } from './opinion/bootstrap'
import LanguageSelector from './opinion/LanguageSelector.vue'
import { useApiStore } from '../stores/api'


const api = useApiStore()

const modal = ref<typeof BModal | null>(null)

watch(
  [modal, api.auth.isAuthenticated, api.auth.expiresSoon],
  () => {
    if (modal.value !== null && (!api.auth.isAuthenticated.value || api.auth.expiresSoon.value)) {
      modal.value.show()
    }
  },
)

const username = ref('')
const password = ref('')

async function login() {
  console.assert(modal.value !== null)
  if (await api.auth.login(username.value, password.value)) {
    modal.value.hide()
  }
}
</script>

<template>
  <BModal ref="modal" :close="false" backdrop="static" :keyboard="false">
    <template #header>
      <div class="container-fluid">
        <BRow>
          <BCol>
            <h1>{{ $t('pleaseLogin') }}</h1>
          </BCol>
          <BCol :w="3">
            <LanguageSelector />
          </BCol>
        </BRow>
      </div>
    </template>
    <template #body>
      <BLabeledInput :label="$t('emailAddress')" name="username" v-model="username" />
      <BLabeledInput :label="$t('password')" name="password" type="password" v-model="password" />
    </template>
    <template #footer>
      <BButton primary @click="login" :disabled="login === '' || password === ''">{{ $t('loginButton') }}</BButton>
    </template>
  </BModal>
</template>
