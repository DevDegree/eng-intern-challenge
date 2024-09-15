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
const BRAILLE_CAPITOL = ".....O";
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

const BRAILLE_ACCEPTED = [BRAILLE_0, BRAILLE_1, BRAILLE_2, BRAILLE_3, BRAILLE_4, BRAILLE_5, BRAILLE_6, BRAILLE_7, BRAILLE_8, BRAILLE_9, BRAILLE_A, BRAILLE_B, BRAILLE_C, BRAILLE_D, BRAILLE_E, BRAILLE_F, BRAILLE_G, BRAILLE_H, BRAILLE_I, BRAILLE_J, BRAILLE_K, BRAILLE_L, BRAILLE_M, BRAILLE_N, BRAILLE_O, BRAILLE_P, BRAILLE_Q, BRAILLE_R, BRAILLE_S, BRAILLE_T, BRAILLE_U, BRAILLE_V, BRAILLE_W, BRAILLE_X, BRAILLE_Y, BRAILLE_Z, BRAILLE_CAPITOL, BRAILLE_DECIMAL, BRAILLE_NUMBER, BRAILLE_SPACE, BRAILLE_PERIOD, BRAILLE_COMMA, BRAILLE_QUESTION, BRAILLE_EXCLAIM, BRAILLE_COLON, BRAILLE_SEMI_COLON, BRAILLE_DASH, BRAILLE_SLASH, BRAILLE_LEFT_ANGLE, BRAILLE_RIGHT_ANGLE, BRAILLE_LEFT_BRACKET, BRAILLE_RIGHT_BRACKET];

const BRAILLE_ALPAH_LETTERS = [BRAILLE_A, BRAILLE_B, BRAILLE_C, BRAILLE_D, BRAILLE_E, BRAILLE_F, BRAILLE_G, BRAILLE_H, BRAILLE_I, BRAILLE_J, BRAILLE_K, BRAILLE_L, BRAILLE_M, BRAILLE_N, BRAILLE_O, BRAILLE_P, BRAILLE_Q, BRAILLE_R, BRAILLE_S, BRAILLE_T, BRAILLE_U, BRAILLE_V, BRAILLE_W, BRAILLE_X, BRAILLE_Y, BRAILLE_Z];

const BRAILLE_NUMBERS = [BRAILLE_0, BRAILLE_1, BRAILLE_2, BRAILLE_3, BRAILLE_4, BRAILLE_5, BRAILLE_6, BRAILLE_7, BRAILLE_8, BRAILLE_9];

//--BRAILLE CONSTANTS END--

// --HELPER METHODS START--

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

function isBrailleAlphabet(blocks){
    
    for(let index = 0; index < blocks.length; index++){
        // If the block is found in the accepted braille library ignore, otherwise return false
        if(!BRAILLE_ACCEPTED.includes(blocks[index])){
            return false;
        }
    }

    // Looped through the entire message with no braille conterfits
    return true;
}

function isBrailleLetter(block){
    if(BRAILLE_ALPAH_LETTERS.includes(block)){
        return true;
    }else{
        return false;
    }
}

function isBrailleNumber(block){
    if(BRAILLE_NUMBERS.includes(block)){
        return true;
    }else{
        return false;
    }
}

function getAlphaLetter(braille, isCapitol){
    // Find the position of the given letter in the alphabet
    const positionInAlphabet = BRAILLE_ALPAH_LETTERS.indexOf(braille) + 1;

    // Using that position, find the ASCII value
    const asciiValue = positionInAlphabet + 64; //NOTE: ASCII letter values start at 65 with A. A would be the first position in the alphabet, so 1 + 64 will get the ascii value 65 and so on

    // Convert the ASCII value to the uppercase character
    let alphaValue = String.fromCharCode(asciiValue);
    
    // Return the upper or lower case character as appropriate
    if(isCapitol){
        return alphaValue;
    }else{
        return alphaValue.toLowerCase();
    }
}

function getAlphaNumber(braille){
        // Find the position of the given number in the numbers array
        return BRAILLE_NUMBERS.indexOf(braille);
}

// --HELPER METHODS END--


//Get input from the terminal
const {argv} = require('node:process');
const originalMsg = argv[2];

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

    // Translate avvordingly
    if(isBraille){
        // Proceed to translate to English
        let englishMsg = "";

        let isCap = false;
        let isNum = false;

        for(let index = 0; index < brailleMsg.length; index++){
            // Get the current block
            let currBlock = brailleMsg[index];

            // If it is a "follows" indecator, update the relevant booleans
            if(currBlock === BRAILLE_CAPITOL){
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

            // NOTE: Current requirements do not worry about punctuation characters
            // NOTE: Current requirement do not worry about the irrational usage of following indicators
        }

        // Print the braille to English message
        console.log(englishMsg);

    }else{
        // This should be English translating to Braille
        // TODO
        console.log("i wasn't braille");
    }