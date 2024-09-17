// Braille mappings
const Braille_dict = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ',
    '.....O': 'CAPITAL', '.O.OOO': 'NUMBER'
};

// Reverse Braille mappings
const Braille_dict_reverse = {};
for (let key in Braille_dict) {
    Braille_dict_reverse[Braille_dict[key]] = key;
}

// Number mappings
const NUMBER_MAP = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
    'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
};

// Reverse number mappings
const NUMBER_MAP_reverse = {};
for (let key in NUMBER_MAP) {
    NUMBER_MAP_reverse[NUMBER_MAP[key]] = key;
}

// Function to convert Braille to English
function brailleToEnglish(braille) {
    let english = "";
    let isCapital = false;
    let isNumber = false;
    for (let i = 0; i < braille.length; i += 6) {
        let bchar = braille.slice(i, i + 6);
        // Check for capital indicator
        if (bchar === Braille_dict_reverse['CAPITAL']) {
            isCapital = true;
            continue;
        }
        // Check for number indicator
        else if (bchar === Braille_dict_reverse['NUMBER']) {
            isNumber = true;
            continue;
        }
        else {
            let echar = Braille_dict[bchar];
            // Convert to uppercase if capital indicator was found
            if (isCapital) {
                echar = echar.toUpperCase();
                isCapital = false;
            }
            // Convert to number if number indicator was found
            else if (isNumber) {
                if (echar !== " ")
                    echar = NUMBER_MAP[echar];
                else
                    isNumber = false;
            }
            english += echar;
        }
    }
    return english;
}

// Function to convert English to Braille
function englishToBraille(eng) {
    let braille = "";
    let bchar = "";
    for (const echar of eng) {
        // Check if character is a number
        if (!isNaN(echar)) {
            if (echar === " ")
                bchar = Braille_dict_reverse[" "];
            else {
                bchar = Braille_dict_reverse["NUMBER"];
                bchar += Braille_dict_reverse[NUMBER_MAP_reverse[echar]];
            }
        }
        else {
            // Check if character is uppercase
            if (echar === echar.toUpperCase()) {
                bchar = Braille_dict_reverse["CAPITAL"];
                bchar += Braille_dict_reverse[echar.toLowerCase()];
            }
            else {
                bchar = Braille_dict_reverse[echar];
            }
        }
        braille += bchar;
    }
    return braille;
}

// Function to check if text is Braille
function isBraille(text) {
    const BRAILLE_REGEX = /^[O.]+$/
    return BRAILLE_REGEX.test(text) && text.length % 6 === 0;
}

// Function to translate text between Braille and English
function translate(text) {
    return isBraille(text) ? brailleToEnglish(text) : englishToBraille(text);
}

// Get input text from command line arguments
const inputText = process.argv.slice(2).join(' ');

// Output the translated text
console.log(translate(inputText));
