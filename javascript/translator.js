const brailleDict = {
  'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
  'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
  'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
  'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
  'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
  'z': 'O..OOO', ' ': '......', 'cap': '.....O', 'num': '.O.OOO',
  '0': '.OOOOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
  '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}

const reverseBrailleDict = Object.entries(brailleDict).reduce((acc, [key, value]) => {
  acc[value] = key
  return acc
}, {})

function isBraille(input) {
  return /^[O.]+$/.test(input)
}

function englishToBraille(input) {
  let brailleOutput = ''
  let numberMode = false

  for (let char of input) {
    if (char === ' ') {
      brailleOutput += brailleDict[' ']
      numberMode = false
    } else if (/[A-Z]/.test(char)) {
      brailleOutput += brailleDict['cap'] + brailleDict[char.toLowerCase()]
      numberMode = false
    } else if (/[0-9]/.test(char)) {
      if (!numberMode) {
        brailleOutput += brailleDict['num']
        numberMode = true
      }
      brailleOutput += brailleDict[char]
    } else {
      brailleOutput += brailleDict[char]
      numberMode = false
    }
  }

  return brailleOutput
}

function brailleToEnglish(input) {
  let englishOutput = ''
  let i = 0
  let capitalMode = false
  let numberMode = false

  while (i < input.length) {
    let brailleChar = input.slice(i, i + 6)

    if (brailleChar === brailleDict[' ']) {
      englishOutput += ' '
      numberMode = false
      capitalMode = false
    } else if (brailleChar === brailleDict['cap']) {
      capitalMode = true
    } else if (brailleChar === brailleDict['num']) {
      numberMode = true
    } else {
      let char = reverseBrailleDict[brailleChar]
      if (numberMode) {
        englishOutput += char
      } else {
        englishOutput += capitalMode ? char.toUpperCase() : char
        capitalMode = false
      }
    }

    i += 6
  }

  return englishOutput
}

function main() {
  const input = process.argv.slice(2).join(' ')

  if (isBraille(input)) {
    console.log(brailleToEnglish(input))
  } else {
    console.log(englishToBraille(input))
  }
}

main()
