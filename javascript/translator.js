const englishToBrailleMap = {
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
    'capital start': '.....O',
    'number start': '.O.OOO',
    'space': '......'
};

const brailleToEnglishMap = {
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
    'O.....N': '1',
    'O.O...N': '2',
    'OO....N': '3',
    'OO.O..N': '4',
    'O..O..N': '5',
    'OOO...N': '6',
    'OOOO..N': '7',
    'O.OO..N': '8',
    '.OO...N': '9',
    '.OOO..N': '0',
    '.....O': 'capital start',
    '.O.OOO': 'number start',
    '......': 'space'
};

//Func to convert Braille to English
function brailleToEnglish(braille) {
    let text = "";
    let numberMode = false;
    let capitalMode = false;

    for (let i = 0; i < braille.length; i += 6) {
        const brailleChar = braille.substring(i, i + 6);

        switch (brailleToEnglishMap[brailleChar]) {
            case 'number start':
                numberMode = true;
                continue;
            case 'capital start':
                capitalMode = true;
                continue;
            case 'space':
                text += " ";
                numberMode = false;
                continue;
            default:
                let char = brailleToEnglishMap[brailleChar];
                if (capitalMode) {
                    char = char.toUpperCase();
                    capitalMode = false;
                }
                if (numberMode) {
                    char = brailleToEnglishMap[brailleChar + 'N'];
                }
                text += char;
        }
    }

    return text;
}

//Func to convert English to Braille
function englishToBraille(english) {
    let braille = "";
    let numberMode = false;

    for (let char of english) {
        if (char.match(/[0-9]/) && !numberMode) {
            braille += englishToBrailleMap['number start'];
            numberMode = true;
        } else if (char.match(/[A-Z]/)) {
            braille += englishToBrailleMap['capital start'];
            char = char.toLowerCase();
        }

        if (char === " ") {
            braille += englishToBrailleMap['space'];
            numberMode = false; //Exiting number mode
        } else {
            braille += englishToBrailleMap[char];
        }
    }

    return braille;
}


function main() {
    const input = process.argv.slice(2).join(" ");

    if (/^[O.]+$/.test(input)) { // Checking if it is braile or not
        console.log(brailleToEnglish(input));
    } else {
        console.log(englishToBraille(input));
    }
}


main();
