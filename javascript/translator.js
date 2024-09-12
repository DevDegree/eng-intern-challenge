/**
 * Kirill Kirnichansky, kirill@kirnichansky.com
 * 
 * The technical requirements specifically say to implement letters a-z, numbers 0-9 and ability to include spaces.
 * Therefore, I have not implemented any of the special characters (including decimal logic) in the program.  
 * 
 * In the case special characters are expected, I ask that you consider commit 8036c851459ad367e4f37f83edf5dece452d63f1
 * where I added logic for special characters (excluding < & >) that is commented out.
 */

const args = process.argv.slice(2);
let input;

// check if an argument is passed 
if (args.length > 0) {
    input = args.join(' ');
} else {
    return;
}

// map of English characters to its Braille equivalent 
const englishToBraille = {
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
    'capital': '.....O',
    'number': '.O.OOO',
    'space': '......'
};

// This method accepts a string of expected English content and returns the Braille translation.
function translateEnglishToBraille(input) {
    let braille = "";
    // flag to check if currently translating a number
    let isNumber = false;
    for (let i = 0; i < input.length; i++) {
        let char = input[i];
        switch (char) {
            case ' ':
                braille += englishToBraille['space'];
                // a space will terminate translation of a number
                isNumber = false;
                break;
            default:
                // check if numeric
                if (/^[0-9]$/.test(char)) {
                    if (!isNumber) {
                        braille += englishToBraille['number'];
                        isNumber = true;
                    }
                    // the first 10 letters of the alphabet have the same Braille symbols as the digits 1,2,...,9,0 , respectively
                    // therefore, since we know we are currently translating a number we can get the letter symbol corresponding to the digit through ASCII values (1 -> a, 2 -> b, ...)
                    // the special case is when the digit is 0 where we just use the symbol for 'j'.
                    let charFromDigit = parseInt(char) == 0 ? 'j' : String.fromCharCode(parseInt(char)+96);
                    braille += englishToBraille[charFromDigit];
                } else {
                    // check if capital
                    if (char == char.toUpperCase() && char != char.toLowerCase()) {
                        braille += englishToBraille['capital'];
                        char = char.toLowerCase();
                    }
    
                    braille += englishToBraille[char];
                }
        }
    }

    return braille;
}

// This method accepts a string of expected Braille content and returns the English translation.
function translateBrailleToEnglish(input) {
    // create a reverse map of the englishToBraille dict
    let brailleToEnglish = {};
    for (const key in englishToBraille)
        brailleToEnglish[englishToBraille[key]] = key;

    let english = "";
    // flags used to check if currently translating a number or capital letter
    let isCapital = false;
    let isNumber = false;
    // loop through input with a step size of 6 since Braille symbols are 6 characters long
    // 'i' will always be the index of the first char in a Braille symbol 
    for (let i = 0; i < input.length; i+=6) {
        let char = brailleToEnglish[input.slice(i, i+6)];
        switch (char) {
            case 'capital':
                // set flag so program knows the next char is capitalized
                isCapital = true;
                break;
            case 'space':
                english += " ";
                // a space will terminate translation of a number
                isNumber = false;
                break;
            case 'number':
                // set flag so program knows it is translating a number
                isNumber = true;
                break;
            default:
                if (isCapital) {
                    english += char.toUpperCase();
                    // captial flag is only valid for one char 
                    isCapital = false;
                } else if (isNumber) {
                    // the first 10 letters of the alphabet have the same Braille symbols as the digits 1,2,...,9,0 , respectively
                    // therefore, since we know we are currently translating a number we can get the digit in respect to the ASCII value of the letter (a -> 1, b -> 2, ...)
                    let number = char.charCodeAt(0) - 96;
                    // since the first letter (a) is maps to 1, the 10th letter (j) maps to 0 instead of 10
                    // assuming a valid input, we should never get a number > 10 (as there are only 10 digits), but the program will translate the symbol to nothing in that case 
                    english += number == 10 ? 0 : number < 10 ? number : "";
                } else {
                    english += char;
                }
        }
    }
    return english;
}

const uniqueCharSet = new Set(input);
// since special characters are not included in the translation logic we can identify if the input string is Braille if it contains the '.' char
// there are no Braille symbols with only raised dots ('O'), atleast for the Braille symbols in question 
// therfore, we can always expect a Braille string to contain a '.' 
if (uniqueCharSet.has('.'))
    console.log(translateBrailleToEnglish(input))
else
    console.log(translateEnglishToBraille(input));