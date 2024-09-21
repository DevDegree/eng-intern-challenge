import {BrailleChar, EnglsihChar} from '../types/types';
import {modifyiers, brailleDictionary, numbersDictionary} from '../utils/constants';
import getKeyByValue from '../utils/getKeyByValue';
import splitByNumberOfChar from '../utils/splitByNumberOfChar';

export function translateToEnglish(textToTranslate: string) {
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
      englishChar = getKeyByValue(numbersDictionary, brailleChar);
    } else {
      englishChar = getKeyByValue(brailleDictionary, brailleChar);
      if (isCapital) {
        englishChar = englishChar?.toUpperCase();
        isCapital = false;
      }
    }
    englishCharacters.push(englishChar as EnglsihChar);
  }
  const textInEnglish = englishCharacters.join('');
  return textInEnglish;
}
