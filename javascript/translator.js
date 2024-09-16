#!/usr/bin/env node

const brailleMap = {
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
  ' ': '......',
  CAP: '.....O',
  NUM: '.O.OOO' // Add number sign for numbers
}

const reverseBrailleMap = Object.fromEntries(
  Object.entries(brailleMap).map(([letter, braille]) => [braille, letter])
)

function isBraille (input) {
  return /^[O.]+$/.test(input)
}

function translateEnglishToBraille (input) {
  let braille = ''
  let isNumber = false // Flag for number mode

  for (const char of input) {
    switch (true) {
      case char >= '0' && char <= '9': // Handle digits
        if (!isNumber) {
          braille += brailleMap.NUM // Add number sign before the first digit
          isNumber = true
        }
        braille += brailleMap[char]
        break
      case char >= 'A' && char <= 'Z': // Handle uppercase letters
        if (isNumber) {
          isNumber = false // Exit number mode if a letter is encountered
        }
        braille += brailleMap.CAP + brailleMap[char.toLowerCase()]
        break
      case brailleMap[char] !== undefined: // Handle lowercase letters and spaces
        if (isNumber) {
          isNumber = false // Exit number mode if a non-digit is encountered
        }
        braille += brailleMap[char]
        break
      default:
        // Optionally handle unexpected characters
        break
    }
  }

  return braille
}

function translateBrailleToEnglish (input) {
  let english = ''
  let i = 0
  let isNumber = false

  while (i < input.length) {
    let charBraille = input.substring(i, i + 6)
    switch (charBraille) {
      case brailleMap.CAP:
        i += 6 // Move index past the CAP marker
        charBraille = input.substring(i, i + 6)
        english += reverseBrailleMap[charBraille] ? reverseBrailleMap[charBraille].toUpperCase() : ''
        break
      case brailleMap.NUM:
        isNumber = true // Enter number mode
        break
      case '......':
        english += ' ' // Add a space
        isNumber = false // Exit number mode
        break
      default:
        // Ternary to handle whether it's a number or letter
        english += isNumber
          ? (Object.entries(brailleMap).find(([key, value]) => value === charBraille && key >= '0' && key <= '9')?.[0] || '')
          : (reverseBrailleMap[charBraille] || '')
        break
    }
    // Move to the next Braille character (6 dots per character)
    i += 6
  }
  return english
}

function main () {
  const input = process.argv.slice(2).join(' ')

  if (!input) {
    console.error('Please provide a string to translate.')
    process.exit(1)
  }

  if (isBraille(input)) {
    console.log(translateBrailleToEnglish(input))
  } else {
    console.log(translateEnglishToBraille(input))
  }
}

main()
