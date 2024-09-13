// The character mappings from English to Braille.
const brailleLetters = {
    a: 'O.....',
    b: 'O.O...', 
    c: 'OO....', 
    d: 'OO.O..', 
    e: 'O..O..', 
    f: 'OOO...', 
    g: 'OOOO..', 
    h: 'O.OO..', 
    i: '.OO...', 
    j: '.OOO..',
    k: 'O...O.', 
    l: 'O.O.O.', 
    m: 'OO..O.', 
    n: 'OO.OO.', 
    o: 'O..OO.', 
    p: 'OOO.O.', 
    q: 'OOOOO.', 
    r: 'O.OOO.', 
    s: '.OO.O.', 
    t: '.OOOO.',
    u: 'O...OO', 
    v: 'O.O.OO', 
    w: '.OOO.O', 
    x: 'OO..OO', 
    y: 'OO.OOO', 
    z: 'O..OOO', 
}

//Baille Numbers
const brailleNumbers = {
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
};

//Special braille characters
const brailleSpecial = {
    space: '......', 
    capital: '.....O',
    number: '.O.OOO',
    decimal: '.O...O',  
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
};

//function to flip a maps keys and values.
const flip = (data) => {
    return Object.entries(data).map(([key, value]) => [value, key]);
}

//Flip all three mappings above.
const flippedBrailleLetters = flip(brailleLetters);
const flippedBrailleNumbers = flip(brailleNumbers);
const flippedBrailleSpecial = flip(brailleSpecial);

//Check if the sequence is braille
const isBraille = (str) => {
    return /^[O.]+$/.test(input);
}

//Translate English to Braille
//reversing the mappings should have been done first but doesnt make a difference in the end
const engToBrl = (eng) => {
    let result = '';
    let isNumber = false; //boolean to see if its a number

    //Loop through each char of 'str' and perform a check to see which mappings are appropriate.
    for(let char of eng) {
        // If the character is a space append a 'braille' space to result.
        if(char === ' ') {
            result += brailleChars.space; 
        } else if (/[A-Z]/.test(char)) { //check if it is an uppercase;
            result += brailleChars.capital + brailleChars[char.toLowerCase()];
        } else if(/[1-9]/.test(char)) {
            if(!isNumber) { // if it isnt a number make it a number
                result += brailleChars.number; //prefix
                isNumber = true;
            }
            result += brailleChars[char]; // append the character
        } else if(char === '.') { // check if it is a period or a decimal
            if(isNumber) {
                result += brailleChars.decimal;
            } else {
                result += brailleChars[char];
            }
        } else {
            isNumber = false;
            result += brailleChars[char]; //  for default
        }
    }

    return result;
}



const brlToEng = (braille) => {
    

    for(let i = 0; i < braille.length; i+=6) { //in chunks of 6
        const symbol = braille.substr(i,i + 6);

        
    }
}


flip(engToBrailleChars);
console.log(brailleToEngChars)

// Test isBraille
// console.log(isBraille("O....."));      // should be true 'a' 
// console.log(isBraille("OO.O.."));      // true 'd'
// console.log(isBraille("O.OO.. "));     // f 'space 
// console.log(isBraille("O.....1"));     // f there is a 1
// console.log(isBraille("abc.OOO"));     // f 'abc'
// console.log(isBraille("O.....X"));     // f 'X'
// console.log(isBraille(".....O.O...OOO.OOO"));  // t
// console.log(isBraille("O..... O...."));        // f 'space in middle'

// Test engToBrl function
// console.log(engToBrl("hello")); 
// console.log(engToBrl("HELLO")); 
// console.log(engToBrl("Hello World")); 
// console.log(engToBrl("abc 123"));
// console.log(engToBrl("Good Morning!"));
// O.OO..O..O..O.O.O.O.O.O.O..OO.
// .....OO.OO.......OO..O.......OO.O.O......OO.O.O......OO..OO.
// .....OO.OO..O..O..O.O.O.O.O.O.O..OO............O.OOO.OO..OO.O.OOO.O.O.O.OO.O..
// O.....O.O...OO...........O.OOOO.....O.O...OO....
// .....OOOOO..O..OO.O..OO.OO.O.............OOO..O.O..OO.O.OOO.OO.OO..OO...OO.OO.OOOO..undefined






