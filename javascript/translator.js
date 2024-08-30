const brailleDictionary = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....',
    'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...',
    'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......', 'capital': '.....O', 'number': '.O.OOO',
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....',
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
};

const reverseBrailleDictionary = Object.fromEntries(
    Object.entries(brailleDictionary).map(([key, value]) => [value, key])
);

function textToBraille(text) {
    let result = '';
    let isNumber = false;
    for (const char of text) {
        if (char >= 'A' && char <= 'Z') {
            result += brailleDictionary['capital'] + brailleDictionary[char.toLowerCase()];
        } else if (char >= '0' && char <= '9') {
            if(!isNumber) {
                result += brailleDictionary['number'] + brailleDictionary[char];
                isNumber = true;
            } else {
                result += brailleDictionary[char];
            }
        } else  {
            if(char === ' ') {
                isNumber = false;
            }
            result += brailleDictionary[char];
        }
    }
    return result;
}

function brailleToText(braille) {
    let result = '';
    let i = 0;
    let capitalizeNext = false;
    let isNumber = false;

    while (i < braille.length) {
        const brailleChar = braille.substring(i, i + 6);
        i += 6;

        if (brailleChar === brailleDictionary['capital']) {
            capitalizeNext = true;
        } else if (brailleChar === brailleDictionary['number']) {
            isNumber = true;
        } else if (brailleChar === brailleDictionary[' ']) {
            result += ' ';
            isNumber = false;
        } else {
            let char;
            if (isNumber) {
                char = Object.keys(brailleDictionary).find(key => brailleDictionary[key] === brailleChar && !isNaN(key));
            } else {
                char = reverseBrailleDictionary[brailleChar];
            }

            if (capitalizeNext) {
                char = char.toUpperCase();
                capitalizeNext = false;
            }
            result += char;
        }
    }
    return result;
}

const input = process.argv.slice(2).join(' ');

if (/^[O\.]+$/.test(input)) {
    console.log(brailleToText(input));
} else {
    console.log(textToBraille(input));
}
