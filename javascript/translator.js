// Create an Object for mapping English characters, numbers, space, capitalization to their Braille equivalents.
const brailleAlphabet = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......',
    'capital': '.....O',
    'number': '.O.OOO'
};

// Create the reverse mapping 
const englishAlphabet = {};
for (let char in brailleAlphabet) {
    englishAlphabet[brailleAlphabet[char]] = char;
}

// Create Function to check if input is Braille
function isBraille(input) {
    for (let i = 0; i < input.length; i++) {
        if (input[i] !== 'O' && input[i] !== '.') {
            return false;
        }
    }
    return true;
}

// Create Function to translate from English to Braille
function englishToBraille(text) {
    let resulte = '';
    let isNumber = false;

    for (let i = 0; i < text.length; i++) {
        let char = text[i];
        if (char >= '0' && char <= '9') {
            if (!isNumber) {
                resulte += brailleAlphabet['number'];
                isNumber = true;
            }
            char = String.fromCharCode(char.charCodeAt(0) - 48 + 97);
        } else {
            isNumber = false;
            if (char === char.toUpperCase() && char !== ' ') {
                resulte += brailleAlphabet['capital'];
                char = char.toLowerCase();
            }
        }
        resulte += brailleAlphabet[char] || '';
    }
    return resulte;
}

// Create Function to translate from Braille to English
function brailleToEnglish(braille) {
    let result = '';
    let isCapital = false;
    let isNumber = false;

    for (let i = 0; i < braille.length; i += 6) {
        let char = braille.slice(i, i + 6);
        if (char === brailleAlphabet['capital']) {
            isCapital = true;
        } else if (char === brailleAlphabet['number']) {
            isNumber = true;
        } else {
            let translated = englishAlphabet[char] || '';
            if (isCapital) {
                translated = translated.toUpperCase();
                isCapital = false;
            }
            if (isNumber) {
                if (translated >= 'a' && translated <= 'j') {
                    let num = translated.charCodeAt(0) - 97 + 1;
                    translated = num === 10 ? '0' : num.toString();
                } else if (translated === ' ') {
                    isNumber = false;
                }
            }
            result += translated;
        }
    }
    return result;
}

// Create Main function to Call translation functions (brailleToEnglish(input) OR englishToBraille(input)) based on the input.
function translate(input) {
    if (isBraille(input)) {
        return brailleToEnglish(input);
    } else {
        return englishToBraille(input);
    }
}

// Get input from the command line and translate it 
let input = process.argv[2]
console.log(translate(input));
