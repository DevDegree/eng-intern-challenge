// taking input from command line
const input = process.argv.slice(2).join(' ');

// braille mapping for letter, number and symbols
const letterMapping = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',  // Space
    'capital': '.....O',  // Capital indicator
    'number': '.O.OOO'  // Number indicator
};

// braille mapping for digits
const brailleDigits = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', ' ': '......',
};

// function to check if input is braille or not
function isBraille(input) {
    return /^[O\.]+$/.test(input);
}

// function to chunk the string
function chunkString(str, length) {
    let result = [];
    for (let i = 0; i < str.length; i += length) {
        result.push(str.slice(i, i + length));
    }
    return result;
}

// function to get key from value
function getKeyFromValue(object, value) {
    return Object.keys(object).find(key => object[key] === value);
}

// function to translate braille to english
function translateToEnglish(braille) {
    console.log("braille text", braille);
    let result = [];
    let isCapitalContext = false;
    let isNumberContext = false;
    const newBrailleLangArr = chunkString(braille, 6);
    // console.log("newBrailleLangArr", newBrailleLangArr);

    for (let token of newBrailleLangArr) {
        let key;

        // Handle Capital Context
        if (token === '.....O') {
            isCapitalContext = true;
            continue;
        }

        // Handle Number Context
        if (token === '.O.OOO') {
            isNumberContext = true;
            continue;
        }

        // Translate the Braille token to English character
        if (isNumberContext) {
            key = getKeyFromValue(brailleDigits, token);
            if (key) {
                result.push(key);
            }
        } else if (isCapitalContext) {
            key = getKeyFromValue(letterMapping, token);
            if (key) {
                result.push(key.toUpperCase());
            }
            isCapitalContext = false; // Reset capital context after processing
        } else {
            key = getKeyFromValue(letterMapping, token);
            if (key) {
                result.push(key);
            }
        }
    }
    return result.join('');
}

// function to check if letter is uppercase
function isUpperCase(letter) {
    return /^[A-Z]$/.test(letter);
}

// function to check if letter is digit
function isDigit(char) {
    return /^\d$/.test(char);
}

// function to translate english to braille
function translateToBraille(english) {
    let result = [];
    let wasNumber = false;  // Track if we're in a number context

    for (let char of english) {
        // Handle uppercase letters
        if (isUpperCase(char)) {
            result.push(letterMapping['capital']);  // Add capitalization indicator
            char = char.toLowerCase();  // Convert the letter to lowercase
        }

        // Handle digits
        if (isDigit(char)) {
            if (!wasNumber) {  // If we're not in a number context, add number indicator
                result.push(letterMapping['number']);
                wasNumber = true;  // Now we are in a number context
            }
            result.push(brailleDigits[char]);
        } else {
            wasNumber = false;  // Reset the number context for non-digit characters
            if (char === ' ') {
                result.push(letterMapping[' ']);  // Add space for spaces
            } else {
                result.push(letterMapping[char]);  // Add regular Braille letter
            }
        }
    }

    return result.join('');
}

// check if input is braille or not
if (isBraille(input)) {
    console.log(translateToEnglish(input));
}
else {
    console.log(translateToBraille(input));
}
