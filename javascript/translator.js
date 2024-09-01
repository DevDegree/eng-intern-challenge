// a dictionary to map english and braille
const brailleDictionary = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
    "capitalFollows": ".....O",
    "decimalFollows": ".O...O",
    "numberFollows": ".O.OOO",
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OO..",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......", 
};

// Reverse map to decode Braille back to English
const ReversebrailleDictionary = Object.entries(brailleDictionary).reduce((acc, [letter, braille]) => {
    acc[braille] = letter;
    return acc;
}, {});

// Function to determine if the input is Braille or English
function isBraille(input) {
    return /^[O.]+$/.test(input);
}

// Function to translate from English to Braille
function translateToBraille(input) {
    let braille = '';
    let isNumber = false;

    for (let char of input) {
        if (/[A-Z]/.test(char)) {
            braille += brailleDictionary["capitalFollows"];
            char = char.toLowerCase();
        } 
        
        if (/[0-9]/.test(char)) {
            if (!isNumber) {
                braille += brailleDictionary["numberFollows"];
                isNumber = true;
            }
        } else {
            isNumber = false;
        }

        braille += brailleDictionary[char] || brailleDictionary[' '];
    }

    return braille;
}

// Function to translate from Braille to English
function translateToEnglish(input) {
    let english = '';
    let isCapital = false;
    let isNumber = false;

    for (let i = 0; i < input.length; i += 6) {
        const brailleChar = input.slice(i, i + 6);
        if (brailleChar === brailleDictionary["capitalFollows"]) {
            isCapital = true;
            continue;
        } else if (brailleChar === brailleDictionary["numberFollows"]) {
            isNumber = true;
            continue;
        }

        let letter = ReversebrailleDictionary[brailleChar] || ' ';
        if (isCapital) {
            letter = letter.toUpperCase();
            isCapital = false;
        }

        english += letter;
    }

    return english;
}

function translate(input) {
    if (isBraille(input)) {
        return translateToEnglish(input);
    } else {
        return translateToBraille(input);
    }
}

const input = process.argv.slice(2).join(' ');
const output = translate(input);

console.log(output);
