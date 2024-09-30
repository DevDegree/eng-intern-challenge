//CONSTANTS

// Key-value pair where the 6 char braile string is the key to the letter value
// Must check for special chars (capital, decimal before). This is  a lot quicker than regex
const BRAILE_TO_LETTER = {
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
const BRAILE_TO_NUMBER = {
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

const BRAILE_SPACE = "......";
const BRAILE_CAPITAL = ".....O";
const BRAILE_NUMBER = ".O.OOO";
const NONE = ""; //Used for char follows checking

//FUNCTIONS
/**
 * Returns the braile value of a given character
 * @param {Object} dict The letter/number dictionary to check for the char
 * @param {string} char The desired character
 */
function charToBraile(dict, char) {
    return Object.keys(dict).find((key) => dict[key] === char);
}

function charsToBraile(input) {
    const braileNumVals = Object.values(BRAILE_TO_NUMBER);
    const braileLetterVals = Object.values(BRAILE_TO_LETTER);

    let output = "";
    let nextCharType = NONE;
    for (let currentChar of input) {
        if (currentChar === " ") {
            output += BRAILE_SPACE;
            if (nextCharType === BRAILE_NUMBER) nextCharType = NONE;
        } else if (
            braileNumVals.includes(currentChar) &&
            nextCharType !== BRAILE_NUMBER
        ) {
            //Number follow character
            output += BRAILE_NUMBER + charToBraile(BRAILE_TO_NUMBER, currentChar);
            nextCharType = BRAILE_NUMBER;
        } else if (
            braileNumVals.includes(currentChar) &&
            nextCharType === BRAILE_NUMBER
        ) {
            //A character which follows a number braile character
            output += charToBraile(BRAILE_TO_NUMBER, currentChar);
        } else if (
            currentChar.toUpperCase() === currentChar &&
            braileLetterVals.includes(currentChar.toLowerCase())
        ) {
            //Uppercase
            output +=
                BRAILE_CAPITAL +
                charToBraile(BRAILE_TO_LETTER, currentChar.toLowerCase());
        } else if (braileLetterVals.includes(currentChar.toLowerCase())) {
            //Lowercase
            output += charToBraile(BRAILE_TO_LETTER, currentChar.toLowerCase());
        } else {
            //Character doesn't exist
            console.error("Character doesn't exist");
        }
    }

    return output;
}

function braileToChars(input) {
    if (input.length % 6 !== 0) {
        console.error("Invalid number of characters for braile string");
        process.exit(1);
    }

    let output = "";
    let nextCharType = NONE;
    for (let i = 0; i < input.length; i += 6) {
        const braileSlice = input.slice(i, i + 6);
        switch (
            braileSlice //Deal with special characters
        ) {
            case BRAILE_SPACE:
                output += " ";
                if (nextCharType === BRAILE_NUMBER) nextCharType = NONE; //Number follows, all following symbols until next space
                break;
            case BRAILE_CAPITAL:
                nextCharType = BRAILE_CAPITAL;
                //output += BRAILE_TO_LETTER(braileSlice).toUpperCase();
                break;
            case BRAILE_NUMBER:
                nextCharType = BRAILE_NUMBER;
                //output += BRAILE_TO_NUMBER(braileSlice);
                break;
            default: //normal characters
                if (nextCharType === BRAILE_CAPITAL) {
                    output += BRAILE_TO_LETTER[braileSlice].toUpperCase();
                    nextCharType = NONE;
                } else if (nextCharType === BRAILE_NUMBER) {
                    output += BRAILE_TO_NUMBER[braileSlice];
                } else {
                    //lower case
                    output += BRAILE_TO_LETTER[braileSlice];
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

    //If string only contains O and . -> it is braile
    const regexBraile = /^[O.]+$/;

    let output = "";
    if (regexBraile.test(input)) {
        //Braile
        output = braileToChars(input);
    } else {
        //English
        output = charsToBraile(input);
    }
    console.log(output);
}

main();
