import { englishBrailleAlphabet } from "./englishBrailleAlphabet.js";

export const translateToEnglish = (inputString) => {
  let englishResult = "";
  let isNumbers = false;
  let isCapital = false;

  for (let i = 0; i < inputString.length; i += 6) {
    const brailleChar = inputString.slice(i, i + 6);
    const brailleTranslation = englishBrailleAlphabet[brailleChar] || [];

    switch (brailleTranslation[0]) {
      case "capital follows":
        isCapital = true;
        break;
      case "numbers follows":
        isNumbers = true;
        break;
      case " ":
        isNumbers = false;
        englishResult += " ";
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
