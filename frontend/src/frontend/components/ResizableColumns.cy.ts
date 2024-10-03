import ResizableColumns from "./ResizableColumns.vue"


function mount(collapsed: Record<string, boolean> = {}, widths: Record<string, string> = {}) {
  // @ts-ignore/* @todo Understand typing issue and fix */
  cy.mount(ResizableColumns, {
    props: {
      widths,
      collapsed,
    },
    slots: {
      one: 'One',
      two: 'Two',
      three: 'Three',
      four: 'Four',
    },
  })
}

describe('TwoResizableColumns', () => {
  before(console.clear)

  it('renders - 0 collapsed', () => {
    mount()

    cy.viewport(846, 400)
    cy.get('div.root').invoke('width').should('eq', 830)
    cy.get('div.split').invoke('width').should('eq', 830)
    cy.get('div.false-gutter').should('not.exist')
    cy.get('div.gutter').should('have.length', 3)
    cy.get('div.gutter').eq(0).invoke('width').should('eq', 10)
    cy.get('div.gutter').eq(1).invoke('width').should('eq', 10)
    cy.get('div.gutter').eq(2).invoke('width').should('eq', 10)
    cy.get('div.column:contains("One")').invoke('width').should('eq', 200)
    cy.get('div.column:contains("Two")').invoke('width').should('eq', 200)
    cy.get('div.column:contains("Three")').invoke('width').should('eq', 200)
    cy.get('div.column:contains("Four")').invoke('width').should('eq', 200)
  })

  it('renders - 1 collapsed - one', () => {
    mount({ one: true })

    cy.viewport(670, 400)
    cy.get('div.root').invoke('width').should('eq', 654)
    cy.get('div.split').invoke('width').should('eq', 620)
    cy.get('div.false-gutter').should('have.length', 1)
    cy.get('div.false-gutter').invoke('width').should('eq', 34)
    cy.get('div.gutter').should('have.length', 2)
    cy.get('div.gutter').eq(0).invoke('width').should('eq', 10)
    cy.get('div.gutter').eq(1).invoke('width').should('eq', 10)
    cy.get('div.column:contains("Two")').invoke('width').should('eq', 200)
    cy.get('div.column:contains("Three")').invoke('width').should('eq', 200)
    cy.get('div.column:contains("Four")').invoke('width').should('eq', 200)
  })

  it('renders - 1 collapsed - two', () => {
    mount({ two: true })

    cy.viewport(666, 400)
    cy.get('div.root').invoke('width').should('eq', 650)
    cy.get('div.split').invoke('width').should('eq', 650)
    cy.get('div.false-gutter').should('not.exist')
    cy.get('div.gutter').should('have.length', 2)
    cy.get('div.gutter').eq(0).invoke('width').should('eq', 40)
    cy.get('div.gutter').eq(1).invoke('width').should('eq', 10)
    cy.get('div.column:contains("One")').invoke('width').should('eq', 200)
    cy.get('div.column:contains("Three")').invoke('width').should('eq', 200)
    cy.get('div.column:contains("Four")').invoke('width').should('eq', 200)
  })

  it('renders - 1 collapsed - three', () => {
    mount({ three: true })

    cy.viewport(666, 400)
    cy.get('div.root').invoke('width').should('eq', 650)
    cy.get('div.split').invoke('width').should('eq', 650)
    cy.get('div.false-gutter').should('not.exist')
    cy.get('div.gutter').should('have.length', 2)
    cy.get('div.gutter').eq(0).invoke('width').should('eq', 10)
    cy.get('div.gutter').eq(1).invoke('width').should('eq', 40)
    cy.get('div.column:contains("One")').invoke('width').should('eq', 200)
    cy.get('div.column:contains("Two")').invoke('width').should('eq', 200)
    cy.get('div.column:contains("Four")').invoke('width').should('eq', 200)
  })

  it('renders - 1 collapsed - four', () => {
    mount({ four: true })

    cy.viewport(670, 400)
    cy.get('div.root').invoke('width').should('eq', 654)
    cy.get('div.split').invoke('width').should('eq', 620)
    cy.get('div.false-gutter').should('have.length', 1)
    cy.get('div.false-gutter').invoke('width').should('eq', 34)
    cy.get('div.gutter').should('have.length', 2)
    cy.get('div.gutter').eq(0).invoke('width').should('eq', 10)
    cy.get('div.gutter').eq(1).invoke('width').should('eq', 10)
    cy.get('div.column:contains("One")').invoke('width').should('eq', 200)
    cy.get('div.column:contains("Two")').invoke('width').should('eq', 200)
    cy.get('div.column:contains("Three")').invoke('width').should('eq', 200)
  })

  it('renders - 2 collapsed - one & two', () => {
    mount({ one: true, two: true })

    cy.viewport(490, 400)
    cy.get('div.root').invoke('width').should('eq', 474)
    cy.get('div.split').invoke('width').should('eq', 410)
    cy.get('div.false-gutter').should('have.length', 1)
    cy.get('div.false-gutter').invoke('width').should('eq', 64)
    cy.get('div.gutter').should('have.length', 1)
    cy.get('div.gutter').invoke('width').should('eq', 10)
    cy.get('div.column:contains("Three")').invoke('width').should('eq', 200)
    cy.get('div.column:contains("Four")').invoke('width').should('eq', 200)
  })

  it('renders - 2 collapsed - two & three', () => {
    mount({ two: true, three: true })

    cy.viewport(486, 400)
    cy.get('div.root').invoke('width').should('eq', 470)
    cy.get('div.split').invoke('width').should('eq', 470)
    cy.get('div.false-gutter').should('not.exist')
    cy.get('div.gutter').should('have.length', 1)
    cy.get('div.gutter').invoke('width').should('eq', 70)
    cy.get('div.column:contains("One")').invoke('width').should('eq', 200)
    cy.get('div.column:contains("Four")').invoke('width').should('eq', 200)
  })

  it('renders - 2 collapsed - three & four', () => {
    mount({ three: true, four: true })

    cy.viewport(490, 400)
    cy.get('div.root').invoke('width').should('eq', 474)
    cy.get('div.split').invoke('width').should('eq', 410)
    cy.get('div.false-gutter').should('have.length', 1)
    cy.get('div.false-gutter').invoke('width').should('eq', 64)
    cy.get('div.gutter').should('have.length', 1)
    cy.get('div.gutter').invoke('width').should('eq', 10)
    cy.get('div.column:contains("One")').invoke('width').should('eq', 200)
    cy.get('div.column:contains("Two")').invoke('width').should('eq', 200)
  })

  it('renders - 2 collapsed - one & three', () => {
    mount({ one: true, three: true })

    cy.viewport(490, 400)
    cy.get('div.root').invoke('width').should('eq', 474)
    cy.get('div.split').invoke('width').should('eq', 440)
    cy.get('div.false-gutter').should('have.length', 1)
    cy.get('div.false-gutter').invoke('width').should('eq', 34)
    cy.get('div.gutter').should('have.length', 1)
    cy.get('div.gutter').invoke('width').should('eq', 40)
    cy.get('div.column:contains("Two")').invoke('width').should('eq', 200)
    cy.get('div.column:contains("Four")').invoke('width').should('eq', 200)
  })

  it('renders - 2 collapsed - two & four', () => {
    mount({ two: true, four: true })

    cy.viewport(490, 400)
    cy.get('div.root').invoke('width').should('eq', 474)
    cy.get('div.split').invoke('width').should('eq', 440)
    cy.get('div.false-gutter').should('have.length', 1)
    cy.get('div.false-gutter').invoke('width').should('eq', 34)
    cy.get('div.gutter').should('have.length', 1)
    cy.get('div.gutter').invoke('width').should('eq', 40)
    cy.get('div.column:contains("One")').invoke('width').should('eq', 200)
    cy.get('div.column:contains("Three")').invoke('width').should('eq', 200)
  })

  it('renders - 2 collapsed - one & four', () => {
    mount({ one: true, four: true })

    cy.viewport(494, 400)
    cy.get('div.root').invoke('width').should('eq', 478)
    cy.get('div.split').invoke('width').should('eq', 410)
    cy.get('div.false-gutter').should('have.length', 2)
    cy.get('div.false-gutter').eq(0).invoke('width').should('eq', 34)
    cy.get('div.false-gutter').eq(1).invoke('width').should('eq', 34)
    cy.get('div.gutter').should('have.length', 1)
    cy.get('div.gutter').invoke('width').should('eq', 10)
    cy.get('div.column:contains("Two")').invoke('width').should('eq', 200)
    cy.get('div.column:contains("Three")').invoke('width').should('eq', 200)
  })

  it('renders - 3 collapsed - one, two & three', () => {
    mount({ one: true, two: true, three: true })

    cy.viewport(310, 400)
    cy.get('div.root').invoke('width').should('eq', 294)
    cy.get('div.split').invoke('width').should('eq', 200)
    cy.get('div.false-gutter').should('have.length', 1)
    cy.get('div.false-gutter').invoke('width').should('eq', 94)
    cy.get('div.gutter').should('not.exist')
    cy.get('div.column:contains("Four")').invoke('width').should('eq', 200)
  })

  it('renders - 3 collapsed - one, two & four', () => {
    mount({ one: true, two: true, four: true })

    cy.viewport(314, 400)
    cy.get('div.root').invoke('width').should('eq', 298)
    cy.get('div.split').invoke('width').should('eq', 200)
    cy.get('div.false-gutter').should('have.length', 2)
    cy.get('div.false-gutter').eq(0).invoke('width').should('eq', 64)
    cy.get('div.false-gutter').eq(1).invoke('width').should('eq', 34)
    cy.get('div.gutter').should('not.exist')
    cy.get('div.column:contains("Three")').invoke('width').should('eq', 200)
  })

  it('renders - 3 collapsed - one, three & four', () => {
    mount({ one: true, three: true, four: true })

    cy.viewport(314, 400)
    cy.get('div.root').invoke('width').should('eq', 298)
    cy.get('div.split').invoke('width').should('eq', 200)
    cy.get('div.false-gutter').should('have.length', 2)
    cy.get('div.false-gutter').eq(0).invoke('width').should('eq', 34)
    cy.get('div.false-gutter').eq(1).invoke('width').should('eq', 64)
    cy.get('div.gutter').should('not.exist')
    cy.get('div.column:contains("Two")').invoke('width').should('eq', 200)
  })

  it('renders - 3 collapsed - two, three & four', () => {
    mount({ two: true, three: true, four: true })

    cy.viewport(310, 400)
    cy.get('div.root').invoke('width').should('eq', 294)
    cy.get('div.split').invoke('width').should('eq', 200)
    cy.get('div.false-gutter').should('have.length', 1)
    cy.get('div.false-gutter').invoke('width').should('eq', 94)
    cy.get('div.gutter').should('not.exist')
    cy.get('div.column:contains("One")').invoke('width').should('eq', 200)
  })

  it('resizes left columns', () => {
    mount()

    cy.viewport(846, 400)

    cy.get('div.column:contains("One")').invoke('width').should('eq', 200)
    cy.get('div.column:contains("Two")').invoke('width').should('eq', 200)

    cy.get('div.gutter').eq(0).trigger('mousedown', { clientX: 423, clientY: 5 })
    cy.window().trigger('mousemove', {clientX: 413, clientY: 5})
    cy.get('div.column:contains("One")').invoke('width').should('be.closeTo', 190, 0.1)
    cy.get('div.column:contains("Two")').invoke('width').should('be.closeTo', 210, 0.1)
    cy.window().trigger('mousemove', {clientX: 403, clientY: 5})
    cy.get('div.column:contains("One")').invoke('width').should('be.closeTo', 180, 0.1)
    cy.get('div.column:contains("Two")').invoke('width').should('be.closeTo', 220, 0.1)
    cy.window().trigger('mouseup', {clientX: 403, clientY: 5})
    cy.get('div.column:contains("One")').invoke('width').should('be.closeTo', 180, 0.1)
    cy.get('div.column:contains("Two")').invoke('width').should('be.closeTo', 220, 0.1)

    cy.get('div.gutter').eq(0).trigger('mousedown', { clientX: 423, clientY: 5 })
    cy.window().trigger('mousemove', {clientX: 433, clientY: 5})
    cy.get('div.column:contains("One")').invoke('width').should('be.closeTo', 190, 0.1)
    cy.get('div.column:contains("Two")').invoke('width').should('be.closeTo', 210, 0.1)
    cy.window().trigger('mousemove', {clientX: 443, clientY: 5})
    cy.get('div.column:contains("One")').invoke('width').should('be.closeTo', 200, 0.1)
    cy.get('div.column:contains("Two")').invoke('width').should('be.closeTo', 200, 0.1)
    cy.window().trigger('mouseup', {clientX: 443, clientY: 5})
    cy.get('div.column:contains("One")').invoke('width').should('be.closeTo', 200, 0.1)
    cy.get('div.column:contains("Two")').invoke('width').should('be.closeTo', 200, 0.1)
  })

  it('resizes middle columns', () => {
    mount()

    cy.viewport(846, 400)

    cy.get('div.column:contains("Two")').invoke('width').should('eq', 200)
    cy.get('div.column:contains("Three")').invoke('width').should('eq', 200)

    cy.get('div.gutter').eq(1).trigger('mousedown', { clientX: 423, clientY: 5 })
    cy.window().trigger('mousemove', {clientX: 413, clientY: 5})
    cy.get('div.column:contains("Two")').invoke('width').should('be.closeTo', 190, 0.1)
    cy.get('div.column:contains("Three")').invoke('width').should('be.closeTo', 210, 0.1)
    cy.window().trigger('mousemove', {clientX: 403, clientY: 5})
    cy.get('div.column:contains("Two")').invoke('width').should('be.closeTo', 180, 0.1)
    cy.get('div.column:contains("Three")').invoke('width').should('be.closeTo', 220, 0.1)
    cy.window().trigger('mouseup', {clientX: 403, clientY: 5})
    cy.get('div.column:contains("Two")').invoke('width').should('be.closeTo', 180, 0.1)
    cy.get('div.column:contains("Three")').invoke('width').should('be.closeTo', 220, 0.1)

    cy.get('div.gutter').eq(1).trigger('mousedown', { clientX: 423, clientY: 5 })
    cy.window().trigger('mousemove', {clientX: 433, clientY: 5})
    cy.get('div.column:contains("Two")').invoke('width').should('be.closeTo', 190, 0.1)
    cy.get('div.column:contains("Three")').invoke('width').should('be.closeTo', 210, 0.1)
    cy.window().trigger('mousemove', {clientX: 443, clientY: 5})
    cy.get('div.column:contains("Two")').invoke('width').should('be.closeTo', 200, 0.1)
    cy.get('div.column:contains("Three")').invoke('width').should('be.closeTo', 200, 0.1)
    cy.window().trigger('mouseup', {clientX: 443, clientY: 5})
    cy.get('div.column:contains("Two")').invoke('width').should('be.closeTo', 200, 0.1)
    cy.get('div.column:contains("Three")').invoke('width').should('be.closeTo', 200, 0.1)
  })

  it('resizes right columns', () => {
    mount()

    cy.viewport(846, 400)

    cy.get('div.column:contains("Three")').invoke('width').should('eq', 200)
    cy.get('div.column:contains("Four")').invoke('width').should('eq', 200)

    cy.get('div.gutter').eq(2).trigger('mousedown', { clientX: 423, clientY: 5 })
    cy.window().trigger('mousemove', {clientX: 413, clientY: 5})
    cy.get('div.column:contains("Three")').invoke('width').should('be.closeTo', 190, 0.1)
    cy.get('div.column:contains("Four")').invoke('width').should('be.closeTo', 210, 0.1)
    cy.window().trigger('mousemove', {clientX: 403, clientY: 5})
    cy.get('div.column:contains("Three")').invoke('width').should('be.closeTo', 180, 0.1)
    cy.get('div.column:contains("Four")').invoke('width').should('be.closeTo', 220, 0.1)
    cy.window().trigger('mouseup', {clientX: 403, clientY: 5})
    cy.get('div.column:contains("Three")').invoke('width').should('be.closeTo', 180, 0.1)
    cy.get('div.column:contains("Four")').invoke('width').should('be.closeTo', 220, 0.1)

    cy.get('div.gutter').eq(2).trigger('mousedown', { clientX: 423, clientY: 5 })
    cy.window().trigger('mousemove', {clientX: 433, clientY: 5})
    cy.get('div.column:contains("Three")').invoke('width').should('be.closeTo', 190, 0.1)
    cy.get('div.column:contains("Four")').invoke('width').should('be.closeTo', 210, 0.1)
    cy.window().trigger('mousemove', {clientX: 443, clientY: 5})
    cy.get('div.column:contains("Three")').invoke('width').should('be.closeTo', 200, 0.1)
    cy.get('div.column:contains("Four")').invoke('width').should('be.closeTo', 200, 0.1)
    cy.window().trigger('mouseup', {clientX: 443, clientY: 5})
    cy.get('div.column:contains("Three")').invoke('width').should('be.closeTo', 200, 0.1)
    cy.get('div.column:contains("Four")').invoke('width').should('be.closeTo', 200, 0.1)
  })

  it('snaps first column', () => {
    mount()

    cy.viewport(846, 400)

    cy.get('div.column:contains("One")').invoke('width').should('eq', 200)

    cy.get('div.gutter').eq(0).trigger('mousedown', { clientX: 423, clientY: 5 })
    cy.window().trigger('mousemove', {clientX: 296, clientY: 5})
    cy.get('div.column:contains("One")').should('not.exist')
    cy.window().trigger('mousemove', {clientX: 297, clientY: 5})
    cy.get('div.column:contains("One")').invoke('width').should('be.closeTo', 74, 0.1)
    cy.window().trigger('mousemove', {clientX: 296, clientY: 5})
    cy.get('div.column:contains("One")').should('not.exist')
    cy.get('div.column:contains("Two")').invoke('width').should('be.closeTo', 376, 0.1)

    cy.window().trigger('mouseup', {clientX: 296, clientY: 5})

    cy.get('.uncollapse').click()
    cy.get('div.column:contains("One")').invoke('width').should('be.closeTo', 164, 0.1)
    cy.get('div.column:contains("Two")').invoke('width').should('be.closeTo', 308.2, 0.1)
    cy.get('div.column:contains("Three")').invoke('width').should('be.closeTo', 164, 0.1)
    cy.get('div.column:contains("Four")').invoke('width').should('be.closeTo', 164, 0.1)
  })

  it('snaps second column - left', () => {
    mount()

    cy.viewport(846, 400)

    cy.get('div.column:contains("Two")').invoke('width').should('eq', 200)

    cy.get('div.gutter').eq(0).trigger('mousedown', { clientX: 423, clientY: 5 })
    cy.window().trigger('mousemove', {clientX: 554, clientY: 5})
    cy.get('div.column:contains("Two")').should('not.exist')
    cy.window().trigger('mousemove', {clientX: 553, clientY: 5})
    cy.get('div.column:contains("Two")').invoke('width').should('be.closeTo', 70, 0.1)
    cy.window().trigger('mousemove', {clientX: 554, clientY: 5})
    cy.get('div.column:contains("Two")').should('not.exist')
    cy.get('div.column:contains("One")').invoke('width').should('be.closeTo', 380, 0.1)

    cy.window().trigger('mouseup', {clientX: 554, clientY: 5})

    cy.get('.uncollapse').click()
    cy.get('div.column:contains("One")').invoke('width').should('be.closeTo', 310.2, 0.1)
    cy.get('div.column:contains("Two")').invoke('width').should('be.closeTo', 163.3, 0.1)
    cy.get('div.column:contains("Three")').invoke('width').should('be.closeTo', 163.3, 0.1)
    cy.get('div.column:contains("Four")').invoke('width').should('be.closeTo', 163.3, 0.1)
  })

  it('snaps second column - right', () => {
    mount()

    cy.viewport(846, 400)

    cy.get('div.column:contains("Two")').invoke('width').should('eq', 200)

    cy.get('div.gutter').eq(1).trigger('mousedown', { clientX: 423, clientY: 5 })
    cy.window().trigger('mousemove', {clientX: 292, clientY: 5})
    cy.get('div.column:contains("Two")').should('not.exist')
    cy.window().trigger('mousemove', {clientX: 293, clientY: 5})
    cy.get('div.column:contains("Two")').invoke('width').should('be.closeTo', 70, 0.1)
    cy.window().trigger('mousemove', {clientX: 292, clientY: 5})
    cy.get('div.column:contains("Two")').should('not.exist')
    cy.get('div.column:contains("Three")').invoke('width').should('be.closeTo', 380, 0.1)

    cy.window().trigger('mouseup', {clientX: 292, clientY: 5})

    cy.get('.uncollapse').click()
    cy.get('div.column:contains("One")').invoke('width').should('be.closeTo', 163.3, 0.1)
    cy.get('div.column:contains("Two")').invoke('width').should('be.closeTo', 163.3, 0.1)
    cy.get('div.column:contains("Three")').invoke('width').should('be.closeTo', 310.2, 0.1)
    cy.get('div.column:contains("Four")').invoke('width').should('be.closeTo', 163.3, 0.1)
  })

  it('snaps last column', () => {
    mount()

    cy.viewport(846, 400)

    cy.get('div.column:contains("Four")').invoke('width').should('eq', 200)

    cy.get('div.gutter').eq(2).trigger('mousedown', { clientX: 423, clientY: 5 })
    cy.window().trigger('mousemove', {clientX: 550, clientY: 5})
    cy.get('div.column:contains("Four")').should('not.exist')
    cy.window().trigger('mousemove', {clientX: 549, clientY: 5})
    cy.get('div.column:contains("Four")').invoke('width').should('be.closeTo', 74, 0.1)
    cy.window().trigger('mousemove', {clientX: 550, clientY: 5})
    cy.get('div.column:contains("Four")').should('not.exist')
    cy.get('div.column:contains("Three")').invoke('width').should('be.closeTo', 376, 0.1)

    cy.window().trigger('mouseup', {clientX: 550, clientY: 5})

    cy.get('.uncollapse').click()
    cy.get('div.column:contains("One")').invoke('width').should('be.closeTo', 164, 0.1)
    cy.get('div.column:contains("Two")').invoke('width').should('be.closeTo', 164, 0.1)
    cy.get('div.column:contains("Three")').invoke('width').should('be.closeTo', 308.2, 0.1)
    cy.get('div.column:contains("Four")').invoke('width').should('be.closeTo', 164, 0.1)
  })
})
