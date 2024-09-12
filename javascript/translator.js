
const brailleAlphabet = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", 
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......", 
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", 
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..", 
    "#": ".O.OOO",  // Number follows
    "capital": ".....O"  // Capital follows
};


const englishAlphabet = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", 
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", 
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", 
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t", 
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", 
    "O..OOO": "z", "......": " ", 
    ".O.OOO": "#",  // Number follows
    ".....O": "capital"  // Capital follows
};

// Function to determine if input is Braille
function isBraille(input) {
    return /^[O.]+$/.test(input);
}

// Function to convert Braille to English
function brailleToEnglish(input) {
    let result = '';
    let isNumber = false;  // Flag for number mode
    let isCapital = false; // Flag for capitalization

    
    for (let i = 0; i <= input.length - 6; i += 6) {
        let brailleChar = input.slice(i, i + 6);

        if (brailleChar === brailleAlphabet["#"]) {
            isNumber = true;
            continue;
        }

        if (brailleChar === brailleAlphabet["capital"]) {
            isCapital = true;
            continue;
        }

        let letter = englishAlphabet[brailleChar];
        if (!letter) {
            result += ' ';  // Handle unmapped characters as spaces
            continue;
        }

        if (isNumber) {
            // Convert letter to number
            const numberMap = { "a": "1", "b": "2", "c": "3", "d": "4", "e": "5", 
                                "f": "6", "g": "7", "h": "8", "i": "9", "j": "0" };
            result += numberMap[letter];
        } else if (isCapital) {
            result += letter.toUpperCase();  // Capitalize the next letter only
            isCapital = false;  // Reset capital flag
        } else {
            result += letter;
        }
    }
    return result;
}

// Function to convert English to Braille
// Function to convert English to Braille
function englishToBraille(input) {
    let result = '';
    let isNumber = false;

    for (let char of input) {
        if (!isNaN(char) && char !== ' ') {  // Check if character is a number
            if (!isNumber) {
                result += brailleAlphabet["#"];  // Add number sign
                isNumber = true;
            }
            // Convert numbers to Braille (1-0 -> a-j)
            const numberMap = { "1": "a", "2": "b", "3": "c", "4": "d", "5": "e", 
                                "6": "f", "7": "g", "8": "h", "9": "i", "0": "j" };
            result += brailleAlphabet[numberMap[char]];
        } else {
            isNumber = false;  // Reset number flag

            if (char === char.toUpperCase() && char !== ' ') {
                result += brailleAlphabet["capital"];  // Add capital letter prefix
            }
            result += brailleAlphabet[char.toLowerCase()] || brailleAlphabet[" "];  // Handle space
        }
    }
    return result;
}


const input = process.argv.slice(2).join(' ');


if (isBraille(input)) {
    console.log(brailleToEnglish(input));
} else {
    console.log(englishToBraille(input));
}
