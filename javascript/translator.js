//--BRAILLE CONSTANTS START--
// letters
const BRAILLE_A = "O.....";
const BRAILLE_B = "O.O...";
const BRAILLE_C = "OO....";
const BRAILLE_D = "OO.O..";
const BRAILLE_E = "O..O..";
const BRAILLE_F = "OOO...";
const BRAILLE_G = "OOOO..";
const BRAILLE_H = "O.OO..";
const BRAILLE_I = ".OO...";
const BRAILLE_J = ".OOO..";
const BRAILLE_K = "O...O.";
const BRAILLE_L = "O.O.O.";
const BRAILLE_M = "OO..O.";
const BRAILLE_N = "OO.OO.";
const BRAILLE_O = "O..OO.";
const BRAILLE_P = "OOO.O.";
const BRAILLE_Q = "OOOOO.";
const BRAILLE_R = "O.OOO.";
const BRAILLE_S = ".OO.O.";
const BRAILLE_T = ".OOOO.";
const BRAILLE_U = "O...OO";
const BRAILLE_V = "O.O.OO";
const BRAILLE_W = ".OOO.O";
const BRAILLE_X = "OO..OO";
const BRAILLE_Y = "OO.OOO";
const BRAILLE_Z = "O..OOO";

// numbers
const BRAILLE_1 = "O.....";
const BRAILLE_2 = "O.O...";
const BRAILLE_3 = "OO....";
const BRAILLE_4 = "OO.O..";
const BRAILLE_5 = "O..O..";
const BRAILLE_6 = "OOO...";
const BRAILLE_7 = "OOOO..";
const BRAILLE_8 = "O.OO..";
const BRAILLE_9 = ".OO...";
const BRAILLE_0 = ".OOO..";

// follow indicators
const BRAILLE_CAPITAL = ".....O";
const BRAILLE_DECIMAL = ".O...O";
const BRAILLE_NUMBER = ".O.OOO";

// spacing and puctuation
const BRAILLE_SPACE = "......";
const BRAILLE_PERIOD = "..OO.O";
const BRAILLE_COMMA = "..O...";
const BRAILLE_QUESTION = "..O.OO";
const BRAILLE_EXCLAIM = "..OOO.";
const BRAILLE_COLON = "..OO..";
const BRAILLE_SEMI_COLON = "..O.O.";
const BRAILLE_DASH = "....OO";
const BRAILLE_SLASH = ".O..O.";
const BRAILLE_LEFT_ANGLE = ".OO..O";
const BRAILLE_RIGHT_ANGLE = "O..OO.";
const BRAILLE_LEFT_BRACKET = "O.O..O";
const BRAILLE_RIGHT_BRACKET = ".O.OO.";

const BRAILLE_ACCEPTED = [BRAILLE_0, BRAILLE_1, BRAILLE_2, BRAILLE_3, BRAILLE_4, BRAILLE_5, BRAILLE_6, BRAILLE_7, BRAILLE_8, BRAILLE_9, BRAILLE_A, BRAILLE_B, BRAILLE_C, BRAILLE_D, BRAILLE_E, BRAILLE_F, BRAILLE_G, BRAILLE_H, BRAILLE_I, BRAILLE_J, BRAILLE_K, BRAILLE_L, BRAILLE_M, BRAILLE_N, BRAILLE_O, BRAILLE_P, BRAILLE_Q, BRAILLE_R, BRAILLE_S, BRAILLE_T, BRAILLE_U, BRAILLE_V, BRAILLE_W, BRAILLE_X, BRAILLE_Y, BRAILLE_Z, BRAILLE_CAPITAL, BRAILLE_DECIMAL, BRAILLE_NUMBER, BRAILLE_SPACE, BRAILLE_PERIOD, BRAILLE_COMMA, BRAILLE_QUESTION, BRAILLE_EXCLAIM, BRAILLE_COLON, BRAILLE_SEMI_COLON, BRAILLE_DASH, BRAILLE_SLASH, BRAILLE_LEFT_ANGLE, BRAILLE_RIGHT_ANGLE, BRAILLE_LEFT_BRACKET, BRAILLE_RIGHT_BRACKET];

const BRAILLE_ALPHA_LETTERS = [BRAILLE_A, BRAILLE_B, BRAILLE_C, BRAILLE_D, BRAILLE_E, BRAILLE_F, BRAILLE_G, BRAILLE_H, BRAILLE_I, BRAILLE_J, BRAILLE_K, BRAILLE_L, BRAILLE_M, BRAILLE_N, BRAILLE_O, BRAILLE_P, BRAILLE_Q, BRAILLE_R, BRAILLE_S, BRAILLE_T, BRAILLE_U, BRAILLE_V, BRAILLE_W, BRAILLE_X, BRAILLE_Y, BRAILLE_Z];

const BRAILLE_NUMBERS = [BRAILLE_0, BRAILLE_1, BRAILLE_2, BRAILLE_3, BRAILLE_4, BRAILLE_5, BRAILLE_6, BRAILLE_7, BRAILLE_8, BRAILLE_9];

