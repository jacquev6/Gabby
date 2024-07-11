import { ref, reactive } from 'vue'


export interface ExerciseCreationHistory {
  previous: string | null
  current: string | null
  next: string | null
  empty: boolean
  suggestedNumber: string | null
  reset(): void
  push(id: string): void
  rewind(): void
  forward(): void
}

export function makeExerciseCreationHistory() {
  const previous: string[] = reactive([])
  const next: string[] = reactive([])
  let current = ref<string | null>(null)

  return {
    get previous() {
      return previous[previous.length - 1] || null
    },
    get current() {
      return current.value
    },
    get next() {
      return next[next.length - 1] || null
    },
    get empty() {
      return previous.length === 0 && current.value === null && next.length === 0
    },
    suggestedNumber: null,
    reset() {
      previous.length = 0
      next.length = 0
      this.suggestedNumber = null
    },
    push(id: string) {
      console.assert(next.length === 0)
      previous.push(id)
    },
    rewind() {
      if (current.value !== null) {
        next.push(current.value)
      }
      const newCurrent = previous.pop()
      console.assert(newCurrent !== undefined)
      current.value = newCurrent
    },
    forward() {
      console.assert(current.value !== null)
      previous.push(current.value)
      const newCurrent = next.pop()
      if (newCurrent === undefined) {
        current.value = null
      } else {
        current.value = newCurrent
      }
    },
  }
}
