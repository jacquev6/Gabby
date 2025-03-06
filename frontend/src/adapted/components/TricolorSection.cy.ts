import TricolorSection from './TricolorSection.vue'
import type { Paragraph } from '$adapted/types'


function makeToken(text: string) {
  return {kind: 'text' as const, text}
}

function makeSentence(prefix: string, length=26) {
  const contents: Paragraph['contents'] = [
    makeToken(prefix + 'A')
  ]
  for (let i = 1; i < length; i++) {
    contents.push({kind: 'whitespace'})
    contents.push(makeToken(prefix + String.fromCharCode('A'.charCodeAt(0) + i)))
  }
  contents.push(makeToken('.'))
  return contents
}

const color1 = 'rgb(0, 0, 255)'
const color2 = 'rgb(255, 0, 0)'
const color3 = 'rgb(0, 204, 0)'

const props = {
  paragraphs: [
    {contents: [...makeSentence('A'), {kind: 'whitespace'}, ...makeSentence('B'), {kind: 'whitespace'}, ...makeSentence('C')]},
    {contents: [...makeSentence('D'), {kind: 'whitespace'}, ...makeSentence('E'), {kind: 'whitespace'}, ...makeSentence('F')]},
  ] as Paragraph[],
  first: false,
  centered: false,
  tricolored: false,
  paragraphIndexOffset: 0,
  modelValue: {} as Record<string, any/* @todo Type */>,
}

const mountOptions = {props}

describe('TricolorSection', () => {
  before(console.clear)

  it('renders lines in alternating colors', () => {
    // @ts-ignore// Work around Cypress typing limitations
    cy.mount(TricolorSection, mountOptions)

    cy.viewport(1152, 1200)

    cy.get('span:contains("AA")').last().should('have.css', 'color', color1)
    cy.get('span:contains("AS")').last().should('have.css', 'color', color1)
    cy.get('span:contains("AT")').last().should('have.css', 'color', color2)
    cy.get('span:contains("BL")').last().should('have.css', 'color', color2)
    cy.get('span:contains("BM")').last().should('have.css', 'color', color3)
    cy.get('span:contains("CE")').last().should('have.css', 'color', color3)
    cy.get('span:contains("CF")').last().should('have.css', 'color', color1)
    cy.get('span:contains("CX")').last().should('have.css', 'color', color1)
    cy.get('span:contains("CY")').last().should('have.css', 'color', color2)
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

    cy.viewport(700, 1400)

    cy.get('span:contains("AA")').last().should('have.css', 'color', color1)
    cy.get('span:contains("AL")').last().should('have.css', 'color', color1)
    cy.get('span:contains("AM")').last().should('have.css', 'color', color2)
    cy.get('span:contains("AW")').last().should('have.css', 'color', color2)
    cy.get('span:contains("AX")').last().should('have.css', 'color', color3)
    cy.get('span:contains("BH")').last().should('have.css', 'color', color3)

    cy.viewport(880, 1400)

    cy.get('span:contains("AA")').last().should('have.css', 'color', color1)
    cy.get('span:contains("AO")').last().should('have.css', 'color', color1)
    cy.get('span:contains("AP")').last().should('have.css', 'color', color2)
    cy.get('span:contains("BC")').last().should('have.css', 'color', color2)
    cy.get('span:contains("BD")').last().should('have.css', 'color', color3)
    cy.get('span:contains("BQ")').last().should('have.css', 'color', color3)
    cy.get('span:contains("BR")').last().should('have.css', 'color', color1)
  })

  it('reacts to text changes', () => {
    // @ts-ignore// Work around Cypress typing limitations
    cy.mount(TricolorSection, mountOptions)
    cy.viewport(1140, 600)

    cy.vue().then((w) => w.setProps({
      paragraphs: [{contents: [
        ...makeSentence('A', 10), {kind: 'whitespace'},
        ...makeSentence('B', 10), {kind: 'whitespace'},
        ...makeSentence('C', 10), {kind: 'whitespace'},
        ...makeSentence('D', 10), {kind: 'whitespace'},
        ...makeSentence('E', 10), {kind: 'whitespace'},
        ...makeSentence('F', 10), {kind: 'whitespace'},
        ...makeSentence('G', 10), {kind: 'whitespace'},
        ...makeSentence('H', 10)
      ]}],
      first: false,
      centered: false,
      tricolored: false,
    }))

    cy.get('span:contains("AA")').last().should('have.css', 'color', color1)
    cy.get('span:contains("BI")').last().should('have.css', 'color', color1)
    cy.get('span:contains("BJ")').last().should('have.css', 'color', color2)
    cy.get('span:contains("DH")').last().should('have.css', 'color', color2)
    cy.get('span:contains("DI")').last().should('have.css', 'color', color3)
    cy.get('span:contains("FH")').last().should('have.css', 'color', color3)
    cy.get('span:contains("FI")').last().should('have.css', 'color', color1)
    cy.get('span:contains("HG")').last().should('have.css', 'color', color1)
    cy.get('span:contains("HH")').last().should('have.css', 'color', color2)
    cy.get('span:contains("HJ")').last().should('have.css', 'color', color2)
  })

  it('keeps full stop with last word', () => {
    const width = 566
    cy.viewport(width, 600)
    
    cy.mount(
      // @ts-ignore// Work around Cypress typing limitations
      TricolorSection,
      {
        props: {
          paragraphs: [
            {contents: makeSentence('A', 10)},
          ],
          first: false,
          centered: false,
          tricolored: false,
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
          paragraphs: [{
            contents: [makeToken('abcdefghijkl'), {kind: 'whitespace'}, makeToken('mnopqrstuvwxyz')],
          }],
          first: false,
          centered: false,
          tricolored: false,
          paragraphIndexOffset: 0,
          modelValue: [],
        },
      },
    )

    cy.get('span:contains("abcdefghijkl")').last().should('have.css', 'color', color1)
    cy.get('span:contains("mnopqrstuvwxyz")').last().should('have.css', 'color', color2)
  })
})
