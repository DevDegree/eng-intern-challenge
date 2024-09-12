// VARIABLES

// "dictionary" object with key/value pairs to translate letters and symbols
// object for numbers 
// const for capital follows
// const for decimal follows
// const for number follows
// string to hold the result
// boolean for capital or no? 
// boolean for number? 

// create translator reference as an OBJECT
const engToBraille = {
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
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......',
}

const brailleToEng = inverse(engToBraille);

const engToBrailleNums = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
}

const brailleToEngNums = inverse(engToBrailleNums);

const capitalSign = '.....O';
const decimalSign = '.O...O';
const numberSign = '.O.OOO';
const spaceSign = '......';
let resultString = "";
let isCapital = false;
let isNumber = false;

// create a FUNCTION to translate input string

// determine if string is english or braille 
// if string contains ONLY . & Os, then it is braille
// const userInput = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..";
const userInput = "Hello World!";
let brStrings = [];

// if it is braille, then split string into substrings of 6
if(isBraille(userInput)){
    for(let i = 0; i < userInput.length; i+=6){
        brStrings.push(userInput.substring(i, i+6));
    }

    for(const cluster of brStrings){
        if(cluster === spaceSign){
            isNumber = false;
        }
        if(cluster === capitalSign || cluster === decimalSign || cluster === numberSign){
            switch(cluster){
                case capitalSign: isCapital = true;
                break;
                case decimalSign: isNumber= true;
                break;
                case numberSign: isNumber = true;
                break;
                default: break;
            }
        }
        else{
            if(isCapital){
                let capitalChar = brailleToEng[cluster];
                resultString += capitalChar.toUpperCase();
                isCapital = false;
            }
            else if(isNumber){
               resultString += brailleToEngNums[cluster];
            } else {
                resultString += brailleToEng[cluster];
            }
        }

    }
    
    console.log(resultString);
} else {
    for(letter of userInput){
        let capitalRegex = /^[A-Z]*$/;
        let digitRegex = /^[0-9]*$/

        if(letter === " "){
            resultString += spaceSign;
            isNumber = false;
        } else if(isNumber){
            resultString += engToBrailleNums[letter];
        } else if(letter.match(capitalRegex)){
            resultString +=capitalSign;
            resultString += engToBraille[letter.toLowerCase()]
        } else if(letter.match(digitRegex)){
            resultString += numberSign;
            resultString += engToBrailleNums[letter];
            isNumber = true;
        } else{
            resultString += engToBraille[letter];

        }
    
    }
    console.log(resultString);
    
}




// if braille, split string into substrings of 6 characters (or arrays?)
// each string of 6 characters will be translated into English/symbols/numbers
// look up in object to find corresponding character and add to result string
// return result string

// else it is english
// split string into characters
// for each character, find the corresponding braille string in the translator object
// add braille strings to result string 
// return result string

// dealing with capital, decimal, number follows & spaces
// IF substring matches capital pattern, then append the next letter with ToUpperCase

// IF it matches number, use numbers object until SPACE is reached using a while loop


// IF it matches decimal, append the next symbol


// checks if string is Braille
// returns true/false
function isBraille(input){
    const brailleRegex = /^[O.]+$/;
    return brailleRegex.test(input);
}

// inverse function to create reverse map of english-braille map
function inverse(obj){
    const inverseObj = {};
    for (const entry in obj){
        inverseObj[obj[entry]]= entry;
    }
    return inverseObj;
}