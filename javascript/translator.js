// Define Braille and English mapping
const brailleAlphabet = {
    a: "O.....", b: "O.O...", c: "OO....", d: "OO.O..", e: "O..O..", f: "OOO...", g: "OOOO..", h: "O.OO..", i: ".OO...", j: ".OOO..",
    k: "O...O.", l: "O.O.O.", m: "OO..O.", n: "OO.OO.", o: "O..OO.", p: "OOO.O.", q: "OOOOO.", r: "O.OOO.", s: ".OO.O.", t: ".OOOO.",
    u: "O...OO", v: "O.O.OO", w: ".OOO.O", x: "OO..OO", y: "OO.OOO", z: "O..OOO",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    space: "......",
    capital: ".....O", 
    number: ".O.OOO"
};

const reverseBraille = Object.fromEntries(
    Object.entries(brailleAlphabet).map(([key, value]) => [value, key])
);

const numbersMap = { a: '1', b: '2', c: '3', d: '4', e: '5', f: '6', g: '7', h: '8', i: '9', j: '0' };

// Function to detect if the input is Braille
function isBraille(input) {
    return /^[O.]+$/.test(input);
}

// Function to translate from English to Braille
function translateToBraille(input) {
    let result = [];
    let numberMode = false;

    for (let char of input) {
        if (char === ' ') {
            result.push(brailleAlphabet.space);
            numberMode = false;
        } else if (/[0-9]/.test(char)) {
            if (!numberMode) {
                result.push(brailleAlphabet.number);
                numberMode = true;
            }
            result.push(brailleAlphabet[char]);
        } else if (/[A-Z]/.test(char)) {
            result.push(brailleAlphabet.capital, brailleAlphabet[char.toLowerCase()]);
            numberMode = false;
        } else if (/[a-z]/.test(char)) {
            result.push(brailleAlphabet[char]);
            numberMode = false;
        }
    }

    return result.join('');
}

// Function to translate from Braille to English
function translateToEnglish(input) {
    let result = [];
    let capitalMode = false;
    let numberMode = false;

    for (let i = 0; i < input.length; i += 6) {
        const brailleChar = input.slice(i, i + 6);

        if (brailleChar === brailleAlphabet.space) {
            result.push(' ');
            numberMode = false;
        } else if (brailleChar === brailleAlphabet.capital) {
            capitalMode = true;
        } else if (brailleChar === brailleAlphabet.number) {
            numberMode = true;
        } else {
            let letter = reverseBraille[brailleChar] || '';

            if (numberMode && numbersMap[letter]) {
                letter = numbersMap[letter];
            } else if (numberMode) {
                numberMode = false;
            }

            if (capitalMode) {
                letter = letter.toUpperCase();
                capitalMode = false;
            }

            result.push(letter);
        }
    }

    return result.join('');
}

// Capture input from command-line arguments and execute translation
const input = process.argv.slice(2).join(' ');

try {
    const result = isBraille(input) ? translateToEnglish(input) : translateToBraille(input);
    console.log(result);
} catch (error) {
    console.error(error.message);
}