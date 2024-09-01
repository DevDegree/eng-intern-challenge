/**
 * The fixed number of braille symbols
 * that compose a unique braille character.
 */
const BRAILLE_CHUNK_SIZE = 6

/**
 * The symbol set that braille characters are comprised of
 */
type BrailleSymbol = 'O' | '.'

/**
 * A Braille string is only composed of only braille symbols
 */
type Braille = string & { __isBrailleString: true }

/**
 * A Braille character is a braille string of length brailleChunkSize (6)
 */
type BrailleCharacter = Braille & { __isBrailleCharacter: true }

const LOWER_CASE_ENGLISH_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
const UPPER_CASE_ENGLISH_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
const NUMBERS = '0123456789'
const SPECIAL_CHARACTERS = '.,?!:;-/<>() '
const CHARACTER_MODIFIERS = 'capital-follows,decimal-follows,number-follows'

type LowerCaseEnglishAlphabet = (typeof LOWER_CASE_ENGLISH_ALPHABET)[number]
type UpperCaseEnglishAlphabet = (typeof UPPER_CASE_ENGLISH_ALPHABET)[number]
type NumberCharacter = (typeof NUMBERS)[number]
type SpecialCharacter = (typeof SPECIAL_CHARACTERS)[number]
type CharacterModifier = (typeof CHARACTER_MODIFIERS)[number]

type English =
  | LowerCaseEnglishAlphabet
  | UpperCaseEnglishAlphabet
  | NumberCharacter
  | SpecialCharacter
  | CharacterModifier

export {
  BRAILLE_CHUNK_SIZE,
  BrailleSymbol,
  Braille,
  BrailleCharacter,
  English,
  LowerCaseEnglishAlphabet,
  UpperCaseEnglishAlphabet,
  NumberCharacter,
  SpecialCharacter,
  CharacterModifier,
  LOWER_CASE_ENGLISH_ALPHABET,
  UPPER_CASE_ENGLISH_ALPHABET,
  NUMBERS,
  SPECIAL_CHARACTERS,
  CHARACTER_MODIFIERS,
}
