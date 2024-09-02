import { getConvertedChar } from "../lib/libFunctions";
import { CAPITALFOLLOWS, NUMBERFOLLOWS, SPACEBRAILLE } from "../variables/constants";
import { alphToBraille, digitToBraille, punctToBraille } from "../variables/mappings";

export const englishToBraille = (englishArray: string[]): string => {
  let isNum: boolean = false; // Track when we have numbers
  let brailleStr: string = ""; // This will be the returned string

  const periodToBraille = (char: string) => {
    const period = getConvertedChar(char, punctToBraille);
    brailleStr += period;
    isNum = false;
  };

  // Check context of '.' is not in number format, if not convert to braille and add to string
  const isCharacterPeriodAndConvert = (char: string, idx: number): boolean => {
    const nextChar: string = englishArray[idx + 1];
    const isNextDigit: boolean = digitToBraille.get(nextChar) !== undefined && nextChar !== "."; // check for !=="." to account for strings with "..."
    const isPeriod = char === "." && !isNextDigit;
    if (isPeriod) {
      // Convert period to braille equivalent
      periodToBraille(char);
      return true;
    }
    return false;
  };

  for (let ii = 0; ii < englishArray.length; ii++) {
    const char: string = englishArray[ii];

    if (digitToBraille.has(char) && !isNum) {
      // Check context of '.' is not in number format, if not convert to braille and add to string
      if (isCharacterPeriodAndConvert(char, ii)) {
        continue;
      }
      isNum = true;
      brailleStr += NUMBERFOLLOWS;
    }

    if (char === " ") {
      brailleStr += SPACEBRAILLE;
      isNum = false;
      continue;
    }

    // punctuation -- don't care about 'number follows' since it can appear in any context
    if (char !== ".") {
      const braillePunct = getConvertedChar(char, punctToBraille);
      brailleStr += braillePunct;
    }
    // Check context of '.' is not in number format, if not convert to braille and add to string
    else if (isCharacterPeriodAndConvert(char, ii)) {
      continue;
    }

    // alphabet
    if (!isNum) {
      const isCapital = char >= "A" && char <= "Z";
      const brailleLetter = getConvertedChar(char.toLowerCase(), alphToBraille);
      brailleStr += isCapital ? CAPITALFOLLOWS + brailleLetter.toUpperCase() : brailleLetter;
    }
    // Number
    else {
      const brailleNumber = getConvertedChar(char, digitToBraille);
      brailleStr += brailleNumber;
    }
  }

  return brailleStr;
};
