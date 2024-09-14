const message = process.argv.slice(2).join(' ');

const brailleAlphabet: { [key: string]: string } = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',

    'capital': '.....O',
    'number': '.O.OOO', 
    'space': '......'
};

const brailleNumbers: { [key: string]: string } = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
};

const reversedBrailleAlphabet = Object.fromEntries(
    Object.entries(brailleAlphabet).map(([key, value]) => [value, key])
);

const reversedBrailleNumbers = Object.fromEntries(
    Object.entries(brailleNumbers).map(([key, value]) => [value, key])
);

// Determines if message is in Braille or English and translate accordingly
function translate(message: string) {
    if (/^[O.]+$/.test(message)) {
        return brailleToEnglish(message);
    }
    else if (/^[a-zA-Z0-9\s]+$/.test(message)) {
        return englishToBraille(message);
    }
    return "Invalid input";
}

// Translates English message to Braille
function englishToBraille(message: string): string {
    let currChar: string;
    let translatedMessage = "";

    // Iterate through each character in the message and append its Braille value to the translated message
    for (let i = 0; i < message.length; i++) {
        currChar = message[i];
        // Case 1: Character is capital letter
        if (/^[A-Z]$/.test(currChar)) {
            translatedMessage += brailleAlphabet['capital'] + brailleAlphabet[currChar.toLowerCase()];
        }
        // Case 2: Number
        else if (/^[0-9]$/.test(currChar)) {
            // If previous character was also a number, simply append the braille translation of the number
            if (i - 1 >= 0 && /^[0-9]$/.test(message[i-1])) {
                translatedMessage += brailleNumbers[currChar];
            }
            else {
                translatedMessage += brailleAlphabet['number'] + brailleNumbers[currChar];
            }
        }
        // Case 3: Space
        else if (currChar === ' ') {
            translatedMessage += brailleAlphabet['space'];
        }
        // Case 4: Lowercase letter
        else translatedMessage += brailleAlphabet[currChar];
    }

    return translatedMessage;
}

// Translates Braille message to English
// **NOTE**: if 6-character substring does not correspond to an english value, 
// I assume to ignore it and move to next substring
function brailleToEnglish(message: string): string {
    let currChar: string;
    let translatedMessage: string = "";

    // Iterate through each 6 character Braille substring and translate it to English character
    for (let i = 0; i < message.length; i += 6) {
        // Get English value of Braille substring
        currChar = reversedBrailleAlphabet[message.slice(i, i + 6)];

        // Case 1: Capital letter
        if (currChar === 'capital') {
            // Get next character
            i += 6;
            currChar = reversedBrailleAlphabet[message.slice(i, i + 6)]
            // If next character is a letter, then apppend capitalized letter to message
            if (/^[a-z]$/.test(currChar)) {
                translatedMessage += currChar.toUpperCase();
            }
        }
        // Case 2: Number
        else if (currChar === 'number') {
            // Convert every subsequent substring to a number until it does not correspond to one
            // or the message is completely translated
            i += 6;
            while (i < message.length && reversedBrailleNumbers[message.slice(i, i + 6)]) {
                translatedMessage += reversedBrailleNumbers[message.slice(i, i + 6)];
                i += 6;
            }
            i -= 6;
        }
        // Case 3: Space
        else if (currChar === 'space') {
            translatedMessage += ' ';
        }
        // Case 4: Lowercase letter
        else if (currChar) {
            translatedMessage += currChar;
        }
    }
    return translatedMessage;
}
// Print translated message
console.log(translate(message));