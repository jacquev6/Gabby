import { useApiStore } from '../../frontend/src/frontend/stores/api'


function test(path, title, f = () => {}) {
  it(`${title} looks like this`, () => {
    cy.visit(path)
    cy.get('select').first().select('fr')
    cy.get('select').first().blur()
    cy.get('.busy').should('not.exist')
    f()
    cy.get('.busy').should('not.exist')
    cy.screenshot(title)
  })
}

function loadTestPdf() {
  cy.get('input[type=file]').selectFile('../pdf-examples/test.pdf')
}

describe('Gabby', () => {
  before(() => {
    console.clear
    cy.request('POST', '/reset-for-tests/yes-im-sure?fixtures=more-test-exercises,empty-project')
  })

  beforeEach(() => {
    cy.viewport(1600, 1200)
    cy.wrap(useApiStore()).then(api => api.auth.login('admin', 'password'))
  })

  test('/', 'home')

  test('/project-xkopqm', 'project-with-textbook')
  test('/project-fryrbl', 'project-with-independent-exercises')
  test('/project-ztmcex', 'empty-project')
  test('/project-xkopqm', 'edit-project', () => cy.get('button:contains("Modifier")').click())

  test('/project-xkopqm/textbook-klxufv/page-6', 'list-exercises-without-pdf')
  test('/project-xkopqm/textbook-klxufv/page-6', 'list-exercises', loadTestPdf)
  test('/project-xkopqm/textbook-klxufv/page-6/new-exercise', 'create-exercise', loadTestPdf)
  test('/project-xkopqm/textbook-klxufv/page-6/exercise-wbqloc', 'edit-exercise', loadTestPdf)

  test('/project-nope', 'project-not-found')
  test('/project-xkopqm/textbook-nope', 'textbook-not-found')
  // @todo /project-xkopqm/textbook-klxufv/page-6/exercise-nope
})
