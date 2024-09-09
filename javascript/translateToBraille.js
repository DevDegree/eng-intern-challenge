import { englishBrailleAlphabet } from "./englishBrailleAlphabet.js";

const getBrailleEnglishAlphabet = () => {
  return new Map(
    Object.entries(englishBrailleAlphabet).flatMap(([key, [dot1, dot2]]) => [
      [dot1, key],
      [dot2, key],
    ])
  );
};

export const translateToBraille = (inputString) => {
  if (!inputString) return "";

  const brailleEnglishAlphabet = getBrailleEnglishAlphabet();
  let result = "";
  let isNumber = false;

  //Find Braille representation
  const findKeyByValue = (value) => brailleEnglishAlphabet.get(value) || "";

  for (let char of inputString) {
    //  Add uppercase letter
    if (/[A-Z]/.test(char)) {
      result += findKeyByValue("capital follows");
      char = char.toLowerCase();
    }

    // Add numbers
    if (/[0-9]/.test(char)) {
      if (!isNumber) {
        result += findKeyByValue("numbers follows");
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
