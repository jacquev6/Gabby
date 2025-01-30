import TricolorSection from './OldTricolorSection.vue'
import type { Paragraph } from '$adapted/types'


const lipsum: Paragraph = {
  tokens: [
    { type: 'plainText', text: 'Lorem' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'ipsum' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'dolor' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'sit' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'amet' },
    { type: 'plainText', text: ',' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'consectetur' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'adipiscing' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'elit' },
    { type: 'plainText', text: '.' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'Mauris' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'nec' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'posuere' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'est' },
    { type: 'plainText', text: ',' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'in' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'lacinia' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'nibh' },
    { type: 'plainText', text: '.' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'Sed' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'auctor' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'id' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'tortor' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'id' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'aliquet' },
    { type: 'plainText', text: '.' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'Nam' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'eu' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'nisi' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'et' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'risus' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'ultricies' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'pretium' },
    { type: 'plainText', text: '.' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'Proin' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'imperdiet' },
    { type: 'plainText', text: ',' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'erat' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'nec' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'ultrices' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'volutpat' },
    { type: 'plainText', text: ',' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'justo' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'nunc' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'tincidunt' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'neque' },
    { type: 'plainText', text: ',' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'et' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'faucibus' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'turpis' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'sapien' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'ac' },
    { type: 'whitespace' },
    { type: 'plainText', text: 'sem' },
    { type: 'plainText', text: '.' },
  ]
}

interface TestOptions {
  steps?: (() => undefined)[]
  viewportHeight?: number
}

function test(name: string, paragraphs: Paragraph[], options: TestOptions = {}) {
  const steps = options.steps ?? []
  const viewportHeight = options.viewportHeight ?? 200

  it(`renders ${name}`, () => {
    cy.viewport(800, viewportHeight)

    // @ts-ignore// Work around Cypress typing limitations
    cy.mount(TricolorSection, {
      props: {
        paragraphs,
        modelValue: {},
      }
    })

    cy.screenshot(`${name}-0`)

    for (let i = 0; i < steps.length; ++i) {
      steps[i]()
      cy.screenshot(`${name}-${i + 1}`)
    }
  })
}

