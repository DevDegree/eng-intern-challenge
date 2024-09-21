import {BrailleChar, NumberChar, NonNumberChar} from '../types/types';
import {isNumber, isUpperCase} from '../utils/checkTypeOfChar';
import {modifyiers, numbersDictionary, brailleDictionary} from '../utils/constants';


export function translateToBraille(textToTranslate: string) {
  const englishCharacters = textToTranslate.split('');
  let isFirstNumber = true;
  const brailleCharacters: BrailleChar[] = [];
  for (let englishChar of englishCharacters) {
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
        englishChar = englishChar.toLowerCase();
      }
      brailleChar = brailleDictionary[englishChar as NonNumberChar];
      isFirstNumber = true;
    }
    brailleCharacters.push(brailleChar);
  }
  const textInBraille = brailleCharacters.join('');
  return textInBraille;
}
