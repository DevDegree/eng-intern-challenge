// Braille lookup tables for letters, numbers, and special symbols
const brailleAlphabet = {
  a: "O.....",
  b: "O.O...",
  c: "OO....",
  d: "OO.O..",
  e: "O..O..",
  f: "OOO...",
  g: "OOOO..",
  h: "O.OO..",
  i: ".OO...",
  j: ".OOO..",
  k: "O...O.",
  l: "O.O.O.",
  m: "OO..O.",
  n: "OO.OO.",
  o: "O..OO.",
  p: "OOO.O.",
  q: "OOOOO.",
  r: "O.OOO.",
  s: ".OO.O.",
  t: ".OOOO.",
  u: "O...OO",
  v: "O.O.OO",
  w: ".OOO.O",
  x: "OO..OO",
  y: "OO.OOO",
  z: "O..OOO",
  " ": "......",
}

// Special symbols for capital letters and numbers
const capitalIndicator = ".....O"
const numberIndicator = ".O.OOO"

const brailleNumbers = {
  1: "O.....",
  2: "O.O...",
  3: "OO....",
  4: "OO.O..",
  5: "O..O..",
  6: "OOO...",
  7: "OOOO..",
  8: "O.OO..",
  9: ".OO...",
  0: ".OOO..",
}

// Reverse lookup table for translating Braille back to English
const brailleToEnglish = Object.entries(brailleAlphabet).reduce(
  (obj, [key, value]) => {
    obj[value] = key
    return obj
  },
  {}
)

const brailleToNumbers = Object.entries(brailleNumbers).reduce(
  (obj, [key, value]) => {
    obj[value] = key
    return obj
  },
  {}
)

// detect if input is Braille or English
function isBraille(input) {
  return /^[O.]+$/.test(input) // checks if the string contains only 'O' and '.'
}

// translate English to Braille
function englishToBraille(text) {
  let brailleText = ""
  let isNumberMode = false

  for (const char of text) {
    if (/[A-Z]/.test(char)) {
      brailleText += capitalIndicator + brailleAlphabet[char.toLowerCase()]
    } else if (/[0-9]/.test(char)) {
      if (!isNumberMode) {
        brailleText += numberIndicator
        isNumberMode = true
      }
      brailleText += brailleNumbers[char]
    } else {
      if (isNumberMode && char === " ") {
        isNumberMode = false
      }
      brailleText += brailleAlphabet[char]
    }
  }

  return brailleText
}

// translate Braille to English
function brailleToEnglishTranslator(braille) {
  let englishText = ""
  let isCapital = false
  let isNumber = false

  for (let i = 0; i < braille.length; i += 6) {
    const symbol = braille.substring(i, i + 6)
    if (symbol === capitalIndicator) {
      isCapital = true
      continue
    } else if (symbol === numberIndicator) {
      isNumber = true
      continue
    }

    let letter = isNumber ? brailleToNumbers[symbol] : brailleToEnglish[symbol]
    if (isCapital) {
      letter = letter.toUpperCase()
      isCapital = false
    }
    isNumber = false
    englishText += letter
  }

  return englishText
}

// handle input and output
function translate(input) {
  if (isBraille(input)) {
    console.log(brailleToEnglishTranslator(input))
  } else {
    console.log(englishToBraille(input))
  }
}

// Get input from command line arguments
const args = process.argv.slice(2).join(" ")
translate(args)
