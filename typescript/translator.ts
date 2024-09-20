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
  const englishCharacters: string[] = [];
  for (const brailleChar of brailleCharacters) {
    if (brailleChar === modifyiers.capitalFollows) {
      isCapital = true;
      continue;
    }
    if (brailleChar === modifyiers.numberFollows) {
      isNumber = true;
      continue;
    }
    if (brailleChar === numbersDictionary['.']) { continue; }
    if (isNumber) {
      englishChar = getKeyByValue(numbersDictionary, brailleChar) as EnglsihChar;
      englishCharacters.push(englishChar);
      continue;
    }
    englishChar = getKeyByValue(brailleDictionary, brailleChar) as EnglsihChar;
    if (isCapital) {
      englishChar = englishChar?.toUpperCase() as EnglsihChar;
      isCapital = false;
    }
    if (brailleChar === brailleDictionary[' ']) {
      isNumber = false;
    }
    englishCharacters.push(englishChar);
  }
  const textInEnglish = englishCharacters.join();
  return textInEnglish;
}

function translateToBraille(textToTranslate : string) {
  const characters = textToTranslate.split('');
  const textInBraille = characters.map((character) => {
    return (convertToBraille(character));
  }).join();
  return textInBraille;
}

const textToTranslate = process.argv[2];

if (isBraille(textToTranslate)) {
  translateToEnglish(textToTranslate);
} else {
  translateToBraille(textToTranslate);
}

