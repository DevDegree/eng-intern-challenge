const CHAR_ASCII_TABLE = [
  97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112,
  113, 114, 115, 116, 117, 118, 119, 120, 121, 122,
]

const NUMBER_ASCII_TABLE = [49, 50, 51, 52, 53, 54, 55, 56, 57, 48]

const SIGN_ASCII_TABLE = [46, 44, 63, 33, 58, 59, 45, 47, 60, 62, 40, 41, 32]

const SYMBOL = ['CAPITAL', 'DECIMAL', 'NUMBER']

const BRAILLE_CHAR_ALPHABET = [
  'O.....',
  'O.O...',
  'OO....',
  'OO.O..',
  'O..O..',
  'OOO...',
  'OOOO..',
  'O.OO..',
  '.OO...',
  '.OOO..',
  'O...O.',
  'O.O.O.',
  'OO..O.',
  'OO.OO.',
  'O..OO.',
  'OOO.O.',
  'OOOOO.',
  'O.OOO.',
  '.OO.O.',
  '.OOOO.',
  'O...OO',
  'O.O.OO',
  '.OOO.O',
  'OO..OO',
  'OO.OOO',
  'O..OOO',
]

const BRAILLE_NUMBER_ALPHABET = [
  'O.....',
  'O.O...',
  'OO....',
  'OO.O..',
  'O..O..',
  'OOO...',
  'OOOO..',
  'O.OO..',
  '.OO...',
  '.OOO..',
]

const BRAILLE_SIGN_ALPHABET = [
  '..OO.O',
  '..O...',
  '..O.OO',
  '..OOO.',
  '..OO..',
  '..O.O.',
  '....OO',
  '.O..O.',
  '.OO..O',
  'O..OO.',
  'O.O..O',
  '.O.OO.',
  '......',
]

const BRAILLE_SYMBOL = ['.....O', '.O...O', '.O.OOO']

const join = (arr: string[]) => {
  let tempStr: string = ''
  for (var i in arr) {
    tempStr = tempStr + arr[i] + ' '
  }
  return tempStr
}

const checkInput = (arr: string[]) => {
  for (var i in arr) {
    if (arr[i] === '.' || arr[i] === 'O') {
      continue
    } else {
      return 'ENG'
    }
  }
  return 'BRA'
}

const brailleToEnglish = (myStr: string, checkStr: string[]) => {
  let tempArr: string[] = []
  let result: string = ''
  let symbol: string = 'NORMAL'
  let currentBrailleWord: string | undefined = ''
  let currentEnglishWord: string = ''
  // if input is Braille
  for (let i: number = 0; i < checkStr.length; i = i + 6) {
    tempArr.push(myStr.substring(i, i + 6))
  }
  for (var i in tempArr) {
    currentBrailleWord = tempArr[i]

    // if the current element can be found in BRAILLE_SYMBOL, give it to brailleSymbol; if it can not, give undefined to brailleSymbol.
    let brailleSymbol: string | undefined = BRAILLE_SYMBOL.find(
      (item) => item === currentBrailleWord
    )

    if (brailleSymbol) {
      // if brailleSymbol is exist, find the index of it in BRAILLE_SYMBOL
      let index: number = BRAILLE_SYMBOL.indexOf(brailleSymbol)
      // then give the English Symbol to symbol
      symbol = SYMBOL[index]

      currentEnglishWord = ''
      result = result + currentEnglishWord
    } else {
      //if current braille word is not one of the braille symbol, it should be number, english char or sign
      if (symbol === 'CAPITAL') {
        // if symbol is 'CAPITAL'
        // current element will be CAPITAL
        let index: number = BRAILLE_CHAR_ALPHABET.indexOf(currentBrailleWord)
        currentEnglishWord = String.fromCharCode(CHAR_ASCII_TABLE[index] - 32)
        result = result + currentEnglishWord
        symbol = 'NORMAL'
      } else if (symbol === 'DECIMAL') {
        // if symbol is 'CAPITAL'
        // following element will be DECIMAL
      } else if (symbol === 'NUMBER') {
        // if symbol is 'CAPITAL'
        // following element will be NUMBER until SPACE
        let index: number = BRAILLE_NUMBER_ALPHABET.indexOf(currentBrailleWord)
        if (index !== -1) {
          currentEnglishWord = String.fromCharCode(NUMBER_ASCII_TABLE[index])
        } else {
          index = BRAILLE_SIGN_ALPHABET.indexOf(currentBrailleWord)

          if (index === 12) {
            currentEnglishWord = String.fromCharCode(SIGN_ASCII_TABLE[index])
            symbol = 'NORMAL'
          } else {
            currentEnglishWord = String.fromCharCode(SIGN_ASCII_TABLE[index])
          }
        }

        result = result + currentEnglishWord
      } else {
        let index: number = BRAILLE_CHAR_ALPHABET.indexOf(currentBrailleWord)
        if (index !== -1) {
          currentEnglishWord = String.fromCharCode(CHAR_ASCII_TABLE[index])
        } else {
          index = BRAILLE_SIGN_ALPHABET.indexOf(currentBrailleWord)
          currentEnglishWord = String.fromCharCode(SIGN_ASCII_TABLE[index])
        }
        result = result + currentEnglishWord
      }
    }
  }
  return result
}

