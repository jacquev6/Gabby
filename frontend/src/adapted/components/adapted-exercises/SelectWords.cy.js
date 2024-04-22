import SelectWords from './SelectWords.vue'


const wording = 'AA AB AC AD AE AF AG AH AI AJ AK AL AM AN AO AP AQ AR AS AT AU AV AW AX AY AZ. BA BB BC BD BE BF BG BH BI BJ BK BL BM BN BO BP BQ BR BS BT BU BV BW BX BY BZ. CA CB CC CD CE CF CG CH CI CJ CK CL CM CN CO CP CQ CR CS CT CU CV CW CX CY CZ. DA DB DC DD DE DF DG DH DI DJ DK DL DM DN DO DP DQ DR DS DT DU DV DW DX DY DZ. EA EB EC ED EE EF EG EH EI EJ EK EL EM EN EO EP EQ ER ES ET EU EV EW EX EY EZ. FA FB FC FD FE FF FG FH FI FJ FK FL FM FN FO FP FQ FR FS FT FU FV FW FX FY FZ. GA GB GC GD GE GF GG GH GI GJ GK GL GM GN GO GP GQ GR GS GT GU GV GW GX GY GZ. HA HB HC HD HE HF HG HH HI HJ HK HL HM HN HO HP HQ HR HS HT HU HV HW HX HY HZ. IA IB IC ID IE IF IG IH II IJ IK IL IM IN IO IP IQ IR IS IT IU IV IW IX IY IZ. JA JB JC JD JE JF JG JH JI JJ JK JL JM JN JO JP JQ JR JS JT JU JV JW JX JY JZ. KA KB KC KD KE KF KG KH KI KJ KK KL KM KN KO KP KQ KR KS KT KU KV KW KX KY KZ. LA LB LC LD LE LF LG LH LI LJ LK LL LM LN LO LP LQ LR LS LT LU LV LW LX LY LZ. MA MB MC MD ME MF MG MH MI MJ MK ML MM MN MO MP MQ MR MS MT MU MV MW MX MY MZ. NA NB NC ND NE NF NG NH NI NJ NK NL NM NN NO NP NQ NR NS NT NU NV NW NX NY NZ. OA OB OC OD OE OF OG OH OI OJ OK OL OM ON OO OP OQ OR OS OT OU OV OW OX OY OZ. PA PB PC PD PE PF PG PH PI PJ PK PL PM PN PO PP PQ PR PS PT PU PV PW PX PY PZ. QA QB QC QD QE QF QG QH QI QJ QK QL QM QN QO QP QQ QR QS QT QU QV QW QX QY QZ.'
const otherWording = 'A0 A1 A2 A3 A4 A5 A6 A7 A8 A9. B0 B1 B2 B3 B4 B5 B6 B7 B8 B9. C0 C1 C2 C3 C4 C5 C6 C7 C8 C9. D0 D1 D2 D3 D4 D5 D6 D7 D8 D9. E0 E1 E2 E3 E4 E5 E6 E7 E8 E9. F0 F1 F2 F3 F4 F5 F6 F7 F8 F9. G0 G1 G2 G3 G4 G5 G6 G7 G8 G9. H0 H1 H2 H3 H4 H5 H6 H7 H8 H9. I0 I1 I2 I3 I4 I5 I6 I7 I8 I9. J0 J1 J2 J3 J4 J5 J6 J7 J8 J9. K0 K1 K2 K3 K4 K5 K6 K7 K8 K9. L0 L1 L2 L3 L4 L5 L6 L7 L8 L9. M0 M1 M2 M3 M4 M5 M6 M7 M8 M9. N0 N1 N2 N3 N4 N5 N6 N7 N8 N9. O0 O1 O2 O3 O4 O5 O6 O7 O8 O9. P0 P1 P2 P3 P4 P5 P6 P7 P8 P9. Q0 Q1 Q2 Q3 Q4 Q5 Q6 Q7 Q8 Q9.'
const transparent = 'rgba(0, 0, 0, 0)'
const color1 = 'rgb(102, 194, 165)'
const color2 = 'rgb(199, 177, 139)'
const color3 = 'rgb(179, 179, 179)'

describe('SelectWords', () => {
  before(console.clear)

  it('renders clickable words', () => {
    cy.mount(SelectWords, {props: {exercise: {wording, adaptation: {colors: 3}}}})

    cy.get('span:contains("AA")').last().should('have.css', 'background-color', transparent)
    cy.get('span:contains("AA")').last().click()
    cy.get('span:contains("AA")').last().should('have.css', 'background-color', color1)
    cy.get('span:contains("AA")').last().click()
    cy.get('span:contains("AA")').last().should('have.css', 'background-color', color2)
    cy.get('span:contains("AA")').last().click()
    cy.get('span:contains("AA")').last().should('have.css', 'background-color', color3)
    cy.get('span:contains("AA")').last().click()
    cy.get('span:contains("AA")').last().should('have.css', 'background-color', transparent)

    cy.get('span:contains("BU")').last().should('have.css', 'background-color', transparent)
    cy.get('span:contains("BU")').last().click()
    cy.get('span:contains("BU")').last().should('have.css', 'background-color', color1)
    cy.get('span:contains("BU")').last().click()
    cy.get('span:contains("BU")').last().should('have.css', 'background-color', color2)
    cy.get('span:contains("BU")').last().click()
    cy.get('span:contains("BU")').last().should('have.css', 'background-color', color3)
    cy.get('span:contains("BU")').last().click()
    cy.get('span:contains("BU")').last().should('have.css', 'background-color', transparent)
  })

  it('resets colors on text change', () => {
    cy.mount(SelectWords, {props: {exercise: {wording, adaptation: {colors: 3}}}})

    cy.get('span:contains("AA")').last().click()

    cy.vue().then((w) => w.setProps({exercise: {wording: otherWording, adaptation: {colors: 3}}}))

    cy.get('span:contains("A0")').last().should('have.css', 'background-color', transparent)
  })
})
