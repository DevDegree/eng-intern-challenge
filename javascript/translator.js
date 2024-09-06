// This program assumes all inputs are valid.
// Possible invalid situations:
// - Braille input is invalid:
//     - length not divisible by 6
//     - group of 6 characters does not correspond to a valid Braille character
//     - "capital follows" character not followed by a letter
//     - "number follows" character not followed by a number
//     - numbers not terminated by a space
// - English input is invalid:
//     - input contains unsupported characters
//     - numbers not terminated by a space

const CAPITAL_FOLLOWS = ".....O"
const NUMBER_FOLLOWS = ".O.OOO"
const DECODE_LETTERS = {
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
    "......": " "
}
const ENCODE_LETTERS = {};
for (const key in DECODE_LETTERS) {
    ENCODE_LETTERS[DECODE_LETTERS[key]] = key;
}
const DECODE_NUMBERS = {
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
    "......": " "
}
const ENCODE_NUMBERS = {};
for (const key in DECODE_NUMBERS) {
    ENCODE_NUMBERS[DECODE_NUMBERS[key]] = key;
}

function decode(braille) {
    english = "";
    isCapitalFollows = false;
    isNumberFollows = false;
    for (let i = 0 ; i < braille.length ; i += 6) {
        symbol = braille.substr(i, 6);
        if (symbol == CAPITAL_FOLLOWS) {
            isCapitalFollows = true;
            continue;
        }
        if (symbol == NUMBER_FOLLOWS) {
            isNumberFollows = true;
            continue;
        }
        if (isNumberFollows) {
            translation = DECODE_NUMBERS[symbol];
            if (translation == " ") {
                isNumberFollows = false;
            }
        } else {
            translation = DECODE_LETTERS[symbol];
            if (isCapitalFollows) {
                translation = translation.toUpperCase();
                isCapitalFollows = false;
            }
        }
        english += translation;
    }
    return english;
}

function encodeWord(word) {
    braille = "";
    isNumberFollows = false;
    for (let j = 0 ; j < word.length ; j++) {
        c = word.substr(j, 1);
        if (c >= '0' && c <= '9') {
            if (!isNumberFollows) {
                braille += NUMBER_FOLLOWS;
                isNumberFollows = true;
            }
            braille += ENCODE_NUMBERS[c];
        } else if (c == ' ') { 
            isNumberFollows = false;
            braille += ENCODE_LETTERS[c];
        } else if (c >= 'a' && c <= 'z') {
            braille += ENCODE_LETTERS[c];
        } else {
            braille += CAPITAL_FOLLOWS;
            braille += ENCODE_LETTERS[c.toLowerCase()];
        }
    }
    return braille;
}

function encode(words) {
    braille = "";
    for (let i in words) {
        if (i != 0) {
            braille += ENCODE_LETTERS[" "];
        }
        braille += encodeWord(words[i]);
    }
    return braille;
}

function main(argv) {
    // all braille characters contain at least one '.', and English alphabet does not contain '.'
    if (argv.length == 1 && argv[0].indexOf('.') >= 0) {
        console.log(decode(argv[0]));
    } else {
        console.log(encode(argv));
    }
}

main(process.argv.slice(2));