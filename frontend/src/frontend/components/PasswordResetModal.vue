<script setup lang="ts">
import { ref } from 'vue'
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'

import { BRow, BCol, BBusy, BModal, BButton, BLabeledInput } from './opinion/bootstrap'
import LanguageSelector from './opinion/LanguageSelector.vue'
import { useApiStore } from '../stores/api'


const props = defineProps<{
  emailAddress: string,
  token: string,
}>()

const api = useApiStore()
const router = useRouter()

const modal = ref<InstanceType<typeof BModal> | null>(null)

const busy = ref(false)

const emailAddress = ref(props.emailAddress)
const newPassword1 = ref('')
const newPassword2 = ref('')

onMounted(() => {
  console.assert(modal.value !== null)
  modal.value.show()
})

async function resetPassword() {
  busy.value = true
  api.auth.setToken(props.token)
  await api.cache.getOne('user', 'current').patch({ clearTextPassword: newPassword1.value }, {})
  await api.auth.login(emailAddress.value, newPassword1.value)
  busy.value = false
  console.assert(modal.value !== null)
  modal.value.hide()
  router.push({ name: 'index' })
}
</script>

<template>
  <BModal ref="modal" :close="false" backdrop="static" :keyboard="false">
    <template #header>
      <div class="container-fluid">
        <BRow>
          <BCol>
            <h1>{{ $t('resetPasswordTitle') }}</h1>
          </BCol>
          <BCol :w="3">
            <LanguageSelector />
          </BCol>
        </BRow>
      </div>
    </template>
    <template #body>
      <BBusy :busy>
        <BLabeledInput :label="$t('emailAddress')" type="email" v-model="emailAddress" disabled />
        <BLabeledInput :label="$t('newPasswordField')" type="password" v-model="newPassword1" />
        <BLabeledInput :label="$t('confirmNewPasswordField')" type="password" v-model="newPassword2" />
      </BBusy>
    </template>
    <template #footer>
      <p v-if="newPassword2 !== newPassword1" class="text-danger">{{ $t('passwordsAreDifferent') }}</p>
      <BButton primary @click="resetPassword" :disabled="busy || newPassword1 === '' || newPassword2 !== newPassword1">{{ $t('resetPasswordButton') }}</BButton>
    </template>
  </BModal>
</template>
