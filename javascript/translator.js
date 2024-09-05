
const { braille_dict, braille_symbols_dict, braille_precursor_dict } = require('./constants')
const { isBrailleCheck, splitEverySixChars } = require('./utils')

const arg = process.argv.slice(2);
console.log("arg>>", arg)


/**
 * This function translates alpha-numeric character to Braille
 * 
 * @param {string} value - Braille string that will need to be translated
 * @returns
 * 
 */
function getBrailleCharacter(value) {

}

function getAlphaNumeric(key) {

}

function getSymbol(key) {

}

const isBraille = isBrailleCheck(arg)

if (isBraille) {
    const english_translation_array = [];
    console.log("is braille")

    // Split into chunks of 6 characters
    const braille_array = splitEverySixChars(arg[0]);

    console.log(braille_array);
    for (let braille of braille_array) {
        // handle translation of braille to english here
    }


} else {
    const braille_translation_array = [];
    console.log("is not braille")

    const english_array = arg;
    console.log(english_array)

    for (let word of english_array) {
        // handle alphabet to braille translation here.
        const alphabets = word.split('')
        console.log("alphabets", alphabets)
    }
}
