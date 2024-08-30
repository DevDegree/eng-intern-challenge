export function isValidBraille(input) {
  const validChars = /^[O.]+$/.test(input);
  const validLength = input.length % 6 === 0;

  return validChars && validLength;
}

export function validateBrailleInput(braille) {
  if (!isValidBraille(braille)) {
    throw new Error(
      "Invalid Braille input: Ensure it contains only 'O' or '.' and the length is a multiple of 6."
    );
  }
}
