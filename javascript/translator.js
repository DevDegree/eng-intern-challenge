const brailleMap = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    " ": "......", 'capital': '.....O', 'number': '.O.OOO'
};

const reverseBrailleMap = Object.fromEntries(Object.entries(brailleMap).map(([k, v]) => [v, k]));

function isBraille(text) {
    return /^[O.]{6,}$/.test(text);
}

function translateToBraille(text) {
    let brailleTranslation = '';
    let isNumber = false;
    for (let char of text) {
        if (char >= 'A' && char <= 'Z') {
            brailleTranslation += brailleMap['capital'];
            char = char.toLowerCase();
        }
        if (char >= '0' && char <= '9' && !isNumber) {
            brailleTranslation += brailleMap['number'];
            isNumber = true;
        } else if (char === ' ') {
            isNumber = false;
        }
        brailleTranslation += brailleMap[char] || '';
    }
    return brailleTranslation;
}

function translateToEnglish(brailleText) {
    let englishTranslation = '';
    let isCapital = false;
    let isNumber = false;
    for (let i = 0; i < brailleText.length; i += 6) {
        const brailleChar = brailleText.slice(i, i + 6);
        if (brailleChar === brailleMap['capital']) {
            isCapital = true;
            continue;
        }
        if (brailleChar === brailleMap['number']) {
            isNumber = true;
            continue;
        }
        let char = reverseBrailleMap[brailleChar] || '';
        if (isCapital) {
            char = char.toUpperCase();
            isCapital = false;
        }
        if (isNumber && char >= 'a' && char <= 'j') {
            char = (char.charCodeAt(0) - 'a'.charCodeAt(0) + 1).toString();
        }
        englishTranslation += char;
        if (char === ' ') {
            isNumber = false;
        }
    }
    return englishTranslation;
}

function main() {
    const input = process.argv.slice(2).join(' ');
    if (isBraille(input)) {
        console.log(translateToEnglish(input));
    } else {
        console.log(translateToBraille(input));
    }
}

main();