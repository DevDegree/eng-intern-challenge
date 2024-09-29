// Run the code: node translator.js "your input"

// create a object map
const brailleDict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', 'cap': '.....O', 'num': '.O.OOO', 'space': '......',
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': 'O...OO'
};
// reverse dictionary to translate Braille back to English letters.
const brailleToEnglishDict = Object.fromEntries(
    Object.entries(brailleDict).map(([char, braille]) => [braille, char])
);

// checks if the input string is in Braille.
function isBraille(input) {
    return /^[O.]+$/.test(input.trim());
}
// translates English text to Braille.
function translateToBraille(text) {
    let brailleOutput = [];
    let numberMode = false;

    for (let char of text) {
        if (char === ' ') {
            brailleOutput.push(brailleDict['space']);
        } else if (/\d/.test(char)) {
            if (!numberMode) {
                brailleOutput.push(brailleDict['num']);
                numberMode = true;
            }
            brailleOutput.push(brailleDict[char]);
        } else {
            if (!brailleDict[char.toLowerCase()]) {
                console.warn(`Warning: Character "${char}" is not supported.`);
                continue;
            }

            if (char === char.toUpperCase() && char !== ' ') {
                brailleOutput.push(brailleDict['cap']);
            }
            brailleOutput.push(brailleDict[char.toLowerCase()]);
            numberMode = false;
        }
    }
    return brailleOutput.join('');
}
// translates Braille text back to English.
function translateFromBraille(brailleText) {
    let englishOutput = [];
    let numberMode = false;
    let capitalizeNext = false;

    for (let i = 0; i < brailleText.length; i += 6) {
        let symbol = brailleText.slice(i, i + 6);

        if (symbol === brailleDict['num']) {
            numberMode = true;
            continue;
        }

        if (symbol === brailleDict['cap']) {
            capitalizeNext = true;
            continue;
        }

        if (symbol === brailleDict['space']) {
            englishOutput.push(' ');
            numberMode = false;
            continue;
        }

        let char = brailleToEnglishDict[symbol];

        if (numberMode) {
            if (char >= 'a' && char <= 'j') {
                let number = (char.charCodeAt(0) - 'a'.charCodeAt(0) + 1).toString();
                englishOutput.push(number);
            } else if (char === 'j') {
                englishOutput.push('0');
            }
            continue;
        }

        if (capitalizeNext && char) {
            englishOutput.push(char.toUpperCase());
            capitalizeNext = false;
        } else {
            englishOutput.push(char);
        }
    }
    return englishOutput.join('');
}

// Get the input from the command line arguments.
const input = process.argv.slice(2).join(' ');

// Decide whether to translate the input to Braille or from Braille based on its format.
if (isBraille(input)) {
    console.log(translateFromBraille(input));
} else {
    console.log(translateToBraille(input));
}
