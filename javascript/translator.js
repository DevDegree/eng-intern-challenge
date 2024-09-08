// Braille character mappings (Letter to Braille)
const alphabetBrailleMap = {
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
    " ": "......"
};

// Braille character mappings (Number to Braille)
const numberBrailleMap = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO.."
};

const capsFollows = ".....O";
const numberFollows = ".O.OOO";

// Reverse character mappings (Braille to Letter)
const brailleAlphabetMap = {};
Object.keys(alphabetBrailleMap).forEach(key => {
    brailleAlphabetMap[alphabetBrailleMap[key]] = key;
})

// Reverse character mappings (Braille to Number)
const brailleNumberMap = {};
Object.keys(numberBrailleMap).forEach(key => {
    brailleNumberMap[numberBrailleMap[key]] = key;
})

// Function to translate English to Braille
function translateToBraille(input) {
    let output = "";
    let isNum = false;

    for (const char of input) {
        if (/[A-Z]/.test(char)) { // Capital letter
            output += capsFollows + alphabetBrailleMap[char.toLowerCase()];
        } else if (/[0-9]/.test(char)) { // Number
            if (!isNum) {
                output += numberFollows; // Switch to number mode
                isNum = true;
            }
            output += numberBrailleMap[char];
        } else if (char === " ") { // Space
            output += alphabetBrailleMap[" "];
            isNum = false; // Reset isNum
        } else { // Lowercase letter
            output += alphabetBrailleMap[char];
        }
    }

    return output;
}

// Function to translate Braille to English
function translateToEnglish(input) {
    let output = "";
    let isCaps = false;
    let isNum = false;

    for (let i = 0; i < input.length; i += 6) {
        const brailleChar = input.slice(i, i + 6);

        if (brailleChar === capsFollows) {
            isCaps = true;
        } else if (brailleChar === numberFollows) {
            isNum = true;
        } else if (brailleChar === "......") { // Space
            output += " ";
            isNum = false; // Reset isNum
        } else {
            if (isNum) { // Map to number 
                output += brailleNumberMap[brailleChar];
            } else if (isCaps) { // Capital Letter
                output += brailleAlphabetMap[brailleChar].toUpperCase();
                isCaps = false; // Only capitalize the next letter
            } else {
                output += brailleAlphabetMap[brailleChar];
            }
        }
    }

    return output;
}

// Function to translate user input based on type of input
function translateInput(input) {
    if (/^[O.]+$/.test(input)) {  // Braille Input

        return translateToEnglish(input);
    }

    return translateToBraille(input); // English Input
}

// Get user input from arguments
const args = process.argv.slice(2);

const userInput = args.join(' ');

console.log(translateInput(userInput));