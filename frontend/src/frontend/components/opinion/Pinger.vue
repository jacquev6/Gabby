<script setup lang="ts">
import { ref } from 'vue'

import { useApiStore } from '$frontend/stores/api'
import { BBusy, BLabeledInput, BButton } from './bootstrap'
import { type Ping } from '$frontend/types/api'


const api = useApiStore()

const pings = api.auto.getAll<Ping>('ping')

const creatingPing = ref(false)
const newPingMessage = ref('')
async function createPing() {
  const message = newPingMessage.value !== '' ? newPingMessage.value : undefined
  creatingPing.value = true
  await api.client.createOne<Ping>('ping', {message}, {next: []})
  creatingPing.value = false
  newPingMessage.value = ''
  await pings.refresh()
}

async function setMessage(ping: Ping) {
  await ping.patch({message: 'Hello!'}, {})
}
async function resetMessage(ping: Ping) {
  await ping.patch({message: null}, {})
}
async function deletePing(ping: Ping) {
  await ping.delete()
  await pings.refresh()
}
</script>

<template>
  <BBusy :busy="pings.loading">
    <ul v-if="pings.items.length">
      <template v-for="ping in pings.items" :key="ping.id">
        <li v-if="ping.exists">
          <BBusy :busy="ping.loading">
            {{ ping.id }} - {{ ping.attributes!.createdAt }}<span v-if="ping.attributes!.message">: {{ ping.attributes!.message }}</span>
            <BButton sm secondary @click="setMessage(ping)">Set message</BButton>
            <BButton sm secondary @click="resetMessage(ping)">Reset message</BButton>
            <BButton sm secondary @click="deletePing(ping)">Delete</BButton>
            <template v-if="ping.relationships!.prev">Prev: {{ ping.relationships!.prev.id }}</template>
            <template v-if="ping.relationships!.next.length">Next:<template v-for="next in ping.relationships!.next">&nbsp;{{ next.id }}</template></template>
          </BBusy>
        </li>
      </template>
    </ul>
    <p v-else>{{ $t('opinion.noPings') }}</p>
  </BBusy>
  <BBusy :busy="creatingPing">
    <BLabeledInput label="Message" v-model="newPingMessage"/>
    <BButton primary @click="createPing">{{ $t('opinion.ping') }}</BButton>
  </BBusy>
</template>

<!-- @todo Make https://vue-i18n.intlify.dev/guide/advanced/sfc.html work and move translations from locales/opinion to here -->
