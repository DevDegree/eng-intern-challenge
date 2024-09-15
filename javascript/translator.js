const translationMap = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...",
    "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.",
    "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO",
    "cap": ".....O",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...",
    "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    "num": ".O.OOO",
    " ": "......"
};

const reverseTranslationMap = Object.entries(translationMap).reduce((map, [key, value]) => {
    if (!map[value]) map[value] = key;
    return map;
}, {});

function translateToBraille(input) {
    let result = "";
    let numberMode = false;

    for (const char of input) {
        if (char >= 'A' && char <= 'Z') {
            result += translationMap["cap"] + translationMap[char.toLowerCase()];
        } else if (char >= '0' && char <= '9') {
            if (!numberMode) {
                result += translationMap["num"];
                numberMode = true;
            }
            result += translationMap[char];
        } else if (char === ' ') {
            numberMode = false;
            result += translationMap[char];
        } else {
            numberMode = false;
            result += translationMap[char];
        }
    }
    return result;
}

function translateToEnglish(input) {
    let result = "";
    let i = 0;
    let capitalizeNext = false;
    let numberMode = false;

    while (i < input.length) {
        const brailleChar = input.substring(i, i + 6);

        if (brailleChar === translationMap["cap"]) {
            capitalizeNext = true;
        } else if (brailleChar === translationMap["num"]) {
            numberMode = true;
        } else if (reverseTranslationMap[brailleChar]) {
            let char = reverseTranslationMap[brailleChar];

            if (numberMode && char >= 'a' && char <= 'j') {
                char = String.fromCharCode(char.charCodeAt(0) - 49);
            }

            if (capitalizeNext) {
                char = char.toUpperCase();
                capitalizeNext = false;
            }

            result += char;

            if (char === ' ') {
                numberMode = false;
            }
        }
        i += 6;
    }
    return result;
}

function detectAndTranslate(input) {
    const isBraille = /^[O.]+$/.test(input.trim());
    return isBraille ? translateToEnglish(input) : translateToBraille(input);
}

const userInput = process.argv.slice(2).join(' ');
const translationResult = detectAndTranslate(userInput);
console.log(translationResult);

