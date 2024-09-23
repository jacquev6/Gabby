import TricolorSection from './TricolorSection.vue'
import type { Paragraph } from '$adapted/types'


function makeToken(text: string) {
  return {type: 'plainText' as const, text}
}

function makeSentence(prefix: string, length=26) {
  const tokens: Paragraph['sentences'][number]['tokens'] = [
    makeToken(prefix + 'A')
  ]
  for (let i = 1; i < length; i++) {
    tokens.push({type: 'whitespace'})
    tokens.push(makeToken(prefix + String.fromCharCode('A'.charCodeAt(0) + i)))
  }
  tokens.push(makeToken('.'))
  return {tokens}
}

const color1 = 'rgb(255, 0, 0)'
const color2 = 'rgb(0, 0, 255)'
const color3 = 'rgb(0, 204, 0)'

const props = {
  paragraphs: [
    {sentences: [makeSentence('A'), makeSentence('B'), makeSentence('C')]},
    {sentences: [makeSentence('D'), makeSentence('E'), makeSentence('F')]},
  ] as Paragraph[],
  paragraphIndexOffset: 0,
  modelValue: {} as Record<string, any/* @todo Type */>,
}

const mountOptions = {props}

describe('TricolorSection', () => {
  before(console.clear)

  it('renders lines in alternating colors', () => {
    // @ts-ignore// Work around Cypress typing limitations
    cy.mount(TricolorSection, mountOptions)

    cy.viewport(990, 1200)

    cy.get('span:contains("AA")').last().should('have.css', 'color', color1)
    cy.get('span:contains("AT")').last().should('have.css', 'color', color1)
    cy.get('span:contains("AU")').last().should('have.css', 'color', color2)
    cy.get('span:contains("BM")').last().should('have.css', 'color', color2)
    cy.get('span:contains("BN")').last().should('have.css', 'color', color3)
    cy.get('span:contains("CF")').last().should('have.css', 'color', color3)
    cy.get('span:contains("CG")').last().should('have.css', 'color', color1)
    cy.get('span:contains("CY")').last().should('have.css', 'color', color1)
    cy.get('span:contains("CZ")').last().should('have.css', 'color', color2)

    cy.get('span:contains("DA")').last().should('have.css', 'color', color3)
    cy.get('span:contains("DR")').last().should('have.css', 'color', color3)
    cy.get('span:contains("DS")').last().should('have.css', 'color', color1)
    cy.get('span:contains("EL")').last().should('have.css', 'color', color1)
    cy.get('span:contains("EM")').last().should('have.css', 'color', color2)
    cy.get('span:contains("FF")').last().should('have.css', 'color', color2)
    cy.get('span:contains("FG")').last().should('have.css', 'color', color3)
    cy.get('span:contains("FZ")').last().should('have.css', 'color', color3)
  })

  it('reacts to window size changes', () => {
    // @ts-ignore// Work around Cypress typing limitations
    cy.mount(TricolorSection, mountOptions)

    cy.viewport(780, 1400)

    cy.get('span:contains("AA")').last().should('have.css', 'color', color1)
    cy.get('span:contains("AO")').last().should('have.css', 'color', color1)
    cy.get('span:contains("AP")').last().should('have.css', 'color', color2)
    cy.get('span:contains("BD")').last().should('have.css', 'color', color2)
    cy.get('span:contains("BE")').last().should('have.css', 'color', color3)
    cy.get('span:contains("BS")').last().should('have.css', 'color', color3)
    cy.get('span:contains("BT")').last().should('have.css', 'color', color1)
  })

  it('reacts to text changes', () => {
    // @ts-ignore// Work around Cypress typing limitations
    cy.mount(TricolorSection, mountOptions)
    cy.viewport(995, 600)

    cy.vue().then((w) => w.setProps({paragraphs: [{sentences: [
      makeSentence('A', 10),
      makeSentence('B', 10),
      makeSentence('C', 10),
      makeSentence('D', 10),
      makeSentence('E', 10),
      makeSentence('F', 10),
      makeSentence('G', 10),
      makeSentence('H', 10),
    ]}]}))

    cy.get('span:contains("AA")').last().should('have.css', 'color', color1)
    cy.get('span:contains("BJ")').last().should('have.css', 'color', color1)
    cy.get('span:contains("CA")').last().should('have.css', 'color', color2)
    cy.get('span:contains("DI")').last().should('have.css', 'color', color2)
    cy.get('span:contains("DJ")').last().should('have.css', 'color', color3)
    cy.get('span:contains("FJ")').last().should('have.css', 'color', color3)
    cy.get('span:contains("GA")').last().should('have.css', 'color', color1)
    cy.get('span:contains("HH")').last().should('have.css', 'color', color1)
    cy.get('span:contains("HI")').last().should('have.css', 'color', color2)
    cy.get('span:contains("HJ")').last().should('have.css', 'color', color2)
  })

  it('keeps full stop with last word', () => {
    const width = 491
    cy.viewport(width, 600)
    
    cy.mount(
      // @ts-ignore// Work around Cypress typing limitations
      TricolorSection,
      {
        props: {
          paragraphs: [
            {sentences: [makeSentence('A', 10)]},
          ],
          paragraphIndexOffset: 0,
          modelValue: [],
        },
      },
    )

    cy.get('span:contains("AJ")').last().should('have.css', 'color', color1)
    cy.get('span:contains(".")').last().should('have.css', 'color', color1)

    cy.viewport(width - 1, 600)

    cy.get('span:contains("AJ")').last().should('have.css', 'color', color2)
    cy.get('span:contains(".")').last().should('have.css', 'color', color2)
  })

  it('colors single-token lines', () => {
    cy.viewport(400, 600)

    cy.mount(
      // @ts-ignore// Work around Cypress typing limitations
      TricolorSection,
      {
        props: {
          paragraphs: [{sentences: [{
            tokens: [makeToken('abcdefghijkl'), makeToken(' '), makeToken('mnopqrstuvwxyz')],
          }]}],
          paragraphIndexOffset: 0,
          modelValue: [],
        },
      },
    )

    cy.get('span:contains("abcdefghijkl")').last().should('have.css', 'color', color1)
    cy.get('span:contains("mnopqrstuvwxyz")').last().should('have.css', 'color', color2)
  })
})
