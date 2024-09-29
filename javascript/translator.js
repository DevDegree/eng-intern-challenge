// tu run the code:
// node translator.js "Hello World"
// node translator.js "O..... O.O... ...... O..O.. OOO..."

// Dictionary to map each English letter, number, and symbol to its corresponding Braille representation
const brailleDict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    'cap': '.....O', 
    'num': '.O.OOO',
    'space': '......', 
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
};

// Create a reverse mapping from Braille to English
const brailleToEnglishDict = Object.fromEntries(
    Object.entries(brailleDict).map(([englishChar, braille]) => [braille, englishChar])
);

// Helper function to check if the input is Braille (it should contain only 'O', '.' and spaces)
function isBraille(input) {
    return /^[O. ]+$/.test(input.trim());  // Regular expression to verify Braille characters
}

// Function to translate from English to Braille
function translateToBraille(text) {
    let brailleOutput = [];  // Store translated Braille symbols
    let numberMode = false;  // Track if we are in "number mode" (when a number marker has been detected)

    for (let char of text) {
        // Handle numbers: activate number mode and translate digits
        if (/\d/.test(char) && !numberMode) {
            brailleOutput.push(brailleDict['num']);  // Add the number marker
            numberMode = true;  // Enter number mode
        } else if (/[a-zA-Z]/.test(char) && numberMode) {
            numberMode = false;  // Exit number mode when we encounter a letter
        }

        // Translate space
        if (char === ' ') {
            brailleOutput.push(brailleDict['space']);
        }
        // Translate numbers (while in number mode)
        else if (/\d/.test(char)) {
            brailleOutput.push(brailleDict[char]);
        }
        // Translate letters (with capitalization handling)
        else if (/[a-zA-Z]/.test(char)) {
            if (char === char.toUpperCase()) {
                brailleOutput.push(brailleDict['cap']);  // Add capitalization marker for uppercase letters
            }
            brailleOutput.push(brailleDict[char.toLowerCase()]);  // Add corresponding Braille symbol
        }
    }
    return brailleOutput.join(' ');  // Join all symbols with spaces between them
}

// Function to translate from Braille to English
function translateFromBraille(brailleText) {
    const brailleSymbols = brailleText.split(' ');  // Split Braille input into individual symbols
    let englishOutput = [];  // Store the translated English characters
    let numberMode = false;  // Track if we are in "number mode"
    let capitalizeNext = false;  // Track if the next letter should be capitalized

    for (let symbol of brailleSymbols) {
        // Handle the number marker: enter number mode
        if (symbol === brailleDict['num']) {
            numberMode = true;
            continue;
        }
        // Handle capitalization marker: capitalize the next letter
        else if (symbol === brailleDict['cap']) {
            capitalizeNext = true;
            continue;
        }
        // Translate space
        else if (symbol === brailleDict['space']) {
            englishOutput.push(' ');
            continue;
        }

        // Translate Braille to English (either number or letter)
        if (numberMode) {
            englishOutput.push(brailleToEnglishDict[symbol]);  // Add number
        } else {
            let char = brailleToEnglishDict[symbol];  // Get the corresponding letter
            if (capitalizeNext) {
                englishOutput.push(char.toUpperCase());  // Capitalize the letter if needed
                capitalizeNext = false;  // Reset capitalization flag
            } else {
                englishOutput.push(char);  // Add the letter as lowercase
            }
            numberMode = false;  // Reset number mode after each letter
        }
    }

    return englishOutput.join('');  // Join the English letters into a complete string
}

// Get the input from the terminal (first argument passed when running the script)
const input = process.argv[2];

// Determine if the input is in Braille or English and perform the appropriate translation
if (input) {
    const trimmedInput = input.trim();
    if (isBraille(trimmedInput)) {
        // If it's Braille, translate to English
        console.log(translateFromBraille(trimmedInput));
    } else {
        // Otherwise, translate from English to Braille
        console.log(translateToBraille(trimmedInput));
    }
} else {
    console.log("Please provide an input to translate.");
}

