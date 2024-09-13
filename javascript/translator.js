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
    ' ': '......',
    'CAP': '.....O', 
    'NUM': '.O.OOO',
    'DEC': '.O...O',
    ',': '.O....',
    ';': '.OO...',
    ':': '.O.O..',
    '.': '.O..O.',
    '!': '.OOO.O',
    '?': '.O.OO.',
    "'": '.O.O..',
    '-': '.OO.O.',
    '(': '.O.OO.',
    ')': '.OOO.O',
    '"': '.OOO.O' 
};

const digitsToBrailleMap = {
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
};

function brailleToEnglish(brailleString) {
    let brailleToEnglishMap = {};
    let brailleToDigitsMap = {};
    
    Object.entries(englishToBrailleMap).forEach(([key, value]) => {
        brailleToEnglishMap[value] = key;
    });

    Object.entries(digitsToBrailleMap).forEach(([key, value]) => {
        brailleToDigitsMap[value] = key;
    });

    let result = [];
    let capitalFollows = false;
    let numberFollows = false;

    const brailleSymbols = [];
    for (let i = 0; i < brailleString.length; i += 6) {
        brailleSymbols.push(brailleString.slice(i, i + 6));
    }

    for (let symbol of brailleSymbols) {
        if (symbol === englishToBrailleMap['CAP']) {
            capitalFollows = true;
            continue;
        }

        if (symbol === englishToBrailleMap['NUM']) {
            numberFollows = true;
            continue;
        }

        if (symbol === englishToBrailleMap[' ']) {
            result.push(' ');
            numberFollows = false;
            continue;
        }

        let translatedChar = '';
        
        if (symbol === englishToBrailleMap['DEC']) {
            translatedChar = '.';
        } else if (numberFollows) {
            translatedChar = brailleToDigitsMap[symbol];
        } else {
            translatedChar = brailleToEnglishMap[symbol]; 
        }

        if (capitalFollows) {
            translatedChar = translatedChar.toUpperCase();
            capitalFollows = false;
        }

        result.push(translatedChar);

        if (numberFollows && !/[0-9]/.test(translatedChar)) {
            numberFollows = false;
        }
    }

    return result.join('');
}

function englishToBraille(englishString) {
    let result = '';
    let isNum = false;

    for (let i = 0; i < englishString.length; i++) {
        let char = englishString[i];

        if (char === ' ') {
            result += englishToBrailleMap[char];
            isNum = false; 
            continue;
        }

        if (char >= 'A' && char <= 'Z') {
            result += englishToBrailleMap['CAP'];
            char = char.toLowerCase();
        }

        if (char >= '0' && char <= '9') {
            if (!isNum) {
                result += englishToBrailleMap['NUM'];
                isNum = true;
            }
            result += digitsToBrailleMap[char];
        } else if (char === '.' && isNum) {
            result += englishToBrailleMap['DEC'];
        } else {
            if (isNum) {
                isNum = false;
            }
            result += englishToBrailleMap[char];
        }
    }

    return result;
}


function isBraille(toTranslate) {
    if (toTranslate.length % 6 !== 0) {
        return false;
    }
    return /^[O.]+$/.test(toTranslate);
}

const args = process.argv.slice(2);
const toTranslate = args.join(' ');

const translateFromBraille = isBraille(toTranslate);

let output = translateFromBraille ? brailleToEnglish(toTranslate) : englishToBraille(toTranslate);

console.log(output);