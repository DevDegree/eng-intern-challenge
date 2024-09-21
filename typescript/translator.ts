/* eslint-disable no-console */
import isBraille from './services/isBraille';
import {BrailleChar, EnglsihChar, NonNumberChar, NumberChar} from './types/types';
import {isNumber, isUpperCase} from './utils/checkTypeOfChar';
import {brailleDictionary, modifyiers, numbersDictionary} from './utils/constants';
import getKeyByValue from './utils/getKeyByValue';
import splitByNumberOfChar from './utils/splitByNumberOfChar';

// TODO improve types
function translateToEnglish(textToTranslate : string) {
  const brailleCharacters = splitByNumberOfChar(textToTranslate, 6) as BrailleChar[];
  let isCapital = false;
  let isStillNumber = false;
  const englishCharacters: EnglsihChar[] = [];
  for (const brailleChar of brailleCharacters) {
    let englishChar;
    if (brailleChar === modifyiers.capitalFollows) {
      isCapital = true;
      continue;
    }
    if (brailleChar === modifyiers.numberFollows) {
      isStillNumber = true;
      continue;
    } else if (brailleChar === brailleDictionary[' ']) {
      isStillNumber = false;
    }
    if (isStillNumber) {
      englishChar = getKeyByValue(numbersDictionary, brailleChar) as EnglsihChar;
    } else {
      englishChar = getKeyByValue(brailleDictionary, brailleChar) as EnglsihChar;
      if (isCapital) {
        englishChar = englishChar?.toUpperCase() as EnglsihChar;
        isCapital = false;
      }
    }
    englishCharacters.push(englishChar);
  }
  const textInEnglish = englishCharacters.join();
  return textInEnglish;
}

function translateToBraille(textToTranslate : string) {
  const englishCharacters = textToTranslate.split('') as EnglsihChar[];
  let isFirstNumber = true;
  const brailleCharacters : BrailleChar[] = [];
  for (const englishChar of englishCharacters) {
    let brailleChar;
    if (isNumber(englishChar)) {
      if (isFirstNumber) {
        brailleCharacters.push(modifyiers.numberFollows);
      }
      brailleChar = numbersDictionary[englishChar as NumberChar];
      isFirstNumber = false;
    } else {
      if (isUpperCase(englishChar)) {
        brailleCharacters.push(modifyiers.capitalFollows);
      }
      brailleChar = brailleDictionary[englishChar as NonNumberChar];
      isFirstNumber = true;
    }
    brailleCharacters.push(brailleChar);
  }
  const textInBraille = brailleCharacters.join();
  return textInBraille;
}
const textToTranslate = process.argv[2];

if (isBraille(textToTranslate)) {
  console.log(translateToEnglish(textToTranslate));
} else {
  console.log(translateToBraille(textToTranslate));
}

