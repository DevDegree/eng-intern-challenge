const capitalIndicator = ".....O";
const numberIndicator = ".O.OOO";

const Alphabet = {
    A: "O.....", B: "O.O...", C: "OO....", D: "OO.O..", E: "O..O..", F: "OOO...",
    G: "OOOO..", H: "O.OO..", I: ".OO...", J: ".OOO..", K: "O...O.", L: "O.O.O.",
    M: "OO..O.", N: "OO.OO.", O: "O..OO.", P: "OOO.O.", Q: "OOOOO.", R: "O.OOO.",
    S: ".OO.O.", T: ".OOOO.", U: "O...OO", V: "O.O.OO", W: ".OOO.O", X: "OO..OO",
    Y: "OO.OOO", Z: "O..OOO",
};

const numbers = {
    1: "O.....", 2: "O.O...", 3: "OO....", 4: "OO.O..", 5: "O..O..", 6: "OOO...",
    7: "OOOO..", 8: "O.OO..", 9: ".OO...", 0: ".OOO.."
};

const symbols = {
    ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..",
    ";": "..O.O.", "-": "....OO", "/": ".O..O.", "<": ".OO..O", ">": "O..OO.",
    "(": "O.O..O", ")": ".O.OO."
};

const space = "......";

function isBraille(input) {
    return /^[O.]+$/.test(input) && input.length % 6 === 0;
}

function translateToBraille(text) {
    let brailleOutput = [];
    let isNumberMode = false;

    for (let char of text) {
        if (char === ' ') {
            brailleOutput.push(space);
            isNumberMode = false;
        } else if (/[a-zA-Z]/.test(char)) {
            if (isNumberMode) {
                brailleOutput.push(space);
                isNumberMode = false;
            }

            if (char === char.toUpperCase()) {
                brailleOutput.push(capitalIndicator);
                char = char.toLowerCase();
            }

            brailleOutput.push(Alphabet[char.toUpperCase()]);
        } else if (/\d/.test(char)) {
            if (!isNumberMode) {
                brailleOutput.push(numberIndicator);
                isNumberMode = true;
            }
            brailleOutput.push(numbers[char]);
        } else if (symbols[char]) {
            brailleOutput.push(symbols[char]);
        }
    }

    return brailleOutput.join('');
}

function translateToEnglish(braille) {
    let englishOutput = [];
    let isCapital = false;
    let isNumberMode = false;

    for (let i = 0; i < braille.length; i += 6) {
        let symbol = braille.slice(i, i + 6);

        if (symbol === space) {
            englishOutput.push(' ');
            isNumberMode = false;
        } else if (symbol === capitalIndicator) {
            isCapital = true;
        } else if (symbol === numberIndicator) {
            isNumberMode = true;
        } else {
            let char = null;

            if (isNumberMode) {
                char = Object.keys(numbers).find(key => numbers[key] === symbol);
                isNumberMode = char !== null;
            }

            if (!char) {
                if (isCapital) {
                    char = Object.keys(Alphabet).find(key => Alphabet[key] === symbol) ||
                    Object.keys(symbols).find(key => symbols[key] === symbol);
                } else if (!isCapital) {
                    char = Object.keys(Alphabet).find(key => Alphabet[key] === symbol).toLowerCase() ||
                    Object.keys(symbols).find(key => symbols[key] === symbol).toLowerCase();
                }
                char = Object.keys(Alphabet).find(key => Alphabet[key] === symbol).toLowerCase() ||
                    Object.keys(symbols).find(key => symbols[key] === symbol).toLowerCase();
            }

            if (char) {
                if (isCapital) {
                    char = char.toUpperCase();
                    isCapital = false;
                }
                englishOutput.push(char);
            }
        }
    }

    return englishOutput.join('');
}

const args = process.argv.slice(2);
if (args.length < 1) {
    console.log("Usage: node translator.js <text>");
    process.exit(1);
}

const input = args.join(' ');
if (isBraille(input)) {
    const englishTranslation = translateToEnglish(input);
    console.log(englishTranslation);
} else {
    const brailleTranslation = translateToBraille(input);
    console.log(brailleTranslation);
}
