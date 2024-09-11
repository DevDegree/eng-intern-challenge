import { getConvertedChar } from "../lib/libFunctions";
import { CAPITALFOLLOWS, NUMBERFOLLOWS, SPACEBRAILLE } from "../variables/constants";
import { brailleToAlph, brailleToDigit, brailleToPunct } from "../variables/mappings";

export const brailleToEnglish = (brailleArray: string[]): string => {
  let engStr: string = ""; // This will be the returned string
  let isNum: boolean = false; // Track when we have numbers
  let isCapital: boolean = false;
  let isAlphabet: boolean = false;

  for (let jj = 0; jj < brailleArray.length; jj++) {
    const brailleCell = brailleArray[jj];

    // console.log(brailleCell);

    // Check to see if the incoming braille cell is an identifier
    if (brailleCell === CAPITALFOLLOWS) {
      isCapital = true;
      isAlphabet = true;
      continue;
    } else if (brailleCell === NUMBERFOLLOWS) {
      isNum = true;
      isAlphabet = false;
      continue;
    }

    if (isNum && isAlphabet) {
      return "Error: Invalid sentence, cannot have letter immediately after digit";
    }

    // Check to see if the incoming braille cell is a space
    if (brailleCell === SPACEBRAILLE) {
      engStr += getConvertedChar(SPACEBRAILLE, brailleToPunct);
      isNum = false;
      continue;
    }

    // Check punctation (appears regardless of isNum or isCapital)
    if (brailleToPunct.has(brailleCell)) {
      engStr += getConvertedChar(brailleCell, brailleToPunct);
      continue;
    }

    // alphabet
    if (!isNum) {
      const letter = getConvertedChar(brailleCell, brailleToAlph);
      engStr += isCapital ? letter.toUpperCase() : letter;
      isAlphabet = true;
      isCapital = false;
    }
    // number
    else {
      isAlphabet = false;
      const num = getConvertedChar(brailleCell, brailleToDigit);
      engStr += num;
    }
  }

  return engStr;
};
