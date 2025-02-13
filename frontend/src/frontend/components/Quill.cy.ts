import Quill, { type Model, InlineBlot, BoldBlot, ItalicBlot, BlockEmbed, InlineEmbed } from './Quill.vue'


class StrBlot extends InlineBlot {
  static override blotName = 'string'
  static override tagName = 'string-blot'

  static override create(s: string) {
    let node = super.create()
    node.setAttribute('data-s', s)
    return node
  }

  static override formats(node: HTMLElement) {
    return node.getAttribute('data-s')
  }
}

class DividerBlot extends BlockEmbed {
  static override blotName = 'divider'
  static override tagName = 'hr'
}

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

describe('Quill', () => {
  before(console.clear)

  it('renders its model', () => {
    cy.mount(Quill, {props: {
      blots: [BoldBlot, ItalicBlot],
      compatibleFormats: [],
      contagiousFormats: [],
      modelValue: [
        {insert: '1-plain', attributes: {}},
        {insert: '2-bold', attributes: {bold: true}},
        {insert: '3-italic', attributes: {italic: true}},
        {insert: '4-bold-italic', attributes: {bold: true, italic: true}},
        {insert: '\n', attributes: {}},
      ],
    }})

    cy.get(':contains("1-plain")').last().should('have.css', 'font-weight', '400')
    cy.get(':contains("2-bold")').last().should('have.css', 'font-weight', '700')
    cy.get(':contains("3-italic")').last().should('have.css', 'font-weight', '400')
    cy.get(':contains("4-bold-italic")').last().should('have.css', 'font-weight', '700')

    cy.get(':contains("1-plain")').last().should('not.have.css', 'font-style', 'italic')
    cy.get(':contains("2-bold")').last().should('not.have.css', 'font-style', 'italic')
    cy.get(':contains("3-italic")').last().should('have.css', 'font-style', 'italic')
    cy.get(':contains("4-bold-italic")').last().should('have.css', 'font-style', 'italic')
  })

  it('updates its model when typing', () => {
    let modelValue: Model = []
    cy.mount(Quill, {props: {
      blots: [BoldBlot, ItalicBlot],
      compatibleFormats: [],
      contagiousFormats: [],
      modelValue,
      'onUpdate:modelValue': (m: Model) => { modelValue = m },
    }})
    cy.get('div.ql-editor').type('plain text with spaces').then(() => {
      expect(modelValue).to.deep.equal([{insert: 'plain text with spaces\n', attributes: {}}])
    })
  })

  function selectRange(startNode: Node, startOffset: number, endNode: Node, endOffset: number) {
    var range = document.createRange()
    range.setStart(startNode, startOffset)
    range.setEnd(endNode, endOffset)

    var sel = window.getSelection()
    console.assert(sel !== null)
    sel.removeAllRanges()
    sel.addRange(range)
  }

  it('adds a boolean format to the selection', () => {
    let modelValue: Model = [{insert: 'abcdefghi', attributes: {}}]
    cy.mount(Quill, {props: {
      blots: [BoldBlot, ItalicBlot],
      compatibleFormats: [],
      contagiousFormats: [],
      modelValue,
      'onUpdate:modelValue': (m: Model) => { modelValue = m },
    }})
    cy.get('div.ql-editor').focus()
    cy.get('div.ql-editor > p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 3, node, 6)
    })
    cy.vue<typeof Quill>()
      .then(w => w.componentVM.toggle('bold'))
      .then(() => {
        expect(modelValue).to.deep.equal([
          {insert: 'abc', attributes: {}},
          {insert: 'def', attributes: {bold: true}},
          {insert: 'ghi\n', attributes: {}},
        ])
      })
  })

  it('removes a boolean format from the selection', () => {
    let modelValue: Model = [{insert: 'abcdefghi', attributes: {bold: true}}]
    cy.mount(Quill, {props: {
      blots: [BoldBlot, ItalicBlot],
      compatibleFormats: [],
      contagiousFormats: [],
      modelValue,
      'onUpdate:modelValue': (m: Model) => { modelValue = m },
    }})
    cy.get('div.ql-editor').focus()
    cy.get('div.ql-editor > p > bold-blot').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 3, node, 6)
    })
    cy.vue<typeof Quill>()
      .then(w => w.componentVM.toggle('bold'))
      .then(() => {
        expect(modelValue).to.deep.equal([
          {insert: 'abc', attributes: {bold: true}},
          {insert: 'def', attributes: {}},
          {insert: 'ghi', attributes: {bold: true}},
          {insert: '\n', attributes: {}},
        ])
      })
  })

  it('removes a boolean format from the selection before adding another', () => {
    let modelValue: Model = [{insert: 'abcdefghi', attributes: {bold: true}}]
    cy.mount(Quill, {props: {
      blots: [BoldBlot, ItalicBlot],
      compatibleFormats: [],
      contagiousFormats: [],
      modelValue,
      'onUpdate:modelValue': (m: Model) => { modelValue = m },
    }})
    cy.get('div.ql-editor').focus()
    cy.get('div.ql-editor > p > bold-blot').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 3, node, 6)
    })
    cy.vue<typeof Quill>()
      .then(w => w.componentVM.toggle('italic'))
      .then(() => {
        expect(modelValue).to.deep.equal([
          {insert: 'abc', attributes: {bold: true}},
          {insert: 'def', attributes: {italic: true}},
          {insert: 'ghi', attributes: {bold: true}},
          {insert: '\n', attributes: {}},
        ])
      })
  })

  it('does not remove a compatible boolean format from the selection before adding another', () => {
    let modelValue: Model = [{insert: 'abcdefghi', attributes: {bold: true}}]
    cy.mount(Quill, {props: {
      blots: [BoldBlot, ItalicBlot],
      compatibleFormats: [['bold', 'italic']],
      contagiousFormats: [],
      modelValue,
      'onUpdate:modelValue': (m: Model) => { modelValue = m },
    }})
    cy.get('div.ql-editor').focus()
    cy.get('div.ql-editor > p > bold-blot').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 3, node, 6)
    })
    cy.vue<typeof Quill>()
      .then(w => w.componentVM.toggle('italic'))
      .then(() => {
        expect(modelValue).to.deep.equal([
          {insert: 'abc', attributes: {bold: true}},
          {insert: 'def', attributes: {bold: true, italic: true}},
          {insert: 'ghi', attributes: {bold: true}},
          {insert: '\n', attributes: {}},
        ])
      })
  })

  it('removes a boolean format from a part of the selection before adding another', () => {
    let modelValue: Model = [{insert: 'abcd', attributes: {}}, {insert: 'e', attributes: {bold: true}}, {insert: 'fghi', attributes: {}}]
    cy.mount(Quill, {props: {
      blots: [BoldBlot, ItalicBlot],
      compatibleFormats: [],
      contagiousFormats: [],
      modelValue,
      'onUpdate:modelValue': (m: Model) => { modelValue = m },
    }})
    cy.get('div.ql-editor > p').then($el => {
      selectRange($el[0].firstChild!, 3, $el[0].firstChild!.nextSibling!.nextSibling!, 1)
    })
    cy.wait(200)  // I've not investigated why this is needed
    cy.vue<typeof Quill>()
      .then(w => w.componentVM.toggle('italic'))
      .then(() => {
        expect(modelValue).to.deep.equal([
          {insert: 'abc', attributes: {}},
          {insert: 'def', attributes: {italic: true}},
          {insert: 'ghi\n', attributes: {}},
        ])
      })
  })

  it('does not remove a compatible boolean format from a part of the selection before adding another', () => {
    let modelValue: Model = [{insert: 'abcd', attributes: {}}, {insert: 'e', attributes: {bold: true}}, {insert: 'fghi', attributes: {}}]
    cy.mount(Quill, {props: {
      blots: [BoldBlot, ItalicBlot],
      compatibleFormats: [['bold', 'italic']],
      contagiousFormats: [],
      modelValue,
      'onUpdate:modelValue': (m: Model) => { modelValue = m },
    }})
    cy.get('div.ql-editor > p').then($el => {
      selectRange($el[0].firstChild!, 3, $el[0].firstChild!.nextSibling!.nextSibling!, 1)
    })
    cy.wait(200)  // I've not investigated why this is needed
    cy.vue<typeof Quill>()
      .then(w => w.componentVM.toggle('italic'))
      .then(() => {
        expect(modelValue).to.deep.equal([
          {insert: 'abc', attributes: {}},
          {insert: 'd', attributes: {italic: true}},
          {insert: 'e', attributes: {bold: true, italic: true}},
          {insert: 'f', attributes: {italic: true}},
          {insert: 'ghi\n', attributes: {}},
        ])
      })
  })

  it('adds, changes and removes a boolean format to/from the caret', () => {
    let modelValue: Model = [{insert: 'abc', attributes: {}}]
    cy.mount(Quill, {props: {
      blots: [BoldBlot, ItalicBlot],
      compatibleFormats: [],
      contagiousFormats: [],
      modelValue,
      'onUpdate:modelValue': (m: Model) => { modelValue = m },
    }})
    cy.get('div.ql-editor').focus().type('{rightarrow}{rightarrow}{rightarrow}')
    cy.vue<typeof Quill>().then(w => w.componentVM.toggle('bold'))
    cy.get('div.ql-editor').type('def')
    cy.vue<typeof Quill>().then(w => w.componentVM.toggle('italic'))
    cy.get('div.ql-editor').type('ghi')
    cy.vue<typeof Quill>().then(w => w.componentVM.toggle('italic'))
    cy.get('div.ql-editor').type('jkl')
      .then(() => {
        expect(modelValue).to.deep.equal([
          {insert: 'abc', attributes: {}},
          {insert: 'def', attributes: {bold: true}},
          {insert: 'ghi', attributes: {italic: true}},
          {insert: 'jkl\n', attributes: {}},
        ])
      })
  })

  it('adds a string format to the selection', () => {
    let modelValue: Model = [{insert: 'abcdefghi', attributes: {}}]
    cy.mount(Quill, {props: {
      blots: [StrBlot],
      compatibleFormats: [],
      contagiousFormats: [],
      modelValue,
      'onUpdate:modelValue': (m: Model) => { modelValue = m },
    }})
    cy.get('div.ql-editor').focus()
    cy.get('div.ql-editor > p').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 3, node, 6)
    })
    cy.vue<typeof Quill>()
      .then(w => w.componentVM.toggle('string', 'A'))
      .then(() => {
        expect(modelValue).to.deep.equal([
          {insert: 'abc', attributes: {}},
          {insert: 'def', attributes: {string: 'A'}},
          {insert: 'ghi\n', attributes: {}},
        ])
      })
  })

  it('removes a string format from the selection', () => {
    let modelValue: Model = [{insert: 'abcdefghi', attributes: {string: 'A'}}]
    cy.mount(Quill, {props: {
      blots: [StrBlot],
      compatibleFormats: [],
      contagiousFormats: [],
      modelValue,
      'onUpdate:modelValue': (m: Model) => { modelValue = m },
    }})
    cy.get('div.ql-editor').focus()
    cy.get('div.ql-editor > p > string-blot').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 3, node, 6)
    })
    cy.vue<typeof Quill>()
      .then(w => w.componentVM.toggle('string', 'A'))
      .then(() => {
        expect(modelValue).to.deep.equal([
          {insert: 'abc', attributes: {string: 'A'}},
          {insert: 'def', attributes: {}},
          {insert: 'ghi', attributes: {string: 'A'}},
          {insert: '\n', attributes: {}},
        ])
      })
  })

  it('changes a string format from the selection', () => {
    let modelValue: Model = [{insert: 'abcdefghi', attributes: {string: 'A'}}]
    cy.mount(Quill, {props: {
      blots: [StrBlot],
      compatibleFormats: [],
      contagiousFormats: [],
      modelValue,
      'onUpdate:modelValue': (m: Model) => { modelValue = m },
    }})
    cy.get('div.ql-editor').focus()
    cy.get('div.ql-editor > p > string-blot').then($el => {
      const node = $el[0].firstChild
      console.assert(node !== null)
      selectRange(node, 3, node, 6)
    })
    cy.vue<typeof Quill>()
      .then(w => w.componentVM.toggle('string', 'B'))
      .then(() => {
        expect(modelValue).to.deep.equal([
          {insert: 'abc', attributes: {string: 'A'}},
          {insert: 'def', attributes: {string: 'B'}},
          {insert: 'ghi', attributes: {string: 'A'}},
          {insert: '\n', attributes: {}},
        ])
      })
  })

  it('adds, changes and removes a string format to/from the caret', () => {
    let modelValue: Model = [{insert: 'abc', attributes: {}}]
    cy.mount(Quill, {props: {
      blots: [StrBlot],
      compatibleFormats: [],
      contagiousFormats: [],
      modelValue,
      'onUpdate:modelValue': (m: Model) => { modelValue = m },
    }})
    cy.get('div.ql-editor').focus().type('{rightarrow}{rightarrow}{rightarrow}')
    cy.vue<typeof Quill>().then(w => w.componentVM.toggle('string', 'A'))
    cy.get('div.ql-editor').type('def')
    cy.vue<typeof Quill>().then(w => w.componentVM.toggle('string', 'B'))
    cy.get('div.ql-editor').type('ghi')
    cy.vue<typeof Quill>().then(w => w.componentVM.toggle('string', 'B'))
    cy.get('div.ql-editor').type('jkl')
      .then(() => {
        expect(modelValue).to.deep.equal([
          {insert: 'abc', attributes: {}},
          {insert: 'def', attributes: {string: 'A'}},
          {insert: 'ghi', attributes: {string: 'B'}},
          {insert: 'jkl\n', attributes: {}},
        ])
      })
  })

  it('reacts to model changes', () => {
    cy.mount(Quill, {props: {blots: [BoldBlot, ItalicBlot], compatibleFormats: [], contagiousFormats: [], modelValue: [{insert: 'initial', attributes: {}}]}})
    cy.get(':contains("initial")').should('exist')
    cy.vue<typeof Quill>().then(w => {w.setProps({modelValue: [{insert: 'changed'}]})})
    cy.get(':contains("initial")').should('not.exist')
    cy.get(':contains("changed")').should('exist')
  })

  it("reacts to 'props.blots' changes", () => {
    cy.mount(Quill, {props: {blots: [BoldBlot], compatibleFormats: [], contagiousFormats: [], modelValue: [{insert: 'bold', attributes: {bold: true}}]}})
    cy.get(':contains("bold")').last().should('have.css', 'font-weight', '700')
    cy.vue<typeof Quill>().then(w => {w.setProps({blots: []})})
    cy.get(':contains("bold")').last().should('have.css', 'font-weight', '400')
    cy.vue<typeof Quill>().then(w => {w.setProps({blots: [BoldBlot]})})
    cy.get(':contains("bold")').last().should('have.css', 'font-weight', '700')
  })

  it('preserves a block embed in the model', () => {
    let modelValue: Model = [{insert: 'a\n', attributes: {}}, {insert: {divider: true}}, {insert: 'b\n', attributes: {}}]
    cy.mount(Quill, {props: {
      blots: [StrBlot, DividerBlot],
      compatibleFormats: [],
      contagiousFormats: [],
      modelValue,
      'onUpdate:modelValue': (m: Model) => { modelValue = m },
    }})
    cy.get('div.ql-editor').type('A').then(() => {
      expect(modelValue).to.deep.equal([
        {insert: 'a\n', attributes: {}},
        {insert: {divider: true}},
        {insert: 'bA\n', attributes: {}},
      ])
    })
  })

  it('preserves an inline embed in the model', () => {
    let modelValue: Model = [{insert: 'a', attributes: {}}, {insert: {'inl-emb': {color: 'green'}}}, {insert: 'b\n', attributes: {}}]
    cy.mount(Quill, {props: {
      blots: [StrBlot, InlEmbBlot],
      compatibleFormats: [],
      contagiousFormats: [],
      modelValue,
      'onUpdate:modelValue': (m: Model) => { modelValue = m },
    }})
    cy.get('div.ql-editor').type('A').then(() => {
      expect(modelValue).to.deep.equal([
        {insert: 'a', attributes: {}},
        {insert: {'inl-emb': {color: 'green'}}},
        {insert: 'bA\n', attributes: {}},
      ])
    })
  })

  it('allows adding an insert operation with the same attributes', () => {
    cy.mount(Quill, {props: {blots: [StrBlot], compatibleFormats: [], contagiousFormats: [], modelValue: [{insert: 'abc', attributes: {}}]}})
    cy.vue<typeof Quill>().then(w => {w.setProps({modelValue: [{insert: 'abc', attributes: {}}, {insert: 'def', attributes: {}}]})})
    cy.get(':contains("abcdef")').should('exist')
  })

  it('spreads contagious format to the left - at index zero', () => {
    let modelValue: Model = [{insert: 'abc', attributes: {bold: true}}, {insert: '\n', attributes: {}}]
    cy.mount(Quill, {props: {
      blots: [BoldBlot],
      compatibleFormats: [],
      contagiousFormats: ['bold'],
      modelValue,
      'onUpdate:modelValue': (m: Model) => { modelValue = m },
    }})
    cy.get('div.ql-editor').type('{moveToStart}blah').then(() => {
      expect(modelValue).to.deep.equal([{insert: 'blahabc', attributes: {bold: true}}, {insert: '\n', attributes: {}}])
    })
    cy.get('bold-blot').should('have.text', 'blahabc')
  })

  it('spreads contagious format to the left - at non-zero index - coming from the left', () => {
    let modelValue: Model = [{insert: 'abc ', attributes: {}}, {insert: 'def', attributes: {bold: true}}, {insert: '\n', attributes: {}}]
    cy.mount(Quill, {props: {
      blots: [BoldBlot],
      compatibleFormats: [],
      contagiousFormats: ['bold'],
      modelValue,
      'onUpdate:modelValue': (m: Model) => { modelValue = m },
    }})
    cy.get('div.ql-editor').type('{moveToStart}{rightArrow}{rightArrow}{rightArrow}{rightArrow}blah').then(() => {
      expect(modelValue).to.deep.equal([{insert: 'abc ', attributes: {}}, {insert: 'blahdef', attributes: {bold: true}}, {insert: '\n', attributes: {}}])
    })
    cy.get('bold-blot').should('have.text', 'blahdef')
  })

  it('spreads contagious format to the left - at non-zero index - coming from the right', () => {
    let modelValue: Model = [{insert: 'abc ', attributes: {}}, {insert: 'def', attributes: {bold: true}}, {insert: '\n', attributes: {}}]
    cy.mount(Quill, {props: {
      blots: [BoldBlot],
      compatibleFormats: [],
      contagiousFormats: ['bold'],
      modelValue,
      'onUpdate:modelValue': (m: Model) => { modelValue = m },
    }})
    cy.get('div.ql-editor').type('{moveToEnd}{leftArrow}{leftArrow}{leftArrow}blah').then(() => {
      expect(modelValue).to.deep.equal([{insert: 'abc ', attributes: {}}, {insert: 'blahdef', attributes: {bold: true}}, {insert: '\n', attributes: {}}])
    })
    cy.get('bold-blot').should('have.text', 'blahdef')
  })

  it('spreads contagious format to the right - coming from the right', () => {
    let modelValue: Model = [{insert: 'abc', attributes: {bold: true}}, {insert: ' def\n', attributes: {}}]
    cy.mount(Quill, {props: {
      blots: [BoldBlot],
      compatibleFormats: [],
      contagiousFormats: ['bold'],
      modelValue,
      'onUpdate:modelValue': (m: Model) => { modelValue = m },
    }})
    cy.get('div.ql-editor').type('{moveToEnd}{leftArrow}{leftArrow}{leftArrow}{leftArrow}blah').then(() => {
      expect(modelValue).to.deep.equal([{insert: 'abcblah', attributes: {bold: true}}, {insert: ' def\n', attributes: {}}])
    })
    cy.get('bold-blot').should('have.text', 'abcblah')
  })

  it('spreads contagious format to the right - coming from the left', () => {
    let modelValue: Model = [{insert: 'abc', attributes: {bold: true}}, {insert: ' def\n', attributes: {}}]
    cy.mount(Quill, {props: {
      blots: [BoldBlot],
      compatibleFormats: [],
      contagiousFormats: ['bold'],
      modelValue,
      'onUpdate:modelValue': (m: Model) => { modelValue = m },
    }})
    cy.get('div.ql-editor').type('{moveToStart}{rightArrow}{rightArrow}{rightArrow}blah').then(() => {
      expect(modelValue).to.deep.equal([{insert: 'abcblah', attributes: {bold: true}}, {insert: ' def\n', attributes: {}}])
    })
    cy.get('bold-blot').should('have.text', 'abcblah')
  })

  it('spreads non-contagious format to the left - at index zero', () => {
    // Inconsistent behavior from Quill?
    let modelValue: Model = [{insert: 'abc', attributes: {bold: true}}, {insert: '\n', attributes: {}}]
    cy.mount(Quill, {props: {
      blots: [BoldBlot],
      compatibleFormats: [],
      contagiousFormats: [],
      modelValue,
      'onUpdate:modelValue': (m: Model) => { modelValue = m },
    }})
    cy.get('div.ql-editor').type('{moveToStart}blah').then(() => {
      expect(modelValue).to.deep.equal([{insert: 'blahabc', attributes: {bold: true}}, {insert: '\n', attributes: {}}])
    })
    cy.get('bold-blot').should('have.text', 'blahabc')
  })

  it('does not spread non-contagious format to the left - at non-zero index - coming from the left', () => {
    // Default behavior in Chrome: don't spread format to the left
    // Default behavior in Firefox: spread format to the left when cursor came from the right
    let modelValue: Model = [{insert: 'abc ', attributes: {}}, {insert: 'def', attributes: {bold: true}}, {insert: '\n', attributes: {}}]
    cy.mount(Quill, {props: {
      blots: [BoldBlot],
      compatibleFormats: [],
      contagiousFormats: [],
      modelValue,
      'onUpdate:modelValue': (m: Model) => { modelValue = m },
    }})
    cy.get('div.ql-editor').type('{moveToStart}{rightArrow}{rightArrow}{rightArrow}{rightArrow}blah').then(() => {
      expect(modelValue).to.deep.equal([{insert: 'abc blah', attributes: {}}, {insert: 'def', attributes: {bold: true}}, {insert: '\n', attributes: {}}])
    })
    cy.get('bold-blot').should('have.text', 'def')
  })

  it('does not spread non-contagious format to the left - at non-zero index - coming from the right', () => {
    let modelValue: Model = [{insert: 'abc ', attributes: {}}, {insert: 'def', attributes: {bold: true}}, {insert: '\n', attributes: {}}]
    cy.mount(Quill, {props: {
      blots: [BoldBlot],
      compatibleFormats: [],
      contagiousFormats: [],
      modelValue,
      'onUpdate:modelValue': (m: Model) => { modelValue = m },
    }})
    cy.get('div.ql-editor').type('{moveToEnd}{leftArrow}{leftArrow}{leftArrow}blah').then(() => {
      expect(modelValue).to.deep.equal([{insert: 'abc blah', attributes: {}}, {insert: 'def', attributes: {bold: true}}, {insert: '\n', attributes: {}}])
    })
    cy.get('bold-blot').should('have.text', 'def')
  })

  it('spreads non-contagious format to the right - coming from the right', () => {
    // Default behavior in Chrome: spread format to the right
    // Default behavior in Firefox: spread format to the right when cursor came from the left
    let modelValue: Model = [{insert: 'abc', attributes: {bold: true}}, {insert: ' def\n', attributes: {}}]
    cy.mount(Quill, {props: {
      blots: [BoldBlot],
      compatibleFormats: [],
      contagiousFormats: [],
      modelValue,
      'onUpdate:modelValue': (m: Model) => { modelValue = m },
    }})
    cy.get('div.ql-editor').type('{moveToEnd}{leftArrow}{leftArrow}{leftArrow}{leftArrow}blah').then(() => {
      expect(modelValue).to.deep.equal([{insert: 'abcblah', attributes: {bold: true}}, {insert: ' def\n', attributes: {}}])
    })
    cy.get('bold-blot').should('have.text', 'abcblah')
  })

  it('spreads non-contagious format to the right - coming from the left', () => {
    let modelValue: Model = [{insert: 'abc', attributes: {bold: true}}, {insert: ' def\n', attributes: {}}]
    cy.mount(Quill, {props: {
      blots: [BoldBlot],
      compatibleFormats: [],
      contagiousFormats: [],
      modelValue,
      'onUpdate:modelValue': (m: Model) => { modelValue = m },
    }})
    cy.get('div.ql-editor').type('{moveToStart}{rightArrow}{rightArrow}{rightArrow}blah').then(() => {
      expect(modelValue).to.deep.equal([{insert: 'abcblah', attributes: {bold: true}}, {insert: ' def\n', attributes: {}}])
    })
    cy.get('bold-blot').should('have.text', 'abcblah')
  })
})
