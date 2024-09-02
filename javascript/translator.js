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
    'capital': '.....O',
    'number': '.O.OOO',
    'space': '......', 
};

// braille to english dictionary 
const brailleToEnglish = {};

for (let key in englishToBraille) {
    brailleToEnglish[englishToBraille[key]] = key;
}

// get user input from terminal -> process.argv.slice(2)

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
    let newString = '';
    let capitalize = false;
    let number = false;

    for (let character of input.split('')) {
        if(character === ' ') { //check for space
            newString += englishToBraille['space'];
            number = false; //exit number mode
            continue;
        }

        if (/[A-Z]/.test(character)) {
            newString += englishToBraille['capital'];
            character = character.toLowerCase();
        }
        if (/[0-9]/.test(character)) {
            if (!number) {
                newString += englishToBraille['number'];
                number = true; // enter number mode
            }
        } else {
            number = false;
        }
        newString += englishToBraille[character] || '';
    }
    return newString;
    //return input.split('').map(letter => englishToBraille[letter] || '').join(''); //split each character from input and map the key values
};

// function for converting braille to english
const brailleConverter = (input) => {
    let brailleCharacters = input.match(/.{1,6}/g); //splits user input into substrings of 6 
    let newString = '';
    let capitalize = false;
    let number = false;
    
    for (let i = 0; i<brailleCharacters.length; i++) {
        let substring = brailleCharacters[i];
        
       if (substring === '.....O') {  // check for capital symbol
        capitalize = true;
        continue; 
       } 

       if (substring === '.O.OOO') { //check for number symbol
        number = true;
        continue;
       }

       if (substring === '......') { //check for space
        newString += ' '; 
        number = false; //exit number follows mode when there is a space
        continue; 
       }

       let translatedCharacter;

       if (number) {
        translatedCharacter = Object.keys(englishToBraille).find(key => englishToBraille[key] === substring && key.match(/[0-9]/)) || ''; //find the number keys from dictionary
        //number = false;
    } else {
        translatedCharacter = brailleToEnglish[substring] || '';
    }

    if(capitalize && translatedCharacter) {
        translatedCharacter = translatedCharacter.toUpperCase();
        capitalize = false;
       } 
       newString += translatedCharacter || '';
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