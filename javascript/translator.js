const BRAILLE_TO_ENGLISH = {
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
  '......': ' ',
  '.....O': 'cap',
  '.O.OOO': 'number',
  'O.O.OO': '.',
  'O..O.O': ',',
  '..O...': '?',
  '..OO.O': '!',
  '.O.O.O': ':',
  '..OO..': ';',
  '..O.O.': '-',
  '..O.OO': '/',
  '.OO..O': '<',
  'O..OO.': '>',
  'O...O.': '(',
  'O...OO': ')'
}

const BRAILLE_NUMBERS_TO_ENGLISH = {
  'O.....': '1',
  'O.O...': '2',
  'OO....': '3',
  'OO.O..': '4',
  'O..O..': '5',
  'OOO...': '6',
  'OOOO..': '7',
  'O.OO..': '8',
  '.OO...': '9',
  '.OOO..': '0'
}

const ENGLISH_TO_BRAILLE = {
  a: 'O.....',
  b: 'O.O...',
  c: 'OO....',
  d: 'OO.O..',
  e: 'O..O..',
  f: 'OOO...',
  g: 'OOOO..',
  h: 'O.OO..',
  i: '.OO...',
  j: '.OOO..',
  k: 'O...O.',
  l: 'O.O.O.',
  m: 'OO..O.',
  n: 'OO.OO.',
  o: 'O..OO.',
  p: 'OOO.O.',
  q: 'OOOOO.',
  r: 'O.OOO.',
  s: '.OO.O.',
  t: '.OOOO.',
  u: 'O...OO',
  v: 'O.O.OO',
  w: '.OOO.O',
  x: 'OO..OO',
  y: 'OO.OOO',
  z: 'O..OOO',
  ' ': '......',
  1: 'O.....',
  2: 'O.O...',
  3: 'OO....',
  4: 'OO.O..',
  5: 'O..O..',
  6: 'OOO...',
  7: 'OOOO..',
  8: 'O.OO..',
  9: '.OO...',
  0: '.OOO..',
  cap: '.....O',
  number: '.O.OOO',
  '.': 'O.O.OO',
  ',': 'O..O.O',
  '?': '..O...',
  '!': '..OO.O',
  ':': '.O.O.O',
  ';': '..OO..',
  '-': '..O.O.',
  '/': '..O.OO',
  '<': '.OO..O',
  '>': 'O..OO.',
  '(': 'O...O.',
  ')': 'O...OO'
}

function translateEnglishToBraille(input) {
  let result = ''
  let isNumber = false

  for (const char of input) {
    if (char >= '0' && char <= '9') {
      if (!isNumber) {
        result += '.O.OOO'
        isNumber = true
      }
      result += ENGLISH_TO_BRAILLE[char]
    } else {
      if (isNumber) {
        isNumber = false
      }
      if (char >= 'A' && char <= 'Z') {
        result +=
          ENGLISH_TO_BRAILLE['cap'] + ENGLISH_TO_BRAILLE[char.toLowerCase()]
      } else {
        result += ENGLISH_TO_BRAILLE[char]
      }
    }
  }
  return result
}

function translateBrailleToEnglish(input) {
  let result = ''
  let capitalFollows = false
  let numberFollows = false

  for (let i = 0; i < input.length; i += 6) {
    const brailleChar = input.slice(i, i + 6)

    if (brailleChar === '.....O') {
      capitalFollows = true
    } else if (brailleChar === '.O.OOO') {
      numberFollows = true
    } else if (brailleChar === '.O...O') {
      result += '.'
    } else if (numberFollows) {
      if (brailleChar === ENGLISH_TO_BRAILLE[' ']) {
        result += ' '
        numberFollows = false
      } else {
        result += BRAILLE_NUMBERS_TO_ENGLISH[brailleChar]
      }
    } else {
      let char = BRAILLE_TO_ENGLISH[brailleChar]
      if (capitalFollows) char = char.toUpperCase()
      capitalFollows = false
      result += char
    }
  }
  return result
}

function isBraille(input) {
  return /^[O. ]+$/.test(input)
}

function translate(input) {
  if (isBraille(input)) {
    return translateBrailleToEnglish(input)
  } else {
    return translateEnglishToBraille(input)
  }
}

const input = process.argv.slice(2).join(' ')
console.log(translate(input))

// module.exports = { translateEnglishToBraille, translateBrailleToEnglish }
