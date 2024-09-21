const brailleAlphabets= {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO",
    "cap": ".....O", "num": ".O.OOO", " ": "......",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
};

//Reversing Braille to English mapping
const brailleToEnglish = Object.keys(brailleAlphabets).reduce((obj, key) => {
    obj[brailleAlphabets[key]] = key;
    return obj;
}, {});

function isBraille(str) {
    return /^[O.]+$/.test(str);
}

//Translating English to Braille
function translateToBraille(input) {
    let result = "";
    let isNumber = false;
    for (let char of input) {
        if (char >= 'A' && char <= 'Z') {
            result += brailleAlphabets['cap'];
            char = char.toLowerCase();
        } else if (char >= '0' && char <= '9' && !isNumber) {
            result += brailleAlphabets['num'];
            isNumber = true;
        } else if (char === " ") {
            isNumber = false;
        }
        result += brailleAlphabets[char] || "";
    }
    return result;
}

//Translating Braille to English
function translateToEnglish(input) {
    let result = "";
    let isCapital = false;
    let isNumber = false;

    for (let i = 0; i < input.length; i += 6) {
        const symbol = input.slice(i, i + 6);
        if (symbol === brailleAlphabets['cap']) {
            isCapital = true;
            continue;
        } else if (symbol === brailleAlphabets['num']) {
            isNumber = true;
            continue;
        }
        let char = brailleToEnglish[symbol] || "";
        if (isNumber && /[a-j]/.test(char)) {
            char = String.fromCharCode(char.charCodeAt(0) - 49 + 1);
        }
        if (isCapital) {
            char = char.toUpperCase();
            isCapital = false;
        }

        result += char;
    }
    return result;
}

// Main function
function brailleTranslator(input) {
    if (isBraille(input)) {
        return translateToEnglish(input);
    } else {
        return translateToBraille(input);
    }
}

const input = process.argv.slice(2).join(' ');
console.log(brailleTranslator(input));
