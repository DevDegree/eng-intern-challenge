//English to braille map
const englishBrailleMap ={
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
    ' ': '......'
}

//Braille to english map
const brailleEnglishMap = Object.fromEntries(Object.entries(englishBrailleMap).map(([key,value]) => [value,key]));

//Number to braille map
const numberBrailleMap = {
    'O': '.OOO..',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...'
}

//Braille to number map
const brailleNumbersMap = Object.fromEntries(Object.entries(numberBrailleMap).map(([key,value]) => [value,key]));

//Special character to braille map
const specialBrailleMap = {
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
    ')': '.O.OO.'
}

//Braille to special character map
const brailleSpecialMap = Object.fromEntries(Object.entries(specialBrailleMap).map(([key,value]) => [value,key]));

//Braille for capitals, decimals and number map
const brailleFollowsMap = {
    '.....O': 'capital',
    '.O...O': 'decimal',
    '.O.OOO': 'number'
}


/* 
convertToEnglish is a function that converts the braille sentence to 
english recieved through the command line 
*/
function convertToEnglish (braille){
    if (braille.length % 6 !== 0){
        return "Cannot be translated. Invalid braille text. ";
    }

    let isCapital = false;
    let isNumber = false;
    let result = '';

    for (let i = 0; i < braille.length; i+=6){

        if (brailleFollowsMap[braille.slice (i, (i+6))] === 'capital'){
            isCapital = true;
            continue;
        } else if (brailleFollowsMap[braille.slice (i, (i+6))] === 'number'){
            isNumber = true;
            continue;
        } else if(brailleEnglishMap[braille.slice (i, (i+6))] === ' '){
            result += ' ';
            isNumber = false;
            continue;
        }

        if(isCapital){
            result += brailleEnglishMap[braille.slice (i, (i+6))].toUpperCase();
            isCapital = false;
        }else if (isNumber){
            result += brailleNumbersMap[braille.slice (i, (i+6))];   
        }else{
            result += brailleEnglishMap[braille.slice (i, (i+6))];
        }
    }

    return result;
}

