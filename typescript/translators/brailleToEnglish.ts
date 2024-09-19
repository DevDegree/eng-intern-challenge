import { brailleToEnglishLetterMap, brailleToEnglishNumberMap } from "../constants/brailleToEnglishMaps";
import { englishToBrailleCharacterizationMap } from "../constants/englishToBrailleMaps";
import { validateBrailleInput } from "../utils";

enum BrailleSpecialCharacters {
  Capital = "capital",
  Number = "number",
}

/**
 * Translates a string of Braille characters (as O's and .'s) into English text.
 *
 * This function validates the input and handles special Braille characters for capitalization and numbers.
 *
 * @param {string} input - A string of Braille characters (O's and .'s ) to be translated.
 *                         Each Braille character is represented by a 6-character string.
 * @returns {string} - The translated English text.
 *
 * @throws {Error} - Throws an error if the input is invalid Braille.
 *
 */
export default function translateToEnglish(input: string): string {
  if (!validateBrailleInput(input)) {
    throw new Error("Invalid Braille input");
  }

  const brailleSymbols: string[] = input.match(/.{1,6}/g) || []; // Match every 6 characters, put into array

  let result: string[] = [];
  let isCapital = false;
  let isNumber = false;

  for (let symbol of brailleSymbols) {
    if (symbol === englishToBrailleCharacterizationMap[BrailleSpecialCharacters.Capital].join("")) {
      isCapital = true; // Capital follows next character
      continue;
    } else if (symbol === englishToBrailleCharacterizationMap[BrailleSpecialCharacters.Number].join("")) {
      isNumber = true; // Number follows next character
      continue;
    }

    let character: string;

    if (isNumber) {
      character = brailleToEnglishNumberMap[symbol];
      if (character === " ") {
        isNumber = false;
      }
    } else {
      character = brailleToEnglishLetterMap[symbol];
    }

    if (isCapital && character) {
      character = character.toUpperCase();
      isCapital = false; // Reset capital mode
    }

    result.push(character);
  }

  return result.join("");
}
