// Constants
const BRAILLE_CHAR_LENGTH = 6;

// Braille cypher
const alphaCypher = {
    alpha: {
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
        'SPACE': '......',
    },
    number: {
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
    },
    special: {
        'CAP': '.....O',
        'NUM': '.O.OOO',
    }
};

// Flip the cypher for easier lookup
function flipCypher(cypher) {
    const flipped = {};
    for (const [category, dict] of Object.entries(cypher)) {
        flipped[category] = {};
        for (const [k, v] of Object.entries(dict)) {
            flipped[category][v] = k;
        }
    }
    return flipped;
}

// Check if the input is braille
function isBraille(input) {
    if (!/^[.O]+$/.test(input)) {
        return false;
    }
    if (input.length % BRAILLE_CHAR_LENGTH !== 0) {
        throw new Error('Invalid Braille input length.');
    }
    return true;
}

// Convert braille to English
function brailleToEnglish(input) {
    const brailleCypher = flipCypher(alphaCypher);
    let result = '';
    let flag = '';

    for (let i = 0; i < input.length; i += BRAILLE_CHAR_LENGTH) {
        const brailleChar = input.slice(i, i + BRAILLE_CHAR_LENGTH);

        if (flag) { // if there is an active flag...
            switch (flag) {
                case "NUM": // number
                    if (brailleChar === alphaCypher.alpha.SPACE) {
                        result += ' ';
                        flag = '';
                    } else {
                        result += brailleCypher.number[brailleChar] || '?';
                    }
                    break;
                case "CAP": // capital
                    result += (brailleCypher.alpha[brailleChar] || '?').toUpperCase();
                    flag = '';
                    break;
            }
        } else { // now we can process this brail char string
            switch (brailleChar) {
                case alphaCypher.special.NUM: // number
                    flag = "NUM";
                    break;
                case alphaCypher.special.CAP: // capital
                    flag = "CAP";
                    break;
                case alphaCypher.alpha.SPACE: // space
                    result += ' ';
                    break;
                default: // letter
                    result += brailleCypher.alpha[brailleChar] || '?';
            }
        }
    }
    return result;
}

// Convert English to braille
function englishToBraille(input) {
    let result = '';
    let numFlag = false;

    for (const char of input) {
        const lowerChar = char.toLowerCase();
        switch (true) {
            case char === ' ': // space
                numFlag = false;
                result += alphaCypher.alpha.SPACE;
                break;
            case /[0-9]/.test(char): // number
                if (!numFlag) {
                    result += alphaCypher.special.NUM;
                    numFlag = true;
                }
                result += alphaCypher.number[char] || '';
                break;
            case /[a-z]/i.test(char): // lowercase letter
                if (char !== lowerChar) {
                    result += alphaCypher.special.CAP;
                }
                result += alphaCypher.alpha[lowerChar] || '';
                break;
            default: // not found in cypher
                result += '';
                break;
        }
    }
    return result;
}

// Main function to process input
function main() {
    // Get all command-line arguments and join them into a single string
    const input = process.argv.slice(2).join(' ');

    // Check if the input is empty
    if (!input) {
        console.error('No input provided.');
        return;
    }

    try {
        // Determine the translation direction based on the input
        const result = isBraille(input) ? brailleToEnglish(input) : englishToBraille(input);

        // Output the result
        console.log(result);
    } catch (error) {
        console.error(error.message);
    }
}

main();