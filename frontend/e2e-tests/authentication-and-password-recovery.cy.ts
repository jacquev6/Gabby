import { loadFixtures, notBusy, visit } from './utils'


describe('Gabby\'s authentication system', () => {
  before(() => {
    console.clear()
    loadFixtures('test-users')
  })

  it('logs in and out', () => {
    visit('/')
    cy.wait(1000)  // This is a workaround for fields being reset after we type in them. I can't figure out why this happens.

    cy.get('h1:contains("Existing projects")').should('not.exist')
    cy.get('h1:contains("Please log in")').should('exist')

    cy.get('[name=username]').type('jacquev6+gabby-dev-alice@gmail.com', {delay: 0})
    cy.get('[name=password]').type('alice-password', {delay: 0})
    cy.get('button:contains("Log in")').click()

    notBusy()

    cy.get('h1:contains("Please log in")').should('not.exist')
    cy.get('h1:contains("Existing projects")').should('exist')

    cy.get('a:contains("Log out")').click()

    cy.get('h1:contains("Existing projects")').should('not.exist')
    cy.get('h1:contains("Please log in")').should('exist')
  })

  it('warns about wrong credentials', () => {
    visit('/')
    cy.wait(1000)  // Workaround, described above.

    cy.get('[name=username]').type('jacquev6+gabby-dev-alice@gmail.com', {delay: 0})
    cy.get('[name=password]').type('not-alice-password', {delay: 0})
    cy.get('button:contains("Log in")').click()

    notBusy()

    cy.get('h1:contains("Please log in")').should('exist')
    cy.get('p:contains("Login failed. Please check your credentials.")').should('exist')
    cy.get('[name=password]').should('have.value', '')
  })

  it('does not request a password recovery link', () => {
    visit('/')
    cy.wait(1000)  // Workaround, described above.

    cy.get('h1:contains("Please log in")').should('exist')

    cy.get('a:contains("Lost password?")').click()

    cy.get('h1:contains("Please log in")').should('not.exist')
    cy.get('h1:contains("Lost password")').should('exist')

    cy.get('button:contains("Back")').click()

    cy.get('h1:contains("Please log in")').should('exist')
    cy.get('h1:contains("Lost password")').should('not.exist')
  })

  it('requests a password recovery link', () => {
    visit('/')
    cy.wait(1000)  // Workaround, described above.

    cy.get('h1:contains("Please log in")').should('exist')

    cy.get('a:contains("Lost password?")').click()

    cy.get('h1:contains("Please log in")').should('not.exist')
    cy.get('h1:contains("Lost password")').should('exist')

    cy.get('[name=username]').type('jacquev6+gabby-dev-alice@gmail.com', {delay: 0})

    cy.intercept('POST', '/api/recoveryEmailRequests', {
      statusCode: 201,
      headers: {
        'Content-Type': 'application/vnd.api+json',
      },
      body: {
        "data": {
          "type": "recoveryEmailRequest",
          "id": "random-uuid",
          "links": {
              "self": "http://fanout:8080/api/recoveryEmailRequests/random-uuid"
          }
        }
      },
    }).as('recoveryEmailRequest')

    cy.get('button:contains("Send")').click()

    cy.wait('@recoveryEmailRequest')

    cy.get('p:contains("Recovery e-mail submitted. Please check your inbox.")').should('exist')
  })

  // Get a token (hack for testing, not the usual flow)
  function getTokenThen(f: (token: string) => void) {
    visit('/')
    cy.wait(1000)  // Workaround, described above.
    cy.get('[name=username]').type('jacquev6+gabby-dev-alice@gmail.com', {delay: 0})
    cy.get('[name=password]').type('alice-password', {delay: 0})
    cy.intercept('POST', '/api/token').as('tokenRequest')
    cy.get('button:contains("Log in")').click()
    notBusy()
    cy.get('a:contains("Log out")').click()
    cy.wait('@tokenRequest').its('response.body.access_token').then(f)
  }

  it('resets a password', () => {
    getTokenThen((token) => {
      visit(`/reset-password/jacquev6+gabby-dev-alice@gmail.com/${token}`)
      cy.wait(1000)  // Workaround, described above.

      cy.get('h1:contains("Reset password")').should('exist')
      cy.get('label:contains("New password")').first().next().type('new-alice-password', {delay: 0})
      cy.get('label:contains("New password")').last().next().type('new-alice-password', {delay: 0})
      cy.get('button:contains("Reset password")').click()

      notBusy()

      cy.get('h1:contains("Reset password")').should('not.exist')
      cy.get('h1:contains("Please log in")').should('not.exist')
      cy.get('h1:contains("Existing projects")').should('exist')

      cy.get('a:contains("Log out")').click()

      cy.get('[name=username]').type('jacquev6+gabby-dev-alice@gmail.com', {delay: 0})
      cy.get('[name=password]').type('alice-password', {delay: 0})
      cy.get('button:contains("Log in")').click()

      notBusy()
      cy.get('h1:contains("Please log in")').should('exist')
      cy.get('p:contains("Login failed. Please check your credentials.")').should('exist')

      cy.get('[name=password]').type('new-alice-password', {delay: 0})
      cy.get('button:contains("Log in")').click()

      cy.get('h1:contains("Please log in")').should('not.exist')
      cy.get('h1:contains("Existing projects")').should('exist')
    })
  })

  it('warns about passwords being different', () => {
    visit('/reset-password/jacquev6+gabby-dev-alice@gmail.com/unused-json-web-token')
    cy.wait(1000)  // Workaround, described above.

    cy.get('button:contains("Reset password")').should('be.disabled')
    cy.get('p:contains("Passwords are different.")').should('not.exist')

    cy.get('label:contains("New password")').first().next().type('new-alice-password', {delay: 0})
    cy.get('label:contains("New password")').last().next().type('new-alice', {delay: 0})

    cy.get('button:contains("Reset password")').should('be.disabled')
    cy.get('p:contains("Passwords are different.")').should('exist')

    cy.get('label:contains("New password")').last().next().type('-password', {delay: 0})

    cy.get('button:contains("Reset password")').should('be.enabled')
    cy.get('p:contains("Passwords are different.")').should('not.exist')
  })
})
