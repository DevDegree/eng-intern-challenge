import {BrailleChar, EnglsihChar} from '../types/types';
import {modifyiers, brailleDictionary, numbersDictionary} from '../utils/constants';
import getKeyByValue from '../utils/getKeyByValue';
import splitByNumberOfChar from '../utils/splitByNumberOfChar';


// TODO improve types
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
  const textInEnglish = englishCharacters.join('');
  return textInEnglish;
}
