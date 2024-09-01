const { translateBrailleToEnglish } = require('../translator')

describe(translateBrailleToEnglish, () => {
  it('should translate a Braille input into an English output, considering capital letters, spaces and special characters', () => {
    const expectedInput =
      '.....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOOO...OO'
    const expectedEnglishMessage = 'Abc 123 xYz)'

    const englishMessage = translateBrailleToEnglish(expectedInput)

    expect(englishMessage).toEqual(expectedEnglishMessage)
  })
})
describe(translateBrailleToEnglish, () => {
  it('should translate a Braille input into an English output, considering capital letters, spaces and special characters', () => {
    const expectedInput =
      '.....OO.....O.O...OO...........O.OOOO.....O.O...OO....'
    const expectedEnglishMessage = 'Abc 123'

    const englishMessage = translateBrailleToEnglish(expectedInput)

    expect(englishMessage).toEqual(expectedEnglishMessage)
  })
})
