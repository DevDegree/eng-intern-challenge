import { englishToBraille, brailleToEng } from './conversion';
import { isBraille, hasMultipleUppercase, hasSpecialCharacters } from './utils';

const input = process.argv.slice(2).join(' ');

if (isBraille(input)) {
    console.log(brailleToEng(input));
} else {
    console.log(englishToBraille(input));
}