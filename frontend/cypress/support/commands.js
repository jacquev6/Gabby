import 'cypress-wait-until'

Cypress.Commands.add('waitUntilLoaded', () => {
  cy.waitUntil(() => Cypress.$('.spinner-border').length == 0)
})
