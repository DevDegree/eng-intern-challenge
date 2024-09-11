/*
This is a braille translating application, that will take an input from the terminal representing either a braille string or text string.
The inputted string will then be translated to the corresponding language, either text->braille or braille->text.
The main function "translate(input)"" takes the entered input from the terminal and will determine whether or not it is in a braille or text format, 
and then perform the necessary operations to translate it.
*/

// Mapping of letters to their corresponding Braille representation 
const brailleMap = {
    "a" : "O.....",
    "b" : "O.O...",
    "c" : "OO....",
    "d" : "OO.O..",
    "e" : "O..O..",
    "f" : "OOO...",
    "g" : "OOOO..",
    "h" : "O.OO..",
    "i" : ".OO...",
    "j" : ".OOO..",
    "k" : "O...O.",
    "l" : "O.O.O.",
    "m" : "OO..O.",
    "n" : "OO.OO.",
    "o" : "O..OO.",
    "p" : "OOO.O.",
    "q" : "OOOOO.",
    "r" : "O.OOO.",
    "s" : ".OO.O.",
    "t" : ".OOOO.",
    "u" : "O...OO",
    "v" : "O.O.OO",
    "w" : ".OOO.O",
    "x" : "OO..OO",
    "y" : "OO.OOO",
    "z" : "O..OOO"
};

// Mapping of numbers to their corresponding Braille representation
const numberMap = {
    "1" : "O.....",
    "2" : "O.O...",
    "3" : "OO....",
    "4" : "OO.O..",
    "5" : "O..O..",
    "6" : "OOO...",
    "7" : "OOOO..",
    "8" : "O.OO..",
    "9" : ".OO...",
    "0" : ".OOO.."
};

// Mapping of symbols to their corresponding Braille representation
const symbolCharMap = {
    "." : "..OO.O",
    "," : "..O...",
    "?" : "..O.OO",
    "!" : "..OOO.",
    ":" : "..OO..",
    ";" : "..O.O.",
    "-" : "....OO",
    "/" : ".O..O.",
    "<" : ".OO..O",
    "(" : "O.O..O",
    ")" : ".O.OO."
};

const symbolMap = Object.fromEntries(Object.entries(symbolCharMap).map(([k, v]) => [v, k]));
const letterMap = Object.fromEntries(Object.entries(brailleMap).map(([k, v]) => [v, k]));
const NumberMap = Object.fromEntries(Object.entries(numberMap).map(([k, v]) => [v, k]));

const numberIndicator = '.O.OOO'; // Braille representation for number indicator
const spaceIndicator = '......'; // Braille representation for space
const capitalIndicator = '.....O'; // Braille representation for capital letter indicator

function translate(input) {
    let isNumberMode = false; // Flag to indicate if the next characters should be interpreted as numbers
    let isCapitalNext = false; // Flag to indicate if the next character should be capitalized
    let result = '';

    // Checking if the input is in braille format using regex, and converting it to alphanumeric format.
    if (/^[.O]+$/.test(input)) {

        // Input is Braille, translate every 6 characters to a letter or number (3x2 matrix for one braille char)
        for (let i = 0; i < input.length; i += 6) {
            let brailleChar = input.slice(i, i + 6);

            // Check if next input will be a number
            if (brailleChar === numberIndicator) {
                isNumberMode = true;
            }

            // Check if the braille character is a space (if it is, numbermode MUST be false)
             else if (brailleChar === spaceIndicator) {
                result += ' ';
                isNumberMode = false; 
            } 
            
            // Check if next input will be a capitalized letter
            else if (brailleChar === capitalIndicator) {
                isCapitalNext = true;
            } 
            
            // Check if braille character is a special symbol
            else if(Object.keys(symbolMap).includes(brailleChar)){ 
                result+= symbolMap[brailleChar] || 'Invalid input';
            }

            // Check if the braille character is a number or letter and add appropriate one to result
            else {
                // Only add number if numbermode is true
                if (isNumberMode) {
                    result += NumberMap[brailleChar] || 'Invalid input';
                } else {
                    let letter = letterMap[brailleChar] || 'Invalid input';

                    // Check if letter must be capitalized
                    if (isCapitalNext) {
                        letter = letter.toUpperCase();
                        isCapitalNext = false; 
                    }
                    result += letter;
                }
            }
        }
    } else 
    {
        // Input is text, translate each character to Braille
        for (let char of input) {

            // Check if char is a space 
            // If it is, numbermode must be false
            if (char === ' ') {
                result += spaceIndicator;
                isNumberMode = false;
                continue;
            }

            // Check if char is a special character
            if(Object.values(symbolMap).includes(char)){
                result+= symbolMap[char] || 'Invalid input';
                continue;
            }

            // Check if char is a number
            if (/[0-9]/.test(char)) {
                //if numbermode is false, add number indicator braille character
                if (!isNumberMode) {
                    result += numberIndicator;
                    isNumberMode = true;
                }
                result += numberMap[char];
            } 
            else {
                // Check if the char is capitalized
                // If it is, add capitalindicator braille character
                if (char === char.toUpperCase()) {
                    result += capitalIndicator;
                }
                result += brailleMap[char.toLowerCase()];
            }
        }
    }
    // Removing trailing spaces
    return result.trim();
}

// Joining the argumments and printing the translated input
if (require.main === module) {
    const input = process.argv.slice(2).join(" ");
    console.log(translate(input));
  }
