// The character mappings from English to Braille.
const brailleChars = {
    a: 'O.....',
    b: 'O.O...', 
    c: 'OO....', 
    d: 'OO.O..', 
    e: 'O..O..', 
    f: 'OOO...', 
    g: 'OOOO..', 
    h: 'O.OO.', 
    i: '.OO...', 
    j: '.OOO..',
    k: 'O...O.', 
    l: 'O.O.O.', 
    m: 'OO..O.', 
    n: 'OO.OO.', 
    o: 'O.OO.', 
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
    space: '......', 
    capital: '.....O', 
    number: '.O.OOO'
}

//Check if the sequence is braille
const isBraille = (str) => {
    return /^[O.]+$/.test(input);
}

//Translate English to Braille
//reversing the mappings should have been done first but doesnt make a difference in the end
const engToBrl = (str) => {

}


// Test isBraille
console.log(isBraille("O....."));      // should be true 'a' 
console.log(isBraille("OO.O.."));      // true 'd'
console.log(isBraille("O.OO.. "));     // f 'space 
console.log(isBraille("O.....1"));     // f there is a 1
console.log(isBraille("abc.OOO"));     // f 'abc'
console.log(isBraille("O.....X"));     // f 'X'
console.log(isBraille(".....O.O...OOO.OOO"));  // t
console.log(isBraille("O..... O...."));        // f 'space in middle'