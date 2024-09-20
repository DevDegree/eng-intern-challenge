const brailleDict = {
    'a': [[true, false], [false, false], [false, false]], // 'O.....'
    'b': [[true, false], [true, false], [false, false]],  // 'O.O...'
    'c': [[true, true], [false, false], [false, false]],  // 'OO....'
    'd': [[true, true], [false, true], [false, false]],   // 'OO.O..'
    'e': [[true, false], [false, true], [false, false]],  // 'O..O..'
    'f': [[true, true], [true, false], [false, false]],   // 'OOO...'
    'g': [[true, true], [true, true], [false, false]],    // 'OOOO..'
    'h': [[true, false], [true, true], [false, false]],   // 'O.OO..'
    'i': [[false, true], [true, false], [false, false]],  // '.OO...'
    'j': [[false, true], [true, true], [false, false]],   // '.OOO..'
    'k': [[true, false], [false, false], [true, false]],  // 'O...O.'
    'l': [[true, false], [true, false], [true, false]],   // 'O.O.O.'
    'm': [[true, true], [false, false], [true, false]],   // 'OO..O.'
    'n': [[true, true], [false, true], [true, false]],    // 'OO.OO.'
    'o': [[true, false], [false, true], [true, false]],   // 'O..OO.'
    'p': [[true, true], [true, false], [true, false]],    // 'OOO.O.'
    'q': [[true, true], [true, true], [true, false]],     // 'OOOOO.'
    'r': [[true, false], [true, true], [true, false]],    // 'O.OOO.'
    's': [[false, true], [true, false], [true, false]],   // '.OO.O.'
    't': [[false, true], [true, true], [true, false]],    // '.OOOO.'
    'u': [[true, false], [false, false], [true, true]],   // 'O...OO'
    'v': [[true, false], [true, false], [true, true]],    // 'O.O.OO'
    'w': [[false, true], [true, true], [false, true]],    // '.OOO.O'
    'x': [[true, true], [false, false], [true, true]],    // 'OO..OO'
    'y': [[true, true], [false, true], [true, true]],     // 'OO.OOO'
    'z': [[true, false], [false, true], [true, true]],    // 'O..OOO'
    '1': [[true, false], [false, false], [false, false]], // Same as 'a'
    '2': [[true, false], [true, false], [false, false]],  // Same as 'b'
    '3': [[true, true], [false, false], [false, false]],  // Same as 'c'
    '4': [[true, true], [false, true], [false, false]],   // Same as 'd'
    '5': [[true, false], [false, true], [false, false]],  // Same as 'e'
    '6': [[true, true], [true, false], [false, false]],   // Same as 'f'
    '7': [[true, true], [true, true], [false, false]],    // Same as 'g'
    '8': [[true, false], [true, true], [false, false]],   // Same as 'h'
    '9': [[false, true], [true, false], [false, false]],  // Same as 'i'
    '0': [[false, true], [true, true], [false, false]],   // Same as 'j'
    ' ': [[false, false], [false, false], [false, false]] // Space is empty
};

// Braille indicators
const capitalIndicator = [[false, false], [false, false], [false, true]];  // Capital follows: '.....O'
const numberIndicator = [[false, true], [false, true], [true, true]];      // Number follows: '.O.OOO'
const decimalPoint = [[false, true], [false, false], [false, true]];       // Decimal point: '.O...O'

// Create a reverse Braille lookup for Braille-to-text translation
function reverseBrailleDict() {
    const reverseDict = {};
    for (const [char, matrix] of Object.entries(brailleDict)) {
        reverseDict[matrixToBraille(matrix)] = char;
    }
    reverseDict[matrixToBraille(capitalIndicator)] = 'CAPITAL';
    reverseDict[matrixToBraille(numberIndicator)] = 'NUMBER';
    reverseDict[matrixToBraille(decimalPoint)] = '.';
    return reverseDict;
}

const reverseBraille = reverseBrailleDict();

// Convert a Braille matrix to string representation
function matrixToBraille(matrix) {
    return matrix.flat().map(dot => dot ? 'O' : '.').join('');
}

// Convert Braille back to text
function brailleToText(brailleString) {
    let result = [];
    let isCapitalMode = false;
    let isNumberMode = false;

    for (let i = 0; i < brailleString.length; i += 6) {
        const brailleChar = brailleString.slice(i, i + 6);
        const mappedChar = reverseBraille[brailleChar];

        if (mappedChar === 'CAPITAL') {
            isCapitalMode = true;
            continue;
        }
        if (mappedChar === 'NUMBER') {
            isNumberMode = true;
            continue;
        }

        if (isCapitalMode) {
            result.push(mappedChar.toUpperCase());
            isCapitalMode = false;
        } else if (isNumberMode) {
            result.push(mappedChar);
        } else {
            result.push(mappedChar);
        }

        if (mappedChar === ' ') {
            isNumberMode = false;
        }
    }

    return result.join('');
}

// Convert text to Braille
function translateToBraille(text) {
    let result = [];
    let isNumberMode = false;

    for (const char of text) {
        if (/\d/.test(char)) {  // If character is a digit
            if (!isNumberMode) {
                result.push(matrixToBraille(numberIndicator));  // Add number indicator
                isNumberMode = true;
            }
            result.push(matrixToBraille(brailleDict[char]));  // Add Braille equivalent of the digit
        } else if (/[a-zA-Z]/.test(char)) {  // If character is an alphabet
            if (isNumberMode) {
                isNumberMode = false;  // Exit number mode when an alphabet is encountered
            }
            if (char === char.toUpperCase()) {
                result.push(matrixToBraille(capitalIndicator));  // Add capital indicator for uppercase letters
            }
            result.push(matrixToBraille(brailleDict[char.toLowerCase()]));  // Add Braille equivalent of the letter
        } else if (char === '.') {  // If it's a decimal point
            result.push(matrixToBraille(decimalPoint));  // Add Braille equivalent for decimal point
        } else {
            result.push(matrixToBraille(brailleDict[char]));  // Handle spaces
            isNumberMode = false;  // Reset number mode for spaces
        }
    }

    return result.join('');
}

// Detect if the input is Braille or text
function detectAndTranslate(input) {
    if (/^[O.]+$/.test(input)) {
        // If the input consists only of O and ., it's Braille
        return brailleToText(input);
    } else {
        // Otherwise, it's text
        return translateToBraille(input);
    }
}

// Handle command line arguments and detect input type
if (require.main === module) {
    const inputText = process.argv.slice(2).join(' ');
    const output = detectAndTranslate(inputText);
    console.log(output);
}
