import { englishBrailleAlphabet } from "./englishBrailleAlphabet.js";

export const isValidBraille = (input) => {
  const braillePatternLength = 6;
  if (input.length % braillePatternLength !== 0) {
    return false;
  }

  for (let i = 0; i < input.length; i += braillePatternLength) {
    const pattern = input.substring(i, i + braillePatternLength);

    // Check if the pattern is valid
    if (!englishBrailleAlphabet.hasOwnProperty(pattern)) {
      return false;
    }
  }
  return true;
};
