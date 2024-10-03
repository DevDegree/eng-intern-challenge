// Mapping English to Braille
var englishToBraille = {
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
    '0': '.OOO..',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    'CAPITAL': '..O...',
    'NUMBER': '.O.OOO'
};
// Mapping Braille to English
var brailleToEnglish = Object.fromEntries(Object.entries(englishToBraille).map(function (_a) {
    var key = _a[0], value = _a[1];
    return [value, key];
}));
// Check if the input is Braille
function isBraille(text) {
    return text.length % 6 === 0 && /^[O.]+$/.test(text); // Input should only consist of O and .
}
// Translator function to convert between English and Braille
function translate(text) {
    var numberMode = false;
    var capitalizeNext = false;
    var result = '';
    if (isBraille(text)) {
        // Braille to English conversion
        for (var i = 0; i < text.length; i += 6) {
            var brailleChar = text.substring(i, i + 6);
            var char = brailleToEnglish[brailleChar];
            if (char === 'NUMBER') {
                numberMode = true;
            }
            else if (char === 'CAPITAL') {
                capitalizeNext = true;
            }
            else if (numberMode && char >= 'a' && char <= 'j') {
                // Handle numbers (Braille numbers use 'a' to 'j')
                result += (char.charCodeAt(0) - 'a'.charCodeAt(0) + 1) % 10;
                numberMode = false;
            }
            else {
                result += capitalizeNext ? char.toUpperCase() : char;
                capitalizeNext = false;
            }
        }
    }
    else {
        // English to Braille conversion
        for (var _i = 0, text_1 = text; _i < text_1.length; _i++) {
            var char = text_1[_i];
            if (char >= 'A' && char <= 'Z') {
                result += englishToBraille['CAPITAL'] + englishToBraille[char.toLowerCase()];
            }
            else if (char >= '0' && char <= '9') {
                result += englishToBraille['NUMBER'] + englishToBraille[char];
            }
            else {
                result += englishToBraille[char] || '';
            }
        }
    }
    return result;
}
// Get input from command-line arguments
var args = process.argv.slice(2);
if (args.length !== 1) {
    console.error('Usage: translator <text>');
    process.exit(1);
}
var input = args[0];
var translatedText = translate(input);
console.log(translatedText);
