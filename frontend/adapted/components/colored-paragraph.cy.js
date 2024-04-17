import { h } from 'vue'

import ColoredParagraph from './colored-paragraph.vue'


const text = 'AA AB AC AD AE AF AG AH AI AJ AK AL AM AN AO AP AQ AR AS AT AU AV AW AX AY AZ. BA BB BC BD BE BF BG BH BI BJ BK BL BM BN BO BP BQ BR BS BT BU BV BW BX BY BZ. CA CB CC CD CE CF CG CH CI CJ CK CL CM CN CO CP CQ CR CS CT CU CV CW CX CY CZ. DA DB DC DD DE DF DG DH DI DJ DK DL DM DN DO DP DQ DR DS DT DU DV DW DX DY DZ. EA EB EC ED EE EF EG EH EI EJ EK EL EM EN EO EP EQ ER ES ET EU EV EW EX EY EZ. FA FB FC FD FE FF FG FH FI FJ FK FL FM FN FO FP FQ FR FS FT FU FV FW FX FY FZ.'
const color1 = 'rgb(255, 0, 0)'
const color2 = 'rgb(0, 128, 0)'
const color3 = 'rgb(0, 0, 255)'

describe('ColoredParagraph', () => {
  before(console.clear)

  it('renders lines in alternating colors', () => {
    cy.mount(ColoredParagraph, {props: {text}})

    cy.get('span:contains("AA")').should('have.css', 'color', color1)
    cy.get('span:contains("AT")').should('have.css', 'color', color1)
    cy.get('span:contains("AU")').should('have.css', 'color', color2)
    cy.get('span:contains("BM")').should('have.css', 'color', color2)
    cy.get('span:contains("BN")').should('have.css', 'color', color3)
    cy.get('span:contains("CF")').should('have.css', 'color', color3)
    cy.get('span:contains("CG")').should('have.css', 'color', color1)
  })

  it('reacts to window size changes', () => {
    cy.mount(ColoredParagraph, {props: {text}})

    cy.viewport(400, 600)

    cy.get('span:contains("AA")').should('have.css', 'color', color1)
    cy.get('span:contains("AO")').should('have.css', 'color', color1)
    cy.get('span:contains("AP")').should('have.css', 'color', color2)
    cy.get('span:contains("BD")').should('have.css', 'color', color2)
    cy.get('span:contains("BE")').should('have.css', 'color', color3)
    cy.get('span:contains("BS")').should('have.css', 'color', color3)
    cy.get('span:contains("BT")').should('have.css', 'color', color1)
  })

  it('reacts to text changes', () => {
    cy.mount(ColoredParagraph, {props: {text}})

    cy.vue().then((w) => w.setProps({text: 'A0 A1 A2 A3 A4 A5 A6 A7 A8 A9. B0 B1 B2 B3 B4 B5 B6 B7 B8 B9. C0 C1 C2 C3 C4 C5 C6 C7 C8 C9. D0 D1 D2 D3 D4 D5 D6 D7 D8 D9. E0 E1 E2 E3 E4 E5 E6 E7 E8 E9. F0 F1 F2 F3 F4 F5 F6 F7 F8 F9. G0 G1 G2 G3 G4 G5 G6 G7 G8 G9. H0 H1 H2 H3 H4 H5 H6 H7 H8 H9. I0 I1 I2 I3 I4 I5 I6 I7 I8 I9. J0 J1 J2 J3 J4 J5 J6 J7 J8 J9. K0 K1 K2 K3 K4 K5 K6 K7 K8 K9. L0 L1 L2 L3 L4 L5 L6 L7 L8 L9. M0 M1 M2 M3 M4 M5 M6 M7 M8 M9. N0 N1 N2 N3 N4 N5 N6 N7 N8 N9. O0 O1 O2 O3 O4 O5 O6 O7 O8 O9. P0 P1 P2 P3 P4 P5 P6 P7 P8 P9. Q0 Q1 Q2 Q3 Q4 Q5 Q6 Q7 Q8 Q9.'}))

    cy.get('span:contains("A0")').should('have.css', 'color', color1)
    cy.get('span:contains("B9")').should('have.css', 'color', color1)
    cy.get('span:contains("C0")').should('have.css', 'color', color2)
    cy.get('span:contains("D8")').should('have.css', 'color', color2)
    cy.get('span:contains("D9")').should('have.css', 'color', color3)
    cy.get('span:contains("F9")').should('have.css', 'color', color3)
    cy.get('span:contains("G0")').should('have.css', 'color', color1)
  })

  it('keeps full stop with last word', () => {
    const width = 263
    cy.viewport(width, 600)
    
    cy.mount(ColoredParagraph, {props: {text: 'A single blah blah blah sentence.'}})

    cy.get('span:contains("sentence")').should('have.css', 'color', color1)
    cy.get('span:contains(".")').should('have.css', 'color', color1)

    cy.viewport(width - 1, 600)

    cy.get('span:contains("sentence")').should('have.css', 'color', color2)
    cy.get('span:contains(".")').should('have.css', 'color', color2)
  })

  it('colors single-token lines', () => {
    cy.viewport(200, 600)

    cy.mount(ColoredParagraph, {props: {text: 'abcdefghijkl mnopqrstuvwxyz.'}})

    cy.get('span:contains("abcdefghijkl")').should('have.css', 'color', color1)
    cy.get('span:contains("mnopqrstuvwxyz")').should('have.css', 'color', color2)
  })

  it('renders lines in alternating colors even with higher slots', () => {
    cy.mount(
      ColoredParagraph,
      {
        props: {text},
        slots: {
          default: ({token}) => h(
            'span',
            {
              style: {
                'border-top': '2px solid black',
                'border-bottom': '2px solid blue',
              }
            },
            token.text,
          ),
        },
      },
    )

    cy.get('span:contains("AA")').should('have.css', 'color', color1)
    cy.get('span:contains("AT")').should('have.css', 'color', color1)
    cy.get('span:contains("AU")').should('have.css', 'color', color2)
    cy.get('span:contains("BM")').should('have.css', 'color', color2)
    cy.get('span:contains("BN")').should('have.css', 'color', color3)
    cy.get('span:contains("CF")').should('have.css', 'color', color3)
    cy.get('span:contains("CG")').should('have.css', 'color', color1)
  })
})
