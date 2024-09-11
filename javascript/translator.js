// Setting up the translator

// 1. Redefining the Braille code to differentiate between numbers and letters

// This map connects Braille symbols to English letters, numbers, and punctuation.
const brailleToEng = {
    'O.....': 'a', 
    'O.O...': 'b', 
    'OO....': 'c', 
    'OO.O..': 'd', 
    'O..O..': 'e',
    'OOO...': 'f', 
    'OOOO..': 'g', 
    'O.OO..': 'h', 
    '.OO...': 'i', 
    '.OOO..': 'j',
    'O...O.': 'k', 
    'O.O.O.': 'l', 
    'OO..O.': 'm', 
    'OO.OO.': 'n', 
    'O..OO.': 'o',
    'OOO.O.': 'p', 
    'OOOOO.': 'q', 
    'O.OOO.': 'r', 
    '.OO.O.': 's', 
    '.OOOO.': 't',
    'O...OO': 'u', 
    'O.O.OO': 'v', 
    '.OOO.O': 'w', 
    'OO..OO': 'x', 
    'OO.OOO': 'y',
    'O..OOO': 'z', 
    '......': ' ',   
    '.....O': 'capf', 
    '.O...O':'decf', 
    '.O.OOO': 'numf', 
    '..OO.O':'.',     
    '..O...':',',     
    '..O.OO':'?',     
    '..OOO.':'!',    
    '..OO..':':',     
    '..O.O.':';',     
    '....OO':'-',     
    '.O..O.':'/',     
    '.OO..O':'<',     
    'O..OO.':'>',     
    'O.O..O':'(',    
    '.O.OO.':')'      
};

// Map specifically for numbers to their Braille symbols
const numbersMap = {
    '0': '.OOO..', 
    '1': 'O.....', 
    '2': 'O.O...', 
    '3': 'OO....',
    '4': 'OO.O..', 
    '5': 'O..O..', 
    '6': 'OOO...', 
    '7': 'OOOO..',
    '8': 'O.OO..', 
    '9': '.OO...' 
};

// Creating a reverse map to convert English letters to Braille symbols
const engToBraille = {};

// Filling the map with English characters and their Braille equivalents, avoiding prefixes
Object.keys(brailleToEng).forEach(key => {

    if (brailleToEng[key] !== 'capf' && brailleToEng[key] !== 'numf') {
        engToBraille[brailleToEng[key]] = key;
    }

});

// Adding numbers to the English-to-Braille map
Object.keys(numbersMap).forEach(key => {

    engToBraille[key] = numbersMap[key];

});

// 2. Identifying the user input type (English or Braille)

function detectInputType(input) {
    
    // Check if input contains only Braille characters (dots and spaces)
    return /^[O. ]+$/.test(input) ? 'braille' : 'english';
}

// 3. Translating from English to Braille

function translateToBraille(input) {
    let output = '';

    // Flag to track if we're in a number sequence
    let isNum = false; 

    // Loop through each character in the input
    for (let i = 0; i < input.length; i++) {
        const char = input[i];

        // Check for uppercase letters and add a capitalization prefix
        if (/[A-Z]/.test(char) && char !== ' ') {
            output += '.....O'; // Prefix indicating the next letter is uppercase
        }

        // Check if the character is a number
        if (/[0-9]/.test(char)) {
            if (!isNum) {
                output += '.O.OOO'; // Add number prefix at the start of the number sequence
                isNum = true;
            }
            output += numbersMap[char]; // Add the Braille symbol for the number
        } else {
            // If switching from a number sequence, reset the flag
            if (isNum) { 
                isNum = false; 
            }
            // Handle spaces
            if (char === ' ') {
                output += '......'; // Add space in Braille
            } else {
                // Convert regular letters to Braille
                output += engToBraille[char.toLowerCase()] || ''; 
            }
        }
    }
    return output;
}

// 4. Translating from Braille to English
function translateToEng(input) {
    let output = '';

    // Flags for capitalization and number sequences
    let isCap = false; 
    let isNum = false; 

    // Process input in chunks of 6 characters (each Braille symbol)
    for (let i = 0; i < input.length; i += 6) {
        const slice = input.slice(i, i + 6);

        // Detect capitalization prefix
        if (slice === '.....O') { 
            isCap = true;
            continue; // Skip to the next symbol
        }

        // Detect number sequence prefix
        if (slice === '.O.OOO') { 
            isNum = true;
            continue; // Skip to the next symbol
        }

        // Handle spaces unless it's part of a number sequence
        if (slice === '......' && !isNum) {
            output += ' ';
            continue;
        }

        // Find the corresponding character for the Braille symbol
        let char = isNum ? Object.keys(numbersMap).find(key => numbersMap[key] === slice) : brailleToEng[slice];

        // If capitalization is flagged, make the character uppercase
        if (isCap && char) {
            char = char.toUpperCase();
            isCap = false;
        }

        // Add the character to the output, and handle end of number sequences
        output += char || '';
        if (slice === '......' && isNum) {
            isNum = false; 
        }
    }
    return output;
}

// 5. Main function to decide the direction of translation and perform it

function translate(input) {
    const type = detectInputType(input); // Determine if input is English or Braille
    return type === 'braille' ? translateToEng(input) : translateToBraille(input); // Perform the correct translation
}

// Handling command line input using Node.js
const input = process.argv.slice(2).join(' '); // Join input arguments into a single string
console.log(translate(input)); // Output the translated text
