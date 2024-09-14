// Create a map of Braille characters to English characters using object literals
const brailleMap = {
    // English letters
    a: 'O.....', b: 'O.O...', c: 'OO....', d: 'OO.O..', e: 'O..O..',
    f: 'OOO...', g: 'OOOO..', h: 'O.OO..', i: '.OO...', j: '.OOO..',
    k: 'O...O.', l: 'O.O.O.', m: 'OO..O.', n: 'OO.OO.', o: 'O..OO.',
    p: 'OOO.O.', q: 'OOOOO.', r: 'O.OOO.', s: '.OO.O.', t: '.OOOO.',
    u: 'O...OO', v: 'O.O.OO', w: '.OOO.O', x: 'OO..OO', y: 'OO.OOO', z: 'O..OOO',
    // Numbers
    1: 'O.....', 2: 'O.O...', 3: 'OO....', 4: 'OO.O..', 5: 'O..O..',
    6: 'OOO...', 7: 'OOOO..', 8: 'O.OO..', 9: '.OO...', 0: '.OOO..',
    // Special characters
    ' ': '......', capital: '.....O', number: '.O.OOO'
};

// Reverse mapping for Braille to character conversion
const brailleToChar = Object.fromEntries(Object.entries(brailleMap).map(([k, v]) => [v, k]));

// Function to split input into chunks of 6 characters each
function splitIntoChunks(input, chunkSize = 6) {
    const characters = [];
    for (let i = 0; i < input.length; i += chunkSize) {
        characters.push(input.slice(i, i + chunkSize));
    }
    return characters;
}

// Function to check if the input is Braille
function isBraille(input) {

    // Split the input into chunks of 6 characters each
    const characters = splitIntoChunks(input);

    // Check if all characters are valid Braille characters
    const isBraille = characters.every(char => brailleToChar[char] !== undefined);

    return isBraille;

}


// Function to translate English to Braille
function englishToBraille(input) {

    // Return empty string if a number followed by a letter without a space
    if (/[0-9][a-zA-Z]/.test(input)) {
        return '';
    }

    let result = '';
    let isNumberMode = false;

    for (let char of input) {
        // Check if the character is a capital letter
        if (/[A-Z]/.test(char)) {

            // Exit number mode
            isNumberMode = false;

            // Add the capital indicator and the value of the character in lowercase
            result += brailleMap.capital + brailleMap[char.toLowerCase()];

            // Check if the character is a lowercase letter
        } else if (/[a-z]/.test(char)) {

            // Exit number mode
            isNumberMode = false;

            // Add the value of the character
            result += brailleMap[char];


            // Check if the character is a number
        } else if (/[0-9]/.test(char)) {

            // Enter number mode
            if (!isNumberMode) {
                result += brailleMap.number;
                isNumberMode = true;
            }
            // Add the value of the number
            result += brailleMap[char];

            // Check if the character is a space
        } else if (char === ' ') {

            // Exit number mode
            isNumberMode = false;
            // Add the space
            result += brailleMap[' '];

        } else {

            // Return empty string if the character is not a letter, number, or space
            return '';
        }
    }

    return result;
}



// Function to translate Braille to English
function brailleToEnglish(input) {

    // Split the input into chunks of 6 characters each
    const characters = splitIntoChunks(input);

    let result = '';
    let capitalizeNext = false;
    let isNumber = false;

    for (let i = 0; i < characters.length; i++) {
        const brailleChar = characters[i];

        // Check if the character is a capital indicator
        if (brailleChar === brailleMap.capital) {

            // In number mode, a capital indicator should not appear
            if (isNumber) {
                return '';
            }

            capitalizeNext = true;
            continue;
        }

        // Check if the character is a number indicator
        if (brailleChar === brailleMap.number) {

            // In number mode, another number indicator should not appear
            if (isNumber) {
                return '';
            }

            isNumber = true;
            continue;
        }

        // Check if the character is a space
        if (brailleChar === brailleMap[' ']) {
            
            result += ' ';

            // Stop number mode after a space
            isNumber = false;

            continue;
        }

        // Get the English character corresponding to the Braille character
        let char = brailleToChar[brailleChar] || '';

        // Handle numbers
        if (isNumber && char) {
            // If the corresponding character is (a-j)
            if (/[a-j]/.test(char)) {
                // Replace the character with the corresponding number (1-9)
                const numberEquivalent = '1234567890'['abcdefghij'.indexOf(char)];
                char = numberEquivalent || char;

                // If the corresponding character is (k-z)
            } else if (/[k-z]/.test(char)) {
                // In number mode, should not have (k-z) Braille characters
                // Return empty string to quit
                return '';
            }

        }

        // Handle capitalization
        if (capitalizeNext && char) {
            char = char.toUpperCase();
            capitalizeNext = false;
        }

        result += char;
    }

    return result;
}

// Main function to handle input and output
function main() {
    const input = process.argv.slice(2).join(' ');
    if (isBraille(input)) {
        console.log(brailleToEnglish(input));
    } else {
        console.log(englishToBraille(input));
    }
}

main();