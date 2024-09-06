// braille to english mapping
const brailleToEnglishMapping = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", 
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", 
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", 
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", 
    "O..OOO": "z", "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!",
    "..OO..": ":", "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", 
    "O..OO.": ">", "O.O..O": "(", ".O.OO.": ")"
};

// braille to english mapping for numbers
const brailleToEnglishNumberMapping = {
    ".OOO..": "0", "O.....": "1", "O.O...": "2", "OO....": "3",
    "OO.O..": "4", "O..O..": "5", "OOO...": "6", "OOOO..": "7", "O.OO..": "8", 
    ".OO...": "9"
}

// english to braille mapping
const englishToBrailleMapping = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", 
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", 
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", 
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", 
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", 
    "z": "O..OOO", "0": ".OOO..", "1": "O.....", "2": "O.O...", "3": "OO....", 
    "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", 
    "9": ".OO...", ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", 
    ":": "..OO..", ";": "..O.O.", "-": "....OO", "/": ".O..O.", "<": ".OO..O", 
    ">": "O..OO.", "(": "O.O..O", ")": ".O.OO.", " ": "......", "capital": ".....O", 
    "decimal": ".O...O", "number": ".O.OOO"
};

const CAPITAL_BRAILLE = '.....O';
const NUMBER_BRAILLE = '.O.OOO';
const SPACE_BRAILLE = '......';

// function to translate to english
function translateToEnglish(input) {
    let englishText = '';
    let capitalFollows = false;
    let numberFollows = false;

    // split the input into group of 6-character
    const characters = input.match(/.{6}/g);

    for (const char of characters) {
        if (char === CAPITAL_BRAILLE) {
            capitalFollows = true;
            continue;
        } 
        else if (char === NUMBER_BRAILLE) {
            numberFollows = true;
            continue;
        } 
        else if (char === SPACE_BRAILLE) {
            englishText += ' ';
            numberFollows = false;
            continue;
        }

        if (numberFollows) {
            englishText += brailleToEnglishNumberMapping[char];
        } 
        else {
            newChar = brailleToEnglishMapping[char];
            if (capitalFollows) {
                englishText += newChar.toUpperCase();
                capitalFollows = false;
            } else {
                englishText += newChar;
            }
        }
    }
    console.log(englishText);
}

// function to translate to braille
function translateToBraille(input) {
    let brailleText = '';
    let numberFollows = false;

    for(const char of input) {
        const isCapital = (char === char.toUpperCase() && char !== char.toLowerCase());
        const isNumber = (char >= '0' && char <= '9');

        if(isCapital) {
            brailleText += englishToBrailleMapping['capital'];
        }
        else if(isNumber) {
            if(!numberFollows) {
                numberFollows = true;
                brailleText += englishToBrailleMapping['number'];
            }
        }
        else {
            numberFollows = false;
        }
        brailleText += englishToBrailleMapping[char.toLowerCase()];
    }
    console.log(brailleText);
}

// read input string from cmd
const inputStringArray = process.argv.slice(2);

// exit if no input string
if(inputStringArray.length === 0) {
    console.log("Please enter string to be converted!!!");
    process.exit(1);
}

// Join array of string to string
const inputString = inputStringArray.join(" ");

if(inputString.includes('.') || inputString.includes('O')) {
    // translate to English
    translateToEnglish(inputString);
}
else {
    // translate to Braille
    translateToBraille(inputString);
}