<script setup>
import { ref, reactive } from 'vue'

import { useApiStore } from '../../stores/api'
import { BBusy, BLabeledInput, BButton } from './bootstrap'


const api = useApiStore()

const pings = api.auto.getAll('pings')

const creatingPing = ref(false)
const newPingMessage = ref('')
async function createPing() {
  const message = newPingMessage.value !== '' ? newPingMessage.value : undefined
  creatingPing.value = true
  await api.client.post('ping', {message}, {'next': []})
  creatingPing.value = false
  newPingMessage.value = ''
  pings.refresh()
}

const patchingPing = reactive({})
async function setMessage(id) {
  patchingPing[id] = true
  await api.client.patch('ping', id, {message: 'Hello!'}, {})
  patchingPing[id] = undefined
}
async function resetMessage(id) {
  patchingPing[id] = true
  await api.client.patch('ping', id, {message: null}, {})
  patchingPing[id] = undefined
}
async function deletePing(id) {
  patchingPing[id] = true
  await api.client.delete('ping', id, {})
  patchingPing[id] = undefined
}
</script>

<template>
  <BBusy :busy="pings.loading">
    <ul v-if="pings.length">
      <li v-for="ping in pings" :key="ping.id">
        <BBusy :busy="!!patchingPing[ping.id]">
          {{ ping.id }} - {{ ping.attributes.createdAt }}<span v-if="ping.attributes.message">: {{ ping.attributes.message }}</span>
          <BButton sm secondary @click="setMessage(ping.id)">Set message</BButton>
          <BButton sm secondary @click="resetMessage(ping.id)">Reset message</BButton>
          <BButton sm secondary @click="deletePing(ping.id)">Delete</BButton>
          <template v-if="ping.relationships.prev">Prev: {{ ping.relationships.prev.id }}</template>
          <template v-if="ping.relationships.next.length">Next:<template v-for="next in ping.relationships.next">&nbsp;{{ next.id }}</template></template>
        </BBusy>
      </li>
    </ul>
    <p v-else>{{ $t('opinion.noPings') }}</p>
  </BBusy>
  <BBusy :busy="creatingPing">
    <BLabeledInput label="Message" v-model="newPingMessage"/>
    <BButton primary @click="createPing">{{ $t('opinion.ping') }}</BButton>
  </BBusy>
</template>

<!-- @todo Make https://vue-i18n.intlify.dev/guide/advanced/sfc.html work and move translations from locales/opinion to here -->
