const braille = {
    'a' : 'O.....',
    'b' : 'O.O...',
    'c' : 'OO....',
    'd' : 'OO.O..',
    'e' : 'O..O..',
    'f' : 'OOO...',
    'g' : 'OOOO..',
    'h' : 'O.OO..',
    'i' : '.OO...',
    'j' : '.OOO..',
    'k' : 'O...O.',
    'l' : 'O.O.O.',
    'm' : 'OO..O.',
    'n' : 'OO.OO.',
    'o' : 'O..OO.',
    'p' : 'OOO.O.',
    'q' : 'OOOOO.',
    'r' : 'O.OOO.',
    's' : '.OO.O.',
    't' : '.OOOO.',
    'u' : 'O...OO',
    'v' : 'O.O.OO',
    'w' : '.OOO.O',
    'x' : 'OO..OO',
    'y' : 'OO.OOO',
    'z' : 'O..OOO',
    'capital' : '.....O',
    'decimal' : '.O...O',
    'number' : '.O.OOO',
    '.' : '..OO.O',
    ',' : '..O...',
    '?' : '..O.OO',
    '!' : '..OOO.',
    ':' : '..OO..',
    ';' : '..O.O.',
    '-' : '....OO',
    '/' : '.O..O.',
    '<' : '.OO..O',
    '(' : 'O.O..O',
    ')' : '.O.OO.',
    ' ' : '......'
};

const brailleNum = {
    '1' : 'O.....',
    '2' : 'O.O...',
    '3' : 'OO....',
    '4' : 'OO.O..',
    '5' : 'O..O..',
    '6' : 'OOO...',
    '7' : 'OOOO..',
    '8' : 'O.OO..',
    '9' : '.OO...',
    '0' : '.OOO..',
    '>' : 'O..OO.'
};

//flip the braille object to make it easier to handle using keys
const FlipBraille = (braille) => {
    const flipBraille = {};
    for (const [key, value] of Object.entries(braille)) {
        flipBraille[value] = key;
    }
    return flipBraille;
};

//flip both alphabet and number objects
const flipBraille = FlipBraille(braille);
const flipBrailleNum = FlipBraille(brailleNum);

const brailleToEng = (val) => {

    let translatedVal = '';
    let brailleCounter = 0;
    let loopLength = val.length;
    let letter = '';
    let isnum = false;
    let iscapital = false;

    for(i=0; i<loopLength; i++) {
        letter = val.slice(brailleCounter, brailleCounter+6);

        if(letter == braille['number']) {
            isnum = true;
            brailleCounter += 6;
        } else if(letter == braille['capital']) {
            iscapital = true;
            brailleCounter += 6;
        } else if(letter == braille[' ']) {
            isnum = false;
            translatedVal = translatedVal + flipBraille[letter];
            brailleCounter += 6;
        } else if ((flipBraille[letter] >= 'a' && flipBraille[letter] <= 'z') && isnum == false) {            
            if (iscapital == true) {
                translatedVal = translatedVal + flipBraille[letter].toUpperCase();
                iscapital = false;
            } else {
                translatedVal = translatedVal + flipBraille[letter];
            }
            brailleCounter += 6;
        } else if (isnum == false) {
            translatedVal = translatedVal + flipBraille[letter];

        } else {
            brailleCounter += 6;
        }

        if(isnum == true && letter != braille['number']) {
            translatedVal = translatedVal + flipBrailleNum[letter];
        }
        i=i+5;
    }
    return translatedVal;
};

const engToBraille = (val) => {
    let translatedVal = '';
    let numericChecker = true;
    for (let instance of val) {
        if (instance >= 'a' && instance <='z') {
            translatedVal = translatedVal + braille[instance];
        } else if (instance >= 'A' && instance <= 'Z') {
            translatedVal = translatedVal + braille['capital'] + braille[instance.toLowerCase()];
        } else if (instance >= '0' && instance <= '9') {
            if(numericChecker == true) {
                translatedVal = translatedVal + braille['number'] + brailleNum[instance];
                numericChecker = false;
            } else {
                translatedVal = translatedVal + brailleNum[instance];
            }
        } else if (instance == '.' && (val.indexOf(instance)-1 >= '0' && val.indexOf(instance)-1 <= '9') && (val.indexOf(instance)+1 >= '0' && val.indexOf(instance)+1 <= '9')) { // check if decimal needs to be used, if there is a number before and after decimal eg 3.2
            translatedVal = translatedVal + braille['decimal'];
        }
        else if (instance == ' ') {
            numericChecker = true;
            translatedVal = translatedVal + braille[instance];
        }
        else {
            translatedVal = translatedVal + braille[instance];
        }
    }
    return translatedVal;
};

//check if the input value is in english or in braille
const identifyValue = (val) => {
    if(val.includes('.') || val.includes('O')) {
        console.log(brailleToEng(val));
    } else {
        console.log(engToBraille(val));
    }
};

let inputVal = process.argv.slice(2);
if (inputVal.length > 0) {
    inputVal = inputVal.join(' ');
    identifyValue(inputVal);
} else {
    console.log('You have not entered any input value to translate.');
}