const brailleSymbols = {
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
    ' ': '......',

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
};

const charCategories = {
    LowerCase: 'LowerCase',
    UpperCase: 'UpperCase',
    Digit: 'Digit',
    Blank: 'Blank',
    Other: 'Other',
};

const identifyCharType = char => {
    if (/[a-z]/.test(char)) {
        return charCategories.LowerCase;
    } else if (/[A-Z]/.test(char)) {
        return charCategories.UpperCase;
    } else if (/[0-9]/.test(char)) {
        return charCategories.Digit;
    } else if (/[ ]/.test(char)) {
        return charCategories.Blank;
    } else {
        return charCategories.Other;
    }
};

const isBrailleInput = input => {
    return /^[O.]+$/.test(input);
};

const findBrailleKey = (brailleCode, isNumContext) => {
    if (isNumContext) {
        return Object.keys(brailleSymbols).find(key => brailleSymbols[key] === brailleCode && !isNaN(key));
    } else {
        return Object.keys(brailleSymbols).find(key => brailleSymbols[key] === brailleCode && isNaN(parseInt(key)));
    }
};

const brailleToText = brailleStr => {
    let isUpper = false;
    let isNumberContext = false;
    let output = '';

    for (let i = 0; i < brailleStr.length; i += 6) {
        const brailleChar = brailleStr.substr(i, 6);
        const charKey = findBrailleKey(brailleChar, isNumberContext);

        if (charKey.length === 1) {
            if (charKey === ' ') {
                isNumberContext = false;
                output += charKey;
                continue;
            }
            output += isUpper ? charKey.toUpperCase() : charKey;
            isUpper = false;
        } else if (charKey === 'capital') {
            isUpper = true;
        } else if (charKey === 'number') {
            isNumberContext = true;
        }
    }
    return output;
};

const textToBraille = inputStr => {
    let brailleOutput = '';
    let isNumberActive = false;

    for (let char of inputStr) {
        const charCategory = identifyCharType(char);

        switch (charCategory) {
            case charCategories.LowerCase:
                brailleOutput += brailleSymbols[char];
                break;
            case charCategories.UpperCase:
                brailleOutput += brailleSymbols.capital;
                brailleOutput += brailleSymbols[char.toLowerCase()];
                break;
            case charCategories.Digit:
                if (!isNumberActive) {
                    isNumberActive = true;
                    brailleOutput += brailleSymbols.number;
                }
                brailleOutput += brailleSymbols[char];
                break;
            case charCategories.Blank:
                brailleOutput += brailleSymbols[' '];
                isNumberActive = false;
                break;
            case charCategories.Other:
                brailleOutput += brailleSymbols[char];
                break;
        }
    }

    return brailleOutput;
};

const mainTranslation = input => {
    if (isBrailleInput(input)) {
        console.log(brailleToText(input));
    } else {
        console.log(textToBraille(input));
    }
};

const inputArgument = process.argv.slice(2).join(' ');
mainTranslation(inputArgument);
