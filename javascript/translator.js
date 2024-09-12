/**
 * letters is an object that maps each letter to its Braille representation.
 */
const letters = {
    "a":"O.....",
    "b":"O.O...",
    "c":"OO....",
    "d":"OO.O..",
    "e":"O..O..",
    "f":"OOO...",
    "g":"OOOO..",
    "h":"O.OO..",
    "i":".OO...",
    "j":".OOO..",
    "k":"O...O.",
    "l":"O.O.O.",
    "m":"OO..O.",
    "n":"OO.OO.",
    "o":"O..OO.",
    "p":"OOO.O.",
    "q":"OOOOO.",
    "r":"O.OOO.",
    "s":".OO.O.",
    "t":".OOOO.",
    "u":"O...OO",
    "v":"O.O.OO",
    "w":".OOO.O",
    "x":"OO..OO",
    "y":"OO.OOO",
    "z":"O..OOO",
    " ":"......",
    ".":"..OO.O",
    ",":"..O...",
    "?":"..O.OO",
    "!":"..OOO.",
    ":":"..OO..",
    ";":"..O.O.",
    "-":"....OO",
    "/":".O..O.",
    "<":".OO..O",
    "(":"O.O..O",
    ")":".O.OO.",
    "cap":".....O",
    "num":".O.OOO", 
}
/**
 * brailleToLetters is an object that maps each Braille representation to its letter. I determined it was better to have both a braille table and an english table as it makes 
 * access to the information easier and more efficient.
 */
const brailleToLetters = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
    "......": " ",
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "O.O..O": "(",
    ".O.OO.": ")",
    ".....O": "cap",
    ".O.OOO": "num",
};

/**
 * numbers is an object that maps each number to its Braille representation.
 */
const numbers = {
    "1": "O.....",
    "2": "O.O...",
    "3":"OO....",
    "4":"OO.O..",
    "5":"O..O..",
    "6":"OOO...",
    "7":"OOOO..",
    "8":"O.OO..",
    "9":".OO...",
    "0":".OOO.."
}
/**
 * brailleToNumbers is an object that maps each Braille representation to its number. I determined it was better to have both a braille table and an english table as it makes 
 * access to the information easier and more efficient.
 */
const brailleToNumbers = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0"
}
/**
 * Will convert the given text to braille by iterating through each character and referencing the letters object. It will then add those values
 * to the result string. In the case that the value is a number using isNAN and checking that it is in the numbers object, it will then add the number as well as an
 * indicator for the first number in the sequence. If the character is capitalized, it will add an indicator for it and then add the lowercase version and if it is neither a 
 * number or a capital letter it will add the character as is. 
 * 
 * running time: O(n) where n is the length of the text
 * 
 * @param {String} text is the text that is to be converted to braille  
 * @returns the braille version for the text
 */

function toBraille(text) {
    let result = "";
    let inNumberSequence = false;  // Flag to track if we are in a sequence of numbers

    for (let i = 0; i < text.length; i++) {
        let char = text[i]; // get the character at the current index in the text

        if (!isNaN(char) && numbers[char]) {  // Check if the character is a number and inside of the numbers object
            if (!inNumberSequence) {  // Add number indicator only once at the start
                result += letters["num"]; 
                inNumberSequence = true;  // Set the flag to true so we dont keep on adding number indicator
            }
            result += numbers[char];  // Add the Braille representation of the number
        } else {
            // If we're currently in a number sequence, reset the flag
            if (inNumberSequence) {
                inNumberSequence = false; 
            }

            if (char === char.toUpperCase() && letters[char.toLowerCase()] && char !== " ") {// if the character is the uppercase version and is in the letters object and is not a space
                result += letters["cap"]; //add capital indicator
                result += letters[char.toLowerCase()]; //add lowercase version of character
            } else if (letters[char]) {
                result += letters[char]; //add character as us
            }
        }
    }

    return result; //returns braille version of text
}

/**
 * wiil take the given text and then iterate through the whole text in increments of 6 characters that can then be used to reference the brailltoletters object.
 * It will then check for capital letters and numbers and if so it will change the isNum or isCap flag to true and then continue to next iteration. It will then use those
 * flags to determine what it is doing to the information. If it is a capital it will then get the character from brailleToLetters and then convert it to uppercase and add it to the result.
 * and then set the flag back to false. If it is a number it will check if the character is in the brailleToNumbers object and then add the number to the result. If it is a space it will add a space to the result.
 * 
 * running time: `O(n)` where n is the length of the text
 * 
 * @param {String} text is the braile text that is to be converted to english
 * @returns the english version of the braille text
 */
function toText(text) {
    let result = "";
    let isCap = false; //check if the next character is a capital letter
    let isNum = false; //check if the next sequence is numbers

    for (let i = 0; i < text.length; i += 6) {//iterates by increments of 6 for each braille character
        let char = text.slice(i, i + 6);//chunks of six characters

        if (char === letters["cap"]) {//if capital then set flag to true
            isCap = true; 
            continue; 
        }
        else if(char === letters["num"]) {//if number then set flag to true
            isNum = true;
            continue;
        }

        if(isNum){ //if it is a number then add the number to the result
            if(brailleToNumbers[char]){
                result += brailleToNumbers[char];
            }
            else if(char === letters[" "]){//if it is a space then add a space to the result and set the flag to false
                isNum = false;
                result += " ";
            }
        }
        else if( isCap){//if it is a capital then add the uppercase version of the character to the result and set the flag to false
            result += brailleToLetters[char].toUpperCase();
            isCap = false;
        }//if it is not a number or a capital letter then add the character to the result
        else {
            result += brailleToLetters[char];
        }
    }

    return result; //english text from braille
}
/**
 * This will take the text input and determine whether or not it is braille or text by checking if the braille patter is present in the input. It will then use the chunks to determine if it is braille or text.
 * After the check it will then use the isBraille flag to determine if it is braille or text and then call the appropriate function to translate the input.
 * @param {String} input is the input that will first be checked to see if it is braille or text and then will be translated to the opposite 
 * @returns the translated version of the input
 */
function translate(input) { 
    const braillePattern = /^[O.]{6}$/; //determines the braille pattern as being 6 characters long and containing only O and .
    const chunks = input.match(/.{1,6}/g);  // Split the input into chunks of 6 characters

    
    const isBraille = chunks.every(chunk => braillePattern.test(chunk)); // this will check every chunk to see if it matches the pattern of braille

    if (isBraille) {
        return toText(input);//if it is braille then call the toText function
    } else {
        return toBraille(input);//if it is text then call the toBraille function
    }
}


const args = process.argv.slice(2);

const input = args.join(' ');

console.log(translate(input));