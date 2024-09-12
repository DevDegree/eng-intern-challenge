import { CAPITAL_FOLLOWS, NUMBERS_FOLLOWS } from "../constants/appConstants.js";
import { getBrailleEnglishAlphabet } from "./getBrailleToEnglishAlphabet.js";

export const translateToBraille = (inputString) => {
  const brailleEnglishAlphabet = getBrailleEnglishAlphabet();
  let result = "";
  let isNumber = false;

  //Find Braille representation
  const findKeyByValue = (value) => brailleEnglishAlphabet.get(value) || "";

  for (let char of inputString) {
    //  Add uppercase letters
    if (/[A-Z]/.test(char)) {
      result += findKeyByValue(CAPITAL_FOLLOWS);
      char = char.toLowerCase();
    }

    // Add numbers
    if (/[0-9]/.test(char)) {
      if (!isNumber) {
        result += findKeyByValue(NUMBERS_FOLLOWS);
        isNumber = true;
      }
      result += findKeyByValue(char);
    } else {
      isNumber = false;

      // Add lowercase letters
      result += findKeyByValue(char);
    }
  }

  return result;
};
