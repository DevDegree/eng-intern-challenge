/**
 * Mapping characters to Braille representation shown in braille.jpg
 */
const CHAR_TO_BRAILLE: { [key: string]: string } = {
  // alphabet mappings
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
  // space char mapping
  " ": "......",
  // numeric mappings
  "1": "O.....",
  "2": "O.O...",
  "3": "OO....",
  "4": "OO.O..",
  "5": "O..O..",
  "6": "OOO...",
  "7": "OOOO..",
  "8": "O.OO..",
  "9": ".OO...",
  "0": ".OOO..",
};

/**
 * Reverse mapping from Braille representation to character
 */
const BRAILLE_TO_CHAR = Object.fromEntries(
  Object.entries(CHAR_TO_BRAILLE).map(([char, braille]) => [braille, char])
);

/**
 * Patterns for numeric and capital letters
 */
const NUMERIC_PREFIX = ".O.OOO"; // following characters are numbers
const CAPITAL_PREFIX = ".....O"; // following character is uppercase

/**
 * Checks if the string is valid Braille
 * @param input - String to check
 * @returns True if the input is a valid Braille, or else false.
 */
function isBraille(input: string): boolean {
  // checks if input is a multiple of 6 and contains only 0 and . characters
  return input.length % 6 === 0 && /^[O.]+$/.test(input);
}

/**
 * Converts a Braille into text string
 * @param braille - Braille string to convert
 * @returns Decoded text string
 */
function brailleToText(braille: string): string {
  // split the braille string into 6 character cells
  const brailleCells = Array.from({ length: braille.length / 6 }, (_, i) =>
    braille.slice(i * 6, i * 6 + 6)
  );

  let text = "";
  let isNumericMode = false; // flag for numbers
  let isUpperCase = false; // flag for uppercase

  // iterate over each cell
  for (const cell of brailleCells) {
    switch (cell) {
      case NUMERIC_PREFIX:
        isNumericMode = true;
        break;
      case CAPITAL_PREFIX:
        isUpperCase = true;
        break;
      case CHAR_TO_BRAILLE[" "]:
        isNumericMode = false;
        text += " ";
        break;
      default:
        // get the corresponding character from the mapping
        const character = BRAILLE_TO_CHAR[cell];
        if (character) {
          // check for uppercase
          text += isUpperCase ? character.toUpperCase() : character;
          isUpperCase = false;
        } else {
          // for unknown characters or invalid braille
          text += "?";
        }
    }
  }
  return text;
}

/**
 * Converts a text string into Braille
 * @param text - Text string to convert
 * @returns Braille string
 */
function textToBraille(text: string): string {
  let braille = "";
  let isNumericMode = false; // flag for numbers

  // iterate over each character
  for (const char of text) {
    const lowerChar = char.toLowerCase();

    if (lowerChar === " ") {
      isNumericMode = false;
      braille += CHAR_TO_BRAILLE[" "]; // apend space Braille representation
    } else if (/\d/.test(lowerChar)) {
      if (!isNumericMode) {
        isNumericMode = true;
        braille += NUMERIC_PREFIX; // append numeric prefix
      }
      braille += CHAR_TO_BRAILLE[lowerChar]; // append numeric Braille representation
    } else if (/[a-z]/.test(lowerChar)) {
      if (isNumericMode) {
        isNumericMode = false;
        braille += CHAR_TO_BRAILLE[" "]; // Append space
      }
      if (char !== lowerChar) {
        braille += CAPITAL_PREFIX; // append capital prefix
      }
      braille += CHAR_TO_BRAILLE[lowerChar]; // append numeric Braille representation
    } else {
      // for unknown characters
      braille += "??????";
    }
  }

  return braille;
}

/**
 * Main function to process input and converts between text and Braille.
 */
function main() {
  // combine input args into a single string
  const input = process.argv.slice(2).join(" ");

  // Determine input type
  if (isBraille(input)) {
    console.log(brailleToText(input)); // Braille to text
  } else {
    console.log(textToBraille(input)); // text to Braille
  }
}

main();
