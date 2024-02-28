import 'cypress-wait-until'

Cypress.Commands.add('waitUntilLoaded', () => {
  cy.waitUntil(() => Cypress.$('.spinner-border').length == 0)
})

// https://github.com/cypress-io/cypress/issues/17712#issuecomment-1646614336
Cypress.Commands.add('vue', () => {
  return cy.wrap(Cypress.vueWrapper);
});
