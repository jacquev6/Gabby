const wordChar = String.raw`\p{L}\p{M}\w`
const wordRegex = new RegExp(`[${wordChar}]+`, 'u')
const whitespaceChar = String.raw`\s`  // Could be completed with \p{Zs}
const whitespaceRegex = new RegExp(`[${whitespaceChar}]+`, 'u')
const splitRegex = new RegExp(`([${wordChar}]+)|([${whitespaceChar}]+)|([^${wordChar}${whitespaceChar}])`, 'gu')

// @todo Find a way to give this type to 'console.assert' globally, and use 'console.assert' itself instead of creating a local alias
const assert: (condition: any, message?: string) => asserts condition = console.assert

export function tokenize(input: string): Array<{kind: 'word' | 'whitespace' | 'punctuation', text: string}> {
  if (input === '') {
    return []
  } else {
    const tokens = input.match(splitRegex)

    assert(tokens !== null)
    assert(tokens.join('') === input, `Tokenization failed: ${input} !== ${tokens.join(' ')}`)

    return tokens.map(text => {
      if (text.match(wordRegex)) {
        return {kind: 'word', text}
      } else if (text.match(whitespaceRegex)) {
        return {kind: 'whitespace', text}
      } else {
        return {kind: 'punctuation', text}
      }
    })
  }
}
