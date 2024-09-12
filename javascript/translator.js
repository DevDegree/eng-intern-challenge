const brailleMap = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", 
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    " ": "......"
};

const reverseBrailleMap = {};
for (let key in brailleMap) {
    reverseBrailleMap[brailleMap[key]] = key;
}

// Function to translate from English to Braille
function translateToBraille(input) {
    let result = '';
    for (let char of input) {
        const lowerChar = char.toLowerCase();
        if (char >= 'A' && char <= 'Z') {
            result += ".....O"; // Capital letter symbol
        }
        result += brailleMap[lowerChar] || ' ';
    }
    return result;
}

// Function to translate from Braille to English
function translateToEnglish(input) {
    let result = '';
    const brailleSymbols = input.match(/.{1,6}/g);
    let capitalizeNext = false;
    for (let symbol of brailleSymbols) {
        if (symbol === ".....O") {
            capitalizeNext = true;
        } else {
            let char = reverseBrailleMap[symbol];
            if (capitalizeNext && char) {
                char = char.toUpperCase();
                capitalizeNext = false;
            }
            result += char || ' ';
        }
    }
    return result;
}

// Determine if the input is Braille or English
const input = process.argv.slice(2).join(" ");
if (input.includes("O") || input.includes(".")) {
    console.log(translateToEnglish(input));
} else {
    console.log(translateToBraille(input));
}
