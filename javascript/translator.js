// Data for translating Braille to English
const BRAILLE_TO_ENGLISH = {
    'O.....': 'A',
    'O.O...': 'B',
    'OO....': 'C',
    'OO.O..': 'D',
    'O..O..': 'E',
    'OOO...': 'F',
    'OOOO..': 'G',
    'O.OO..': 'H',
    '.OO...': 'I',
    '.OOO..': 'J',
    'O...O.': 'K',
    'O.O.O.': 'L',
    'OO..O.': 'M',
    'OO.OO.': 'N',
    'O..OO.': 'O',
    'OOO.O.': 'P',
    'OOOOO.': 'Q',
    'O.OOO.': 'R',
    '.OO.O.': 'S',
    '.OOOO.': 'T',
    'O...OO': 'U',
    'O.O.OO': 'V',
    '.OOO.O': 'W',
    'OO..OO': 'X',
    'OO.OOO': 'Y',
    'O..OOO': 'Z',
    '......': ' ',
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '?',
    '..OOO.': '!',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.O..O.': '/',
    'O.O..O': '(',
    '.O.OO.': ')',
  };
  
// Data for translating Braille to Numbers
const BRAILLE_TO_NUMBERS = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0',
};
  
// Data for Special Cases
const SPACE = "......";
const CAPITAL_FOLLOWS = ".....O";
const NUMBER_FOLLOWS = ".O.OOO";
const DECIMAL_FOLLOWS = ".O...O";
  
// map the reverse of the keys and values of BRAILLE_TO_ENGLISH
const ENGLISH_TO_BRAILLE = Object.keys(BRAILLE_TO_ENGLISH).reduce((acc, e) => {
    const key = BRAILLE_TO_ENGLISH[e];
    const value = e;
    acc[key] = value;
    return acc;
}, {});
  
// map the reverse of the keys and values of BRAILLE_TO_NUMBERS
const NUMBERS_TO_BRAILLE = Object.keys(BRAILLE_TO_NUMBERS).reduce((acc, e) => {
    const key = BRAILLE_TO_NUMBERS[e];
    const value = e;
    acc[key] = value;
    return acc;
}, {});
  
// combine the ENGLISH_TO_BRAILLE and NUMBERS_TO_BRAILLE objects
const ALL_ENGLISH_TO_BRAILLE = {
    ...ENGLISH_TO_BRAILLE,
    ...NUMBERS_TO_BRAILLE,
};

/**
 * Converts the braille string to english and prints the result
 * @param {string} inputString 
 */
function translateBrailleToEnglish(inputString) {
    const braille = [];

    let makeUpperCase = false;
    let checkNumbers = false;
    let addDecimal = false;

    let english = "";

    // split the input string into an array of 6 characters each
    for (let i = 0; i < inputString.length; i = i + 6) {
        braille.push(inputString.slice(i, i + 6));
    }

    for (let i = 0; i < braille.length; i++) {
        if (braille[i] === CAPITAL_FOLLOWS) {
            makeUpperCase = true;
            continue;
        } else if (braille[i] === NUMBER_FOLLOWS) {
            checkNumbers = true;
            continue;
        } else if (braille[i] === DECIMAL_FOLLOWS) {
            addDecimal = true;
            continue;
        }

        if (checkNumbers) {
            if (braille[i] !== SPACE) {
                english = english + BRAILLE_TO_NUMBERS[braille[i]];
            } else {
                english = english + BRAILLE_TO_ENGLISH[braille[i]];
                checkNumbers = false;
            }
        } else {
            if (makeUpperCase) {
                english = english + BRAILLE_TO_ENGLISH[braille[i]];
                makeUpperCase = false;
            } else {
                english = english + BRAILLE_TO_ENGLISH[braille[i]].toLowerCase();
            }
        }
    }
    console.log(english);
}
  
/**
 * Converts the english string to braille and prints the result
 * @param {string} inputString 
 */
function translateEnglishToBraille(inputString) {
    let braille = "";
    let prevLetter = "";
    const regexToCheckUpperCase = /^[A-Z]$/;
    const regexToCheckLowerCase = /^[a-z]$/;
    const regexToCheckSpecialCharacters = /^[.,?!:;/<>()-]$/;
    const regexToCheckNumber = /^[0-9]$/;

    for (let i = 0; i < inputString.length; i++) {
        const letter = inputString[i];

        if (i > 0) {
        prevLetter = inputString[i - 1];
        }
        if (regexToCheckUpperCase.test(letter)) {
        braille = braille + CAPITAL_FOLLOWS;
        braille = braille + ALL_ENGLISH_TO_BRAILLE[letter];
        }

        if (regexToCheckLowerCase.test(letter)) {
        const capitalLetter = letter.toUpperCase();
        braille = braille + ALL_ENGLISH_TO_BRAILLE[capitalLetter];
        }

        if (regexToCheckSpecialCharacters.test(letter)) {
        braille = braille + ALL_ENGLISH_TO_BRAILLE[letter];
        }

        if (regexToCheckNumber.test(letter)) {
        const isPrevNumber = regexToCheckNumber.test(prevLetter);
        const isFirstLetter = i === 0 ? true : false;
        const isNewSentence = prevLetter === " " ? true : false;

        if (!isPrevNumber || isFirstLetter || isNewSentence) {
            braille = braille + NUMBER_FOLLOWS;
        }
        braille = braille + ALL_ENGLISH_TO_BRAILLE[letter];
        }

        if (letter === " ") {
        braille = braille + SPACE;
        }
    }
    console.log(braille);
}

/**
 * Checks if the input string is a valid braille string
 * @param {string} inputString 
 * @returns {boolean} true if the input string is a valid braille string
 */
function isBraille (inputString) {
    // regex to check if the input string contains only 'O' and '.'
    const regexToCheckBraille = /^[O.]+$/;
    return regexToCheckBraille.test(inputString) && inputString.length % 6 === 0;
}

/**
 * Checks if the input argument is valid
 * @param {Array} inputArg 
 * @returns {boolean} true if the input is valid
 */
function isValidInput (inputArg) {
    if (inputArg.length === 0) {
        console.log('INVALID INPUT: Please provide an argument');
        return false;
    }

    if (inputArg.length > 1 && isBraille(inputArg[0])) {
        console.log('INVALID INPUT: Please provide only one argument');
        return false
    }
    return true;
}

function translate(inputArg) {
    if (!isValidInput(inputArg)) {
        return;
    }

    let inputString = inputArg[0];

    if (isBraille(inputString)) {

        // this check is to prevent multiple arguments or space
        // when the input is braille
        if (inputArg.length > 1) {
            console.log('INVALID INPUT: Please provide only one argument');
            return;
        }
        // translate braille to english
        translateBrailleToEnglish(inputString);
    } else {
        if (inputArg.length > 1) {
        inputString = inputArg.join(" ");
        }
        // translate english to braille
        translateEnglishToBraille(inputString);
    }
}

translate(process.argv.slice(2));


