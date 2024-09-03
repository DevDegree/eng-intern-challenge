const readline = require('readline');

const brailleToEnglish = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", "......": " ", ".....O": "cap", ".....O.O": "num",
};

const englishToBraille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......", "1": "O.....", "2": "O.O...", "3": "OO....",
    "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..",
    "9": ".OO...", "0": ".OOO..",
};

function translateToEnglish(braille) {
    let result = "";
    let isCapital = false;
    let isNumber = false;

    for (let i = 0; i < braille.length; i += 6) {
        const symbol = braille.substring(i, i + 6);
        if (symbol === ".....O") {
            isCapital = true;
            continue;
        } else if (symbol === "....O.O") {
            isNumber = true;
            continue;
        }
        const char = brailleToEnglish[symbol];
        if (char) {
            if (isNumber) {
                result += isCapital ? char : char;
                isNumber = false;
            } else {
                result += isCapital ? char.toUpperCase() : char;
                isCapital = false;
            }
        }
    }
    return result;
}

function translateToBraille(english) {
    let result = "";
    let isNumber = false;

    for (const char of english) {
        const charStr = char.toLowerCase();

        if (char >= 'A' && char <= 'Z') {
            result += ".....O";
        }

        if (char >= '0' && char <= '9') {
            if (!isNumber) {
                result += "....O.O";
                isNumber = true;
            }
        } else {
            isNumber = false;
        }

        result += englishToBraille[charStr] || "??????";
    }

    return result;
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Enter a string to translate: ', (input) => {
    if (input.includes("O.") || input.includes("O.....")) {
        console.log(translateToEnglish(input));
    } else {
        console.log(translateToBraille(input));
    }
    rl.close();
});