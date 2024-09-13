
const brailleLetters = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z"
}

const brailleNumbers = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0"
}

const brailleSymbols = {
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "O..OO.": ">",
    "O.O..O": "(",
    ".O.OO.": ")",
}

const brailleSpace = "......";
const brailleCapitalFollows = ".....O";
const brailleDecimalFollows = ".O...O";
const brailleNumberFollows = ".O.OOO";

const englishToBraille = (text) => {
    let brailleText = "";
    let isNumber = false;

    for (const char of text) {
        if (char === " ") {
            brailleText += brailleSpace;
            isNumber = false;
            continue;
        }

        if (char >= "a" && char <= "z") {
            brailleText += brailleLetters[`O${char}`];
            isNumber = false;
        } else if (char >= "0" && char <= "9") {
            if (!isNumber) {
                brailleText += brailleNumberFollows;
                isNumber = true;
            }
            brailleText += brailleNumbers[`O${char}`];
        } else {
            brailleText += brailleSymbols[brailleChar(char)] || "?";
        }
    }

    return brailleText;
};

const brailleChar = (char) => {
    const symbols = {
        '.': "..OO.O",
        ',': "..O...",
        '?': "..O.OO",
        '!': "..OOOO",
        ':': "..OO..",
        ';': "..O.O.",
        '-': "....OO",
        '/': ".O..O.",
        '<': ".OO..O",
        '>': "O..OO.",
        '(': "O.O..O",
        ')': ".O.OO."
    };
    return symbols[char] || "";
};

const brailleToEnglish = (braille) => {
    let englishText = "";
    let isNumber = false;
    let isCapital = false;

    for (let i = 0; i < braille.length; i+= 6) {
        const brailleChar = braille.slice(i, i + 6);

        if (brailleChar === brailleCapitalFollows) {
            isCapital = true;
            continue;
        }

        if (brailleChar === brailleNumberFollows) {
            isNumber = true;
            continue;
        }

        if (brailleChar === brailleSpace) {
            englishText += " ";
            isNumber = false;
            continue;
        }

        if (isNumber) {
            englishText += brailleNumbers[brailleChar]|| "?";
            isNumber = false;
        } else {
            if (brailleLetters[brailleChar]) {
                let char = brailleLetters[brailleChar];
                if (isCapital) {
                    char = char.toUpperCase();
                    isCapital = false;
                }
                englishText += char;
            } else if (brailleSymbols[brailleChar]) {
                englishText += brailleSymbols[brailleChar];
            } else {
                englishText += "?";
            }
        }
    }
    return englishText;
}

const isBraille = (str) => /^[O.]{6,}$/.test(str);

const translateString = (input) => {
    if (isBraille(input)) {
        return brailleToEnglish(input);
    } else {
        return englishToBraille(input);
    }
};

const input = process.argv[2];
console.log(translateString(input))

// if (!input) {
//     console.log(translateString(input));
// } else {
//     console.error("Please provide a string to translate.");
// }

// need to fix the number translation, and need to be able to translate without having the string within quotations