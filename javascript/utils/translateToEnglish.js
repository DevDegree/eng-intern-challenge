import {
  CAPITAL_FOLLOWS,
  NUMBERS_FOLLOWS,
  SPACE,
} from "../constants/appConstants.js";
import { englishBrailleAlphabet } from "../constants/englishBrailleAlphabet.js";

export const translateToEnglish = (inputString) => {
  let englishResult = "";
  let isNumbers = false;
  let isCapital = false;

  for (let i = 0; i < inputString.length; i += 6) {
    const brailleChar = inputString.slice(i, i + 6);
    const brailleTranslation = englishBrailleAlphabet[brailleChar] || [];

    switch (brailleTranslation[0]) {
      case CAPITAL_FOLLOWS:
        isCapital = true;
        break;
      case NUMBERS_FOLLOWS:
        isNumbers = true;
        break;
      case SPACE:
        isNumbers = false;
        englishResult += SPACE;
        break;
      default:
        if (isCapital) {
          englishResult += brailleTranslation[0].toUpperCase();
          isCapital = false;
        } else if (isNumbers) {
          englishResult += brailleTranslation[1] || "";
        } else {
          englishResult += brailleTranslation[0] || "";
        }
        break;
    }
  }

  return englishResult;
};
