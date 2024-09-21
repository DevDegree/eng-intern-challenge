/* eslint-disable no-console */
import isBraille from './services/isBraille';
import {translateToBraille} from './services/translateToBraille';
import {translateToEnglish} from './services/translateToEnglish';
import getTextFromTerminal from './utils/getTexrFromTerminal';

const textToTranslate = getTextFromTerminal();

if (isBraille(textToTranslate)) {
  console.log(translateToEnglish(textToTranslate));
} else {
  console.log(translateToBraille(textToTranslate));
}

