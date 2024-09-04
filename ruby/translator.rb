/*storing the braille alphabets for alphabets*/
const brailleAlphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......',
    'capital': '.....O',  
    'number': '.O.OOO'   
};

/* storing numbers format of braille*/
const brailleDigits = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
};
/*checking if input is in braille or english */
function detectInputType(input) {
    if (/^[O.]+$/.test(input)) {  // If all characters are 'O' or '.'
        return 'braille';
    } else {
        return 'english';
    }
}
/*converting to braille with english input*/
function translateToBraille(input) {
    let result = '';
    let numberMode = false;
/*iterating for input*/
    for (let char of input) {
        if (char >= 'A' && char <= 'Z') {
          /*coverting to braille*/
            result += brailleAlphabet['capital'];
            char = char.toLowerCase();
        }
/*checking for numbers*/
        if (char >= '0' && char <= '9') {
            if (!numberMode) { /*if number is true*/
              /*convert to number*/
                result += brailleAlphabet['number'];
                numberMode = true;
            }
            result += brailleDigits[char];
        } else {
            numberMode = false;
            result += brailleAlphabet[char];
        }
    }
/*return string */
    return result;
}
/*converting braille to english*/
function translateToEnglish(input) {
    let result = '';
    let isCapital = false;
    let isNumber = false;
/*interating through input length */
  /*since braille words are seperated in 6 characters hence i+=6*/
    for (let i = 0; i < input.length; i += 6) {
        const char = input.substring(i, i + 6);
/*checking edge cases*/
        if (char === brailleAlphabet['capital']) {
            isCapital = true;
        } else if (char === brailleAlphabet['number']) {
            isNumber = true;
        }
          /*converting to enlish*/
        else {
            if (isNumber) {
                for (const [key, value] of Object.entries(brailleDigits)) {
                    if (value === char) {
                        result += key;
                        break;
                    }
                }
                isNumber = false;
            } else {
                for (const [key, value] of Object.entries(brailleAlphabet)) {
                    if (value === char) {
                        result += isCapital ? key.toUpperCase() : key;
                        isCapital = false;
                        break;
                    }
                }
            }
        }
    }

    return result;
}
/*checking input and translating it*/
function translator(input) {
    const inputType = detectInputType(input);
    if (inputType === 'english') {
        return translateToBraille(input);
    } else if (inputType === 'braille') {
        return translateToEnglish(input);
    }
} 
