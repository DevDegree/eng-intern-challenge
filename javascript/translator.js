//**note that the braille alphabet for the letter O and the > symbol are the same. find a solution after your basic code works./ 

//English characters to braille object
const brailleDict = {
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
    'k': 'O....O',
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
    '-': '....OO',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......'
}

//English numbers to braille object
const brailleNums = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
}

//Braille to English characters object
engDict = Object.fromEntries(Object.entries(brailleDict).map(([key, value]) => ([value,key])));

//Braille to English numbers object
engNums = Object.fromEntries(Object.entries(brailleNums).map(([key, value]) => ([value, key])));

const capitalNext = '.....O';
const numberNext = '.O.OOO';
const decimalNext = '.O...O';

//PSEUDOCODE

//function to tranlate English to braille
    //use split() method to split the string into individual characters.
    //use map() method to map over all characters.
        //if alphabet letter is capitalized, add braille indicator for capital follows before the corresponding braille sympbol. 
            //ensure only the character that follows the braille indicator for capital follows is capitalized. maybe use boolean here. 
        //if character is a number, add braille indicator for number follows before the corresponding braille symbol.
            //ensure all characters that follow the braille indicator for number follows are numbers until the use hits space bar. maybe use boolean here. 
            //if decimal is used, add braille indicator for decimal follows before the corresponding braille symbol, else print braille symbol for period. 
        //return all characters
    //use join() method to concatenate all characters into a string 

function translateEngToBraille(input) {
    let capitalize = false;
    let inNumberMode = false;

    return input
    .split('')
    .map((char) => {
        if (char === char.toUpperCase() && char !== char.toLowerCase()) {
            capitalize = true;
        }

        if (capitalize) {
            capitalize = false;
            return capitalNext + brailleDict[char.toLowerCase()] || 'ERROR';
        }

        if (/^\d$/.test(char)) {
            inNumberMode = true;
            return numberNext + brailleNums[char] || 'ERROR'
        }

        if (char === '.' && inNumberMode) {
            return decimalNext + brailleDict[char] || 'ERROR';
        }

        if (char === ' ' && inNumberMode) {
            inNumberMode = false;
        }

        return brailleDict[char] || 'ERROR'
    })
    .join('');
}

console.log(translateEngToBraille('Hello Erika 1.2 a.@'));
    

//function to translate braille to English
    //since braille segements follow a six dot pattern, create a regex for 6 characters
    //use regex and match() method to split the braille into 6-chacter segments
    //use map() method to map over all the segments and follow logic in function above
    //use join() method to concatenate all characters into a string

    //function to detect language (English or braille), then convert to opposite language with one of the correspoding two functions below.
    //maybe detect if language is only in O and . using a regex.