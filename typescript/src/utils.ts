import {
  BRAILLE_CHUNK_SIZE,
  BrailleSymbol,
  BrailleCharacter,
  Braille,
  LOWER_CASE_ENGLISH_ALPHABET,
  UPPER_CASE_ENGLISH_ALPHABET,
  NUMBERS,
  SPECIAL_CHARACTERS,
  CHARACTER_MODIFIERS,
  English,
} from './types'

const isBrailleSymbol = (char: any): char is BrailleSymbol =>
  char === 'O' || char === '.'

const isBraille = (text: string): text is Braille =>
  text.length % 6 === 0 && text.split('').every(isBrailleSymbol)

const isBrailleCharacter = (text: string): text is BrailleCharacter =>
  text.length === BRAILLE_CHUNK_SIZE && isBraille(text)

/**
 * Asserts that a string is a BrailleCharacter
 *
 * @param {string} str - The string to assert
 * @returns {BrailleCharacter} The BrailleCharacter
 */
export const toBrailleCharacter = (str: string): BrailleCharacter =>
  str.length == BRAILLE_CHUNK_SIZE
    ? (str as BrailleCharacter)
    : (() => {
        throw new Error(`Invalid BrailleCharacter length: ${str.length}`)
      })()

/**
 * Splits a Braille string into braille characters
 *
 * @param {BrailleString} text  - The braille string to be chunked
 * @returns {BrailleCharacter[]} An array of braille characters
 */
const chunkBrailleCharacters = (text: Braille): BrailleCharacter[] => {
  const chunkedBraille: BrailleCharacter[] = []
  for (let index = 0; index < text.length; index += BRAILLE_CHUNK_SIZE)
    chunkedBraille.push(
      text.substring(index, index + BRAILLE_CHUNK_SIZE) as BrailleCharacter,
    )
  return chunkedBraille
}

const isLowerCaseEnglishAlphabet = (
  char: string,
): char is (typeof LOWER_CASE_ENGLISH_ALPHABET)[number] =>
  LOWER_CASE_ENGLISH_ALPHABET.includes(char)

const isUpperCaseEnglishAlphabet = (
  char: string,
): char is (typeof UPPER_CASE_ENGLISH_ALPHABET)[number] =>
  UPPER_CASE_ENGLISH_ALPHABET.includes(char)

const isNumber = (char: string): char is (typeof NUMBERS)[number] =>
  NUMBERS.includes(char)

const isSpecialCharacter = (
  char: string,
): char is (typeof SPECIAL_CHARACTERS)[number] =>
  SPECIAL_CHARACTERS.includes(char)

const isCharacterModifier = (
  char: string,
): char is (typeof CHARACTER_MODIFIERS)[number] =>
  CHARACTER_MODIFIERS.includes(char)

const isEnglish = (text: string): text is English =>
  text
    .split('')
    .every(
      (char) =>
        isLowerCaseEnglishAlphabet(char) ||
        isUpperCaseEnglishAlphabet(char) ||
        isNumber(char) ||
        isSpecialCharacter(char) ||
        isCharacterModifier(char),
    )

export {
  isBraille,
  isBrailleCharacter,
  chunkBrailleCharacters,
  isEnglish,
  isLowerCaseEnglishAlphabet,
  isUpperCaseEnglishAlphabet,
  isNumber,
  isSpecialCharacter,
  isCharacterModifier,
}
