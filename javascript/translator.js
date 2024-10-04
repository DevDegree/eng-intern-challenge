//Object stores Alphabet
const brailleAlphabet = {
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
    'z': 'O..OOO'
  }
//Object stores Numbers
const brailleNumbers = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
  }

//Object stores special symbols
const brailleSpecial = {
    capital: '.....O',
    number: '.O.OOO',
    ' ': '......'
}

//Translate English to Braille
function EtoB(input) {
    let result = '';
    let numberMode = false;

    for (let i = 0; i < input.length; i++) {
        const a = input[i];

        //Normal Letters
        if (a >= 'a' && a <= 'z') {
            result += brailleAlphabet[a];
            continue;
        }

        //Capital Letters
        if (a >= 'A' && a <= 'Z') {
            result += brailleSpecial.capital;
            result += brailleAlphabet[a.toLowerCase()];
            continue;
        }

        //Numbers
        if (a >= '0' && a <= '9') {
            if (!numberMode) {
                numberMode = true;
                result += brailleSpecial.number;
                result += brailleNumbers[a];
                continue;
            } else result += brailleNumbers[a];
            continue;
        }

        //Space
        if (a == ' ') {
            if (numberMode) {
                numberMode = false;
            }
            result += brailleSpecial[a];
            continue;
        }
    }
    return result;
}

function BtoE (input) {
    let capitalMode = false;
    let numberMode = false;
    let result = '';

    for (let i = 0; i < input.length; i+=6) {
        const a = input.slice(i, i+6);

        //Check if Capital or Number
        if (a === brailleSpecial.capital) {
            capitalMode = true;
            continue;
        }  else if (a === brailleSpecial.number) {
            numberMode = true;
            continue;
        }

        //Space
        if (a === brailleSpecial[' ']) {
            if (numberMode) {
                numberMode = false;
            }
            for (let key in brailleSpecial) {
                if (brailleSpecial[key] === a) {
                    result += key;
                    break;
                }
            }
            continue;
        }

        //Numbers
        if (numberMode) {
            for (let key in brailleNumbers) {
                if (brailleNumbers[key] === a) {
                    result += key;
                    break;
                }
            }
            continue;
        }

        //Capital letter
        if (capitalMode) {
            for (let key in brailleAlphabet) {
                if (brailleAlphabet[key] === a) {
                    result += key.toUpperCase();
                    break;
                }
            }
            capitalMode = false;
            continue;
        }

        //Normal Letter
        if (!capitalMode) {
            for (let key in brailleAlphabet) {
                if (brailleAlphabet[key] === a) {
                    result += key;
                    break;
                }
            }
            continue;
        }

    }
    return result;
}

//Detect Language
function dectecLanguage (input) {
    const validChar = /^[O.]+$/;
    if (validChar.test(input) && (input.length % 6) == 0) {
        return 'Braille';
    } else return 'English';
}

let input = process.argv.slice(2).join(" ");

const language = dectecLanguage(input);
    
if (language == 'English') {
        console.log(EtoB(input));
} else if (language == 'Braille') {
        console.log(BtoE(input));
    }