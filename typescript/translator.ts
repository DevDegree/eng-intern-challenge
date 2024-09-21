import isBraille from './services/isBraille';
import {BrailleChar, EnglsihChar} from './types/types';
import {brailleDictionary, modifyiers, numbersDictionary} from './utils/constants';
import getKeyByValue from './utils/getKeyByValue';
import splitByNumberOfChar from './utils/splitByNumberOfChar';

function translateToEnglish(textToTranslate : string) {
  const brailleCharacters = splitByNumberOfChar(textToTranslate, 6) as BrailleChar[];
  let englishChar;
  let isCapital = false;
  let isNumber = false;
  const englishCharacters: EnglsihChar[] = [];
  for (const brailleChar of brailleCharacters) {
    if (brailleChar === modifyiers.capitalFollows) {
      isCapital = true;
      continue;
    }
    if (brailleChar === modifyiers.numberFollows) {
      isNumber = true;
      continue;
    } else if (brailleChar === brailleDictionary[' ']) {
      isNumber = false;
    }
    if (isNumber) {
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
  const englishCharacters = textToTranslate.split('');
  const isFirstNumber = false;
  const brailleCharacters : BrailleChar[] = [];
  for (const englishChar of englishCharacters) {
    if (isUpperCase) {
      brailleCharacters.push(modifyiers.capitalFollows);
      brailleCharacters.push(brailleChar);
    }
    const textInBraille = brailleCharacters.join();
    return textInBraille;
  }
}
const textToTranslate = process.argv[2];

if (isBraille(textToTranslate)) {
  translateToEnglish(textToTranslate);
} else {
  translateToBraille(textToTranslate);
}

