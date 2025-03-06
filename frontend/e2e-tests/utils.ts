import { useApiStore } from '../src/frontend/stores/api'


export function loadFixtures(...name: string[]) {
  cy.request('POST', `/reset-for-tests/yes-im-sure?fixtures=${name.join(',')}`)
}

export function login(username: string = 'admin', password: string = 'password') {
  cy.wrap(useApiStore()).then(api => api.auth.login(username, password))
}

export function notBusy() {
  cy.get('div.busy', {timeout: 10_000}).should('not.exist')
}

export function loadPdf(name: string) {
  cy.get('input[type=file]').selectFile(`../pdf-examples/${name}.pdf`)
  notBusy()
}

export function visit(
  url: string,
  options: {
    locale?: string
    pdf?: string
  } = {}
) {
  Cypress.on('uncaught:exception', error => {
    if (error.message.includes('ResizeObserver loop completed with undelivered notifications.')) {
      // @todo Deep dive into this issue: avoid the error instead of ignoring it.
      // https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver#observation_errors
      return false
    } else {
      return true
    }
  })

  cy.visit(url)
  cy.get('select[data-cy="language"]').last().select(options.locale ?? 'en')
  notBusy()

  if (options.pdf !== undefined) {
    loadPdf(options.pdf)
  }

  cy.focused().blur()
}

// Coordinates are in percentage of the canvas, for stability
export function traceRectangle(alias: string, x1: number, y1: number, x2: number, y2: number, up=true) {
  cy.get<HTMLCanvasElement>(alias).then(canvas => {
    const w = canvas[0].width
    const h = canvas[0].height
    cy.get(alias).trigger('pointermove', x1 / 100 * w, y1 / 100 * h)
    cy.get(alias).trigger('pointerdown', x1 / 100 * w, y1 / 100 * h, { pointerId: 1 })
    cy.get(alias).trigger('pointermove', x2 / 100 * w, y2 / 100 * h)
    if (up) {
      cy.get(alias).trigger('pointerup', x2 / 100 * w, y2 / 100 * h, { pointerId: 1 })
    }
  })
}

export function selectRange(startNode: Node, startOffset: number, endNode: Node, endOffset: number) {
  cy.window().then(window => {
    cy.document().then(document => {
      var range = document.createRange()
      range.setStart(startNode, startOffset)
      range.setEnd(endNode, endOffset)

      var sel = window.getSelection()
      console.assert(sel !== null)
      sel.removeAllRanges()
      sel.addRange(range)
    })
  })
}

export function pressKey(key: string) {
  cy.document().trigger('keydown', {key})
  cy.wait(100)
  cy.document().trigger('keyup', {key})
}

export function pressEscape() {
  pressKey('Escape')
}

export function pressEnter() {
  pressKey('Enter')
}
