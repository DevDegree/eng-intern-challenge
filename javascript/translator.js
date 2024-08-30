// Braille dataset
const brailleLetters = {
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
}

const brailleNumbers = {
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
}

const checks = {
    ".....O": "capital",
    ".O...O": "decimal",
    ".O.OOO": "number"
}

const special = {
    "..OO.O": '.',
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "O..OO.": ">",
    "O.O..O": "(",
    ".O.OO.": ")"
}

// Check to see if input is in braille
function isBraille(str) {
    return /^[.O]*$/.test(str);
}

// Check if input is a letter
function isLetter(char) {
    return /^[a-zA-Z]$/.test(char);
}

// check if an input is capitalized
function isCapital(char) {
    return /^[A-Z]$/.test(char);
}

// check if an input is a number
function isNumber(char) {
    return /^[0-9]$/.test(char);
}

// Stores final result
let result = "";

// Converts braille to alphanumerics
function braille2Alpha(input) {
    let braille = "";
    let numSwitch = false;
    let capitalize = false;


    for (let i = 0; i < input.length; i++) {
        braille += input[i];
        if ((i + 1) % 6 == 0) {


            if (braille == "......") {
                result += " ";
                if (numSwitch) numSwitch = false;
            }
            else {
                if (checks[braille]) {
                    switch (checks[braille]) {
                        case "capital":
                            capitalize = true;
                            numSwitch = false;
                            break;
                        case "number":
                            numSwitch = true;
                            break;
                        case "decimal":
                            isDecimal = true;
                            numSwitch = true;
                            break;
                    }
                }
                else {
                    if (brailleLetters[braille] && !numSwitch) {
                        str = brailleLetters[braille];
                        if (capitalize) str = str.toUpperCase();
                        result += str;
                        capitalize = false;
                    }
                    else if (brailleNumbers[braille]) {
                        result += brailleNumbers[braille];
                    }
                    else {
                        result += special[braille];
                    }
                }
            }
            braille = ""
        }
    }
}


// Converts alphanumerics to braille
function alpha2Braille(input) {
    let prevCheck = false; // If false prev wasn't a number
    for (let char of input) {
        if (isLetter(char)) {
            prevCheck = false;
            if (isCapital(char)) {
                result += Object.keys(checks)[0];
                result += Object.keys(brailleLetters)[char.charCodeAt(0) - 'A'.charCodeAt(0)];
            }
            else result += Object.keys(brailleLetters)[char.charCodeAt(0) - 'a'.charCodeAt(0)];
        }
        else if (isNumber(char)) {

            if (!prevCheck) {
                result += Object.keys(checks)[2];
                prevCheck = true;
            }
            result += Object.keys(brailleNumbers)[char.charCodeAt(0) - '1'.charCodeAt(0)];
        }
        else {
            switch (char) {
                case '.':
                    result += Object.keys(special)[0];
                    break;
                case ',':
                    result += Object.keys(special)[1];
                    break;
                case '?':
                    result += Object.keys(special)[2];
                    break;
                case '!':
                    result += Object.keys(special)[3];
                    break;
                case ':':
                    result += Object.keys(special)[4];
                    break;
                case ';':
                    result += Object.keys(special)[5];
                    break;
                case '-':
                    result += Object.keys(special)[6];
                    break;
                case '/':
                    result += Object.keys(special)[7];
                    break;
                case '<':
                    result += Object.keys(special)[8];
                    break;
                case '>':
                    result += Object.keys(special)[9];
                    break;
                case '(':
                    result += Object.keys(special)[10];
                    break;
                case ')':
                    result += Object.keys(special)[11];
                    break;
                case ' ':
                    result += "......";
                    break;
            }
        }
    }
}

// Command line arguments
let input = process.argv.slice(2).join(' ');

if (isBraille(input)) {
    braille2Alpha(input);
}
else {
    alpha2Braille(input);
}

// Output
console.log(result);
