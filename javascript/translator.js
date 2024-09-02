const input = process.argv.slice(2).join(' ')

let lang = 'english'
if (input.split('').filter((el) => el != 'O' && el != '.') == '') {
  lang = 'braille'
}

// For Braille to English, we will parse each character, then go through the results

function reverseDict(dict) {
  return Object.fromEntries(
    Object.entries(dict).map(([key, val]) => [val, key]),
  )
}

const brailleToLowerCaseLetter = {
  'O.....': 'a',
  'O.O...': 'b',
  'OO....': 'c',
  'OO.O..': 'd',
  'O..O..': 'e',
  'OOO...': 'f',
  'OOOO..': 'g',
  'O.OO..': 'h',
  '.OO...': 'i',
  '.OOO..': 'j',
  'O...O.': 'k',
  'O.O.O.': 'l',
  'OO..O.': 'm',
  'OO.OO.': 'n',
  'O..OO.': 'o',
  'OOO.O.': 'p',
  'OOOOO.': 'q',
  'O.OOO.': 'r',
  '.OO.O.': 's',
  '.OOOO.': 't',
  'O...OO': 'u',
  'O.O.OO': 'v',
  '.OOO.O': 'w',
  'OO..OO': 'x',
  'OO.OOO': 'y',
  'O..OOO': 'z',
}

const lowerCaseLetterToBraille = reverseDict(brailleToLowerCaseLetter)

const upperCaseLetterToBraille = {
  A: '.....OO.....',
  B: '.....OO.O...',
  C: '.....OOO....',
  D: '.....OOO.O..',
  E: '.....OO..O..',
  F: '.....OOOO...',
  G: '.....OOOOO..',
  H: '.....OO.OO..',
  I: '.....O.OO...',
  J: '.....O.OOO..',
  K: '.....OO...O.',
  L: '.....OO.O.O.',
  M: '.....OOO..O.',
  N: '.....OOO.OO.',
  O: '.....OO..OO.',
  P: '.....OOOO.O.',
  Q: '.....OOOOOO.',
  R: '.....OO.OOO.',
  S: '.....O.OO.O.',
  T: '.....O.OOOO.',
  U: '.....OO...OO',
  V: '.....OO.O.OO',
  W: '.....O.OOO.O',
  X: '.....OOO..OO',
  Y: '.....OOO.OOO',
  Z: '.....OO..OOO',
}

const brailleToNumber = {
  'O.....': '1',
  'O.O...': '2',
  'OO....': '3',
  'OO.O..': '4',
  'O..O..': '5',
  'OOO...': '6',
  'OOOO..': '7',
  'O.OO..': '8',
  '.OO...': '9',
  '.OOO..': '0',
}

const numberToBraille = reverseDict(brailleToNumber)

const brailleToDirective = {
  '.....O': 'capital follows',
  '.O...O': 'decimal follows',
  '.O.OOO': 'number follows',
}

const directiveToBraille = reverseDict(brailleToDirective)

const brailleToSpecialCharacter = {
  '..OO.O': '.',
  '..O...': ',',
  '..O.OO': '?',
  '..OOO.': '!',
  '..OO..': ':',
  '..O.O.': ';',
  '....OO': '-',
  '.O..O.': '/',
  '.OO..O': '<',
  'O..OO.': '>',
  'O.O..O': '(',
  '.O.OO.': ')',
  '......': ' ',
}

const specialCharacterToBraille = reverseDict(brailleToSpecialCharacter)

let chars = []
let inputArr = input.split('')

if (lang === 'braille') {
  let isDecimal = false
  let isCapitalLetter = false
  let isNumber = false

  for (let i = 0; i < inputArr.length - 5; i += 6) {
    const rawChar = inputArr.slice(i, i + 6).join('')

    // console.log(rawChar)

    if (isCapitalLetter) {
      const letter = brailleToLowerCaseLetter[rawChar].toUpperCase()
      //   console.log(letter)
      chars.push(letter)
      isCapitalLetter = false
    } else if (isDecimal) {
      const number = brailleToNumber[rawChar]
      //   console.log(number)
      chars.push(number)
    } else if (isNumber) {
      const number = brailleToNumber[rawChar]
      //   console.log(number)
      chars.push(number)
    } else if (Object.keys(brailleToDirective).includes(rawChar)) {
      const directive = brailleToDirective[rawChar]
      if (directive === 'capital follows') {
        isCapitalLetter = true
      } else if (directive === 'decimal follows') {
        isDecimal = true
      } else if (directive === 'number follows') {
        isNumber = true
      }
    } else if (Object.keys(brailleToLowerCaseLetter).includes(rawChar)) {
      const letter = brailleToLowerCaseLetter[rawChar]
      //   console.log(letter)
      chars.push(letter)
    } else if (Object.keys(brailleToSpecialCharacter).includes(rawChar)) {
      const character = brailleToSpecialCharacter[rawChar]
      //   console.log(character)
      if (character === ' ') {
        isDecimal = false
        isNumber = false
      }
      chars.push(character)
    }
  }
} else {
  for (let i = 0; i < inputArr.length; i += 1) {
    let rawChar = inputArr[i]

    const num = parseInt(inputArr[i])
    // When first number is encountered, start reading each until space or end
    if (!isNaN(num)) {
      let numString = []
      let isDecimal = false
      i--
      while (i < inputArr.length && rawChar !== ' ') {
        i++
        rawChar = inputArr[i]
        if (
          rawChar == '.' &&
          i + 1 < inputArr.length &&
          !isNaN(parseInt(inputArr[i + 1]))
        ) {
          isDecimal = true
          numString.push(specialCharacterToBraille['.'])
        } else {
          numString.push(numberToBraille[rawChar])
        }
      }

      if (rawChar === ' ') {
        numString.push(specialCharacterToBraille[' '])
      }

      if (isDecimal) {
        chars.push(directiveToBraille['decimal follows'])
      } else {
        chars.push(directiveToBraille['number follows'])
      }

      chars.push(...numString)

      continue
    }

    if (Object.keys(lowerCaseLetterToBraille).includes(rawChar)) {
      const letter = lowerCaseLetterToBraille[rawChar]
      chars.push(letter)
      //   console.log(letter)
    } else if (Object.keys(upperCaseLetterToBraille).includes(rawChar)) {
      const letter = upperCaseLetterToBraille[rawChar]
      chars.push(letter)
      //   console.log(letter)
    } else if (Object.keys(specialCharacterToBraille).includes(rawChar)) {
      const character = specialCharacterToBraille[rawChar]
      chars.push(character)
      //   console.log(character)
    }
  }
}

console.log(chars.join(''))
