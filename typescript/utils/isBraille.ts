/**
 * Determines if a given string is in Braille format.
 * 
 * @param message - The string to be checked.
 * @returns True if the string consists only of 'O' and '.' characters, false otherwise.
 */
export const isBraille = (message: string): boolean => {
    return message.split('').every(char => char === 'O' || char === '.');
}