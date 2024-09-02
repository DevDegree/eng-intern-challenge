const brailleToEnglish = {
    // a to z
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z',
    // capitalization, number mode, space, and punctuation
    '.....O': 'CAP', '.O.OOO': 'NUM', '......': ' ',
    '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!', '..O.O.': ';', '..OO..': ':',
    '....OO': '-', '.OO..O': '<', 'O..OO.PUNCT': '>', 'O.O..O': '(', '.O.OO.': ')',
    // combined numbers with the number indicator
    '.O.OOOO.....': '1', '.O.OOOO.O...': '2', '.O.OOOOO....': '3', '.O.OOOOO.O..': '4', '.O.OOOO..O..': '5',
    '.O.OOOOOO...': '6', '.O.OOOOOOO..': '7', '.O.OOOO.OO..': '8', '.O.OOO.OO...': '9', '.O.OOO.OOO..': '0'
};

const englishToBraille = {
    // a to z
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    // capitalization, numbers, space, and punctuation
    'CAP': '.....O', 'NUM': '.O.OOO', ' ': '......',
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ';': '..O.O.',
    ':': '..OO..', '-': '....OO', '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.',
    'PUNCT': '.O.OOOO', // new punctuation mode thing just for this '>' bc its same as letter o... couldnt get it to work though NOO
    // uppercase letters
    'A': '.....O' + 'O.....', 'B': '.....O' + 'O.O...', 'C': '.....O' + 'OO....',
    'D': '.....O' + 'OO.O..', 'E': '.....O' + 'O..O..', 'F': '.....O' + 'OOO...',
    'G': '.....O' + 'OOOO..', 'H': '.....O' + 'O.OO..', 'I': '.....O' + '.OO...',
    'J': '.....O' + '.OOO..', 'K': '.....O' + 'O...O.', 'L': '.....O' + 'O.O.O.',
    'M': '.....O' + 'OO..O.', 'N': '.....O' + 'OO.OO.', 'O': '.....O' + 'O..OO.',
    'P': '.....O' + 'OOO.O.', 'Q': '.....O' + 'OOOOO.', 'R': '.....O' + 'O.OOO.',
    'S': '.....O' + '.OO.O.', 'T': '.....O' + '.OOOO.', 'U': '.....O' + 'O...OO',
    'V': '.....O' + 'O.O.OO', 'W': '.....O' + '.OOO.O', 'X': '.....O' + 'OO..OO',
    'Y': '.....O' + 'OO.OOO', 'Z': '.....O' + 'O..OOO',
    // numbers 1 to 0
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
};

// if input is Braille (only 'O' and '.')
function isBraille(input) {
    return /^[O.]+$/.test(input); // returns true if input only has 'O' and '.'
}

// translate English to Braille
function translateToBraille(input) {
    let output = ''; // store output
    let isNumberMode = false; // to check if we are in number mode

    for (const char of input) {
        // console.log(`Processing character: ${char}`); 
        if (char >= 'A' && char <= 'Z') { // check if uppercase
            // console.log(`Uppercase letter detected: ${char}`);
            output += englishToBraille['CAP'] + englishToBraille[char.toLowerCase()]; // add capitalization symbol and lowercase Braille
        } else if (char >= '0' && char <= '9') { // check if number
            // console.log(`Number detected: ${char}`);
            if (!isNumberMode) {
                // console.log('Entering number mode');
                output += englishToBraille['NUM']; // enter number mode
                isNumberMode = true;
            }
            output += englishToBraille[char]; // Braille for the number
        } else if (char === ' ') { // check if space
            // console.log('Space detected');
            output += englishToBraille[char];
            isNumberMode = false; // exit number mode when space is encountered
        } else {
            // console.log(`Regular character or punctuation detected: ${char}`);
            output += englishToBraille[char]; // Braille for regular lowercase letters or punctuation
        }
        // console.log(`Current output: ${output}`);
    }
    return output; // return the translated Braille output
}

// translate Braille to English
function translateToEnglish(input) {
    const words = input.split(' '); // split Braille input by spaces to handle words separately
    let output = ''; // store output
    let isNumberMode = false; // to check if we are in number mode
    let isCapitalNext = false; // to check if next letter needs to be capitalized

    words.forEach(word => {
        // console.log(`Processing word: ${word}`);
        for (let i = 0; i < word.length; i += 6) { // process by length of 6
            const brailleChar = word.substring(i, i + 6); // extract 6-dot Braille character
            // console.log(`Processing Braille character: ${brailleChar}`); 

            if (brailleChar === '.....O') { // check if capitalization 
                // console.log('Capitalization indicator detected');
                isCapitalNext = true; // set flag to capitalize the next English letter
                isNumberMode = false; // reset number mode if capitalization detected
            } else if (brailleChar === '.O.OOO') { // check if number mode
                // console.log('Number mode indicator detected');
                isNumberMode = true; // enter number mode
            } else {
                let englishChar;
                if (isNumberMode) {
                    // console.log('Number mode active');
                    // check if in number mode and translate as a number
                    englishChar = brailleToEnglish['.O.OOO' + brailleChar] || brailleToEnglish[brailleChar];
                    if (/\d/.test(englishChar)) { // ensure it’s a number
                        // console.log(`Translated to number: ${englishChar}`);
                        output += englishChar;
                    } else {
                        // console.log('Exiting number mode');
                        isNumberMode = false; // exit number mode if not a number
                        if (englishChar) {
                            // console.log(`Translated to regular character: ${englishChar}`);
                            output += englishChar; // translate as regular character
                        }
                    }
                } else {
                    englishChar = brailleToEnglish[brailleChar]; // translate Braille to English
                    if (isCapitalNext) {
                        // console.log(`Capitalizing letter: ${englishChar}`);
                        englishChar = englishChar.toUpperCase(); // capitalize the English letter
                        isCapitalNext = false; // reset capitalization flag after use
                    }
                    output += englishChar; // assemble output
                }
            }
        }
        isNumberMode = false; // reset number mode after each word
        output += ' '; // add space between words in English output
        // console.log(`Current output: ${output}`);
    });

    return output.trim(); // remove extra spaces
}

// determine input type and perform translation
function main() {
    const input = process.argv.slice(2).join(' '); // get all command-line arguments after `node translator.js`

    if (isBraille(input)) {
        console.log(translateToEnglish(input));
    } else {
        console.log(translateToBraille(input));
    }
}

main();
