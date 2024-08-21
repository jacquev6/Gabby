import { useApiStore } from '../src/frontend/stores/api'


function setLocale() {
  cy.get('select[data-cy="language"]').last().select('fr')
  cy.focused().blur()
}

function test(path: string, title: string, f = () => {}, it_: Mocha.ExclusiveTestFunction = it) {
  it_(`${title} looks like this`, () => {
    cy.visit(path)
    setLocale()
    cy.get('.busy').should('not.exist')
    f()
    cy.get('.busy').should('not.exist')
    cy.screenshot(title)
  })
}

test['only'] = (path: string, title: string, f: () => void) => test(path, title, f, it['only'])

function loadPdf(name: string) {
  return () => cy.get('input[type=file]').selectFile(`../pdf-examples/${name}.pdf`)
}

const loadTestPdf = loadPdf('test')

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
  test('/project-xkopqm/textbook-nope/page-1', 'textbook-not-found')
  test('/project-xkopqm/textbook-klxufv/page-6/exercise-nope', 'exercise-not-found')
})
