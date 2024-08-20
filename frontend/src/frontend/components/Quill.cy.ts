import Quill, { type Model, InlineBlot, BoldBlot, ItalicBlot } from './Quill.vue'


class StringBlot extends InlineBlot {
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

describe('Quill', () => {
  before(console.clear)

  it('renders its model', () => {
    cy.mount(Quill, {props: {
      blots: [BoldBlot, ItalicBlot],
      modelValue: [
        {insert: '1-plain'},
        {insert: '2-bold', attributes: {bold: true}},
        {insert: '3-italic', attributes: {italic: true}},
        {insert: '4-bold-italic', attributes: {bold: true, italic: true}},
        {insert: '\n'},
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
      modelValue,
      'onUpdate:modelValue': (m: Model) => { modelValue = m },
    }})
    cy.get('div.ql-editor').type('plain text with spaces').then(() => {
      expect(modelValue).to.deep.equal([{insert: 'plain text with spaces\n', attributes: undefined}])
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
    let modelValue: Model = [{insert: 'abcdefghi'}]
    cy.mount(Quill, {props: {
      blots: [BoldBlot, ItalicBlot],
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
          {insert: 'abc', attributes: undefined},
          {insert: 'def', attributes: {bold: true}},
          {insert: 'ghi\n', attributes: undefined},
        ])
      })
  })

  it('removes a boolean format from the selection', () => {
    let modelValue: Model = [{insert: 'abcdefghi', attributes: {bold: true}}]
    cy.mount(Quill, {props: {
      blots: [BoldBlot, ItalicBlot],
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
          {insert: 'def', attributes: undefined},
          {insert: 'ghi', attributes: {bold: true}},
          {insert: '\n', attributes: undefined},
        ])
      })
  })

  it('removes a boolean format from the selection before adding another', () => {
    let modelValue: Model = [{insert: 'abcdefghi', attributes: {bold: true}}]
    cy.mount(Quill, {props: {
      blots: [BoldBlot, ItalicBlot],
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
          {insert: '\n', attributes: undefined},
        ])
      })
  })

  it('removes a boolean format from a part of the selection before adding another', () => {
    let modelValue: Model = [{insert: 'abcd'}, {insert: 'e', attributes: {bold: true}}, {insert: 'fghi'}]
    cy.mount(Quill, {props: {
      blots: [BoldBlot, ItalicBlot],
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
          {insert: 'abc', attributes: undefined},
          {insert: 'def', attributes: {italic: true}},
          {insert: 'ghi\n', attributes: undefined},
        ])
      })
  })

  it('adds, changes and removes a boolean format to/from the caret', () => {
    let modelValue: Model = [{insert: 'abc'}]
    cy.mount(Quill, {props: {
      blots: [BoldBlot, ItalicBlot],
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
          {insert: 'abc', attributes: undefined},
          {insert: 'def', attributes: {bold: true}},
          {insert: 'ghi', attributes: {italic: true}},
          {insert: 'jkl\n', attributes: undefined},
        ])
      })
  })

  it('adds a string format to the selection', () => {
    let modelValue: Model = [{insert: 'abcdefghi'}]
    cy.mount(Quill, {props: {
      blots: [StringBlot],
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
          {insert: 'abc', attributes: undefined},
          {insert: 'def', attributes: {string: 'A'}},
          {insert: 'ghi\n', attributes: undefined},
        ])
      })
  })

  it('removes a string format from the selection', () => {
    let modelValue: Model = [{insert: 'abcdefghi', attributes: {string: 'A'}}]
    cy.mount(Quill, {props: {
      blots: [StringBlot],
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
          {insert: 'def', attributes: undefined},
          {insert: 'ghi', attributes: {string: 'A'}},
          {insert: '\n', attributes: undefined},
        ])
      })
  })

  it('changes a string format from the selection', () => {
    let modelValue: Model = [{insert: 'abcdefghi', attributes: {string: 'A'}}]
    cy.mount(Quill, {props: {
      blots: [StringBlot],
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
          {insert: '\n', attributes: undefined},
        ])
      })
  })

  it.only('adds, changes and removes a string format to/from the caret', () => {
    let modelValue: Model = [{insert: 'abc'}]
    cy.mount(Quill, {props: {
      blots: [StringBlot],
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
          {insert: 'abc', attributes: undefined},
          {insert: 'def', attributes: {string: 'A'}},
          {insert: 'ghi', attributes: {string: 'B'}},
          {insert: 'jkl\n', attributes: undefined},
        ])
      })
  })

  it('reacts to model changes', () => {
    cy.mount(Quill, {props: {blots: [BoldBlot, ItalicBlot], modelValue: [{insert: 'initial'}]}})
    cy.get(':contains("initial")').should('exist')
    cy.vue<typeof Quill>().then(w => {w.setProps({modelValue: [{insert: 'changed'}]})})
    cy.get(':contains("initial")').should('not.exist')
    cy.get(':contains("changed")').should('exist')
  })

  it("reacts to 'props.blots' changes", () => {
    cy.mount(Quill, {props: {blots: [BoldBlot], modelValue: [{insert: 'bold', attributes: {bold: true}}]}})
    cy.get(':contains("bold")').last().should('have.css', 'font-weight', '700')
    cy.vue<typeof Quill>().then(w => {w.setProps({blots: []})})
    cy.get(':contains("bold")').last().should('have.css', 'font-weight', '400')
    cy.vue<typeof Quill>().then(w => {w.setProps({blots: [BoldBlot]})})
    cy.get(':contains("bold")').last().should('have.css', 'font-weight', '700')
  })
})
