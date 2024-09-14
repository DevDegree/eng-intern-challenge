const input = process.argv.slice(2).join(' ');

const brailleDictionary = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',

    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',

    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', 
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.',

    'capital': '.....O',
    'number': '.O.OOO', 
    'decimal': '.O...O', 
    'space': '......'
};

function braille(input){
    if (/^[O. ]+$/.test(input)){
        brailleToText(input);
    } else {
        textToBraille(input);
    }
}

const reverseBrailleDictionary = Object.fromEntries(
    Object.entries(brailleDictionary).map(([key, value]) => [value, key])
);

function brailleToText(brailleInput) {
    let output = '';
    let currentSymbol = '';
    let isCapital = false;
    let isNumber = false;

    for (let i = 0; i < brailleInput.length; i += 6) {
        currentSymbol = brailleInput.slice(i, i + 6);

        if (currentSymbol === brailleDictionary['capital']) {
            isCapital = true;
            continue;
        }

        if (currentSymbol === brailleDictionary['number']) {
            isNumber = true;
            continue;
        }

        if (isNumber && currentSymbol === brailleDictionary['space']) {
            isNumber = false;
            output += ' ';
            continue;
        }

        let translatedChar = reverseBrailleDictionary[currentSymbol];

        if (translatedChar === 'space') {
            output += ' ';
        } else {
            if (isNumber) {
                translatedChar = translatedChar === 'a' ? '1' : translatedChar;
                translatedChar = translatedChar === 'b' ? '2' : translatedChar;
                translatedChar = translatedChar === 'c' ? '3' : translatedChar;
                translatedChar = translatedChar === 'd' ? '4' : translatedChar;
                translatedChar = translatedChar === 'e' ? '5' : translatedChar;
                translatedChar = translatedChar === 'f' ? '6' : translatedChar;
                translatedChar = translatedChar === 'g' ? '7' : translatedChar;
                translatedChar = translatedChar === 'h' ? '8' : translatedChar;
                translatedChar = translatedChar === 'i' ? '9' : translatedChar;
                translatedChar = translatedChar === 'j' ? '0' : translatedChar;
            }
            if (isCapital) {
                translatedChar = translatedChar.toUpperCase();
                isCapital = false;
            }
            output += translatedChar;
        }
    }

    console.log(output);
}

function textToBraille(input) {
    let output = '';
    let isNum = false;

    for (const char of input) {
        if (!isNaN(char) && char !== ' ') {
            if(!isNum){
                output += brailleDictionary['number'];
                isNum = true;
            }
            output += brailleDictionary[char];
        } else if (char === ' ') {
            output += brailleDictionary['space'];
            isNum == false;
        }
        else if (char === '.') {
            output += brailleDictionary['decimal'];
            isNum == false;
        } else if (char === char.toUpperCase()) {
            output += brailleDictionary['capital'] + brailleDictionary[char.toLowerCase()];
            isNum == false;
        } else {
            output += brailleDictionary[char];
        }
    }
    console.log(output)
}


braille(input);
