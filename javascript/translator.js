const charToBrailleMap = {
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
  capitalFollows: '.....O',
  numberFollows: '.O.OOO',
}
const numToBrailleMap = {
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
}
const symbolToBrailleMap = {
  '.': '..OO.O',
  ',': '..O...',
  '?': '..O.OO',
  '!': '..OOO.',
  ':': '..OO..',
  ';': '..O.O.',
  '-': '....OO',
  '/': '.O..O.',
  '<': '.OO..O',
  '>': 'O..OO.',
  '(': 'O.O..O',
  ')': '.O.OO.',
}

//reverse the maps for braille to anything else
const brailleToCharMap = Object.entries(charToBrailleMap).reduce(
  (acc, [key, value]) => {
    acc[value] = key
    return acc
  },
  {}
)
const brailleToNumMap = Object.entries(numToBrailleMap).reduce(
  (acc, [key, value]) => {
    acc[value] = key
    return acc
  },
  {}
)
const brailleToSymbolMap = Object.entries(symbolToBrailleMap).reduce(
  (acc, [key, value]) => {
    acc[value] = key
    return acc
  },
  {}
)

const args = process.argv.slice(2)
const input = args.join(' ')

const main = () => {
  if (input === undefined) {
    console.log('No input provided')
    return
  }

  if (isBraille(input)) {
    console.log(translateBrailleToText(input))
  } else {
    console.log(translateTextToBraille(input))
  }
}

const isBraille = (input) => {
  const regex = /^(?=.*[O.])[O.]{2,}$/
  return regex.test(input)
}

const translateBrailleToText = (input) => {
  const brailleArray = splitStringIntoChunks(input)
  let result = ''
  let isCapital = false
  let isNumber = false

  const getChar = (braille) =>
    brailleToCharMap[braille] ||
    brailleToNumMap[braille] ||
    brailleToSymbolMap[braille]

  for (const braille of brailleArray) {
    const char = brailleToCharMap[braille]

    // Handle control characters (capitalFollows, numberFollows, and spaces)
    if (char === 'capitalFollows') {
      isCapital = true
      continue
    }
    if (char === 'numberFollows') {
      isNumber = true
      continue
    }
    if (char === ' ') {
      result += ' '
      isNumber = false // Reset number flag after space
      continue
    }

    // Handle numbers
    if (isNumber) {
      result += brailleToNumMap[braille]
      continue
    }

    // Handle symbols or regular characters
    const mappedChar = getChar(braille)
    if (isCapital) {
      result += mappedChar.toUpperCase()
      isCapital = false // Reset capital flag after use
    } else {
      result += mappedChar
    }
  }

  return result
}

const translateTextToBraille = (input) => {
  let braille = ''
  let isNumber = false

  for (let i = 0; i < input.length; i++) {
    const char = input[i]
    // Handle spaces
    if (char === ' ') {
      braille += charToBrailleMap[' '] // Add space
      isNumber = false
      continue
    }
    // Handle numbers
    if (!isNaN(char)) {
      if (!isNumber) {
        braille += charToBrailleMap['numberFollows'] // Add number indicator
        isNumber = true
      }
      braille += numToBrailleMap[char] // Map number to braille
      continue
    }

    // Handle symbols
    if (symbolToBrailleMap[char]) {
      braille += symbolToBrailleMap[char]
      isNumber = false
      continue
    }

    // Handle letters
    if (/[a-zA-Z]/.test(char)) {
      if (char === char.toUpperCase()) {
        braille += charToBrailleMap['capitalFollows'] // Add capital indicator
        braille += charToBrailleMap[char.toLowerCase()]
      } else {
        braille += charToBrailleMap[char]
      }
      isNumber = false
      continue
    }
  }

  return braille
}

const splitStringIntoChunks = (str) => {
  const chunks = []
  for (let i = 0; i < str.length; i += 6) {
    chunks.push(str.slice(i, i + 6))
  }
  return chunks
}

main()
