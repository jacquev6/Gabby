const wordChar = String.raw`\p{L}\p{M}\w`
const wordRegex = new RegExp(`[${wordChar}]+`, 'u')
const whitespaceChar = String.raw`\s`  // Could be completed with \p{Zs}
const whitespaceRegex = new RegExp(`[${whitespaceChar}]+`, 'u')
const splitRegex = new RegExp(`([${wordChar}]+)|([${whitespaceChar}]+)|([^${wordChar}${whitespaceChar}])`, 'gu')

export function tokenize(input) {
  const tokens = input.match(splitRegex)

  console.assert(tokens.join('') === input, `Tokenization failed: ${input} !== ${tokens.join(' ')}`)

  return tokens.map(token => {
    if (token.match(wordRegex)) {
      return {kind: 'word', token}
    } else if (token.match(whitespaceRegex)) {
      return {kind: 'whitespace', token}
    } else {
      return {kind: 'punctuation', token}
    }
  })
}
