import {
  brailleToLetter,
  brailleToNumber,
  letterToBraille,
  modifiersDict,
  numberToBraille,
} from "./brailleEnglishMaps.js";
import { chunkString, isNumber, isUpper } from "./charHelpers.js";

export function translateEnglishToBraille(english) {
  const chars = english.split("");
  const output = [];

  let leadingNumber = true;
  for (let char of chars) {
    let braille = "";

    // If the character is a number, convert from number to braille, else convert from letter to braille
    if (isNumber(char)) {
      if (leadingNumber) output.push(modifiersDict.number);
      leadingNumber = false;
      braille = numberToBraille(char);
    } else {
      if (isUpper(char)) {
        output.push(modifiersDict.capital);
        char = char.toLowerCase();
      }
      braille = letterToBraille(char);
      leadingNumber = true;
    }
    output.push(braille);
  }

  return output.join("");
}

export function translateBrailleToEnglish(braille) {
  braille = chunkString(braille);

  const output = [];

  let capital = false;
  let number = false;

  for (const alphabet of braille) {
    let char = "";

    // If the character is a modifier, set the modifier to true
    if (alphabet === modifiersDict.capital) {
      capital = true;
      continue;
    } else if (alphabet === modifiersDict.number) {
      number = true;
      continue;
    } else if (alphabet === letterToBraille(" ")) {
      number = false;
    }

    // If the character is a number, convert from braille to number, else convert from braille to letter
    if (number) {
      char = brailleToNumber(alphabet);
    } else {
      char = brailleToLetter(alphabet);
      if (capital) {
        char = char.toUpperCase();
        capital = false;
      }
    }
    output.push(char);
  }

  return output.join("");
}
