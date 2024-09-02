import { getConvertedChar } from "../lib/libFunctions";
import { CAPITALFOLLOWS, NUMBERFOLLOWS, SPACEBRAILLE } from "../variables/constants";
import { brailleToAlph, brailleToDigit, brailleToPunct } from "../variables/mappings";

export const brailleToEnglish = (brailleArray: string[]): string => {
  let engStr: string = ""; // This will be the returned string
  let isNum: boolean = false; // Track when we have numbers
  let isCapital: boolean = false;

  for (let jj = 0; jj < brailleArray.length; jj++) {
    const brailleCell = brailleArray[jj];

    // Check to see if the incoming braille cell is an identifier
    if (brailleCell === CAPITALFOLLOWS) {
      isCapital = true;
      continue;
    } else if (brailleCell === NUMBERFOLLOWS) {
      isNum = true;
      continue;
    }

    // Check to see if the incoming braille cell is a space
    if (brailleCell === SPACEBRAILLE) {
      isNum = false;
      engStr += getConvertedChar(SPACEBRAILLE, brailleToPunct);
      continue;
    }

    // Check punctation. Since its independent of capital or number flags set (1?, a!, HEY!, a1!)
    if (brailleToPunct.has(brailleCell)) {
      engStr += getConvertedChar(brailleCell, brailleToPunct);
      continue;
    }

    // alphabet
    if (!isNum) {
      const letter = getConvertedChar(brailleCell, brailleToAlph);
      engStr += isCapital ? letter.toUpperCase() : letter;
      isCapital = false;
    }
    // number
    else {
      const num = getConvertedChar(brailleCell, brailleToDigit);
      engStr += num;
    }
  }

  return engStr;
};
