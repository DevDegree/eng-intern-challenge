/*
Techincal requirements:

Given arguments passed into the program at runtime, determine if the given string should be translated to English or Braille.

1. When a Braille capital follows symbol is read, assume only the next symbol should be capitalized.
2. When a Braille number follows symbol is read, assume all following symbols are numbers until the next space symbol.

Braille Alphabet
1. Letters a through z
2. The ability to capitalize letters
3. Numbers 0 through 9
4. The ability to include spaces ie: multiple words
*/

// english to braille dictionary
const englishToBraille = {
    'a': '0.....', 
    'b': '0.0...',
    'c': '00....',
    'd': '00.0..',
    'e': '0..0..',
    'f': '000...',
    'g': '0000..',
    'h': '0.00..',
    'i': '.00...',
    'j': '.000..',
    'k': '0...0.',
    'l': '0.0.0.',
    'm': '00..0.',
    'n': '00.00.',
    'o': '0..00.',
    'p': '000.0.',
    'q': '00000.',
    'r': '0.000.',
    's': '.00.0.',
    't': '.0000.',
    'u': '0...00',
    'v': '0.0.00',
    'w': '.000.0',
    'x': '00..00',
    'y': '00.000',
    'z': '0..000',
    '1': '0.....',
    '2': '0.0...',
    '3': '00....',
    '4': '00.0..',
    '5': '0..0..',
    '6': '000...',
    '7': '0000..',
    '8': '0.00..',
    '9': '.00...',
    '0': '.000..',
    'capital': '.....0',
    'number': '.0.000',
    'space': '......', 
};

const numberDict = {
    
}

// braille to english dictionary 
const brailleToEnglish = {};

for (let key in englishToBraille) {
    brailleToEnglish[englishToBraille[key]] = key;
}

// get user input from terminal -> process.argv[2]

let userInput = process.argv.slice(2).join(' ');

// parse input to check if it is valid
// /^[0\.]+$/ -> expression to check if input is braille (contains only 0 and .)
// /^[A-Za-z0-9 ]+$/ -> expression to check if input is alphabets, numbers, and spaces

const isAlphanumeric = (input) => {
    return /^[A-Za-z0-9 ]+$/.test(input);
}

const isBraille = (input) => {
    return /^[0\.]+$/.test(input);
}

// function for converting english to braille 
const englishConverter = (input) => {
    return input.split('').map(letter => englishToBraille[letter] || '').join(''); //split each character from input and map the key values
};

// function for converting braille to english
const brailleConverter = (input) => {
    let brailleCharacters = input.match(/.{1,6}/g); //splits user input into substrings of 6 
    let newString = '';
    let capitalize = false;
    let number = false;
    
    for (let i = 0; i<brailleCharacters.length; i++) {
        let substring = brailleCharacters[i];
        
       if (substring === '.....0') {  // check for capital symbol
        capitalize = true;
        continue; 
       } 

       if (substring === '.0.000') { //check for number symbol
        number = true;
        continue;
       }

       let translatedCharacter = brailleToEnglish[substring] || '';

       if(capitalize) {
        translatedCharacter = translatedCharacter.toUpperCase();
        capitalize = false;
       } 

       if (number) {
        translatedCharacter = brailleToEnglish[substring] || '';
        number = false; // reset number flag
    }
       newString += translatedCharacter;
    }
    return newString;
    //return brailleCharacters.map(x => brailleToEnglish[x] || '').join(''); 
};

// main translator function
const translator = (input) => {
    if (isAlphanumeric(input)) {
        console.log(englishConverter(input));
    } else if (isBraille(input)) {
        console.log(brailleConverter(input));
    } else {
        console.log("Not a valid input");
    }
}

translator(userInput);