import {
    assert,
    getObjectKeyByValue,
    isBraille,
    isCapitalLetter,
    isDigit,
} from './utils';

const CAPITAL_FOLLOWS = 'CAPITAL_FOLLOWS';
const NUMBER_FOLLOWS = 'NUMBER_FOLLOWS';

const brailleAlphabetMap: Record<string, string> = {
    a: 'O.....',
    b: 'O.O...',
    c: 'OO....',
    d: 'OO.O..',
    e: 'O..O..',
    f: 'OOO...',
    g: 'OOOO..',
    h: 'O.OO..',
    i: '.OO...',
    j: '.OOO..',
    k: 'O...O.',
    l: 'O.O.O.',
    m: 'OO..O.',
    n: 'OO.OO.',
    o: 'O..OO.',
    p: 'OOO.O.',
    q: 'OOOOO.',
    r: 'O.OOO.',
    s: '.OO.O.',
    t: '.OOOO.',
    u: 'O...OO',
    v: 'O.O.OO',
    w: '.OOO.O',
    x: 'OO..OO',
    y: 'OO.OOO',
    z: 'O..OOO',
    ' ': '......',
    [CAPITAL_FOLLOWS]: '.....O',
    [NUMBER_FOLLOWS]: '.O.OOO',
};

const brailleNumberMap: Record<string, string> = {
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
    ' ': '......',
};

function translateEnglishToBraille(englishText: string) {
    let output = '';
    let numberFollows = false;

    for (let char of englishText) {
        if (isCapitalLetter(char)) {
            output += brailleAlphabetMap[CAPITAL_FOLLOWS];
            char = char.toLowerCase();
        }

        if (isDigit(char) && !numberFollows) {
            output += brailleAlphabetMap[NUMBER_FOLLOWS];
            numberFollows = true;
        }

        if (char === ' ') {
            numberFollows = false;
        }

        const alphabet = numberFollows ? brailleNumberMap : brailleAlphabetMap;
        assert(char in alphabet, `Unexpected english character: "${char}"`);
        output += alphabet[char];
    }

    return output;
}

function translateBrailleToEnglish(brailleText: string) {
    let output = '';
    let numberFollows = false;
    let capitalFollows = false;

    for (let i = 0; i < brailleText.length; i += 6) {
        const brailleChar = brailleText.slice(i, i + 6);

        const char = numberFollows
            ? getObjectKeyByValue(brailleNumberMap, brailleChar)
            : getObjectKeyByValue(brailleAlphabetMap, brailleChar);
        assert(char, `Unexpected braille character: "${brailleChar}"`);

        if (char === NUMBER_FOLLOWS) {
            numberFollows = true;
            continue;
        }

        if (char === CAPITAL_FOLLOWS) {
            capitalFollows = true;
            continue;
        }

        if (capitalFollows) {
            capitalFollows = false;
            output += char.toUpperCase();
            continue;
        }

        if (numberFollows) {
            output += char;
            continue;
        }
        if (char === ' ') {
            numberFollows = false;
        }
        output += char;
    }

    return output;
}

export function translate(text: string) {
    return isBraille(text)
        ? translateBrailleToEnglish(text)
        : translateEnglishToBraille(text);
}

const input = process.argv.slice(2).join(' ');
const output = translate(input);
console.log(output);
