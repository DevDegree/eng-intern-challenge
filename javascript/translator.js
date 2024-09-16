const lettersToBraille = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO"
};

const numbersToBraille = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO.."
};

const brailleToLetter = Object.fromEntries(Object.entries(lettersToBraille).map(([k, v]) => [v, k]));
const brailleToNumber = Object.fromEntries(Object.entries(numbersToBraille).map(([k, v]) => [v, k]));

const CAPITAL_FOLLOWS = ".....O";
const DECIMAL_FOLLOWS = ".O...O";
const NUMBER_FOLLOWS = ".O.OOO";
const SPACE = "......";

function textToBraille(text) {
    const state = {
        numFollows: false,
        lastWasNumber: false
    };

    function processChar(char) {
        let result = [];

        if (/\d/.test(char)) {
            if (!state.numFollows) {
                result.push(NUMBER_FOLLOWS);
                state.numFollows = true;
            }
            result.push(numbersToBraille[char] || '');
            state.lastWasNumber = true;
        } else if (/[a-zA-Z]/.test(char)) {
            if (state.numFollows) {
                state.numFollows = false;
            }
            if (char === char.toUpperCase()) {
                result.push(CAPITAL_FOLLOWS);
            }
            result.push(lettersToBraille[char.toLowerCase()] || '');
            state.lastWasNumber = false;
        } else if (char === ' ') {
            result.push(SPACE);
            state.numFollows = false;
            state.lastWasNumber = false;
        } else if (char === '.') {
            if (state.lastWasNumber) {
                result.push(DECIMAL_FOLLOWS);
            } else {
                result.push(lettersToBraille['.'] || '');
            }
            state.lastWasNumber = false;
        }

        return result.join('');
    }

    return text.split('').map(processChar).join('');
}

function processSymbol(symbol, state) {
    if (state.numberFollows || state.decimalFollows) {
        const char = brailleToNumber[symbol] || '';
        if (!/\d/.test(char)) {
            state.numberFollows = false;
            state.decimalFollows = false;
        }
        return char;
    }

    const char = brailleToLetter[symbol];
    return state.capitalFollows ? char.toUpperCase() : char;
}

function brailleToText(text) {
    const brailleSymbols = text.match(/.{1,6}/g) || [];
    const plainText = [];
    const state = {
        capitalFollows: false,
        numberFollows: false,
        decimalFollows: false
    };

    for (const symbol of brailleSymbols) {
        if (symbol === CAPITAL_FOLLOWS) {
            state.capitalFollows = true;
        } else if (symbol === NUMBER_FOLLOWS) {
            state.numberFollows = true;
        } else if (symbol === DECIMAL_FOLLOWS) {
            state.decimalFollows = true;
            plainText.push('.');
        } else if (symbol === SPACE) {
            state.numberFollows = false;
            state.decimalFollows = false;
            plainText.push(' ');
        } else {
            const char = processSymbol(symbol, state);
            plainText.push(char);

            state.capitalFollows = false;
            if (char === ' ') {
                state.numberFollows = false;
                state.decimalFollows = false;
            }
        }
    }

    return plainText.join('');
}

function isBraille(braille) {
    return /^[O.]+$/.test(braille) && braille.length % 6 === 0;
}

function translate(input) {
    if (isBraille(input)) {
        return brailleToText(input);
    } else {
        return textToBraille(input);
    }
}

if (require.main === module) {
    const args = process.argv.slice(2);
    if (args.length < 1) {
        console.log("Correct use: node translator.js <input>");
        process.exit(-1);
    }
    const input = args.join(' ');
    console.log(translate(input));
}