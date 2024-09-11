const arg = process.argv;  // Get the input from command-line arguments
let input = arg.slice(2); // Pick from index 2 to the end
input = input.join(" "); // Join each argument using space

// Define Braille Alphabets
const brailleAlph = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO",
    " ": "......"
};

// Define Braille Number
const brailleNums = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
};

// Special symbols
const brailleCapitalPrefix = ".....O";
const brailleNumberPrefix = ".O.OOO";
const space = "......";

// Reverse the mappings for Braille to English
const englishAlph = Object.entries(brailleAlph).reduce((acc, [key, value]) => {
    acc[value] = key;
    return acc;
}, {});

const englishNum = Object.entries(brailleNums).reduce((acc, [key, value]) => {
    acc[value] = key;
    return acc;
}, {});
 

// Check if argument passed is Braille or English
function isBraille(input) {
    return /^[O.]+$/.test(input.replace(/\s/g, ""));
}

// Translate English to Braille
function translateToBraille(input) {
    let result = [];
    let numberMode = false;

    for (let char of input) {
        if (/\d/.test(char)) { //check if current char is number
            if (!numberMode) {
                result.push(brailleNumberPrefix); // Append number prefix
                numberMode = true;
            }
            result.push(brailleNums[char]);
        } else if (/[a-z]/.test(char)) { // if char is lowercase alpha
            numberMode = false; // Exit number mode
            result.push(brailleAlph[char]);
        } else if (/[A-Z]/.test(char)) { // if char is uppercase alpha
            numberMode = false; // Exit number mode
            result.push(brailleCapitalPrefix);
            result.push(brailleAlph[char.toLowerCase()]);
        } else if (char === " ") {
            result.push(brailleAlph[" "]);
        } 
    }
    return result.join("");
}

// Translate Braille to English
function translateToEnglish(input) {
    let result = [];
    let numberMode = false;
    let capitalNext = false;
    
    // Split the Braille chars into 6 section each
    const brailleChars =  [];
    for(let c=0; c<(input.length/6); c++){
        const startIndex = c*6;
        brailleChars.push(input.slice(startIndex, startIndex+6))
    }
 
    for (let brailleChar of brailleChars) {
        console.log(brailleChar)
        if (brailleChar === brailleCapitalPrefix) {
            capitalNext = true;
        } else if (brailleChar === brailleNumberPrefix) {
            numberMode = true;
        }  else if (brailleChar === space) { // When a Braille number follows symbol is read, assume all following symbols are numbers until the next space symbol.
            numberMode = false;
            result.push(englishAlph[brailleChar]);
        } else if (englishAlph[brailleChar] && !numberMode ) {
            let letter = englishAlph[brailleChar];
            if (capitalNext) {
                letter = letter.toUpperCase();
                capitalNext = false;
            }
            result.push(letter);
        } else if (englishNum[brailleChar]) {
            result.push(englishNum[brailleChar]); 
        }
    }

    return result.join("");
}

// Handle translation
function translate(input) {
    if (isBraille(input)) {
        return translateToEnglish(input);
    } else {
        return translateToBraille(input);
    }
}
 

console.log(translate(input));  // Output the translation result
