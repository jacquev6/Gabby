<script setup lang="ts">
import { ref, watch } from 'vue'

import { BBusy, BModal, BButton, BRow, BCol, BLabeledInput } from './opinion/bootstrap'
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

const busy = ref(false)
const failed = ref(false)

async function login() {
  console.assert(modal.value !== null)
  busy.value = true
  const success = await api.auth.login(username.value, password.value)
  busy.value = false
  password.value = ''
  failed.value = !success
  if (success) {
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
      <BBusy :busy>
        <BLabeledInput :label="$t('emailAddress')" name="username" v-model="username" />
        <BLabeledInput :label="$t('password')" name="password" type="password" v-model="password" />
      </BBusy>
    </template>
    <template #footer>
      <p v-if="failed" class="text-danger">{{ $t('loginFailed') }}</p>
      <BButton primary @click="login" :disabled="username === '' || password === ''">{{ $t('loginButton') }}</BButton>
    </template>
  </BModal>
</template>
