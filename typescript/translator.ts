/**
 * Program to translate between English text and Braille.
 *
 * Developed by: Fwaad Ahmad (https://github.com/fwaadahmad1)
 *
 * A mapping of Braille patterns to their corresponding English characters.
 *
 * The keys in the object represent Braille patterns using a string of six characters,
 * where 'O' indicates a raised dot and '.' indicates no dot. The values are the
 * corresponding English characters or symbols.
 */

/**
 * A mapping of Braille patterns to their corresponding English characters.
 */
const brailleToEnglish: { [key: string]: string } = {
  "O.....": "a",
  "O.O...": "b",
  "OO....": "c",
  "OO.O..": "d",
  "O..O..": "e",
  "OOO...": "f",
  "OOOO..": "g",
  "O.OO..": "h",
  ".OO...": "i",
  ".OOO..": "j",
  "O...O.": "k",
  "O.O.O.": "l",
  "OO..O.": "m",
  "OO.OO.": "n",
  "O..OO.": "o",
  "OOO.O.": "p",
  "OOOOO.": "q",
  "O.OOO.": "r",
  ".OO.O.": "s",
  ".OOOO.": "t",
  "O...OO": "u",
  "O.O.OO": "v",
  ".OOO.O": "w",
  "OO..OO": "x",
  "OO.OOO": "y",
  "O..OOO": "z",
  "......": " ",
  "..OO.O": ",",
  "..O...": ".",
  "..O.OO": "?",
  "..OOO.": "!",
  "..OO..": ":",
  "..O.O.": ";",
  "....OO": "-",
  ".O..O.": "/",
  ".....O": "CAP",
  ".O...O": "DECIMAL",
  ".O.OOO": "NUM",
};

/**
 * A mapping of Braille patterns to their corresponding numbers.
 */
const brailleToNumber: { [key: string]: string } = {
  "O.....": "1",
  "O.O...": "2",
  "OO....": "3",
  "OO.O..": "4",
  "O..O..": "5",
  "OOO...": "6",
  "OOOO..": "7",
  "O.OO..": "8",
  ".OO...": "9",
  ".OOO..": "0",
};

/**
 * A mapping of English characters to their corresponding Braille patterns.
 */
const englishToBraille: { [key: string]: string } = Object.fromEntries(
  Object.entries(brailleToEnglish).map(([braille, english]) => [
    english,
    braille,
  ])
);

/**
 * A mapping of numbers to their corresponding Braille patterns.
 */
const numberToBraille: { [key: string]: string } = Object.fromEntries(
  Object.entries(brailleToNumber).map(([braille, number]) => [number, braille])
);

/**
 * Determines whether the input is a Braille pattern.
 *
 * @param input The input to check.
 * @returns true if the input is a Braille pattern, false otherwise.
 */
function isBraille(input: string): boolean {
  return /^[O.]+$/.test(input);
}

/**
 * Translates a Braille pattern to English text.
 * @param braille The Braille pattern to translate.
 * @returns The English text corresponding to the Braille pattern.
 */
function translateBrailleToEnglish(braille: string): string {
  let result = "";
  let isCapital = false;
  let isNumber = false;

  // Iterate over the Braille string in chunks of 6 characters
  for (let i = 0; i < braille.length; i += 6) {
    const symbol = braille.slice(i, i + 6);

    // Check for capital indicator
    if (symbol === englishToBraille["CAP"]) {
      isCapital = true;
      continue;
    }

    // Check for number indicator
    if (symbol === englishToBraille["NUM"]) {
      isNumber = true;
      continue;
    }

    // Translate Braille to English character
    let char = brailleToEnglish[symbol];

    // Convert to uppercase if capital indicator was found
    if (isCapital) {
      char = char?.toUpperCase();
      isCapital = false;
    }

    // Reset number mode if the character is a space
    if (char === " ") isNumber = false;

    // Translate Braille to number if in number mode
    if (isNumber) char = brailleToNumber[symbol];

    // Append the translated character to the result
    result += char;
  }

  return result;
}

/**
 * Translates English text to Braille.
 * @param english The English text to translate.
 * @returns The Braille pattern corresponding to the English text.
 */
function translateEnglishToBraille(english: string): string {
  let result = "";
  let isNumber = false;

  // Iterate over each character in the English text
  for (const char of english) {
    // Reset number mode if the character is a space
    if (char === " ") isNumber = false;

    // Handle numbers
    if (char >= "0" && char <= "9") {
      if (!isNumber) {
        result += englishToBraille["NUM"]; // Add number indicator if not already in number mode
        isNumber = true;
      }
      result += numberToBraille[char]; // Add the Braille pattern for the number
      continue;
    }

    // Handle uppercase letters
    if (char >= "A" && char <= "Z") {
      result += englishToBraille["CAP"] + englishToBraille[char.toLowerCase()]; // Add capital indicator and the Braille pattern for the lowercase letter
      continue;
    }

    // Handle lowercase letters and other characters
    result += englishToBraille[char];
  }

  return result;
}

/* Main program */

// Get the input from the command line arguments.
const input = process.argv.slice(2).join(" ");

// Translate the input based on whether it is Braille or English.
if (isBraille(input)) {
  console.log(translateBrailleToEnglish(input));
} else {
  console.log(translateEnglishToBraille(input));
}
