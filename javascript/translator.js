/** BRAILLE TRANSLATOR
 * The Braille Translator is used to translate English characters to Braille 
 * characters and vice versa. The translation includes the English alphabet,
 * numbers 0 through 9, spaces and capital letters. This file contains the 
 * translation for Braille to English in the Object<key, pair> constants,
 * 'translationLetter' and 'translationNumber'.  
 */

const translationLetter = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..",
    "e": "O..O..", "f": "OOO...", "g": "OOOO..", "h": "O.OO..",
    "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.",
    "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO", "capital": ".....O", 
    "decimal": ".O...O", "number": ".O.OOO", "space": "......"
}

const translationNumber = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..",
    "9": ".OO...", "0": ".OOO..", "space": "......"
}

// const translationSpecialChar = {
//     ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.",
//     ":": "..OO..", ";": "..O.O.", "-": "....OO", "/": ".O..O.",
//     "<": ".OO..O", ">": "O..OO.", "(": "O.O..O", ")": ".O.OO."
// }

function translator (input) {
    // Since Braille characters do not have empty space in-between,
    // that is considered the main check for either English or Braille.
    if (!input.includes(' ') && (input.startsWith('..') || input.startsWith('.O') || input.startsWith('O.') || input.startsWith('OO'))) {
        return toEnglish(input);
    } else {
        return toBraille(input);
    }
}

/** BRAILLE TO ENGLISH TRANSLATION
 * This function translates the Braille characters passed in
 * command line to English.
 */
function toEnglish(string) {
    let capitalize = false;
    let numbers = false;
    let translated = '';
    let final = '';

    /** BRAILLE ITERATION
     * Iterate through the string in intervals of 6 to capture
     * Braille characters in the given input. 
     */ 
    for (let i = 0; i < string.length; i+=6) {
        translated = string.slice(i, (i + 6))

        if (translated.length < 6 || !translated) {
            return 'Invalid Braille Character detected! Exiting...'
        }

        // Check to see whether the 'number follows' or the
        // default (English alphabet) is triggered
        if (numbers && !translated.includes('......')) {
            translated = Object.keys(translationNumber).find(key =>
                translationNumber[key] === translated
            );
        } else {
            numbers = false;
            translated = Object.keys(translationLetter).find(key =>
                translationLetter[key] === translated
            );
        }
        
        // Scan through the translated string to check whether it
        // denotes 'capital' or 'number' and set the mode to such 
        if (translated === "capital") {
            capitalize = true;
            continue;
        } else if (translated === "number") {
            numbers = true;
            continue;
        } else if (translated === "space") {
            final += " ";
            continue;
        }

        // Capitalize the translated string and deactivate 
        // capitalize mode
        if (capitalize) {
            translated = translated.toUpperCase();
            capitalize = false;
        }
        final += translated;
    }
    // console.log('Translated to English: ', final);
    return final;
}

/** ENGLISH TO BRAILLE TRANSLATION
 * This function translates the English characters passed in
 * command line to Braille.
 */
function toBraille(string) {
    // console.log('Translate this string: ', string);
    let translated = '';
    let final = '';
    let numbers = false;

    /** ENGLISH ITERATION
     * Iterate through each character in the string to capture
     * English characters in the given input.
     */
    for (let i = 0; i < string.length; i++) {
        translated = string[i]

        // Check to see if the character at index i is either
        // a 'space', 'number' or an 'alphabet'
        if (translated == " ") {
            numbers = false;
            final += translationLetter.space;
        }
        else if (!isNaN(translated)) {
            // Set the mode to numbers
            if (!numbers) {
                numbers = true;
                final += translationLetter.number;
            }
            final += translationNumber[translated];
        } else {
            // Included this to consider addresses (1AA 2BB)
            numbers = false;
            // Check to see if the character is capitalized
            if (translated == translated.toUpperCase()) {
                final += translationLetter.capital;
                translated = translated.toLowerCase();
            }
            final += translationLetter[translated];
        }
    }
    return final;
}


/** UNCOMMENT THIS TO INSERT YOUR OWN STRINGS BY TYPING IN AT RUNTIME */
// const readline = require("readline");

// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// });

// var loopQuestion = function () {
//     rl.question('What should I translate? (Type "exit" to leave) ', input => {
//         if (input == 'exit') { return rl.close(); }
//         console.log("Translated to:", translator(input))
//         loopQuestion();
//     })
// }

// loopQuestion();

// rl.on("close", function() {
//     console.log("\nBye!");
//     process.exit(0);
// })
/** ----------AND COMMENT THE PORTION AFTER THIS LINE---------------- */

let arguments = process.argv.slice(2);

console.log(translator(arguments.join(' ')));
process.exit(0);
