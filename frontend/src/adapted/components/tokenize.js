const wordChar = String.raw`\p{L}\p{M}\w`
const wordRegex = new RegExp(`[${wordChar}]+`, 'u')
const whitespaceChar = String.raw`\s`  // Could be completed with \p{Zs}
const whitespaceRegex = new RegExp(`[${whitespaceChar}]+`, 'u')
const splitRegex = new RegExp(`([${wordChar}]+)|([${whitespaceChar}]+)|([^${wordChar}${whitespaceChar}])`, 'gu')

export function tokenize(input) {
  if (input === '') {
    return []
  } else {
    const tokens = input.match(splitRegex)

    console.assert(tokens.join('') === input, `Tokenization failed: ${input} !== ${tokens.join(' ')}`)

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
