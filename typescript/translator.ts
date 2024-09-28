import { translateBrailleToEnglish, translateEnglishToBraille } from './types/braile';

const args = process.argv.slice(2);
console.log(translateEnglishToBraille(args.join(' ')));
  
