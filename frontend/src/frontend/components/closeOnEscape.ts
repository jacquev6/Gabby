import { watch } from "vue"
import { useMagicKeys } from "@vueuse/core"


type Thunk = () => void

let nextClosableIndex = 0
const closables: {[key: number]: Thunk} = {}

export default function closeOnEscape(close: Thunk): Thunk {
  const index = nextClosableIndex++
  closables[index] = close
  console.log('inserted', index)

  return () => {
    delete closables[index]
    console.log('deleted', index)
  }
}

const { escape } = useMagicKeys()

watch(escape, pressed => {
  if (pressed && Object.keys(closables).length > 0) {
    const index = Math.max(...Object.keys(closables).map(Number))
    closables[index]()
  }
})
