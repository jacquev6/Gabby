import { tokenize } from './tokenize'


describe('Tokenize tokenizes...', () => {
  it('empty string', () => {
    expect(tokenize('')).to.deep.equal([])
  })

  it('simple word', () => {
    expect(tokenize('hello')).to.deep.equal([{kind: 'word', text: 'hello'}])
  })

  it('accentuated word', () => {
    expect(tokenize('àéïîöôù')).to.deep.equal([{kind: 'word', text: 'àéïîöôù'}])
  })

  it('german word', () => {
    expect(tokenize('Straße')).to.deep.equal([{kind: 'word', text: 'Straße'}])
  })

  it('numbers (as word, we could decide to change that)', () => {
    expect(tokenize('120')).to.deep.equal([{kind: 'word', text: '120'}])
  })

  it('whitespace', () => {
    expect(tokenize('  \t\n\t  ')).to.deep.equal([{kind: 'whitespace', text: '  \t\n\t  '}])
  })

  it('punctuation', () => {
    expect(tokenize('!')).to.deep.equal([{kind: 'punctuation', text: '!'}])
  })

  it('successive punctuation', () => {
    expect(tokenize('Un martien ?!(vert).')).to.deep.equal([
      {kind: 'word', text: 'Un'},
      {kind: 'whitespace', text: ' '},
      {kind: 'word', text: 'martien'},
      {kind: 'whitespace', text: ' '},
      {kind: 'punctuation', text: '?'},
      {kind: 'punctuation', text: '!'},
      {kind: 'punctuation', text: '('},
      {kind: 'word', text: 'vert'},
      {kind: 'punctuation', text: ')'},
      {kind: 'punctuation', text: '.'},
    ])
  })
})
