//Braille dictionary
const brailleDict = { 
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': "i",
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.O..O.': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',
    '.....O': 'CAP', //Capital follows
    '.O.OOO': 'NUM', //Number follows
    '......': ' ', //Space 
};

//Translate Braille to English
function translateBraille(braille) {
    let output = '';
    let isCapital = false;
    let isNumber = false;
    

    const brailleChars = braille.match(/.{1,6}/g) || []; //Group braille into groups of 6-dot characters global search 

    brailleChars.forEach((char) => {
        if (char === '.O.OOO') {
            isNumber = true; //Number follows
        } else if (char === '.....O') {
            isCapital = true; //Capital follows
        } else if (char === '......') { //Space 
            output += ' ';
            isNumber = false;
            isCapital = false;
        } else {
            let translation = brailleDict[char]; 

            if (translation !== undefined) {
                if (isNumber) {
                    const numberMapping = {'a': '1','b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'}; //Map numbers to letters with same pattern
                    output += numberMapping[translation] || '#error';
                } else if (isCapital) {
                    output += translation.toUpperCase();
                    isCapital = false; //Cap only applies to first symbol following 
                } else {
                    output += translation;
                } 
            } else {
                output += "#error ";
            } 
        }
    });
    return output;
} 

//Translate English to Braille 
function translateEnglish(english) {
    let output = ''; 
    let isNumber = false;

    for(let char of english) {
        if (/\d/.test(char)) {
            if (!isNumber) {
                output += '.O.OOO'; //Next character is a number
                isNumber = true;
             }
            const letterMapping = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'};
            char = letterMapping[char];  
        } else {
            isNumber = false;
        }

        if (char === char.toUpperCase() && char !== ' ') { //Check for uppercase letters
            output += '.....O'; //Next character is a capital letter
        } 

        char = char.toLowerCase(); //convert to lower case to match the dictionary
        const brailleChar = Object.keys(brailleDict).find(key => brailleDict[key] === char); //Get the key for the char from the dictionary 

        if (brailleChar) {
            output += brailleChar; 
        } else if (char === ' ') {
            output += '......';
        } else {
            output += "#error ";
        }
    }
    return output.trim(); 
}

function autoTranslate(input) {
    if (/^[O.]+$/.test(input)) {
        return translateBraille(input);
    } else {
        return translateEnglish(input);
    }
}

//Join arguments into one string 
const input = process.argv.slice(2).join(' ');

console.log(autoTranslate(input));

