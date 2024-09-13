const alphabetToBraille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    'capital': '.....O', 'number': '.O.OOO', ' ': '......'
};

const brailleToAlphabet = Object.fromEntries(
    Object.entries(alphabetToBraille).map(([key, value]) => [value, key])
);


const numToBraille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

const brailleToNum = Object.fromEntries(
    Object.entries(numToBraille).map(([key, value]) => [value, key])
);

// Check if text is in Braille
const isBraille = (text) => {
    const braillePattern = /^[O.]+$/;
    return braillePattern.test(text);
}

// Convert braille to english
const brailleToEnglish = (text) => {
    let english = "";
    let isNum = false;
    let isCapital = false;

    for (let i = 0; i < text.length; i+=6) {
        let braille = text.slice(i, i+6);
        let char = "";

        if (brailleToAlphabet[braille] === ' ') {
            isNum = false;
        }

        if (isNum) {
            char = brailleToNum[braille];
        } else {
            char = brailleToAlphabet[braille];
            if (isCapital) {
                char = char.toUpperCase();
                isCapital = false;
            }
        }

        if (char === 'capital') {
            isCapital = true;
            continue;
        } else if (char === 'number') {
            isNum = true;
            continue;
        }
        
        english += char;
    }

    return english;
}

const englishToBraille = (text) => {
    let braille = "";
    let isNum = false;

    for (const char of text) {
        let brailleChars = "";
        if (!isNaN(parseInt(char))) {
            if (isNum) {
                brailleChars = numToBraille[char];
            } else {
                isNum = true;
                braille += alphabetToBraille['number']
                brailleChars = numToBraille[char];
            }
        } else {
            if (char === ' ') {
                braille += alphabetToBraille[char];
                continue;
            }
            if (char.toUpperCase() === char) {
                braille += alphabetToBraille['capital'];
                brailleChars = alphabetToBraille[char.toLowerCase()];
            } else {
                brailleChars = alphabetToBraille[char];
            }          
        }

        braille += brailleChars;
    }

    return braille;
}

// Get text from command line
const text = process.argv.slice(2).join(" ");
let result = "";

if (isBraille(text)) {
    result = brailleToEnglish(text);
} else {
    result = englishToBraille(text);
}
console.log(result);
