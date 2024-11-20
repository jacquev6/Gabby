import { type SelectionRange, type Model as QuillModel, InlineEmbed } from './Quill.vue'
import WysiwygEditor, { basicFormats, makeModel, makeRange } from './WysiwygEditor.vue'


class InlEmbBlot extends InlineEmbed {
  static override blotName = 'inl-emb'
  static override tagName = 'inl-emb-blot'

  static override create(settings: {color: string}) {
    let node = super.create()
    node.setAttribute('style', `border: 1px solid ${settings.color}; `)
    node.setAttribute('data-settings', JSON.stringify(settings))
    return node
  }

  static value(node: HTMLElement) {
    const settings = node.getAttribute('data-settings')
    console.assert(settings !== null)
    return JSON.parse(settings)
  }
}

const formats = {
  ...basicFormats,
  'inlemb': {
    kind: 'embed' as const,
    blot: InlEmbBlot,
    make: () => '{embed}',
  },
}

describe("WysiwygEditor's makeModel", () => {
  before(console.clear)

  function test(delta: QuillModel, expected: string) {
    expect(makeModel(basicFormats, delta)).to.equal(expected)
  }

  it('makes a simple model', () => {
    test(
      [{insert: 'hello world\n', attributes: {}}],
      'hello world\n',
    )
  })

  it('makes a model with a bold word', () => {
    test(
      [{insert: 'hello', attributes: {bold: true}}, {insert: ' world\n', attributes: {}}],
      '{bold|hello} world\n',
    )
  })
})


describe("WysiwygEditor's makeRange", () => {
  before(console.clear)

  function test(delta: QuillModel, quillRange: SelectionRange, expectedText: string) {
    const range = makeRange(formats, delta, quillRange)
    expect(makeModel(formats, delta).slice(range.index, range.index + range.length)).to.equal(expectedText)
  }

  it('makes a range in a simple model', () => {
    test(
      [{insert: 'hello world\n', attributes: {}}],
      {index: 4, length: 3},
      'o w',
    )
  })

  it('makes a range after a bold', () => {
    test(
      [{insert: 'hello', attributes: {bold: true}}, {insert: ' world\n', attributes: {}}],
      {index: 7, length: 3},
      'orl',
    )
  })

  it('makes a range after a bold and an italic', () => {
    test(
      [{insert: 'he', attributes: {bold: true}}, {insert: 'l', attributes: {}}, {insert: 'lo', attributes: {italic: true}}, {insert: ' world\n', attributes: {}}],
      {index: 7, length: 3},
      'orl',
    )
  })

  it('makes a range just before a bold', () => {
    test(
      [{insert: 'hello ', attributes: {}}, {insert: 'world', attributes: {bold: true}}, {insert: '\n', attributes: {}}],
      {index: 2, length: 4},
      'llo ',
    )
  })

  it('makes a range to the first letter of a bold', () => {
    test(
      [{insert: 'hello ', attributes: {}}, {insert: 'world', attributes: {bold: true}}, {insert: ' blih\n', attributes: {}}],
      {index: 4, length: 3},
      'o {bold|world}',
    )
  })

  it('makes a range just after a bold', () => {
    test(
      [{insert: 'hello', attributes: {bold: true}}, {insert: ' world', attributes: {}}, {insert: '\n', attributes: {}}],
      {index: 5, length: 4},
      ' wor',
    )
  })

  it('makes a range from the last letter of a bold', () => {
    test(
      [{insert: 'hello', attributes: {bold: true}}, {insert: ' world', attributes: {}}, {insert: '\n', attributes: {}}],
      {index: 4, length: 5},
      '{bold|hello} wor',
    )
  })

  it('makes a range from the last letter of an italic to the first letter of a bold', () => {
    test(
      [{insert: 'blah ', attributes: {}}, {insert: 'hello', attributes: {italic: true}}, {insert: ' ', attributes: {}}, {insert: 'world', attributes: {bold: true}}, {insert: ' blih\n', attributes: {}}],
      {index: 9, length: 3},
      '{italic|hello} {bold|world}',
    )
  })

  it('makes a range from the first letter of an italic to the last letter of a bold', () => {
    test(
      [{insert: 'blah ', attributes: {}}, {insert: 'hello', attributes: {italic: true}}, {insert: ' ', attributes: {}}, {insert: 'world', attributes: {bold: true}}, {insert: ' blih\n', attributes: {}}],
      {index: 5, length: 11},
      '{italic|hello} {bold|world}',
    )
  })

  it('makes a range from before an italic to after a bold', () => {
    test(
      [{insert: 'blah ', attributes: {}}, {insert: 'hello', attributes: {italic: true}}, {insert: ' ', attributes: {}}, {insert: 'world', attributes: {bold: true}}, {insert: ' blih\n', attributes: {}}],
      {index: 3, length: 15},
      'h {italic|hello} {bold|world} b',
    )
  })

  it('makes a range after an inline embed', () => {
    test(
      [{insert: 'hello ', attributes: {}}, {insert: {'inlemb': true}}, {insert: ' world\n', attributes: {}}],
      {index: 8, length: 3},
      'wor',
    )
  })

  it('makes a range of just an inline embed', () => {
    test(
      [{insert: 'hello ', attributes: {}}, {insert: {'inlemb': true}}, {insert: ' world\n', attributes: {}}],
      {index: 6, length: 1},
      '{embed}',
    )
  })

  it('makes empty ranges around a bold', () => {
    for (let index = 0; index < 17; index++) {
      test(
        [{insert: 'hello ', attributes: {}}, {insert: 'world', attributes: {bold: true}}, {insert: ' blih\n', attributes: {}}],
        {index, length: 0},
        '',
      )
    }
  })

  it('makes empty ranges around an inline embed', () => {
    for (let index = 0; index < 14; index++) {
      test(
        [{insert: 'hello ', attributes: {}}, {insert: {'inlemb': true}}, {insert: ' world\n', attributes: {}}],
        {index, length: 0},
        '',
      )
    }
  })

  // @todo 'makes a range fully inside a bold'  // inside => we can return the actually selected part
})