//--BRAILLE CONSTANTS END--

// --ASCII CONSTANTS START--

const ASCII_UPPER_LETTER_START = 65;
const ASCII_UPPER_LETTER_END = 90;

const ASCII_LOWER_LETTER_START = 97;
const ASCII_LOWER_LETTER_END = 122;

const ASCII_NUMBERS_START = 48;
const ASCII_NUMBERS_END = 57;

const ASCII_SPACE = 32;
const ASCII_PERIOD = 46;
const ASCII_COMMA = 44;
const ASCII_QUESTION = 63;
const ASCII_EXCLAIM = 33;
const ASCII_COLON = 58;
const ASCII_SEMI_COLON = 59;
const ASCII_DASH = 45;
const ASCII_SLASH = 47;
const ASCII_LEFT_ANGLE = 60;
const ASCII_RIGHT_ANGLE = 62;
const ASCII_LEFT_BRACKET = 40;
const ASCII_RIGHT_BRACKET = 41;

// --ASCII CONSTANTS END--

// --HELPER METHODS START--

/**
 * isBrailleFormat is a function that will check that the input contains only O and . and that the total amount of characters is divisible by 6.
 * 
 * @param {string}      text 
 * 
 * @returns {boolean}
 */
function isBrailleFormat(text){
    const pattern = /[^O.]/;
    if(pattern.test(text)){
        // There is a character that is not 0 or .
        return false;
    }else{
        if(text.length % 6 !== 0){
            // The input is not set into blocks of 6 as is required
            return false;
        }else{
            //The input has braille format (though unsure if matches Braille Library)
            return true;
        }
    }
}

/**
 * makeBrailleBlocks is a function that will parcel out the input text into 6 character Strings and make them into an array that contains all of these strings in the order they appear in the original text.
 * 
 * @param {string}      text 
 * 
 * @returns {String[]}
 */
function makeBrailleBlocks(text){
    // Create the array to hold the braille input
    const brailleBlocks = [];

    // Loop through the input in chunks of 6 to put them into seperate blocks and add each block to the array
    for(let index = 0; (index+5) < text.length; index+=6){
        let brailleBlock = text.charAt(index);
        brailleBlock += text.charAt(index + 1);
        brailleBlock += text.charAt(index + 2);
        brailleBlock += text.charAt(index + 3);
        brailleBlock += text.charAt(index + 4);
        brailleBlock += text.charAt(index + 5);

        brailleBlocks.push(brailleBlock);
    }

    // Return array of braille blocks
    return brailleBlocks;
}

/**
 * isBrailleAlphabet is a function that checks that each block of 6 character strings in a given array match with one of the defined values of a Braille charcter.
 * 
 * @param {String[]}      blocks 
 * 
 * @returns {boolean}
 */
function isBrailleAlphabet(blocks){
    
    for(let index = 0; index < blocks.length; index++){
        // If the block is found in the accepted braille library ignore, otherwise return false
        if(!BRAILLE_ACCEPTED.includes(blocks[index])){
            return false;
        }
    }

    // Looped through the entire message with no braille counterfits
    return true;
}

/**
 * isBrailleLetter is a function that checks is the provided block matches one of the Braille letters
 * 
 * @param {string}      block 
 * 
 * @returns {boolean}
 */
function isBrailleLetter(block){
    if(BRAILLE_ALPHA_LETTERS.includes(block)){
        return true;
    }else{
        return false;
    }
}

/**
 * isBrailleNumber is a function that checks is the provided block matches one of the Braille numbers
 * 
 * @param {string}      block 
 * 
 * @returns {boolean}
 */
function isBrailleNumber(block){
    if(BRAILLE_NUMBERS.includes(block)){
        return true;
    }else{
        return false;
    }
}

/**
 * getAlphaLetter is a function that retrieves the corresponding English letter of the given braille. Capitalization is determined by the isCapital input.
 * 
 * @param {string}      braille
 * @param {boolean}     isCapital 
 * 
 * @returns {string}
 */
function getAlphaLetter(braille, isCapital){
    // Find the position of the given letter in the alphabet
    const positionInAlphabet = BRAILLE_ALPHA_LETTERS.indexOf(braille);

    // Using that position, find the ASCII value
    const asciiValue = positionInAlphabet + ASCII_UPPER_LETTER_START;

    // Convert the ASCII value to the uppercase character
    let alphaValue = String.fromCharCode(asciiValue);
    
    // Return the upper or lower case character as appropriate
    if(isCapital){
        return alphaValue;
    }else{
        return alphaValue.toLowerCase();
    }
}

/**
 * getAlphaNumber is a function that retrieves the corresponding English number of the given braille.
 * 
 * @param {string}      braille
 * 
 * @returns {int}
 */
function getAlphaNumber(braille){
        // Find the position of the given number in the numbers array
        return BRAILLE_NUMBERS.indexOf(braille);
}

