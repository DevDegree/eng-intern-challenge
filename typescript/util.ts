// ascii code values of important characters
export const ASCII_a_CODE = 97;
export const ASCII_z_CODE = 122;
export const ASCII_0_CODE = 48;
export const ASCII_9_CODE = 57;
export const ASCII_A_CODE = 65;
export const ASCII_Z_CODE = 90;

// checks if the character is an alphabet character
export function isalpha(str: string): Boolean {
    const char = str.toLowerCase();
    if (char.length !== 1) {
        return false;
    }

    const code = char.charCodeAt(0);
    return code >= ASCII_a_CODE && code <= ASCII_z_CODE;
}

// checks if the character is in upper case
export function charIsUpperCase(char: string): Boolean {
    if (char.length !== 1) {
        return false;
    }
    const code = char.charCodeAt(0);
    return code >= ASCII_A_CODE && code <= ASCII_Z_CODE;
}

// checks if the character is a number
export function isnum(char: String): Boolean {
    if (char.length !== 1) {
        return false;
    }
    const code = char.charCodeAt(0);
    return code >= ASCII_0_CODE && code <= ASCII_9_CODE;
}

// checks if string has a number character in it
export function strHasNum(str: String): Boolean {
    for (const char of str) {
        if (isnum(char)) return true;
    }
    return false;
}