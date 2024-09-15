import { EnglishText, BrailleText } from './types';
import { convertCharToBraille, convertBrailleToChar } from './utils';
import { functions } from './mappings';

export const englishToBraille = (text: EnglishText): BrailleText => {
    let brailleOutput = [];
    let isNumber = false;

    for (let char of text) {
        if (char === ' ') {
            brailleOutput.push('......');
            isNumber = false;
            continue;
        }

        const brailleChar = convertCharToBraille(char, isNumber);
        brailleOutput.push(brailleChar);

        if (/\d/.test(char)) {
            isNumber = true;
        } else {
            isNumber = false;
        }
    }
    return brailleOutput.join('');
};

export const brailleToEng = (brailleStr: BrailleText): EnglishText => {
    let engOutput = [];
    let isCapital = false;
    let isNumber = false;

    for (let i = 0; i < brailleStr.length; i += 6) {
        const brailleChar = brailleStr.slice(i, i + 6);

        if (brailleChar === '......') {
            engOutput.push(' ');
            isNumber = false;
            continue;
        }

        if (brailleChar === functions.capital) {
            isCapital = true;
            continue;
        } else if (brailleChar === functions.number) {
            isNumber = true;
            continue;
        }

        const engChar = convertBrailleToChar(brailleChar, isCapital, isNumber);
        engOutput.push(engChar);

        if (engChar === ' ') {
            isNumber = false;
        }

        if (isCapital) {
            isCapital = false;
        }
    }
    return engOutput.join('');
};