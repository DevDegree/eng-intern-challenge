import { brlAlph, engAlph } from './alphabets.js';

/**
 * Takes the string as parameter 
 * and translate it from English to Braille.
 * @param {string} engStr string to be translated.
 * @returns translated string.
 */
function engToBraille(engStr) {

    let brlStr = '';     // Stores translated string
    let isNum = false;   // True if next character is number

    for (const char of engStr) {

        // If char is capital letter
        // Push capital follows character
        // Else if char is number
        // Push number follows character
        if ((char <= 'Z') && ('A' <= char)) {
            brlStr += brlAlph['capitalFlw'];
        }
        else if ((char <= '9') && ('0' <= char)) {
            if (!isNum) {
                isNum = true;
                brlStr += brlAlph['numberFlw'];
            }
        }
        
        if (isNum && !((char <= '9') && ('0' <= char))) {
            isNum = false
        }

        brlStr += brlAlph[char.toLowerCase()];
    }

    return brlStr;
}

/**
 * Takes the string as parameter 
 * and translate it from Braille to English.
 * @param {string} brlStr string to be translated.
 * @returns translated string.
 */
function brailleToEng(brlStr) {

    let engStr = '';     // Stores translated string
    let isCap = false;   // True if next char is capital
    let isNum = false;   // True if next char is number

    for (let i = 0; i < brlStr.length; (i += 6)) {

        const char = engAlph[brlStr.substring((0 + i), (6 + i))];

        if (char == 'capitalFlw') {
            isCap = true;
        }
        else if (char == 'numberFlw') {
            isNum = true;
        }
        else {
            if ((char == ' ') && isNum) {
                isNum = false;
            }

            if (isNum) {
                engStr += engAlph['numbers'][char];
            }
            else if (isCap) {
                engStr += char.toUpperCase();
                isCap = false;
            }
            else {
                engStr += char;
            }
        }
    }

    return engStr;
}

function main() {

    const orgStr = process.argv.slice(2).join(' ');
    
    const trlStr = /^[O\.]+$/.test(orgStr) ? brailleToEng(orgStr) : engToBraille(orgStr);
    console.log(trlStr);
}

main();