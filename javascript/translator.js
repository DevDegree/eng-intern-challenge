#!/usr/bin/env node

// Braille mapping for letters, numbers, and symbols
const brailleDict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', ' ': '......',  // Space
    'capital': '.....O',  // Capital indicator
    'number': '.O.OOO'  // Number indicator
};

// Braille digits mapping
const brailleDigits = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
};

// Reverse dictionaries for decoding Braille to English
const englishDict = Object.fromEntries(Object.entries(brailleDict).map(([key, value]) => [value, key]));
const englishDigits = Object.fromEntries(Object.entries(brailleDigits).map(([key, value]) => [value, key]));

// Function to convert English text to Braille
function englishToBraille(text) {
    let brailleOutput = [];
    let isNumber = false;
    for (let char of text.trim()) {  // Trim spaces to avoid unexpected characters
        if (char >= 'A' && char <= 'Z') {
            brailleOutput.push(brailleDict['capital']);  // Capital letter marker
            brailleOutput.push(brailleDict[char.toLowerCase()]);
        } else if (char >= '0' && char <= '9') {
            if (!isNumber) {
                brailleOutput.push(brailleDict['number']);  // Add number marker once
                isNumber = true;
            }
            brailleOutput.push(brailleDigits[char]);
        } else {
            brailleOutput.push(brailleDict[char] || '......');  // Handle lowercase and space
            isNumber = false;  // Reset number mode after space or non-number character
        }
    }
    return brailleOutput.join('');
}


// Function to convert Braille to English
function brailleToEnglish(braille) {
    let englishOutput = [];
    let capitalMode = false;
    let numberMode = false;
    
    for (let i = 0; i < braille.length; i += 6) {
        let brailleChar = braille.slice(i, i + 6);
        
        if (brailleChar === brailleDict['capital']) {
            capitalMode = true;
            continue;
        }
        if (brailleChar === brailleDict['number']) {
            numberMode = true;
            continue;
        }
        
        if (numberMode) {
            englishOutput.push(englishDigits[brailleChar] || '?');
        } else {
            let letter = englishDict[brailleChar] || '?';
            if (capitalMode) {
                englishOutput.push(letter.toUpperCase());
                capitalMode = false;
            } else {
                englishOutput.push(letter);
            }
        }
        
        if (brailleChar === brailleDict[' ']) {
            numberMode = false;  // Reset number mode after space
        }
    }
    
    return englishOutput.join('');
}

// Main function to detect the input and translate
function main() {
    const args = process.argv.slice(2);
    const input = args.join(' ');
    
    if (/^[O\.]+$/.test(input.replace(/\s/g, ''))) {
        // Input is Braille
        console.log(brailleToEnglish(input));
    } else {
        // Input is English
        console.log(englishToBraille(input));
    }
}

// Execute the main function
main();
