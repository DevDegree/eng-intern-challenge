/*
  Shopify Intern Challenge - Winter 2025
  alexstarostadev@gmail.com
*/

class BiMap<K, V> {
  // set up bi-dectional map for easy O(1) lookups
  private englishToBraille: Map<K, V>
  private brailleToEnglish: Map<V, K>

  constructor(translations: [K, V][]) {
    this.englishToBraille = new Map<K, V>(translations)
    this.brailleToEnglish = new Map<V, K>(translations.map(([k, v]) => [v, k]))
  }

  getEnglish(char: V): K {
    let result = this.brailleToEnglish.get(char)
    if (!result) {
      throw new Error(`Invalid character: "${char}"`) // if not found, throw error
    }
    return result
  }

  getBraille(char: K): V {
    let result = this.englishToBraille.get(char)
    if (!result) {
      throw new Error(`Invalid character: "${char}"`) // if not found, throw error
    }
    return result
  }
}

const brailleNumbers: [string, string][] = [
  ["0", ".OOO.."],
  ["1", "O....."],
  ["2", "O.O..."],
  ["3", "OO...."],
  ["4", "OO.O.."],
  ["5", "O..O.."],
  ["6", "OOO..."],
  ["7", "OOOO.."],
  ["8", "O.OO.."],
  ["9", ".OO..."],
]

const brailleLetters: [string, string][] = [
  ["a", "O....."],
  ["b", "O.O..."],
  ["c", "OO...."],
  ["d", "OO.O.."],
  ["e", "O..O.."],
  ["f", "OOO..."],
  ["g", "OOOO.."],
  ["h", "O.OO.."],
  ["i", ".OO..."],
  ["j", ".OOO.."],
  ["k", "O...O."],
  ["l", "O.O.O."],
  ["m", "OO..O."],
  ["n", "OO.OO."],
  ["o", "O..OO."],
  ["p", "OOO.O."],
  ["q", "OOOOO."],
  ["r", "O.OOO."],
  ["s", ".OO.O."],
  ["t", ".OOOO."],
  ["u", "O...OO"],
  ["v", "O.O.OO"],
  ["w", ".OOO.O"],
  ["x", "OO..OO"],
  ["y", "OO.OOO"],
  ["z", "O..OOO"],
]

// create two seperate bi-maps since there are collisions between numbers and letters if combined
const alphaTranslationsBiMap = new BiMap<string, string>(brailleLetters)
const numberTranslationsBiMap = new BiMap<string, string>(brailleNumbers)

const specialCharacters: { [key: string]: string } = {
  NUMBER_FOLLOWS: ".O.OOO",
  CAPITAL_FOLLOWS: ".....O",
  SPACE: "......",
}

function isBraille(str: string): boolean {
  const stringLength = str.length
  if (stringLength % 6 !== 0) {
    // if the string is not a multiple of 6 it cannot be braille
    return false
  }

  const stringSet = new Set(str)
  if (stringSet.size > 2) {
    return false // braille characters can only be '.' and 'O'
  } else if (stringSet.size === 2) {
    if (!stringSet.has("O") || !stringSet.has(".")) {
      // if the set with two characters does not contain '.' and 'O' it is not braille
      return false
    }
  } else if (stringSet.size === 1) {
    if (!stringSet.has(".")) {
      // the only possible senario would be if the string is just braille spaces
      return false
    }
  }

  return true
}

// helper functions
function isUpper(char: string): boolean {
  return char >= "A" && char <= "Z"
}

function isAlpha(char: string): boolean {
  return (char >= "a" && char <= "z") || (char >= "A" && char <= "Z")
}

function isNumeric(char: string): boolean {
  return char >= "0" && char <= "9"
}

function englishToBraille(str: string): string {
  let translation = ""

  let isNumberNext = false
  let index = 0

  while (index < str.length) {
    const char = str[index]

    if (char === " ") {
      isNumberNext = false // reset number flag
      translation += specialCharacters.SPACE
      index += 1
    } else if (isNumeric(char)) {
      if (!isNumberNext) {
        isNumberNext = true
        translation += specialCharacters.NUMBER_FOLLOWS
      }
      translation += numberTranslationsBiMap.getBraille(char)
      index += 1
    } else if (isAlpha(char)) {
      if (isNumberNext) {
        // if a letter follows a number, throw error
        throw new Error(`Invalid character: "${char}". Numbers must end with a space.`)
      }
      if (isUpper(char)) {
        translation += specialCharacters.CAPITAL_FOLLOWS
      }
      translation += alphaTranslationsBiMap.getBraille(char.toLowerCase())
      index += 1
    } else {
      throw new Error(`Invalid character: "${char}"`)
    }
  }

  return translation
}

function brailleToEnglish(str: string): string {
  let translation = ""

  let brailleCharacters: string[] = []
  for (let i = 0; i < str.length; i += 6) {
    brailleCharacters.push(str.slice(i, i + 6))
  }

  let isNumberNext = false
  let index = 0

  while (index < brailleCharacters.length) {
    const char = brailleCharacters[index]

    if (char === specialCharacters.SPACE) {
      isNumberNext = false
      translation += " "
      index += 1
    } else if (char === specialCharacters.NUMBER_FOLLOWS) {
      isNumberNext = true
      index += 1
    } else if (char === specialCharacters.CAPITAL_FOLLOWS) {
      translation += alphaTranslationsBiMap.getEnglish(brailleCharacters[index + 1]).toUpperCase()
      index += 2 // skip the capital indicator character
    } else {
      if (isNumberNext) {
        translation += numberTranslationsBiMap.getEnglish(char)
        index += 1
      } else {
        translation += alphaTranslationsBiMap.getEnglish(char)
        index += 1
      }
    }
  }

  return translation
}

const args = process.argv.slice(2)
const input = args.join(" ") // join all arguments into a single string

if (!input) {
  throw Error("No input provided")
}

if (isBraille(input)) {
  console.log(brailleToEnglish(input))
} else {
  console.log(englishToBraille(input))
}
