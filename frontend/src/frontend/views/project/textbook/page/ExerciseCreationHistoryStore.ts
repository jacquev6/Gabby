import { defineStore } from 'pinia'


export const useExerciseCreationHistoryStore = defineStore('exerciseCreationHistory', {
  state: () => ({
    _previous: [] as string[],
    _next: [] as string[],
    _current: null as string | null,
    suggestedNumber: null as string | null,
  }),
  getters: {
    previous(): string | null {
      return this._previous[this._previous.length - 1] || null
    },
    current(): string | null {
      return this._current
    },
    next(): string | null {
      return this._next[this._next.length - 1] || null
    },
    empty(): boolean {
      return this._previous.length === 0 && this._current === null && this._next.length === 0
    },
  },
  actions: {
    reset() {
      this._previous.length = 0
      this._next.length = 0
      this._current = null
      this.suggestedNumber = null
    },
    push(id: string) {
      console.assert(this._next.length === 0)
      this._previous.push(id)
    },
    rewind() {
      if (this._current !== null) {
        this._next.push(this._current)
      }
      const newCurrent = this._previous.pop()
      console.assert(newCurrent !== undefined)
      this._current = newCurrent
    },
    forward() {
      console.assert(this._current !== null)
      this._previous.push(this._current)
      const newCurrent = this._next.pop()
      if (newCurrent === undefined) {
        this._current = null
      } else {
        this._current = newCurrent
      }
    },
  },
})
