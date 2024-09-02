/* Created By: Mohit Verma */

import { brailleToEnglish } from "./translators/brailleToEngTranslator";
import { engllishToBraille } from "./translators/engToBrailleTranslator";

// Function translates braille language into english equivalent
function translateBrailleToEnglish(sentence: string): string {
  const brailCellLen = 6; // Length of a single braille character
  let brailleArray: string[] = [];
  for (let ii: number = 0; ii < sentence.length; ii += brailCellLen) {
    const brailCell: string = sentence.slice(ii, ii + brailCellLen);
    brailleArray.push(brailCell);
  }
  return brailleToEnglish(brailleArray);
}

// Function translates english language into braille equivalent
function translateEnglishToBraille(english: string): string {
  const englishArray: string[] = english.split("");
  return engllishToBraille(englishArray);
}

// The function checks if the argument passed is braille or english and returns the converted string
function translator(args: string) {
  const regexBraille: RegExp = /^[O.]*$/;
  const isBraille: boolean = args.length >= 6 && regexBraille.test(args);
  isBraille
    ? console.log(translateBrailleToEnglish(args))
    : console.log(translateEnglishToBraille(args));
}

// Take in arguments from command line and unit tests
const args: string = process.argv.slice(2).join(" ");
translator(args);
