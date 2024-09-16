// Create a translation dictionary for char to braille
const {
    ENG_TO_BRAILLE_DICTIONARY,
    BRAILLE_TO_ENGLISH_DICTIONARY
} = require('./utilities/brailleMapping')

// Function to translate English to Braille
function englishToBraille(input) {
    const letterCheck = /^[A-Za-z]+$/
    const numberCheck = /^[0-9]+$/
    let result = '';
    let inNumberMode = false;

    for (let char of input) {
        //Check for capital
        if (letterCheck.test(char)) {
            if(char === char.toUpperCase()) result += ENG_TO_BRAILLE_DICTIONARY['capital']
            char = char.toLowerCase();
            result += ENG_TO_BRAILLE_DICTIONARY[char]
        }
        //Check for number
        if (numberCheck.test(char)) {
            if (!inNumberMode) {
                result += ENG_TO_BRAILLE_DICTIONARY['number']
                inNumberMode = true;
            }
            result += ENG_TO_BRAILLE_DICTIONARY[char]
        } else {
            inNumberMode = false;
        }
        //Check for spaces
        if(char === ' ') {
            result += ENG_TO_BRAILLE_DICTIONARY[" "]
        }
    }

    return result
};

function brailleToEnglish(input) {
    let result = '';
    let capitalMode = false;
    let numberMode = false;

    const brailleChars = splitBraille(input, 6) //each braille string is length 6

    for (const brailleChar of brailleChars) {
        // Check for Capital
        if (brailleChar === ENG_TO_BRAILLE_DICTIONARY['capital']) capitalMode = true;
        // Check for Numbers
        else if (brailleChar === ENG_TO_BRAILLE_DICTIONARY['number']) numberMode = true;
        // Check for space, if there is a space while in numberMode set it to false
        else if (BRAILLE_TO_ENGLISH_DICTIONARY[brailleChar] === ' ') {
            result += ' ';
            numberMode = false;
        } else {
            let translatedChar = BRAILLE_TO_ENGLISH_DICTIONARY[brailleChar];
            // if in number mode and the letters are a - j, convert it to 1 - 9,0
            if (numberMode && translatedChar.match(/[a-j]/)) {
                translatedChar = (translatedChar.charCodeAt(0)  - "a".charCodeAt(0) + 1) % 10
            }
            if (capitalMode) {
                translatedChar = translatedChar.toUpperCase();
                capitalMode = false;
            }
            result += translatedChar;
        }
    }

    return result;
}

// split braille into 6 length chars
function splitBraille(braille, size) {
    const brailleArr = []
    for(let i = 0; i < braille.length; i += size)
        brailleArr.push(braille.slice(i, i + size))

    return brailleArr
}

/**
 * The first item (argv[0]) will be the path to node itself, and the second item (argv[1]) will be the path to your script code.
 * 
 * process.argv is an array and the first two items are:
 * [0]: path to the node
 * [1]: path to the script code (ex. node translate)
 * 
 * by using slice(2) I eliminate these two items and instead focus on the third item, which is the array of the sentence
 * ex. Hello world would come up as ["Hello", "world"]
 * that's why join(' ') is needed to combine the two
 */
const input = process.argv.slice(2).join(' ')

// determine which translator to use by seeing what the input consists of
function transaltor(input) {
    if (input.match(/^[.O\s]+$/)) {
        // Input seems to be Braille
        console.log(brailleToEnglish(input))
    } else {
        // Input seems to be English
        console.log(englishToBraille(input))
    }
}

return transaltor(input)