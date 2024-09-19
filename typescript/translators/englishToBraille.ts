import {
  englishToBrailleCharacterizationMap,
  englishToBrailleNumberMap,
  englishToBraillLetterMap,
} from "../constants/englishToBrailleMaps";
import { validateEnglishInput } from "../utils";

enum EnglishSpecialCharacters {
  Capital = "capital",
  Number = "number",
}

/**
 * Translates a string of English characters into Braille characters (O's and .'s).
 *
 * @param {string} input - A string of English characters to be translated.
 * @returns {string} - The translated Braille text.
 *
 * @throws {Error} - Throws an error if the input is invalid English.
 *
 */
export default function translateToBraille(input: string): string {
  if (!validateEnglishInput(input)) {
    throw new Error("Invalid English input");
  }

  let result: string[] = [];
  let isNumberMode = false; // Flag for whether we're in number mode

  for (let char of input) {
    const isANumber = !isNaN(parseInt(char));

    if (char === char.toUpperCase() && char !== " " && !isANumber) {
      result.push(englishToBrailleCharacterizationMap[EnglishSpecialCharacters.Capital].join(""));
      char = char.toLowerCase();
    }

    if (isANumber) {
      if (!isNumberMode) {
        result.push(englishToBrailleCharacterizationMap[EnglishSpecialCharacters.Number].join(""));
        isNumberMode = true; // Switch to number mode
      }
      result.push(englishToBrailleNumberMap[char].join(""));
    } else {
      isNumberMode = false; // Non-number encountered, switch the flag
      result.push(englishToBraillLetterMap[char].join(""));
    }
  }

  return result.join("");
}
