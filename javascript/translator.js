const brailleDict = {
    a: 'O.....', b: 'O.O...', c: 'OO....', d: 'OO.O..', e: 'O..O..',
    f: 'OOO...', g: 'OOOO..', h: 'O.OO..', i: '.OO...', j: '.OOO..',
    k: 'O...O.', l: 'O.O.O.', m: 'OO..O.', n: 'OO.OO.', o: 'O..OO.',
    p: 'OOO.O.', q: 'OOOOO.', r: 'O.OOO.', s: '.OO.O.', t: '.OOOO.',
    u: 'O...OO', v: 'O.O.OO', w: '.OOO.O', x: 'OO..OO', y: 'OO.OOO',
    z: 'O..OOO',
    1: 'O.....', 2: 'O.O...', 3: 'OO....', 4: 'OO.O..', 5: 'O..O..',
    6: 'OOO...', 7: 'OOOO..', 8: 'O.OO..', 9: '.OO...', 0: '.OOO..',
    capital: '.....O', number: '.O.OOO', '.': '..OO.O', ',': '..O...',
    '?': '..O.OO', '!': '..OOO.', ':': '..OO..', ';': '..O.O.',
    '-': '....OO', '/': '.O..O.', '(': 'O.O..O', ')': '.O.OO.',
    ' ': '......'
};

const brailleToEngDict = Object.fromEntries(
    Object.entries(brailleDict).map(([key, value]) => [value, key])
);

function engToBraille(input) {
    let output = '';
    let isNum = false;

    for (let char of input) {
        if (!isNaN(char) && char !== ' ') {
            if (!isNum) {
                output += brailleDict.number;
                isNum = true;
            }
            output += brailleDict[char];
        } else {
            if (char === char.toUpperCase() && char !== ' ') {
                output += brailleDict.capital;
            }
            output += brailleDict[char.toLowerCase()] || '';
            isNum = false;
        }
    }

    return output;
}

function brailleToEng(input) {
    let output = '';
    const chunks = input.match(/.{6}/g) || [];
    let isCap = false;
    let isNum = false;

    for (let chunk of chunks) {
        if (chunk === brailleDict.capital) {
            isCap = true;
            continue;
        }
        if (chunk === brailleDict.number) {
            isNum = true;
            continue;
        }
        if (chunk === brailleDict[' ']) {
            output += ' ';
            isNum = false;
            continue;
        }

        let engChar = brailleToEngDict[chunk];
        if (isCap) {
            engChar = engChar ? engChar.toUpperCase() : '';
            isCap = false;
        }
        if (isNum) {
            engChar = Object.entries(brailleDict).find(([key, value]) => 
                value === chunk && !isNaN(key))?.[0] || '';
        }

        output += engChar || '';
    }

    return output;
}

function checkLang(input) {
    return input.match(/^[.O\s]*$/) ? 'braille' : 'eng';
}

function translate(input) {
    const type = checkLang(input);
    return type === 'braille' ? brailleToEng(input) : engToBraille(input);
}

const userInput = process.argv.slice(2).join(' ');
console.log(translate(userInput));