const isUpperChar = (char: string) => {
  return char.charCodeAt(0) >= 65 && char.charCodeAt(0) <= 90
}

const isLowerChar = (char: string) => {
  return char.charCodeAt(0) >= 97 && char.charCodeAt(0) <= 122
}

const isNumber = (char: string) => {
  return char.charCodeAt(0) >= 48 && char.charCodeAt(0) <= 57
}

const findIndexOfChar = (ascii: number) => {
  return CHAR_ASCII_TABLE.indexOf(ascii)
}
const getASCII = (char: string) => {
  return char.charCodeAt(0)
}
const findIndexOfNumber = (ascii: number) => {
  return NUMBER_ASCII_TABLE.indexOf(ascii)
}
const findIndexOfSign = (ascii: number) => {
  return SIGN_ASCII_TABLE.indexOf(ascii)
}

const englishToBraille = (myStr: string) => {
  let tempArr: string[] = []
  let result: string = ''
  let symbol: string = 'NORMAL'
  let currentBrailleWord: string | undefined = ''
  let currentEnglishWord: string = ''

  // if input is English
  tempArr = myStr.split('')
  tempArr.pop()

  for (var i in tempArr) {
    currentEnglishWord = tempArr[i]
    // check if current char is Uppercase char
    if (isUpperChar(currentEnglishWord)) {
      currentEnglishWord = currentEnglishWord.toLowerCase()
      let index = findIndexOfChar(getASCII(currentEnglishWord))
      currentBrailleWord = BRAILLE_SYMBOL[0] + BRAILLE_CHAR_ALPHABET[index]
    } else if (isLowerChar(currentEnglishWord)) {
      // check if current char is Lowercase char
      let index = findIndexOfChar(getASCII(currentEnglishWord))
      currentBrailleWord = BRAILLE_CHAR_ALPHABET[index]
    } else if (isNumber(currentEnglishWord)) {
      // check if current char is number
      // if last char is also a number
      if (isNumber(tempArr[Number(i) - 1])) {
        let index = findIndexOfNumber(getASCII(currentEnglishWord))
        currentBrailleWord = BRAILLE_NUMBER_ALPHABET[index]
      } else {
        let index = findIndexOfNumber(getASCII(currentEnglishWord))
        currentBrailleWord = BRAILLE_SYMBOL[2] + BRAILLE_NUMBER_ALPHABET[index]
      }
    } else {
      // check if current char is sign
      let index = findIndexOfSign(getASCII(currentEnglishWord))
      currentBrailleWord = BRAILLE_SIGN_ALPHABET[index]
    }
    result = result + currentBrailleWord
  }
  return result
}

const main = () => {
  let input: string[] = process.argv.slice(2)
  let mode: string = ''
  let myStr = join(input)
  let checkStr: string[] = myStr.split('').filter((c) => c !== ' ')
  let result: string = ''

  mode = checkInput(checkStr)

  if (mode === 'ENG') {
    result = englishToBraille(myStr)
  } else {
    result = brailleToEnglish(myStr, checkStr)
  }
  console.log(result)
}

main()
