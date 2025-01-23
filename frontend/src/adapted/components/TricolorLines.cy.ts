import TricolorLines from './TricolorLines.vue'


function makeSentence(prefix: string, length=26) {
  let sentence = `<span class="tricolorable">${prefix}A</span>`
  for (let i = 1; i < length; i++) {
    sentence += `<span><wbr/> <wbr/></span><span class="tricolorable">${prefix}${String.fromCharCode('A'.charCodeAt(0) + i)}</span>`
  }
  sentence += '<span class="tricolorable">.</span>'
  return sentence
}

const color1 = 'rgb(0, 0, 255)'
const color2 = 'rgb(255, 0, 0)'
const color3 = 'rgb(0, 204, 0)'

const slots = {
  default: `<p>${makeSentence('A')}${makeSentence('B')}${makeSentence('C')}</p><p>${makeSentence('D')}${makeSentence('E')}${makeSentence('F')}</p>`,
}

const mountOptions = {slots}

describe('TricolorLines', () => {
  before(console.clear)

  it('renders lines in alternating colors', () => {
    cy.mount(TricolorLines, mountOptions)

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
    cy.mount(TricolorLines, mountOptions)

    cy.viewport(400, 600)

    cy.get('span:contains("AA")').last().should('have.css', 'color', color1)
    cy.get('span:contains("AO")').last().should('have.css', 'color', color1)
    cy.get('span:contains("AP")').last().should('have.css', 'color', color2)
    cy.get('span:contains("BD")').last().should('have.css', 'color', color2)
    cy.get('span:contains("BE")').last().should('have.css', 'color', color3)
    cy.get('span:contains("BS")').last().should('have.css', 'color', color3)
    cy.get('span:contains("BT")').last().should('have.css', 'color', color1)
  })

  it('keeps full stop with last word', () => {
    const width = 254
    cy.viewport(width, 600)
    
    cy.mount(TricolorLines, {slots: {default: `<p>${makeSentence('A', 10)}</p>`}})

    cy.get('span:contains("AJ")').last().should('have.css', 'color', color1)
    cy.get('span:contains(".")').last().should('have.css', 'color', color1)

    cy.viewport(width - 1, 600)

    cy.get('span:contains("AJ")').last().should('have.css', 'color', color2)
    cy.get('span:contains(".")').last().should('have.css', 'color', color2)
  })

  it('colors single-token lines', () => {
    cy.viewport(200, 600)

    cy.mount(TricolorLines, {slots: {default: `<p><span class="tricolorable">abcdefghijkl</span><span><wbr/> <wbr/></span><span class="tricolorable">mnopqrstuvwxyz</span></p>`}})

    cy.get('span:contains("abcdefghijkl")').last().should('have.css', 'color', color1)
    cy.get('span:contains("mnopqrstuvwxyz")').last().should('have.css', 'color', color2)
  })

  it('uses only the .tricolorable spans for coloring', () => {
    cy.viewport(200, 600)

    cy.mount(TricolorLines, {slots: {default: `<p><span class="tricolorable">A</span> <span class="tricolorable">B</span> <span class="tricolorable">C</span> <span class="tricolorable">D</span> <span class="tricolorable">E</span> <span class="tricolorable">F</span> <span class="tricolorable">G</span> <span class="tricolorable">H</span> <span class="tricolorable">I</span> <span class="tricolorable">J</span> <span><span class="tricolorable">K</span> <span class="tricolorable">L</span> <span class="tricolorable">M</span> <span class="tricolorable">N</span> <span class="tricolorable">O</span> <span class="tricolorable">P</span></span> <span class="tricolorable">Q</span> <span class="tricolorable">R</span> <span class="tricolorable">S</span> <span class="tricolorable">T</span></p>`}})

    cy.get('span:contains("M")').last().should('have.css', 'color', color1)
    cy.get('span:contains("N")').last().should('have.css', 'color', color2)
  })
})
