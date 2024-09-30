//CONSTANTS

// Key-value pair where the 6 char braille string is the key to the letter value
// Must check for special chars (capital, decimal before). This is  a lot quicker than regex
const BRAILLE_TO_LETTER = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
};

//Treat numbers as char so it can be appended to string easily
const BRAILLE_TO_NUMBER = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0",
};

const BRAILLE_SPACE = "......";
const BRAILLE_CAPITAL = ".....O";
const BRAILLE_NUMBER = ".O.OOO";
const NONE = ""; //Used for char follows checking

//FUNCTIONS
/**
 * Returns the braille value of a given character
 * @param {Object} dict The letter/number dictionary to check for the char
 * @param {string} char The desired character
 */
function charToBraille(dict, char) {
    return Object.keys(dict).find((key) => dict[key] === char);
}

function charsToBraille(input) {
    const brailleNumVals = Object.values(BRAILLE_TO_NUMBER);
    const brailleLetterVals = Object.values(BRAILLE_TO_LETTER);

    let output = "";
    let nextCharType = NONE;
    for (let currentChar of input) {
        if (currentChar === " ") {
            output += BRAILLE_SPACE;
            if (nextCharType === BRAILLE_NUMBER) nextCharType = NONE;
        } else if (
            brailleNumVals.includes(currentChar) &&
            nextCharType !== BRAILLE_NUMBER
        ) {
            //Number follow character
            output += BRAILLE_NUMBER + charToBraille(BRAILLE_TO_NUMBER, currentChar);
            nextCharType = BRAILLE_NUMBER;
        } else if (
            brailleNumVals.includes(currentChar) &&
            nextCharType === BRAILLE_NUMBER
        ) {
            //A character which follows a number braille character
            output += charToBraille(BRAILLE_TO_NUMBER, currentChar);
        } else if (
            currentChar.toUpperCase() === currentChar &&
            brailleLetterVals.includes(currentChar.toLowerCase())
        ) {
            //Uppercase
            output +=
                BRAILLE_CAPITAL +
                charToBraille(BRAILLE_TO_LETTER, currentChar.toLowerCase());
        } else if (brailleLetterVals.includes(currentChar.toLowerCase())) {
            //Lowercase
            output += charToBraille(BRAILLE_TO_LETTER, currentChar.toLowerCase());
        } else {
            //Character doesn't exist
            console.error("Character doesn't exist");
        }
    }

    return output;
}

function brailleToChars(input) {
    if (input.length % 6 !== 0) {
        console.error("Invalid number of characters for braille string");
        process.exit(1);
    }

    let output = "";
    let nextCharType = NONE;
    for (let i = 0; i < input.length; i += 6) {
        const brailleSlice = input.slice(i, i + 6);
        switch (
            brailleSlice //Deal with special characters
        ) {
            case BRAILLE_SPACE:
                output += " ";
                if (nextCharType === BRAILLE_NUMBER) nextCharType = NONE; //Number follows, all following symbols until next space
                break;
            case BRAILLE_CAPITAL:
                nextCharType = BRAILLE_CAPITAL;
                //output += BRAILLE_TO_LETTER(brailleSlice).toUpperCase();
                break;
            case BRAILLE_NUMBER:
                nextCharType = BRAILLE_NUMBER;
                //output += BRAILLE_TO_NUMBER(brailleSlice);
                break;
            default: //normal characters
                if (nextCharType === BRAILLE_CAPITAL) {
                    output += BRAILLE_TO_LETTER[brailleSlice].toUpperCase();
                    nextCharType = NONE;
                } else if (nextCharType === BRAILLE_NUMBER) {
                    output += BRAILLE_TO_NUMBER[brailleSlice];
                } else {
                    //lower case
                    output += BRAILLE_TO_LETTER[brailleSlice];
                }
                break;
        }
    }
    return output;
}

function main() {
    if (process.argv.length === 2) {
        console.error("No argument given");
        process.exit(1);
    }

    let input = process.argv[2];
    if (process.argv.length > 3) {
        //I.e. there are multiple words, combine all args to one string
        for (let i = 3; i < process.argv.length; i++) {
            input += " " + process.argv[i];
        }
    }

    //If string only contains O and . -> it is braille
    const regexBraille = /^[O.]+$/;

    let output = "";
    if (regexBraille.test(input)) {
        //Braille
        output = brailleToChars(input);
    } else {
        //English
        output = charsToBraille(input);
    }
    console.log(output);
}

main();
