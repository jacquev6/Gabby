import { watch } from "vue"
import { useMagicKeys } from "@vueuse/core"


type Thunk = () => void

let nextClosableIndex = 0
const closables: {
  [key: number]: {
    withEscape: boolean
    withEnter: boolean
    close: Thunk
  }
} = {}

type Options = {
  withEscape?: boolean
  withEnter?: boolean
}
export default function closeWithKeyboard(close: Thunk, options: Options = {}): Thunk {
  const withEnter = options.withEnter ?? false
  const withEscape = options.withEscape ?? true

  const index = nextClosableIndex++
  closables[index] = {withEscape, withEnter, close}

  return () => {
    delete closables[index]
  }
}

const { escape, enter } = useMagicKeys()

watch([escape, enter], ([escape, enter]) => {
  if (Object.keys(closables).length > 0) {
    const index = Math.max(...Object.keys(closables).map(Number))
    const closable = closables[index]
    if (closable.withEscape && escape || closable.withEnter && enter) {
      closable.close()
    }
  }
})
