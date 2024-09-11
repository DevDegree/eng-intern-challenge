import { SPACE, CAPITALIZE, brailleToAlphabet, NUMBER, brailleToNumber } from "../constants";

/**
 * Converts a Braille string to English.
 * 
 * This function takes a string of Braille characters and converts it to its English representation.
 * It handles uppercase letters, numbers, and spaces. For uppercase letters, it recognizes the
 * capitalization symbol. For numbers, it switches to number mode and uses the appropriate
 * number symbols. Spaces are converted to their English equivalent.
 * 
 * @param message - The Braille text to be converted to English.
 * @returns A string representing the English translation of the input Braille message.
 */
export const brailleToEnglish = (message: string): string => {
    const result: string[] = [];
    let numberMode = false;
    let i = 0;

    while (i < message.length) {
        const symbol = message.slice(i, i + 6);

        if (symbol === SPACE) {
            numberMode = false;
        }

        if (symbol === CAPITALIZE) {
            i += 6;
            const nextSymbol = message.slice(i, i + 6);
            result.push(brailleToAlphabet[nextSymbol].toUpperCase());
        } else if (symbol === NUMBER) {
            numberMode = true;
            i += 6;
            continue;
        } else if (symbol in brailleToAlphabet && !numberMode) {
            result.push(brailleToAlphabet[symbol]);
            numberMode = false;
        } else if (symbol in brailleToNumber) {
            result.push(brailleToNumber[symbol]);
        } else {
            result.push(' ');
        }

        i += 6;
    }

    return result.join('');
}