/**
 * getBrailleNumber is a function that retrieves the corresponding Braille block to the number represented by the given ASCII value.
 * 
 * @param {int}      asciiValue
 * 
 * @returns {string}
 */
function getBrailleNumber(asciiValue){
    // Calculate the position of the number by substracting the first ASCII value
    let indexPosition = asciiValue - ASCII_NUMBERS_START;

    // Return the braille number in that position
    return BRAILLE_NUMBERS[indexPosition];
}

/**
 * getBrailleLetter is a function that retrieves the corresponding Braille block to the letter represented by the given ASCII value, regardless of whether ths ASCII value represents the upper or lower case letter.
 * 
 * @param {int}      asciiValue
 * @param {boolean}  isUpperCase 
 * 
 * @returns {string}
 */
function getBrailleLetter(asciiValue, isUpperCase){
    // Calculate the position of the letter by substracting the first ASCII value (dependent on upper or lower case)
    let indexPosition = asciiValue;
    if(isUpperCase){
        indexPosition -= ASCII_UPPER_LETTER_START;
    }else{
        indexPosition -= ASCII_LOWER_LETTER_START;
    }

    // Return the braille letter in that position
    return BRAILLE_ALPHA_LETTERS[indexPosition];
}

// --HELPER METHODS END--


//Get input from the terminal
const {argv} = require('node:process');

let originalMsg = argv[2];
for(let index = 3; index < argv.length; index++){
    // Add a space that has been removed from the splitting of input
    originalMsg += " ";

    // Add the next part of the input
    originalMsg += argv[index];
}

// Determine if the input is Braille
let isBraille = true;

// Determine if the input is in Braille formatting
if(!isBrailleFormat(originalMsg)){
    isBraille = false;
}
// As it is braille formatting, get the individual braille letters
const brailleMsg = makeBrailleBlocks(originalMsg);

// Check that all the blocks are proper braille, otherwise this is really weird non-sensical English
if(!isBrailleAlphabet(brailleMsg)){
    isBraille = false;
}

    // Translate accordingly
    if(isBraille){
        // Proceed to translate to English
        let englishMsg = "";

        let isCap = false;
        let isNum = false;

        for(let index = 0; index < brailleMsg.length; index++){
            // Get the current block
            let currBlock = brailleMsg[index];

            // If it is a "follows" indecator, update the relevant booleans
            if(currBlock === BRAILLE_CAPITAL){
                isCap = true;
                isNum = false;

            }else if(currBlock === BRAILLE_NUMBER){
                isCap = false;
                isNum = true;
                
            // If it is a letter, add it to the message
            }else if(isBrailleLetter(currBlock) && !isNum){
                englishMsg += getAlphaLetter(currBlock, isCap);

                // there should no longer be a capitalize indicator
                isCap = false;

            // If it is a number, add it to the message
            }else if(isBrailleNumber(currBlock) && !!isNum){
                englishMsg += getAlphaNumber(currBlock);
                isCap = false;
            
            // If it is a space, add a space character and reset "following" booleans to false
            }else if(currBlock === BRAILLE_SPACE){
                isCap = false;
                isNum = false;
                englishMsg += " ";
            }

            // NOTE: Current requirements ignore punctuation characters
            // NOTE: Current requirements ignore the irrational usage of following indicators
        }

        // Print the Braille to English message
        console.log(englishMsg);

    }else{
        // This should be English translating to Braille
        
        // Create the placeholder for the braille message
        let brailleMsg = "";

        // Create a boolean for keeping track of the number following addition
        let isNumFollowing = false;

        // Loop through the input message and translate
        for(let index = 0; index < originalMsg.length; index++){

            // Get the ascii code of the current character
            let currASCII = originalMsg.charCodeAt(index);

            // Check if it is a number
            if(currASCII >= ASCII_NUMBERS_START && currASCII <= ASCII_NUMBERS_END){
                // Add a number following braille character if this is the first number in the sequence
                if(!isNumFollowing){
                    brailleMsg += BRAILLE_NUMBER;
                    isNumFollowing = true;
                }

                // Add the braille number
                brailleMsg += getBrailleNumber(currASCII);
            
            // Check if it is an uppercase letter
            }else if(currASCII >= ASCII_UPPER_LETTER_START && currASCII <= ASCII_UPPER_LETTER_END){
                // Add a capital following braille character
                brailleMsg += BRAILLE_CAPITAL;

                // Add the braille letter
                brailleMsg += getBrailleLetter(currASCII, true);

            // Check if it is an lowercase letter
            }else if(currASCII >= ASCII_LOWER_LETTER_START && currASCII <= ASCII_LOWER_LETTER_END){
                // Add the braille letter
                brailleMsg += getBrailleLetter(currASCII, false);

            
            }else if(currASCII === ASCII_SPACE){
                //Reset the number following boolean to false
                isNumFollowing = false;

                // Add the braille space character
                brailleMsg += BRAILLE_SPACE;

                // NOTE: inclusion of other characters not specified in the techinical requirements of the challenge
            }
        }

        // Print the English to Braille message
        console.log(brailleMsg);
    }