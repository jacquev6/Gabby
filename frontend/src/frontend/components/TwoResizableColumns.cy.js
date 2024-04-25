import TwoResizableColumns from './TwoResizableColumns.vue'


function haveWidth(w) {
  return function(el) {
    expect(el.width()).to.be.within(w - 0.05, w + 0.05)
  }
}

const slots = {
  left: 'Left',
  right: 'Right',
}

describe('TwoResizableColumns', () => {
  before(console.clear)

  it('reacts to props', () => {
    cy.viewport(320, 200)
    cy.mount(
      TwoResizableColumns,
      {
        props: {
          leftWidth: '1fr',
          gutterWidth: '40px',
          rightWidth: '1fr',
        },
        slots,
      },
    )

    cy.get('div:contains("Left")').last().as('left')
    cy.get('div.gutter').as('gutter')
    cy.get('div:contains("Right")').last().as('right')

    cy.get('@left').should(haveWidth(140))
    cy.get('@gutter').should(haveWidth(40))
    cy.get('@right').should(haveWidth(140))

    cy.vue().then((w) => w.setProps({
      leftWidth: '1fr',
      gutterWidth: '20px',
      rightWidth: '2fr',
    }))

    cy.get('@left').should(haveWidth(100))
    cy.get('@gutter').should(haveWidth(20))
    cy.get('@right').should(haveWidth(200))
  })

  it('resizes columns', () => {
    cy.viewport(410, 200)
    cy.mount(
      TwoResizableColumns,
      {
        slots,
      },
    )

    cy.get('div:contains("Left")').last().as('left')
    cy.get('div.gutter').as('gutter')
    cy.get('div:contains("Right")').last().as('right')

    cy.get('@gutter').trigger('mousedown', {clientX: 205, clientY: 5})

    cy.get('@left').should(haveWidth(200))
    cy.get('@gutter').should(haveWidth(10))
    cy.get('@right').should(haveWidth(200))

    cy.window().trigger('mousemove', {clientX: 210, clientY: 5})

    cy.get('@left').should(haveWidth(205))
    cy.get('@gutter').should(haveWidth(10))
    cy.get('@right').should(haveWidth(195))

    cy.window().trigger('mousemove', {clientX: 150, clientY: 5})

    cy.get('@left').should(haveWidth(145))
    cy.get('@gutter').should(haveWidth(10))
    cy.get('@right').should(haveWidth(255))

    cy.window().trigger('mouseup', {clientX: 150, clientY: 5})

    cy.get('@left').should(haveWidth(145))
    cy.get('@gutter').should(haveWidth(10))
    cy.get('@right').should(haveWidth(255))
  })

  it('snaps and unsnaps left column', () => {
    cy.viewport(410, 200)
    cy.mount(
      TwoResizableColumns,
      {
        props: {
          leftWidth: '1fr',
          rightWidth: '1fr',
          snap: 100,
        },
        slots,
      },
    )

    cy.get('div:contains("Left")').last().as('left')
    cy.get('div.gutter').as('gutter')
    cy.get('div:contains("Right")').last().as('right')

    cy.get('@gutter').trigger('mousedown', {clientX: 205, clientY: 5})

    cy.get('@left').should(haveWidth(200))
    cy.get('@gutter').should(haveWidth(10))
    cy.get('@right').should(haveWidth(200))

    cy.window().trigger('mousemove', {clientX: 105, clientY: 5})

    cy.get('@left').should(haveWidth(100))
    cy.get('@gutter').should(haveWidth(10))
    cy.get('@right').should(haveWidth(300))

    cy.window().trigger('mousemove', {clientX: 104, clientY: 5})

    cy.get('@left').should('not.be.visible')
    cy.get('div:contains(">>")').last().should(haveWidth(20))
    cy.get('@gutter').should(haveWidth(10))
    cy.get('@right').should(haveWidth(380))

    cy.window().trigger('mousemove', {clientX: 105, clientY: 5})

    cy.get('@left').should(haveWidth(100))
    cy.get('@gutter').should(haveWidth(10))
    cy.get('@right').should(haveWidth(300))

    cy.window().trigger('mouseup', {clientX: 105, clientY: 5})
  })

  it('does not snap left column', () => {
    cy.viewport(410, 200)
    cy.mount(
      TwoResizableColumns,
      {
        props: {
          leftWidth: '1fr',
          rightWidth: '1fr',
          snap: false,
        },
        slots,
      },
    )

    cy.get('div:contains("Left")').last().as('left')
    cy.get('div.gutter').as('gutter')
    cy.get('div:contains("Right")').last().as('right')

    cy.get('@gutter').trigger('mousedown', {clientX: 205, clientY: 5})

    cy.get('@left').should(haveWidth(200))
    cy.get('@gutter').should(haveWidth(10))
    cy.get('@right').should(haveWidth(200))

    cy.window().trigger('mousemove', {clientX: 104, clientY: 5})

    cy.get('@left').should(haveWidth(99))
    cy.get('@gutter').should(haveWidth(10))
    cy.get('@right').should(haveWidth(301))

    cy.window().trigger('mouseup', {clientX: 104, clientY: 5})
  })

  it('does not display button on zero-width left column', () => {
    cy.viewport(410, 200)
    cy.mount(
      TwoResizableColumns,
      {
        slots,
      },
    )

    cy.get('div:contains("Left")').last().as('left')
    cy.get('div.gutter').as('gutter')
    cy.get('div:contains("Right")').last().as('right')

    cy.get('@gutter').trigger('mousedown', {clientX: 205, clientY: 5})

    cy.get('@left').should(haveWidth(200))
    cy.get('@gutter').should(haveWidth(10))
    cy.get('@right').should(haveWidth(200))

    cy.window().trigger('mousemove', {clientX: 5, clientY: 5})

    cy.get('@left').should(haveWidth(0))
    cy.get('@gutter').should(haveWidth(10))
    cy.get('@right').should(haveWidth(400))
  })

  it('snaps then unsnaps left column', () => {
    cy.viewport(410, 200)
    cy.mount(
      TwoResizableColumns,
      {
        props: {
          leftWidth: '1fr',
          rightWidth: '1fr',
          snap: 100,
        },
        slots,
      },
    )

    cy.get('div:contains("Left")').last().as('left')
    cy.get('div.gutter').as('gutter')
    cy.get('div:contains("Right")').last().as('right')

    cy.get('@gutter').trigger('mousedown', {clientX: 205, clientY: 5})

    cy.get('@left').should(haveWidth(200))
    cy.get('@gutter').should(haveWidth(10))
    cy.get('@right').should(haveWidth(200))

    cy.window().trigger('mousemove', {clientX: 104, clientY: 5})

    cy.get('@left').should('not.be.visible')
    cy.get('div:contains(">>")').last().should(haveWidth(20))
    cy.get('@gutter').should(haveWidth(10))
    cy.get('@right').should(haveWidth(380))

    cy.window().trigger('mouseup', {clientX: 104, clientY: 5})

    cy.get('button:contains(">>")').click()

    cy.get('@left').should(haveWidth(200))
    cy.get('@gutter').should(haveWidth(10))
    cy.get('@right').should(haveWidth(200))

    cy.get('@gutter').trigger('mousedown', {clientX: 205, clientY: 5})

    cy.window().trigger('mousemove', {clientX: 145, clientY: 5})

    cy.get('@left').should(haveWidth(140))
    cy.get('@gutter').should(haveWidth(10))
    cy.get('@right').should(haveWidth(260))

    cy.window().trigger('mouseup', {clientX: 145, clientY: 5})
  })

  it('snaps and unsnaps right column', () => {
    cy.viewport(410, 200)
    cy.mount(
      TwoResizableColumns,
      {
        props: {
          leftWidth: '1fr',
          rightWidth: '1fr',
          snap: 100,
        },
        slots,
      },
    )

    cy.get('div:contains("Left")').last().as('left')
    cy.get('div.gutter').as('gutter')
    cy.get('div:contains("Right")').last().as('right')

    cy.get('@gutter').trigger('mousedown', {clientX: 205, clientY: 5})

    cy.get('@left').should(haveWidth(200))
    cy.get('@gutter').should(haveWidth(10))
    cy.get('@right').should(haveWidth(200))

    cy.window().trigger('mousemove', {clientX: 305, clientY: 5})

    cy.get('@left').should(haveWidth(300))
    cy.get('@gutter').should(haveWidth(10))
    cy.get('@right').should(haveWidth(100))

    cy.window().trigger('mousemove', {clientX: 306, clientY: 5})

    cy.get('@left').should(haveWidth(380))
    cy.get('@gutter').should(haveWidth(10))
    cy.get('@right').should('not.be.visible')
    cy.get('div:contains("<<")').last().should(haveWidth(20))

    cy.window().trigger('mousemove', {clientX: 305, clientY: 5})

    cy.get('@left').should(haveWidth(300))
    cy.get('@gutter').should(haveWidth(10))
    cy.get('@right').should(haveWidth(100))

    cy.window().trigger('mouseup', {clientX: 305, clientY: 5})
  })

  it('does not snap right column', () => {
    cy.viewport(410, 200)
    cy.mount(
      TwoResizableColumns,
      {
        props: {
          leftWidth: '1fr',
          rightWidth: '1fr',
          snap: false,
        },
        slots,
      },
    )

    cy.get('div:contains("Left")').last().as('left')
    cy.get('div.gutter').as('gutter')
    cy.get('div:contains("Right")').last().as('right')

    cy.get('@gutter').trigger('mousedown', {clientX: 205, clientY: 5})

    cy.get('@left').should(haveWidth(200))
    cy.get('@gutter').should(haveWidth(10))
    cy.get('@right').should(haveWidth(200))

    cy.window().trigger('mousemove', {clientX: 306, clientY: 5})

    cy.get('@left').should(haveWidth(301))
    cy.get('@gutter').should(haveWidth(10))
    cy.get('@right').should(haveWidth(99))

    cy.window().trigger('mouseup', {clientX: 306, clientY: 5})
  })

  it('does not display button on zero-width right column', () => {
    cy.viewport(410, 200)
    cy.mount(
      TwoResizableColumns,
      {
        slots,
      },
    )

    cy.get('div:contains("Left")').last().as('left')
    cy.get('div.gutter').as('gutter')
    cy.get('div:contains("Right")').last().as('right')

    cy.get('@gutter').trigger('mousedown', {clientX: 205, clientY: 5})

    cy.get('@left').should(haveWidth(200))
    cy.get('@gutter').should(haveWidth(10))
    cy.get('@right').should(haveWidth(200))

    cy.window().trigger('mousemove', {clientX: 405, clientY: 5})

    cy.get('@left').should(haveWidth(400))
    cy.get('@gutter').should(haveWidth(10))
    cy.get('@right').should(haveWidth(0))
  })

  it('snaps then unsnaps right column', () => {
    cy.viewport(410, 200)
    cy.mount(
      TwoResizableColumns,
      {
        props: {
          leftWidth: '1fr',
          rightWidth: '1fr',
          snap: 100,
        },
        slots,
      },
    )

    cy.get('div:contains("Left")').last().as('left')
    cy.get('div.gutter').as('gutter')
    cy.get('div:contains("Right")').last().as('right')

    cy.get('@gutter').trigger('mousedown', {clientX: 205, clientY: 5})

    cy.get('@left').should(haveWidth(200))
    cy.get('@gutter').should(haveWidth(10))
    cy.get('@right').should(haveWidth(200))

    cy.window().trigger('mousemove', {clientX: 306, clientY: 5})

    cy.get('@left').should(haveWidth(380))
    cy.get('@gutter').should(haveWidth(10))
    cy.get('@right').should('not.be.visible')
    cy.get('div:contains("<<")').last().should(haveWidth(20))

    cy.window().trigger('mouseup', {clientX: 306, clientY: 5})

    cy.get('button:contains("<<")').click()

    cy.get('@left').should(haveWidth(200))
    cy.get('@gutter').should(haveWidth(10))
    cy.get('@right').should(haveWidth(200))

    cy.get('@gutter').trigger('mousedown', {clientX: 205, clientY: 5})

    cy.window().trigger('mousemove', {clientX: 145, clientY: 5})

    cy.get('@left').should(haveWidth(140))
    cy.get('@gutter').should(haveWidth(10))
    cy.get('@right').should(haveWidth(260))

    cy.window().trigger('mouseup', {clientX: 145, clientY: 5})
  })
})
