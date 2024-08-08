import { defineStore } from 'pinia'
import { type Ref, watch } from 'vue'


export const useGloballyBusyStore = defineStore('globallyBusy', {
  state: () => ({
    indicators: {} as Record<string, boolean>,
  }),
  getters: {
    busy(): boolean {
      return Object.values(this.indicators).some(ref => ref)
    },
    reasons(): string[] {
      return Object.entries(this.indicators).filter(([_, ref]) => ref).map(([reason, _]) => reason)
    },
  },
  actions: {
    register(reason: string, busy: Ref<boolean>): Ref<boolean> {
      this.indicators[reason] = busy.value
      watch(busy, (b) => { this.indicators[reason] = b })
      return busy
    },
  }
})
