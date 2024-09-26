const ALPHABET = {
    "English": {
        'a': 'O.....',
        'b': 'O.O...',
        'c': 'OO....',
        'd': 'OO.O..',
        'e': 'O..O..',
        'f': 'OOO...',
        'g': 'OOOO..',
        'h': 'O.OO..',
        'i': '.OO...',
        'j': '.OOO..',
        'k': 'O...O.',
        'l': 'O.O.O.',
        'm': 'OO..O.',
        'n': 'OO.OO.',
        'o': 'O..OO.',
        'p': 'OOO.O.',
        'q': 'OOOOO.',
        'r': 'O.OOO.',
        's': '.OO.O.',
        't': '.OOOO.',
        'u': 'O...OO',
        'v': 'O.O.OO',
        'w': '.OOO.O',
        'x': 'OO..OO',
        'y': 'OO.OOO',
        'z': 'O..OOO',

        '1': 'O.....',
        '2': 'O.O...',
        '3': 'OO....',
        '4': 'OO.O..',
        '5': 'O..O..',
        '6': 'OOO...',
        '7': 'OOOO..',
        '8': 'O.OO..',
        '9': '.OO...',
        '0': '.OOO..',

        'capital': '.....O',
        'decimal': '.O...O',
        'number': '.O.OOO',
        'space': '......',

        '.': '..OO.O',
        ',': '..O...',
        '?': '..O.OO',
        '!': '..OOO.',
        ':': '..OO..',
        ';': '..O.O.',
        '-': '....OO',
        '/': '.O..O.',
        '<': '.OO..O',
        '>': 'O..OO.',
        '(': 'O.O..O',
        ')': '.O.OO.',
    },
    "Braille": {
        'O.....': 'a',
        'O.O...': 'b',
        'OO....': 'c',
        'OO.O..': 'd',
        'O..O..': 'e',
        'OOO...': 'f',
        'OOOO..': 'g',
        'O.OO..': 'h',
        '.OO...': 'i',
        '.OOO..': 'j',
        'O...O.': 'k',
        'O.O.O.': 'l',
        'OO..O.': 'm',
        'OO.OO.': 'n',
        'O..OO.': 'o',
        'OOO.O.': 'p',
        'OOOOO.': 'q',
        'O.OOO.': 'r',
        '.OO.O.': 's',
        '.OOOO.': 't',
        'O...OO': 'u',
        'O.O.OO': 'v',
        '.OOO.O': 'w',
        'OO..OO': 'x',
        'OO.OOO': 'y',
        'O..OOO': 'z',

        '.....O': 'capital',
        '.O...O': 'decimal',
        '.O.OOO': 'number',
        '......': 'space',

    }
}

const BRAILLE_NUMBERS = {
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
}

const COMMAND_LINE_ARGS = process.argv.slice(2); //Drop first two arguments (not needed)
const MESSAGE = COMMAND_LINE_ARGS.join(' ');
const LANGUAGE = CheckLanguage(MESSAGE);

let translation = "";
let splitMessage = [];
let isNumberFlagged = false;
let isCapitalFlagged = false;

//Split the received message into the proper amount of elements based on the language
if (LANGUAGE === 'English') {
    splitMessage = MESSAGE.split('');
} else { //Groups every 6 characters
    splitMessage = MESSAGE.match(/.{1,6}/g) || [];
}

//Translate the message
for (let i = 0; i < splitMessage.length; i++) {
    const currentChar = splitMessage[i];

    if (LANGUAGE === 'English') {

        //Space -> also resets number flag
        if (currentChar === " ") {
            translation += ALPHABET[LANGUAGE]["space"];
            isNumberFlagged = false;
            continue;
        }

        //Letters ->
        if (isNaN(currentChar)) {
            if (currentChar === splitMessage[i].toUpperCase()) { //Letter is capitalized
                translation += ALPHABET[LANGUAGE]["capital"];
                translation += ALPHABET[LANGUAGE][currentChar.toLowerCase()];
            } else if (currentChar !== currentChar.toUpperCase()) { //Letter is not capitalized
                translation += ALPHABET[LANGUAGE][currentChar];
            }

            continue;
        }

        //Numbers ->
        if (!isNumberFlagged) {
            translation += ALPHABET[LANGUAGE]["number"];
            isNumberFlagged = true;
        }

        translation += ALPHABET[LANGUAGE][currentChar]; //Number

    } else { //Braille

        //Space -> also resets number flag
        if (ALPHABET[LANGUAGE][currentChar] === 'space') {
            translation += " ";
            isNumberFlagged = false;
            continue;
        }

        //Letters ->
        if (ALPHABET[LANGUAGE][currentChar] === 'capital' && !isCapitalFlagged) { //Flag next letter as capitalized
            isCapitalFlagged = true;
            continue;
        } else if (isCapitalFlagged) {
            translation += ALPHABET[LANGUAGE][currentChar].toUpperCase();
            isCapitalFlagged = false;
            continue;
        }

        //Numbers ->
        if (ALPHABET[LANGUAGE][currentChar] === 'number') {
            isNumberFlagged = true;
            continue;
        } else if (isNumberFlagged) {
            translation += BRAILLE_NUMBERS[currentChar];
            continue;
        }

        translation += ALPHABET[LANGUAGE][currentChar]; //Remaining lower case letters

    }
}

//Remove all . and O from msgArray, if array is empty then it's Braille
function CheckLanguage(msgToCheck) {
    msgToCheck = msgToCheck.split('').filter(char => char !== '.' && char !== 'O');
    return msgToCheck.length > 0 ? 'English' : 'Braille';
}

//Log the translation
console.log(translation);