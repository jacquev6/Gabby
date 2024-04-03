import { tokenize } from './tokenize.js'


describe('Tokenize tokenizes...', () => {
  it('simple word', () => {
    expect(tokenize('hello')).to.deep.equal([{kind: 'word', token: 'hello'}])
  })

  it('accentuated word', () => {
    expect(tokenize('àéïîöôù')).to.deep.equal([{kind: 'word', token: 'àéïîöôù'}])
  })

  it('german word', () => {
    expect(tokenize('Straße')).to.deep.equal([{kind: 'word', token: 'Straße'}])
  })

  it('numbers (as word, we could decide to change that)', () => {
    expect(tokenize('120')).to.deep.equal([{kind: 'word', token: '120'}])
  })

  it('whitespace', () => {
    expect(tokenize('  \t\n\t  ')).to.deep.equal([{kind: 'whitespace', token: '  \t\n\t  '}])
  })

  it('punctuation', () => {
    expect(tokenize('!')).to.deep.equal([{kind: 'punctuation', token: '!'}])
  })

  it('successive punctuation', () => {
    expect(tokenize('Un martien ?!(vert).')).to.deep.equal([
      {kind: 'word', token: 'Un'},
      {kind: 'whitespace', token: ' '},
      {kind: 'word', token: 'martien'},
      {kind: 'whitespace', token: ' '},
      {kind: 'punctuation', token: '?'},
      {kind: 'punctuation', token: '!'},
      {kind: 'punctuation', token: '('},
      {kind: 'word', token: 'vert'},
      {kind: 'punctuation', token: ')'},
      {kind: 'punctuation', token: '.'},
    ])
  })
})
