import { loadFixtures, login, notBusy, traceRectangle, visit } from "./utils"


describe('Gabby', () => {
  before(() => {
    console.clear()
  })

  beforeEach(() => {
    login()
    loadFixtures('empty-text-extraction-textbook', 'empty-test-textbook')
    cy.viewport(1200, 1000)
  })

  function setupAliases() {
    cy.get('canvas').last().as('canvas')
    cy.get('label:contains("Number") + input').as('number')
    cy.get('label:contains("Adaptation type") + select').as('adaptationType')
    cy.get('label:contains("Instructions") + div.ql-container div.ql-editor').as('instructions')
    cy.get('label:contains("Wording") + div.ql-container div.ql-editor').as('wording')
  }

  it('removes the exercise number from the text', () => {
    visit('/project-fryrbl/textbook-ojsbmy/page-1/new-exercise', {pdf: 'test'})
    setupAliases()

    cy.get('@number').type('3')
    traceRectangle('@canvas', 50, 67, 94, 73)

    cy.get('textarea').should('have.value', 'Complète avec : le, une, un, des, tu, elles, ils. Puis, souligne les verbes.')

    cy.get('div:contains("Strip exercise number") >input').should('be.enabled').should('be.checked').uncheck()
    cy.get('textarea').should('have.value', '3 Complète avec : le, une, un, des, tu, elles, ils. Puis, souligne les verbes.')

    cy.get('div:contains("Strip exercise number") >input').should('be.enabled').should('not.be.checked').check()
    cy.get('textarea').should('have.value', 'Complète avec : le, une, un, des, tu, elles, ils. Puis, souligne les verbes.')
  })

  it('does not remove the exercise number from the text', () => {
    visit('/project-fryrbl/textbook-ojsbmy/page-1/new-exercise', {pdf: 'test'})
    setupAliases()

    cy.get('@number').type('4')  // Wrong number
    traceRectangle('@canvas', 50, 67, 94, 73)

    cy.get('textarea').should('have.value', '3 Complète avec : le, une, un, des, tu, elles, ils. Puis, souligne les verbes.')

    cy.get('div:contains("Strip exercise number") >input').should('be.disabled')
  })

  {
    const paragraphsInPdf = [
      [
        'Lorem ipsum dolor sit amet, consectetur',
        'adipiscing elit. Vivamus a iaculis nisl, a tempus',
        'urna. In porttitor eget neque nec pretium. Fusce',
        'vitae nulla magna. Suspendisse nec est sed est',
        'malesuada hendrerit tempus sagittis nibh.',
        'Aenean eu faucibus neque, ut tristique augue.',
      ],
      [
        'Curabitur fermentum egestas risus, nec fringilla',
        'sapien efficitur quis. Nam dictum blandit nulla',
        'sed lacinia. Nulla tempor sollicitudin facilisis.',
        'Sed non lobortis ante, ac tincidunt urna. Donec',
        'ac aliquet eros. Integer dictum gravida orci,',
        'interdum fringilla sem.',
      ],
      [
        'Aliquam luctus fringilla enim sit amet',
        'dignissim. Proin cursus, erat a commodo',
        'venenatis, lacus magna vehicula ante, sit amet',
        'ultrices tortor lectus eget lacus.',
      ],
    ]

    const linesInPdf = paragraphsInPdf.flat()
    const expectedParagraphs = paragraphsInPdf.map(lines => lines.join(' '))

    it('inserts correct line ends on left-aligned text with space between paragraphs', () => {
      visit('/project-xkopqm/textbook-klxufv/page-1/new-exercise', {pdf: 'text-extraction'})
      setupAliases()

      traceRectangle('@canvas', 7, 6, 49.5, 37)
      cy.get('button:contains("Wording")').click()
      notBusy()

      cy.get('@wording').find('p').should('have.length', expectedParagraphs.length).each(($el, index) => {
        expect($el.text()).to.equal(expectedParagraphs[index])
      })
    })

    it('inserts correct line ends on justified text with paragraphs ending with shorter lines', () => {
      visit('/project-xkopqm/textbook-klxufv/page-1/new-exercise', {pdf: 'text-extraction'})
      setupAliases()

      traceRectangle('@canvas', 50, 6, 93, 34)
      cy.get('button:contains("Wording")').click()
      notBusy()

      cy.get('@wording').find('p').should('have.length', expectedParagraphs.length).each(($el, index) => {
        expect($el.text()).to.equal(expectedParagraphs[index])
      })
    })

    it('keeps all line ends', () => {
      visit('/project-xkopqm/textbook-klxufv/page-1/new-exercise', {pdf: 'text-extraction'})
      setupAliases()

      traceRectangle('@canvas', 50, 6, 93, 34)

      cy.get('textarea').should('have.value', expectedParagraphs.join('\n'))

      cy.get('div:contains("Keep all line ends") >input').should('be.enabled').should('not.be.checked').check()
      cy.get('textarea').should('have.value', linesInPdf.join('\n'))

      cy.get('div:contains("Keep all line ends") >input').should('be.enabled').should('be.checked').uncheck()
      cy.get('textarea').should('have.value', expectedParagraphs.join('\n'))
    })
  }

  {
    const itemsInPdf = [
      [
        'Lorem ipsum dolor sit amet,',
        'consectetur adipiscing elit.',
      ],
      [
        'Vivamus a iaculis nisl, a',
        'tempus urna.',
      ],
      [
        'Curabitur fermentum egestas',
        'risus, nec fringilla sapien',
        'efficitur quis.',
      ],
    ]

    const expectedItems = itemsInPdf.map(lines => lines.join(' '))

    it('inserts correct line ends on list - a. b. c.', () => {
      visit('/project-xkopqm/textbook-klxufv/page-2/new-exercise', {pdf: 'text-extraction'})
      setupAliases()

      traceRectangle('@canvas', 7, 6, 36, 19)
      cy.get('button:contains("Wording")').click()
      notBusy()

      cy.get('@wording').find('p').should('have.length', expectedItems.length).each(($el, index) => {
        expect($el.text()).to.equal(['a', 'b', 'c'][index] + '. ' + expectedItems[index])
      })
    })

    it('inserts correct line ends on list - ◆', () => {
      visit('/project-xkopqm/textbook-klxufv/page-2/new-exercise', {pdf: 'text-extraction'})
      setupAliases()

      traceRectangle('@canvas', 37, 6, 63, 19)
      cy.get('button:contains("Wording")').click()
      notBusy()

      cy.get('@wording').find('p').should('have.length', expectedItems.length).each(($el, index) => {
        expect($el.text()).to.equal('◆ ' + expectedItems[index])
      })
    })

    it('inserts correct line ends on list - 1) 2) 3)', () => {
      visit('/project-xkopqm/textbook-klxufv/page-2/new-exercise', {pdf: 'text-extraction'})
      setupAliases()

      traceRectangle('@canvas', 64, 6, 91, 19)
      cy.get('button:contains("Wording")').click()
      notBusy()

      cy.get('@wording').find('p').should('have.length', expectedItems.length).each(($el, index) => {
        expect($el.text()).to.equal(['1', '2', '3'][index] + ') ' + expectedItems[index])
      })
    })

    it('disables lists detection', () => {
      visit('/project-xkopqm/textbook-klxufv/page-2/new-exercise', {pdf: 'text-extraction'})
      setupAliases()

      traceRectangle('@canvas', 7, 6, 36, 19)

      cy.get('textarea').should('have.value', expectedItems.map((item, index) => ['a', 'b', 'c'][index] + '. ' + item).join('\n'))

      cy.get('div:contains("Detect lists") >input').should('be.enabled').should('be.checked').uncheck()
      cy.get('textarea').should('have.value', expectedItems.map((item, index) => ['a', 'b', 'c'][index] + '. ' + item).join(' '))

      cy.get('div:contains("Detect lists") >input').should('be.enabled').should('not.be.checked').check()
      cy.get('textarea').should('have.value', expectedItems.map((item, index) => ['a', 'b', 'c'][index] + '. ' + item).join('\n'))

      cy.get('div:contains("Keep all line ends") >input').should('be.enabled').should('not.be.checked').check()
      cy.get('div:contains("Detect lists") >input').should('be.disabled')

      cy.get('div:contains("Keep all line ends") >input').should('be.enabled').should('be.checked').uncheck()
      cy.get('div:contains("Detect lists") >input').should('be.enabled')
    })
  }
})
