/**
 * The fixed number of braille symbols
 * that compose a unique braille character.
 */
export const BRAILLE_CHUNK_SIZE = 6

/**
 * The symbol set that braille characters are comprised of
 */
export type BrailleSymbol = 'O' | '.'

/**
 * A Braille string is only composed of only braille symbols
 */
export type Braille = string & { __isBrailleString: true }

/**
 * A Braille character is a braille string of length brailleChunkSize (6)
 */
export type BrailleCharacter = Braille & { __isBrailleCharacter: true }

export const LOWER_CASE_ENGLISH_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
export const UPPER_CASE_ENGLISH_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
export const NUMBERS = '0123456789'
export const SPECIAL_CHARACTERS = '.,?!:;-/<>() '
export const CHARACTER_MODIFIERS =
  'capital-follows,decimal-follows,number-follows'

export type LowerCaseEnglishAlphabet =
  (typeof LOWER_CASE_ENGLISH_ALPHABET)[number]
export type UpperCaseEnglishAlphabet =
  (typeof UPPER_CASE_ENGLISH_ALPHABET)[number]
export type NumberCharacter = (typeof NUMBERS)[number]
export type SpecialCharacter = (typeof SPECIAL_CHARACTERS)[number]
export type CharacterModifier = (typeof CHARACTER_MODIFIERS)[number]

export type English =
  | LowerCaseEnglishAlphabet
  | UpperCaseEnglishAlphabet
  | NumberCharacter
  | SpecialCharacter
  | CharacterModifier
