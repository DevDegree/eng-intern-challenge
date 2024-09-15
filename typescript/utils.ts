import { InputString, SingleChar, SingleBrailleChar, IsNumber, IsCapital } from './types';
import { braille, functions, numberMap, reverseNumberMap, alphabet } from './mappings';

const matchesPattern = (input: InputString, pattern: RegExp): boolean => pattern.test(input);

export const isBraille = (input: InputString): boolean => matchesPattern(input, /^[O. ]+$/);
export const hasMultipleUppercase = (str: string) => (str.match(/[A-Z]/g) || []).length > 1;
export const hasSpecialCharacters = (str: string) => /[^a-zA-Z0-9 .]/.test(str);

export const convertUpperCaseCharToBraille = (char: SingleChar): SingleBrailleChar => {
    return functions.capital + braille[char.toLowerCase()];
};

export const convertNumberCharToBraille = (char: SingleChar, isNumber: IsNumber): SingleBrailleChar => {
    return isNumber ? braille[numberMap[char]] : functions.number + braille[numberMap[char]];
};

export const convertSpaceToBraille = (): SingleBrailleChar => {
    return braille[' '];
};

export const convertDefaultCharToBraille = (char: SingleChar): SingleBrailleChar => {
    return braille[char] || braille[' '];
};

export const convertBrailleToChar = (brailleChar: SingleBrailleChar, isCapital: IsCapital, isNumber: IsNumber): SingleChar => {
    let engChar = alphabet[brailleChar] || ' ';

    if (isCapital && engChar !== ' ') {
        engChar = engChar.toUpperCase();
    }

    if (isNumber && engChar !== ' ') {
        engChar = reverseNumberMap[engChar];
    }

    return engChar;
};

export const convertCharToBraille = (char: SingleChar, isNumber: IsNumber): SingleBrailleChar => {
    if (/[A-Z]/.test(char)) {
        return convertUpperCaseCharToBraille(char);
    } else if (/\d/.test(char)) {
        return convertNumberCharToBraille(char, isNumber);
    } else if (char === ' ') {
        return convertSpaceToBraille();
    } else {
        return convertDefaultCharToBraille(char);
    }
};