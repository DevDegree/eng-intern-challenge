//Define the braille mapping
const brailleMap = {
    // LETTERS
    "LETTERS" : {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
        'z': 'O..OOO',
    },
    
    // NUMBERS
    "NUMBERS": {
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
        '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', 
    },
  
    // Special symbols
    'CAPITAL': '.....O', // Capital letter indicator
    'NUMBER': '.O.OOO', // Number indicator
    'SPACE': '......',  // Space
    'DECIMAL': '.0...0', //Decimal
    'SYMBOLS': {
        '.': '..O0.O',    // Dot indicator
        ',': '..0...', // Comma indicator
        '?': '..0.00', //Question mark indicator
        '!': '..000.', //Exclamation indicator
        ':':'..00..', //Colon indicator
        ';':'..0.0.', //semi-colon indicator
        '-': '....OO',   // Dash indicator
        '/':'.0..0.', //Slash indicator
        '<':'.00..0', //less than indicator
        '>':'0..00.', //greater than indicator
        '(':'0.0..0', //open bracket indicator
        ')':'.0.00.', //close bracket indicator
    },
  };

//helper function
const findKeyByValue = (obj, value) => {
    // Loop through each key in the object
    for (let key in obj) {
      // Check if the value matches the current key's value
      if (obj[key] === value) {
        return key; // Return the key if the value matches
      }
    }
    return null; // Return null if the value is not found
  }

// function to confirm if input is braille or english
const confirmInputType = (input) => {
    const regex = /^[O.]+$/;
    if (regex.test(input)) {
        return 'braille';
    }
    return 'english';
}

// Function to translate English to Braille
function englishToBraille(input) {
    let result = '';
    let isNumber = false;

    for (let char of input) {
      if (char === ' ') {
        result += brailleMap['SPACE'];
      } else if (/[A-Z]/.test(char)) {
        result += brailleMap['CAPITAL'] + brailleMap.LETTERS[char.toLowerCase()];
      } 
      else if (/[0-9]/.test(char)) {
        if (isNumber) {
            result += brailleMap.NUMBERS[char];
        } else {
            result += brailleMap['NUMBER'] + brailleMap.NUMBERS[char];
        }

        isNumber = true;
      }
      else if (char === '.') {
        if (isNumber) {
            result += brailleMap['DECIMAL'];
        } else {
            result += brailleMap.SYMBOLS[char]
        }
      }
      else if (/[.,?!:;\-\/<>()]+/.test(char)) {
        result += brailleMap['SYMBOLS'][char];
    }
    else {
        result += brailleMap.LETTERS[char];
    }
    }
    return result;
}
  
// Function to translate Braille to English
function brailleToEnglish(input) {
let result = '';
let chunks = input.match(/.{1,6}/g); // Split input into chunks of 6
let isCapital = false;
let isNumber = false;

for (let chunk of chunks) {
    if (chunk === brailleMap['CAPITAL']) {
    isCapital = true;
    } else if (chunk === brailleMap['NUMBER']) {
    isNumber = true;
    } else if (chunk === brailleMap['SPACE']) {
    result += ' ';
    } else if (chunk === brailleMap['DECIMAL']) {
    result += '.';
    } else if (findKeyByValue(brailleMap.SYMBOLS, chunk)) {
    result += findKeyByValue(brailleMap.SYMBOLS, chunk);
    }else if (isNumber) {
    let digit = findKeyByValue(brailleMap.NUMBERS,chunk);
    result += digit;
    }
    else {
    let letter = findKeyByValue(brailleMap.LETTERS,chunk);
    if (isCapital) {
        letter = letter.toUpperCase();
        isCapital = false;
    } 
    result += letter;
    }
}
return result;
}

// Function to handle command-line input
const translate = (input) => {
    const inputType = confirmInputType(input);
    if (inputType === 'english') {
      return englishToBraille(input);
    } else {
      return brailleToEnglish(input);
    }
  }
  
// Entry point
const input = process.argv.slice(2).join(" ");
console.log(translate(input));