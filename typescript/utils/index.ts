/**
 * Checks if the input string is in Braille format. Aka O's and .'s
 */
export function isBrailleChars(input: string): boolean {
  return /^[O.]+$/.test(input);
}

/**
 * Validates if the input string is a valid English text
 * Defined as a-z, A-Z, 0-9, spaces
 */
export function validateEnglishInput(input: string): boolean {
  return /^[a-zA-Z0-9 ]*$/.test(input);
}

/**
 * Validates if the input string is a valid Braille format and length
 */
export function validateBrailleInput(input: string): boolean {
  return isBrailleChars(input) && input.length % 6 === 0;
}