describe('WysiwygEditor', () => {
  before(console.clear)

  it("updates its model", () => {
    let modelValue = 'hell\n\n'
    cy.mount(WysiwygEditor, {props: {
      label: 'Test',
      formats: {},
      modelValue,
      'onUpdate:modelValue': (m: string) => {modelValue = m},
      delta: [{insert: modelValue, attributes: {}}],
    }})
    cy.get('div.ql-editor').type('o').then(() => {
      expect(modelValue).to.equal('hell\no\n')
    })
  })

  it("adds characters before the trailing line end when typing at the end", () => {
    let modelValue = 'hell\n'
    cy.mount(WysiwygEditor, {props: {
      label: 'Test',
      formats: {},
      modelValue,
      'onUpdate:modelValue': (m: string) => {modelValue = m},
      delta: [{insert: modelValue, attributes: {}}],
    }})
    cy.get('div.ql-editor').type('o')
    cy.wait(0).then(() => {
      expect(modelValue).to.equal('hello\n')
    })
  })

  it("add characters at the start when typing at the start", () => {
    let modelValue = 'ello\n'
    cy.mount(WysiwygEditor, {props: {
      label: 'Test',
      formats: {},
      modelValue,
      'onUpdate:modelValue': (m: string) => {modelValue = m},
      delta: [{insert: modelValue, attributes: {}}],
    }})
    cy.get('div.ql-editor').type('{moveToStart}h').then(() => {
      expect(modelValue).to.equal('hello\n')
    })
  })

  it("keeps a freshly-added trailing line end", () => {
    let modelValue = 'hello\n'
    cy.mount(WysiwygEditor, {props: {
      label: 'Test',
      formats: {},
      modelValue,
      'onUpdate:modelValue': (m: string) => {modelValue = m},
      delta: [{insert: modelValue, attributes: {}}],
    }})
    cy.get('div.ql-editor').type('\n').then(() => {
      expect(modelValue).to.equal('hello\n\n')
    })
  })

  it("keeps an ever-present trailing line end", () => {
    let modelValue = 'ello\n\n'
    cy.mount(WysiwygEditor, {props: {
      label: 'Test',
      formats: {},
      modelValue,
      'onUpdate:modelValue': (m: string) => {modelValue = m},
      delta: [{insert: modelValue, attributes: {}}],
    }})
    cy.get('div.ql-editor').type('{moveToStart}h').then(() => {
      expect(modelValue).to.equal('hello\n\n')
    })
  })

  it("removes an ever-present trailing line end when deleting all", () => {
    let modelValue = 'hello\n\n'
    cy.mount(WysiwygEditor, {props: {
      label: 'Test',
      formats: {},
      modelValue,
      'onUpdate:modelValue': (m: string) => {modelValue = m},
      delta: [{insert: modelValue, attributes: {}}],
    }})
    cy.get('div.ql-editor').type('{selectAll}{del}').then(() => {
      expect(modelValue).to.equal('\n')
    })
  })
})
