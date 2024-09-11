// Constants
const englishToBraille: { [key: string]: string } = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO'
};

const brailleToEnglish: { [key: string]: string } = Object.fromEntries(
    Object.entries(englishToBraille).map(([key, value]) => [value, key])
);

const numberToBraille: { [key: string]: string } = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
};

const otherToBraille: { [key: string]: string } = {
    'space': '......', 'capitalize': '.....O', 'number': '.O.OOO'
}


// Functions
function translateToBraille(input: string): string {
    let result = '';
    let isNumber = false;

    for (let i = 0; i < input.length; i++) {
        const char = input[i].toLowerCase();

        if (/[a-z]/.test(char)) {
            if (input[i] !== char) {
                result += otherToBraille['capitalize'];
            }
            result += englishToBraille[char];
        } else if (/[0-9]/.test(char)) {
            if (!isNumber) {
                result += otherToBraille['number'];
                isNumber = true;
            }
            result += numberToBraille[char];
        } else if (char === ' ') {
            result += otherToBraille['space'];
            isNumber = false;
        }
    }

    return result;
}

function translateToEnglish(input: string): string {
    let result = '';
    let isCapital = false;
    let isNumber = false;
    const brailleChars = input.match(/.{1,6}/g) || [];

    for (const brailleChar of brailleChars) {
        if (brailleChar === otherToBraille['capitalize']) {
            isCapital = true;
        } else if (brailleChar === otherToBraille['number']) {
            isNumber = true;
        } else if (brailleChar === otherToBraille['space']) {
            result += ' ';
            isNumber = false;
        } else {
            let char = '';
            if (isNumber) {
                char = Object.keys(numberToBraille).find(key => numberToBraille[key] === brailleChar) || '';
            } else {
                char = brailleToEnglish[brailleChar] || '';
            }

            if (isCapital) {
                char = char.toUpperCase();
                isCapital = false;
            }

            result += char;
        }
    }

    return result;
}

function translate(input: string): string {
    // Determine if input is English or Braille and translate accordingly
    if (input.match(/^[O.]+$/)) {
        return translateToEnglish(input);
    } else {
        return translateToBraille(input);
    }
}


// Main execution
if (require.main === module) {
    const input = process.argv.slice(2).join(' ');
    const result = translate(input);
    console.log(result);
}

export { translate };