// https://github.com/cypress-io/cypress/issues/17712#issuecomment-1646614336
Cypress.Commands.add('vue', () => cy.wrap(Cypress.vueWrapper))
