const brailleToEnglish = {
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
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '?',
    '..OOO.': '!',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.O..O.': '/',
    '.OO..O': '<',
    'O.O..O': '(',
    '.O.OO.': ')',
    '......': ' '
};

const specialMeans = {
    '.....O': '',
    '.O...O': '',   //decimal
    '.O.OOO': ''    //num
}

const brailleToNumber = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0'
};

function slice(str, len) {
    let arr = [];

    for (let i = 0; i < str.length; i += len) {
        arr.push(str.substring(i, i + len));
    }

    return arr
}



function brailleToEnglishTranslator(brailleInput) {
    let chars = slice(brailleInput, 6)
    let englishOutput = '';
    let isNum = false;
    let isCapital = false;
    let isDecimal = false;
    for (let index = 0; index < chars.length; index++) {

        const element = chars[index];

        if (element === '.....O') {
            isCapital = true;
            continue;
        }
        else if (element === '.O.OOO') {
            isNum = true;
            continue;
        }
        else if (element === '.O...O') {
            isDecimal = true;
            englishOutput += `.`
            continue;
        }
        else if (element === '......') {
            isDecimal = false
            isNum = false
            englishOutput += ` `
            continue;
        }

        let englishChar = '';

        if (isNum || isDecimal) {
            englishChar = brailleToNumber[element];
            englishOutput += englishChar
            isDecimal = false;
        } else {
            englishChar = brailleToEnglish[element];
            if (isCapital) {
                englishChar = englishChar.toUpperCase(); 
                isCapital = false;
            }
            englishOutput += englishChar
        }


    }


    return englishOutput


}



function getKeyByValue(obj, value) {
    return Object.keys(obj).find(key => obj[key] === value);
}



function englishToBraille(englishInput) {
    let chars = englishInput.split('');
    let brailleOutput = '';
    let isNum = false;
    let isCapital = false;
    let isDecimal = false;
    for (let index = 0; index < chars.length; index++) {

        const element = chars[index];


        if (Number(element) && !isDecimal) {
            isNum = true;
            brailleOutput += ".O.OOO";
            // continue;
        }
        else if (/[A-Z]/.test(element)) {
            // isCapital = true;
            brailleOutput += ".....O";
            // continue;
        }
        else if (element === '.' && Number(chars[index + 1])) {
            isDecimal = true;
            brailleOutput += ".O...O";
            continue;
        }
        else if (element === ` `) {
            isDecimal = false;
            isNum = false
            brailleOutput += "......";
            continue;
        }

        let brailleChar = '';

        if (isNum || isDecimal) {
            brailleChar = getKeyByValue(brailleToNumber, element);
            brailleOutput += brailleChar;
            // isNum = false;
        } else {
            brailleChar = getKeyByValue(brailleToEnglish, element.toLowerCase());
            brailleOutput += brailleChar;
        }
    }
    return brailleOutput
}

function isBrailleString(input) {
    
    const brailleCharacters = [
        'O.....', 'O.O...', 'OO....', 'OO.O..', 'O..O..',
        'OOO...', 'OOOO..', 'O.OO..', '.OO...', '.OOO..',
        'O...O.', 'O.O.O.', 'OO..O.', 'OO.OO.', 'O..OO.',
        'OOO.O.', 'OOOOO.', 'O.OOO.', '.OO.O.', '.OOOO.',
        'O...OO', 'O.O.OO', '.OOO.O', 'OO..OO', 'OO.OOO',
        'O..OOO', '..OO.O', '..O...', '..O.OO', '..OOO.',
        '..OO..', '..O.O.', '....OO', '.O..O.', '.OO..O',
        'O..OO.', 'O.O..O', '.O.OO.', '......', '.....O',
        '.O...O', '.O.OOO'
    ];

    const brailleSet = new Set(brailleCharacters);

    if (input.length % 6 !== 0) {
        return false; 
    }

    for (let i = 0; i < input.length; i += 6) {
        const char = input.slice(i, i + 6);
        if (!brailleSet.has(char)) {
            return false; 
        }
    }

    return true; 
}

function solution(str) {
    if (isBrailleString(str)) {
        return brailleToEnglishTranslator(str);
    } else {
        return englishToBraille(str);
    }
}

console.log(solution(""));
