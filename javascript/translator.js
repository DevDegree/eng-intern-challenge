const args = process.argv.slice(2);
const input = args.join(' ');

// define the english alphabet 
const engAlphabet = 'abcdefghijklmnopqrstuvwxyz';
// define the braille alphabet
const brailleAlphabet = [
    'O.....', // A, a, 1
    'O.O...', // B, b, 2
    'OO....', // C, c, 3
    'OO.O..', // D, d, 4
    'O..O..', // E, e, 5
    'OOO...', // F, f, 6
    'OOOO..', // G, g, 7
    'O.OO..', // H, h, 8
    '.OO...', // I, i, 9
    '.OOO..', // J, j, 0
    'O...O.', // K, k
    'O.O.O.', // L, l
    'OO..O.', // M, m
    'OO.OO.', // N, n
    'O..OO.', // O, o
    'OOO.O.', // P, p
    'OOOOO.', // Q, q
    'O.OOO.', // R, r
    '.OO.O.', // S, s
    '.OOOO.', // T, t
    'O...OO', // U, u
    'O.O.OO', // V, v
    '.OOO.O', // W, w
    'OO..OO', // X, x
    'OO.OOO', // Y, y
    'O..OOO'  // Z, z
];

function translate(input) {
    if (input.length <= 0) return '';

    if (isBraille(input))
        return brailleToEnglish(input);
    else
        return englishToBraille(input);
}

function isBraille(input) {
    return input.match(/^[O.]{6,}$/);
}

// given an english letter, return its position in the english alphabet
function indexForBraille(letter) {
    return engAlphabet.indexOf(letter);
}

// given a braille cell, return its position in the braille alphabet
function indexForEnglish(symbol) {
    return brailleAlphabet.indexOf(symbol);
}

function brailleToEnglish(input) {
    let output = '';
    let isReadingCapitals = false;
    let isReadingNumbers = false;
    // number of braille cells in the input
    let numSymbols = input.length / 6;

    for (let i = 0; i < numSymbols; i++) {
        // the start of the i'th braille cell
        let start = i * 6;
        let symbol = input.substring(start, start + 6);

        // capital follows
        if (symbol === '.....O') {
            isReadingCapitals = true;

            // number follows
        } else if (symbol === '.O.OOO') {
            isReadingNumbers = true;

            // space
        } else if (symbol === '......') {
            output += ' ';
            isReadingNumbers = false;

        } else {
            // position of corresponding english letter
            let index = indexForEnglish(symbol);

            if (isReadingCapitals) {
                // convert to capital
                output += engAlphabet[index].toUpperCase();
                // stop reading capital
                isReadingCapitals = false;

            } else if (isReadingNumbers) {
                // handle special case where symbol corresponds to 0
                if (symbol === '.OOO..')
                    output += '0';
                else
                    output += parseInt(index) + 1;
            } else {
                output += engAlphabet[index];
            }

        }
    }

    return output;
}

function englishToBraille(input) {

    let output = '';
    let isReadingNumbers = false;

    for (letter of input) {
        if (letter.match(/[A-Z]/)) {
            // capital follows
            output += '.....O';
            output += brailleAlphabet[indexForBraille(letter.toLowerCase())];
        }

        if (letter.match(/[a-z]/)) {
            output += brailleAlphabet[indexForBraille(letter)];
        }

        if (letter.match(/[0-9]/)) {
            if (!isReadingNumbers) {
                // number follows
                output += '.O.OOO';
                isReadingNumbers = true;
            }
            let index = parseInt(letter) - 1;
            if (index === -1) index = 9;
            output += brailleAlphabet[index];
        } else {
            isReadingNumbers = false;
        }

        if (letter === ' ') {
            output += '......';
        }
    }

    return output;
}

console.log(translate(input));


