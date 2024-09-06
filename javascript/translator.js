const testInput = process.argv.slice(2)
const input = testInput.join(' ') || 'Abc 123 xYz'
let output = ''
let consecutiveNumberCount = 0
let capitalNext = false
let numberNext = false
const brailleMatch = input.match(/O|\./g)
const braille = {
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
  '.....O': 'capital',
  '.O.OOO': 'number',
  '......': ' '
}

/* === functions === */

// function to determine if the next character(s) requires further logic
const setNextValueType = (value) => {
  if (!value) { return }

  if (value === 'capital' || value.match(/[A-Z]/g)) {
    return capitalNext = true

  } else if (value === 'number' || value.match(/\d/g)) {
    return numberNext = true
  }
}

// function to translate braille to english characters
const brailleToEnglish = (value) => {

  if (value === ' ') {
    numberNext = false

  } else if (capitalNext) {
    capitalNext = false
    return value.toUpperCase()

  } else if (numberNext) {
    let number = Object.values(braille).indexOf(value) + 1

    if (number === 10) {
      number = 0
    } else if (number > 10) {
      number = '[Error: non-numerical character after "number follows"]'
    }

    return number
  }

  return value
}

// function to get the braille string linked to the english character
const getBraille = (value) => {
  return Object.keys(braille).find(key => braille[key] === value)
}

// function to translate english to braille dot series
const englishToBraille = (value) => {
  // reset for letters moving forward
  if (value.match(/^\D$/g)) { numberNext = false }

  if (numberNext) {
    consecutiveNumberCount += 1
    return (consecutiveNumberCount === 1 ? getBraille('number') : '') +
      (value === '0' ? Object.keys(braille)[parseInt(value) + 9] : Object.keys(braille)[parseInt(value) - 1])
  }
  
  value = (consecutiveNumberCount > 0 && value !== ' ' ? getBraille(' ') : '') +
    (capitalNext ? getBraille('capital') : '') +
    (getBraille(value.toLowerCase()))

  // reset next character logic
  if (capitalNext) { capitalNext = false }
  consecutiveNumberCount = 0
  return value
}

/* === begin === */

// translate braille to english if all characters are "O" and "." and total characters can be divided by 6
if (brailleMatch && brailleMatch.length === input.length && input.length % 6 === 0) {
  for (let i = 6; i <= input.length; i += 6) {
    const inputValue = input.slice(i - 6, i)
    const outputValue = braille[inputValue]

    if (!outputValue) {
      output = output.concat('[Error: invalid character]')

    } else if (!setNextValueType(outputValue)) {
      output = output.concat(brailleToEnglish(outputValue))
    }
  }

// otherwise translate english to braille
} else {
  const letters = input.split('')

  for (let i = 0; i <= letters.length - 1; i++) {
    setNextValueType(letters[i])
    output = output.concat(englishToBraille(letters[i]))
  }
}

// log translated string to console
console.log(output)