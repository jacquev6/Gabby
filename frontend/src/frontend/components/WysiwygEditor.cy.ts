import WysiwygEditor from './WysiwygEditor.vue'


describe('WysiwygEditor', () => {
  before(console.clear)

  it("updates its model", () => {
    let modelValue = 'hell\n'
    cy.mount(WysiwygEditor, {props: {
      label: 'Test',
      formats: {},
      modelValue,
      'onUpdate:modelValue': (m: string) => {modelValue = m},
      delta: [{insert: modelValue}],
    }})
    cy.get('div.ql-editor').type('o').then(() => {
      expect(modelValue).to.equal('hell\no')
    })
  })

  it("doesn't add a trailing line end to the model when typing at the end", () => {
    let modelValue = 'hell'
    cy.mount(WysiwygEditor, {props: {
      label: 'Test',
      formats: {},
      modelValue,
      'onUpdate:modelValue': (m: string) => {modelValue = m},
      delta: [{insert: modelValue}],
    }})
    cy.get('div.ql-editor').type('o')
    cy.wait(0).then(() => {
      expect(modelValue).to.equal('hello')
    })
  })

  it("doesn't add a trailing line end to the model when typing at the start", () => {
    let modelValue = 'ello'
    cy.mount(WysiwygEditor, {props: {
      label: 'Test',
      formats: {},
      modelValue,
      'onUpdate:modelValue': (m: string) => {modelValue = m},
      delta: [{insert: modelValue}],
    }})
    cy.get('div.ql-editor').type('{moveToStart}h').then(() => {
      expect(modelValue).to.equal('hello')
    })
  })

  it("keeps a freshly-added trailing line end", () => {
    let modelValue = 'hello'
    cy.mount(WysiwygEditor, {props: {
      label: 'Test',
      formats: {},
      modelValue,
      'onUpdate:modelValue': (m: string) => {modelValue = m},
      delta: [{insert: modelValue}],
    }})
    cy.get('div.ql-editor').type('\n').then(() => {
      expect(modelValue).to.equal('hello\n')
    })
  })

  it("keeps an ever-present trailing line end", () => {
    let modelValue = 'ello\n'
    cy.mount(WysiwygEditor, {props: {
      label: 'Test',
      formats: {},
      modelValue,
      'onUpdate:modelValue': (m: string) => {modelValue = m},
      delta: [{insert: modelValue}],
    }})
    cy.get('div.ql-editor').type('{moveToStart}h').then(() => {
      expect(modelValue).to.equal('hello\n')
    })
  })

  it("removes an ever-present trailing line end when deleting all", () => {
    let modelValue = 'hello\n'
    cy.mount(WysiwygEditor, {props: {
      label: 'Test',
      formats: {},
      modelValue,
      'onUpdate:modelValue': (m: string) => {modelValue = m},
      delta: [{insert: modelValue}],
    }})
    cy.get('div.ql-editor').type('{selectAll}{del}').then(() => {
      expect(modelValue).to.equal('')
    })
  })

  it("removes the trailing line end even when the new delta tries to remove it - no ops", () => {
    let modelValue = 'hello\n'
    cy.mount(WysiwygEditor, {props: {
      label: 'Test',
      formats: {},
      modelValue,
      'onUpdate:modelValue': (m: string) => {modelValue = m},
      delta: [{insert: modelValue}],
    }})
    cy.vue<typeof WysiwygEditor>().then(w => { w.setProps({delta: []}) })
    cy.wait(0).then(() => { expect(modelValue).to.equal('') })
  })

  it("removes the trailing line end even when the new delta tries to remove it - no line end in last op", () => {
    let modelValue = 'hello\n'
    cy.mount(WysiwygEditor, {props: {
      label: 'Test',
      formats: {},
      modelValue,
      'onUpdate:modelValue': (m: string) => {modelValue = m},
      delta: [{insert: modelValue}],
    }})
    cy.vue<typeof WysiwygEditor>().then(w => { w.setProps({delta: [{insert: 'changed'}]}) })
    cy.wait(0).then(() => { expect(modelValue).to.equal('changed') })
  })
})