describe('TricolorSection', () => {
  before(console.clear)

  test('lipsum', [lipsum, lipsum])

  test(
    'basic-formatting',
    [{
      tokens: [
        { type: 'plainText', text: 'plain' },
        { type: 'whitespace' },
        { type: 'passiveFormattedText', bold: true, italic: false, text: 'bold' },
        { type: 'whitespace' },
        { type: 'passiveFormattedText', bold: false, italic: true, text: 'italic' },
        { type: 'whitespace' },
        { type: 'passiveFormattedText', bold: true, italic: true, text: 'bolditalic' },
        { type: 'whitespace' },
        { type: 'boxedText', text: 'boxed' },
        { type: 'whitespace' },
        { type: 'selectedText', text: 'highlighted', color: 'yellow' },
      ]
    }],
  )

  test(
    'basic-inputs',
    [
      { tokens: [{ type: 'multipleChoicesInput', show_arrow_before: false, choices: ['alpha', 'bravo', 'charlie'], show_choices_by_default: false }] },
      { tokens: [{ type: 'freeTextInput' }] },
      { tokens: [{ type: 'selectableText', text: 'selectable', colors: ['red', 'green', 'blue'], boxed: false }] },
    ],
    {
      steps: [
        () => { cy.get('span.main').click() },
        () => { cy.get('span.choice0').click() },
        () => { cy.get('span[contenteditable]').type('foobar') },
        () => { cy.get('span[data-cy="selectable"]').click() },
        () => { cy.get('span[data-cy="selectable"]').click() },
      ],
    },
  )

  test(
    'multiple-choices-options',
    [
      { tokens: [{ type: 'multipleChoicesInput', show_arrow_before: false, choices: ['alpha', 'bravo', 'charlie'], show_choices_by_default: true }] },
      { tokens: [{ type: 'multipleChoicesInput', show_arrow_before: true, choices: ['alpha', 'bravo', 'charlie'], show_choices_by_default: false }] },
    ],
    {
      viewportHeight: 600,
    },
  )

  test(
    'selectable-sentences',
    [{
      tokens: [
        { type: 'selectable', contents: [{ type: 'plainText', text: 'Lorem' }, { type: 'whitespace' }, { type: 'plainText', text: 'ipsum' }, { type: 'whitespace' }, { type: 'plainText', text: 'dolor' }, { type: 'plainText', text: '.' }], colors: ['red', 'green', 'blue'], boxed: false },
        { type: 'whitespace' },
        { type: 'selectable', contents: [{ type: 'plainText', text: 'Lorem' }, { type: 'whitespace' }, { type: 'plainText', text: 'ipsum' }, { type: 'whitespace' }, { type: 'plainText', text: 'dolor' }, { type: 'plainText', text: '.' }], colors: ['red', 'green', 'blue'], boxed: false },
        { type: 'whitespace' },
        { type: 'selectable', contents: [{ type: 'plainText', text: 'Lorem' }, { type: 'whitespace' }, { type: 'plainText', text: 'ipsum' }, { type: 'whitespace' }, { type: 'plainText', text: 'dolor' }, { type: 'plainText', text: '.' }], colors: ['red', 'green', 'blue'], boxed: true },
      ]
    }],
    {
      steps: [
        () => { cy.get('span[data-cy="selectable"]').eq(0).click() },
        () => {
          cy.get('span[data-cy="selectable"]').eq(2).click()
          cy.get('span[data-cy="selectable"]').eq(2).click()
        },
      ],
    }
  )

  test(
    'boxed-sentences',
    [{
      tokens: [
        { type: 'boxed', contents: [{ type: 'plainText', text: 'Lorem' }, { type: 'whitespace' }, { type: 'plainText', text: 'ipsum' }, { type: 'whitespace' }, { type: 'plainText', text: 'dolor' }, { type: 'plainText', text: '.' }] },
        { type: 'whitespace' },
        { type: 'boxed', contents: [{ type: 'plainText', text: 'Lorem' }, { type: 'whitespace' }, { type: 'plainText', text: 'ipsum' }, { type: 'whitespace' }, { type: 'plainText', text: 'dolor' }, { type: 'plainText', text: '.' }] },
        { type: 'whitespace' },
        { type: 'boxed', contents: [{ type: 'plainText', text: 'Lorem' }, { type: 'whitespace' }, { type: 'plainText', text: 'ipsum' }, { type: 'whitespace' }, { type: 'plainText', text: 'dolor' }, { type: 'plainText', text: '.' }] },
      ]
    }],
  )

  test(
    'stacked-multiple-choices',
    [
      {
        tokens: [
          { type: 'plainText', text: 'a' },
          { type: 'plainText', text: '.' },
          { type: 'whitespace' },
          {
            type: 'stack', contents: [
              { type: 'line', contents: [{ type: 'plainText', text: 'Lorem' }, { type: 'whitespace' }, { type: 'plainText', text: 'ipsum' }, { type: 'whitespace' }, { type: 'plainText', text: 'dolor' }, { type: 'plainText', text: '.' }] },
              { type: 'multipleChoicesInput', show_arrow_before: false, choices: ['alpha', 'bravo', 'charlie'], show_choices_by_default: false },
            ],
          },
        ],
      },
      {
        tokens: [
          { type: 'plainText', text: 'b' },
          { type: 'plainText', text: '.' },
          { type: 'whitespace' },
          { type: 'plainText', text: 'Lorem' },
          { type: 'whitespace' },
          {
            type: 'stack', contents: [
              { type: 'plainText', text: 'ipsum' },
              { type: 'multipleChoicesInput', show_arrow_before: true, choices: ['alpha', 'bravo', 'charlie'], show_choices_by_default: true },
            ],
          },
          { type: 'whitespace' },
          { type: 'plainText', text: 'dolor' },
          { type: 'plainText', text: '.' },
        ],
      },
    ],
    {
      viewportHeight: 800,
    },
  )
})
