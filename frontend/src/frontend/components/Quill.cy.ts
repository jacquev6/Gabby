import Quill, { type Model, BoldBlot, ItalicBlot } from './Quill.vue'


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
      'onUpdate:modelValue': (m: Model) => { modelValue = m},
    }})
    cy.get('div.ql-editor').type('plain text with spaces').then(() => {
      expect(modelValue).to.deep.equal([{insert: 'plain text with spaces\n', attributes: undefined}])
    })
  })

  function selectTextRange(obj: HTMLElement, start: number, end: number) {
    const child = obj.firstChild
    console.assert(child !== null)

    var range = document.createRange()
    range.setStart(child, start)
    range.setEnd(child, end)

    var sel = window.getSelection()
    console.assert(sel !== null)
    sel.removeAllRanges()
    sel.addRange(range)
  }

  it('updates its model when formatting', () => {
    let modelValue: Model = [{insert: 'plain'}]
    cy.mount(Quill, {props: {
      blots: [BoldBlot, ItalicBlot],
      modelValue,
      'onUpdate:modelValue': (m: Model) => { modelValue = m},
    }})
    cy.get('div.ql-editor').focus()
    cy.get('div.ql-editor > p').then($el => selectTextRange($el[0], 2, 4))
    cy.vue<typeof Quill>()
      .then(w => w.componentVM.toggle('bold'))
      .then(() => {
        expect(modelValue).to.deep.equal([
          {insert: 'pl', attributes: undefined},
          {insert: 'ai', attributes: {bold: true}},
          {insert: 'n\n', attributes: undefined},
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

  // This reactivity is not used in the project but common implementation patterns make it cheap,
  // and make the component more reliable overall.
  it("reacts to 'props.blots' changes", () => {
    cy.mount(Quill, {props: {blots: [BoldBlot], modelValue: [{insert: 'bold', attributes: {bold: true}}]}})
    cy.get(':contains("bold")').last().should('have.css', 'font-weight', '700')
    cy.vue<typeof Quill>().then(w => {w.setProps({blots: []})})
    cy.get(':contains("bold")').last().should('have.css', 'font-weight', '400')
    cy.vue<typeof Quill>().then(w => {w.setProps({blots: [BoldBlot]})})
    cy.get(':contains("bold")').last().should('have.css', 'font-weight', '700')
  })
})
