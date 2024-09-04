// Harinder Partap Singh

const brailleMap = {
    // Braille representation of letters (a-z)
    a: "O.....", b: "O.O...", c: "OO....", d: "OO.O..", e: "O..O..", f: "OOO...", g: "OOOO..", h: "O.OO..", i: ".OO...", j: ".OOO..",
    k: "O...O.", l: "O.O.O.", m: "OO..O.", n: "OO.OO.", o: "O..OO.", p: "OOO.O.", q: "OOOOO.", r: "O.OOO.", s: ".OO.O.", t: ".OOOO.",
    u: "O...OO", v: "O.O.OO", w: ".OOO.O", x: "OO..OO", y: "OO.OOO", z: "O..OOO",

    // Numbers (0-9)
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",

    // Special symbols
    " ": "......",
    "capital": ".....O",
    "number": ".O.OOO"
};

const englishMap = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z',
    '......': ' ',
    '.....O': 'capital',
    '.O.OOO': 'number'
};


const numberMap = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
};

const checkBraille = (input) => {
    const brailleSet = new Set(['O', '.']);
    const inputSet = new Set(input.split(''));

    if (input.length % 6 !== 0) {
        return false;
    }

    return inputSet.size === brailleSet.size && [...inputSet].every(char => brailleSet.has(char));
}


const translateToBraille = (input) => {
    let result = "";
    let isNumber = false;

    for (const char of input) {
        //Check if character is capital letter
        if (char >= "A" && char <= "Z") {
            result += brailleMap["capital"] + brailleMap[char.toLowerCase()];
        }
        //Check if character is number
        else if (char >= "0" && char <= "9") {
            if (!isNumber) {
                result += brailleMap["number"];
                isNumber = true;
            }
            result += brailleMap[char];
        } else if (char >= "a" && char <= "z") {
            result += brailleMap[char];
        } else if (char === " ") {
            result += brailleMap[" "];
            isNumber = false;
        }
    }
    return result;
}


const translateToEnglish = (input) => {
    let result = "";
    let isCapital = false;
    let isNumber = false;

    //Looping over the input and getting 6 characters in each loop
    for (let i = 0; i < input.length; i += 6) {
        const brailleChar = input.substring(i, i + 6);

        //Check if the characters represent capital, number, space
        if (brailleChar === brailleMap["capital"]) {
            isCapital = true;
        } else if (brailleChar === brailleMap["number"]) {
            isNumber = true;
        } else if (brailleChar === brailleMap[" "]) {
            result += " ";
            isNumber = false;
        } else {
            if (isNumber) {
                const numberChar = numberMap[brailleChar];
                if (numberChar) {
                    result += numberChar;
                }
            } else {
                const englishChar = englishMap[brailleChar];
                if (englishChar) {
                    result += isCapital ? englishChar.toUpperCase() : englishChar;
                    isCapital = false;
                }
            }
        }
    }
    return result;
}


const translate = (input) => {
    if (checkBraille(input)) {
        return translateToEnglish(input);
    } else {
        return translateToBraille(input);
    }
}


const input = process.argv.slice(2).join(" ");

console.log(translate(input));


