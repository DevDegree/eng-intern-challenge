const engToBrailleDict = {
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
    ' ': '......'
};

const brailleToEngDict = Object.fromEntries(Object.entries(engToBrailleDict).map(([k, v]) => [v, k]));

const numToBrailleDict = {
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

const brailleToNumDict = Object.fromEntries(Object.entries(numToBrailleDict).map(([k, v]) => [v, k]));

const capFollows = '.....O';
const numFollows = '.O.OOO';
const space = '......'

let output = [];

const convertBrailleToEnglish = (s) => {
    let numState = false;
    let i = 0;
    while (i + 6 < s.length + 1) {
        let cur = s.substring(i, i + 6);
        if (cur === capFollows) {
            i += 6;
            cur = s.substring(i, i + 6);
            output.push(brailleToEngDict[cur].toUpperCase());
        } else if (cur === numFollows) {
            numState = true;
            i += 6;
            cur = s.substring(i, i + 6);
            output.push(brailleToNumDict[cur]);
        } else if (numState) {
            output.push(brailleToNumDict[cur]);
        } else {
            if (cur === space) numState = false;
            output.push(brailleToEngDict[cur]);
        }
        i += 6;
    }
}

const convertEnglishToBraille = (s) => {
    for (let i = 0; i < s.length; i++) {
        if (/[A-Z]/.test(s[i])) {
            // if uppercase
            output.push(capFollows);
            output.push(engToBrailleDict[s[i].toLowerCase()]);
        } else if (/[0-9]/.test(s[i])) {
            // if number, only add the num follows at the beginning 
            if (!/[0-9]/.test(s[i - 1] ? s[i - 1] : null)) output.push(numFollows);
            output.push(numToBrailleDict[s[i]])
        } else {
            output.push(engToBrailleDict[s[i]]);
        }
    }
}

const engRegex = /^[a-zA-Z0-9 ]+$/;
const isEnglish = (s) => { return engRegex.test(s) };

function translate() {
    const s = process.argv.slice(2).join(' ');

    if (isEnglish(s)) {
        convertEnglishToBraille(s);
    } else {
        convertBrailleToEnglish(s);
    }
    console.log(output.join(''));
}

translate();