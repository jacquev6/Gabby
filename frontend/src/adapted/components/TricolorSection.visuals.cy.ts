import TricolorSection from './TricolorSection.vue'
import type { Paragraph } from '$adapted/types'


const lipsum: Paragraph = {
  contents: [
    { kind: 'text', text: 'Lorem' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'ipsum' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'dolor' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'sit' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'amet' },
    { kind: 'text', text: ',' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'consectetur' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'adipiscing' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'elit' },
    { kind: 'text', text: '.' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'Mauris' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'nec' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'posuere' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'est' },
    { kind: 'text', text: ',' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'in' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'lacinia' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'nibh' },
    { kind: 'text', text: '.' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'Sed' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'auctor' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'id' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'tortor' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'id' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'aliquet' },
    { kind: 'text', text: '.' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'Nam' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'eu' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'nisi' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'et' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'risus' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'ultricies' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'pretium' },
    { kind: 'text', text: '.' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'Proin' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'imperdiet' },
    { kind: 'text', text: ',' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'erat' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'nec' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'ultrices' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'volutpat' },
    { kind: 'text', text: ',' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'justo' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'nunc' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'tincidunt' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'neque' },
    { kind: 'text', text: ',' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'et' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'faucibus' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'turpis' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'sapien' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'ac' },
    { kind: 'whitespace' },
    { kind: 'text', text: 'sem' },
    { kind: 'text', text: '.' },
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
        first: false,
        centered: false,
        tricolored: false,
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
      contents: [
        { kind: 'text', text: 'plain' },
        { kind: 'whitespace' },
        { kind: 'text', bold: true, text: 'bold' },
        { kind: 'whitespace' },
        { kind: 'text', italic: true, text: 'italic' },
        { kind: 'whitespace' },
        { kind: 'text', bold: true, italic: true, text: 'bolditalic' },
        { kind: 'whitespace' },
        { kind: 'passiveSequence', boxed: true, contents: [{ kind: 'text', text: 'boxed' }] },
        { kind: 'whitespace' },
        { kind: 'text', highlighted: 'yellow', text: 'highlighted' },
      ]
    }],
  )

  test(
    'basic-inputs',
    [
      { contents: [{ kind: 'multipleChoicesInput', choices: [[{ kind: 'text', text: 'alpha' }], [{ kind: 'text', text: 'bravo' }], [{ kind: 'text', text: 'charlie' }]] }] },
      { contents: [{ kind: 'freeTextInput' }] },
      { contents: [{ kind: 'selectableInput', colors: ['red', 'green', 'blue'], contents: [{ kind: 'text', text: 'selectable' }] }] },
    ],
    {
      steps: [
        () => { cy.get('span.main').click() },
        () => { cy.get('span.choice0').click() },
        () => { cy.get('span[contenteditable]').type('foobar') },
        () => { cy.get('span[data-cy="selectable"]').click() },
        () => { cy.get('span[data-cy="selectable"]').click() },
      ],
      viewportHeight: 432,
    },
  )

  test(
    'multiple-choices-options',
    [
      { contents: [{ kind: 'multipleChoicesInput', choices: [[{ kind: 'text', text: 'alpha' }], [{ kind: 'text', text: 'bravo' }], [{ kind: 'text', text: 'charlie' }]], show_choices_by_default: true }] },
      { contents: [{ kind: 'multipleChoicesInput', show_arrow_before: true, choices: [[{ kind: 'text', text: 'alpha' }], [{ kind: 'text', text: 'bravo' }], [{ kind: 'text', text: 'charlie' }]] }] },
    ],
    {
      viewportHeight: 600,
    },
  )

  test(
    'selectable-sentences',
    [{
      contents: [
        { kind: 'selectableInput', contents: [{ kind: 'text', text: 'Lorem' }, { kind: 'whitespace' }, { kind: 'text', text: 'ipsum' }, { kind: 'whitespace' }, { kind: 'text', text: 'dolor' }, { kind: 'text', text: '.' }], colors: ['red', 'green', 'blue'] },
        { kind: 'whitespace' },
        { kind: 'selectableInput', contents: [{ kind: 'text', text: 'Lorem' }, { kind: 'whitespace' }, { kind: 'text', text: 'ipsum' }, { kind: 'whitespace' }, { kind: 'text', text: 'dolor' }, { kind: 'text', text: '.' }], colors: ['red', 'green', 'blue'] },
        { kind: 'whitespace' },
        { kind: 'selectableInput', contents: [{ kind: 'text', text: 'Lorem' }, { kind: 'whitespace' }, { kind: 'text', text: 'ipsum' }, { kind: 'whitespace' }, { kind: 'text', text: 'dolor' }, { kind: 'text', text: '.' }], colors: ['red', 'green', 'blue'], boxed: true },
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
    },
  )

  test(
    'boxed-sentences',
    [{
      contents: [
        { kind: 'passiveSequence', contents: [{ kind: 'text', text: 'Lorem' }, { kind: 'whitespace' }, { kind: 'text', text: 'ipsum' }, { kind: 'whitespace' }, { kind: 'text', text: 'dolor' }, { kind: 'text', text: '.' }], boxed: true },
        { kind: 'whitespace' },
        { kind: 'passiveSequence', contents: [{ kind: 'text', text: 'Lorem' }, { kind: 'whitespace' }, { kind: 'text', text: 'ipsum' }, { kind: 'whitespace' }, { kind: 'text', text: 'dolor' }, { kind: 'text', text: '.' }], boxed: true },
        { kind: 'whitespace' },
        { kind: 'passiveSequence', contents: [{ kind: 'text', text: 'Lorem' }, { kind: 'whitespace' }, { kind: 'text', text: 'ipsum' }, { kind: 'whitespace' }, { kind: 'text', text: 'dolor' }, { kind: 'text', text: '.' }], boxed: true },
      ]
    }],
  )

  test(
    'stacked-multiple-choices',
    [
      {
        contents: [
          { kind: 'text', text: 'a' },
          { kind: 'text', text: '.' },
          { kind: 'whitespace' },
          {
            kind: 'sequence', vertical: true, contents: [
              { kind: 'sequence', contents: [{ kind: 'text', text: 'Lorem' }, { kind: 'whitespace' }, { kind: 'text', text: 'ipsum' }, { kind: 'whitespace' }, { kind: 'text', text: 'dolor' }, { kind: 'text', text: '.' }] },
              { kind: 'multipleChoicesInput', choices: [[{ kind: 'text', text: 'alpha' }], [{ kind: 'text', text: 'bravo' }], [{ kind: 'text', text: 'charlie' }]] },
            ]
          },
        ],
      },
      {
        contents: [
          { kind: 'text', text: 'b' },
          { kind: 'text', text: '.' },
          { kind: 'whitespace' },
          { kind: 'text', text: 'Lorem' },
          { kind: 'whitespace' },
          {
            kind: 'sequence', vertical: true, contents: [
              { kind: 'text', text: 'ipsum' },
              { kind: 'multipleChoicesInput', show_arrow_before: true, choices: [[{ kind: 'text', text: 'alpha' }], [{ kind: 'text', text: 'bravo' }], [{ kind: 'text', text: 'charlie' }]], show_choices_by_default: true },
            ]
          },
          { kind: 'whitespace' },
          { kind: 'text', text: 'dolor' },
          { kind: 'text', text: '.' },
        ],
      },
    ],
    {
      viewportHeight: 800,
    },
  )
})
