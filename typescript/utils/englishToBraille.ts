import { CAPITALIZE, alphabetToBraille, NUMBER, numberToBraille } from "../constants";

/**
 * Converts an English string to Braille.
 * 
 * This function takes a string of English text and converts it to its Braille representation.
 * It handles uppercase letters, numbers, and spaces. For uppercase letters, it prepends the
 * capitalization symbol. For numbers, it switches to number mode and uses the appropriate
 * number symbols. Spaces are converted to their Braille equivalent.
 * 
 * @param message - The English text to be converted to Braille.
 * @returns A string representing the Braille translation of the input message.
 */
export const englishToBraille = (message: string): string => {
    const result: string[] = [];
    let numberMode = false;

    for (const char of message) {
        if (/[a-zA-Z]/.test(char)) {
            if (/[A-Z]/.test(char)) {
                result.push(CAPITALIZE);
            }
            result.push(alphabetToBraille[char.toLowerCase()]);
            numberMode = false;
        } else if (/\d/.test(char)) {
            if (!numberMode) {
                result.push(NUMBER);
                numberMode = true;
            }
            result.push(numberToBraille[char]);
        } else if (/\s/.test(char)) {
            result.push(alphabetToBraille[char]);
            numberMode = false;
        }
    }

    return result.join('');
}
