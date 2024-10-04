const ENGLISH_TO_BRAILLE = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
};

const BRAILLE_TO_ENGLISH = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", "......": " ", ".....O": "capital", ".O.OOO": "number",
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
};

function englishToBraille(english) {
    let result = '';

    for (let i = 0; i < english.length; i++) {
        let char = english[i];
        if (char >= '0' && char <= '9') {
            result += '.O.OOO' + ENGLISH_TO_BRAILLE[char]; 
        } else if (char === char.toUpperCase() && char !== ' ') {
            result += '.....O' + ENGLISH_TO_BRAILLE[char.toLowerCase()];
        } else {
            result += ENGLISH_TO_BRAILLE[char.toLowerCase()] || '';
        }
    }

    return result;
}

//I couldn't solve this braille To English and the numbers this what i have so far
function brailleToEnglish(braille) {
    let result = '';
    const brailleChars = braille.match(/.{1,6}/g);

    for (let i = 0; i < brailleChars.length; i++) {
        let char = brailleChars[i];
        if (char === '.....O') {
            result += BRAILLE_TO_ENGLISH[char.toUpperCase()];
        } else if (char === '.O.OOO') {
            result += (parseInt(BRAILLE_TO_ENGLISH[char], 36) - 9).toString();
        } else {
            result += BRAILLE_TO_ENGLISH[char];
        }
    }

    return result;
}

function translate(input) {
    if (/^[O.]+$/.test(input)) {
        return brailleToEnglish(input);
    } else {
        return englishToBraille(input);
    }
}

