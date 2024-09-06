
const brailleAlphabet: { [key: string]: string } = {
    // Letters
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',

    // Numbers 
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',

    // Special symbols
    'capital': '.....O', // Capital follows
    'number': '.O.OOO',  // Number follows
    'space': '......'    // Space
};

// Reverse mapping
const brailleToEnglish: { [key: string]: string } = {};
for (let key in brailleAlphabet) {
    brailleToEnglish[brailleAlphabet[key]] = key;
}

const translateToBraille = (input: string): string => {
    let result = '';
    let numberMode = false;

    for (let char of input) {
        if (char === ' ') {
            result += brailleAlphabet['space'];
            numberMode = false; // Reset number mode after a space
        } else if (/[A-Z]/.test(char)) {
            result += brailleAlphabet['capital'];
            result += brailleAlphabet[char.toLowerCase()];
        } else if (/[0-9]/.test(char)) {
            if (!numberMode) {
                result += brailleAlphabet['number'];
                numberMode = true;
            }
            result += brailleAlphabet[char];
        } else if (/[a-z]/.test(char)) {
            result += brailleAlphabet[char];
            numberMode = false; // Letters break number mode
        }
    }
    return result;
}

// Translate Braille to English
const translateToEnglish = (input: string): string => {
    let result = '';
    let numberMode = false;
    let capitalMode = false;

    for (let i = 0; i < input.length; i += 6) {
        const brailleChar = input.substring(i, i + 6);

        if (brailleChar === brailleAlphabet['space']) {
            result += ' ';
            numberMode = false; // Reset number mode after a space
        } else if (brailleChar === brailleAlphabet['capital']) {
            capitalMode = true;
        } else if (brailleChar === brailleAlphabet['number']) {
            numberMode = true;
        } else {
            let char = brailleToEnglish[brailleChar];
            if (typeof char === 'undefined') {
                // Invalid braille character
                throw 'Invalid braille character: ' + brailleChar;
            }
            if (numberMode && /[a-j]/.test(char)) {
                // Numbers in Braille are represented by letters a-j
                const numberMapping: { [key: string]: string } = {
                    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
                    'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
                };
                result += numberMapping[char];
            } else {
                if (capitalMode) {
                    result += char.toUpperCase();
                    capitalMode = false;
                } else {
                    result += char;
                }
            }
        }
    }
    return result;
}


function main() {
    const args = process.argv.slice(2); // Get args
    const input = args.join(' '); // Join them as one string

    if (/^[O.]+$/.test(input)) {
        if (input.length % 6 !== 0) {
            //log an error if the input isn't valid braille
            throw 'Invalid input: Braille was invalid, the length must be a multiple of 6'
        }

        //if input is all braille, translate to english
        console.log(translateToEnglish(input));
    } else {
        // Otherwise, translate to braille from english
        console.log(translateToBraille(input));
    }
}

main();
