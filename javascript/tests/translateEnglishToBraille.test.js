const { translateEnglishToBraille } = require('../translator')

describe(translateEnglishToBraille, () => {
  it('should translate an English input into a Braille output, considering capital letters, spaces and special characters', () => {
    const expectedInput = 'Abc 123 xYz)'
    const expectedBrailleMessage =
      '.....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOOO...OO'

    const brailleMessage = translateEnglishToBraille(expectedInput)

    expect(brailleMessage).toEqual(expectedBrailleMessage)
  })
})
describe(translateEnglishToBraille, () => {
  it('should translate an English input into a Braille output, considering capital letters, spaces and special characters', () => {
    const expectedInput = '42>'
    const expectedBrailleMessage = '.O.OOOOO.O..O.O...O..OO.'

    const brailleMessage = translateEnglishToBraille(expectedInput)

    expect(brailleMessage).toEqual(expectedBrailleMessage)
  })
})
