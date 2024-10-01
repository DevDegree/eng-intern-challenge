/***** Mapping *****/

// Braille to English 
// a-j/1-0 have the same keys, numbers are at index 1
const brailleToEnglish = {
  'O.....': ['a', '1'],
  'O.O...': ['b', '2'],
  'OO....': ['c', '3'],
  'OO.O..': ['d', '4'],
  'O..O..': ['e', '5'],
  'OOO...': ['f', '6'],
  'OOOO..': ['g', '7'],
  'O.OO..': ['h', '8'],
  '.OO...': ['i', '9'],
  '.OOO..': ['j', '0'],
  'O...O.': ['k'],
  'O.O.O.': ['l'],
  'OO..O.': ['m'],
  'OO.OO.': ['n'],
  'O..OO.': ['o'],
  'OOO.O.': ['p'],
  'OOOOO.': ['q'],
  'O.OOO.': ['r'],
  '.OO.O.': ['s'],
  '.OOOO.': ['t'],
  'O...OO': ['u'],
  'O.O.OO': ['v'],
  '.OOO.O': ['w'],
  'OO..OO': ['x'],
  'OO.OOO': ['y'],
  'O..OOO': ['z'],
  '.....O': ['uppercase'],
  '.O.OOO': ['number'],
  '......': [' ']
};

// English to Braille
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
  'uppercase': '.....O',
  'number': '.O.OOO',
  ' ': '......'
}


/***** Variables *****/

// Get args passed in terminal, and convert the args array to a string
const args = process.argv.slice(2);
const string = args.join(' ');


/***** Functions *****/

// Check input type - Return 0: Braille, 1: English
const checkInputType = () => {
  let inputType = 0;

  // If string has other than '.' or 'O', then it's English
  for (let i = 0; i < string.length; i++) {
    if (string[i] !== '.' && string[i] !== 'O') {
      inputType = 1;
    }
  }

  return inputType;
}

// Translate Braille to English 
const translateBrailleToEnglish = (string) => {
  // Make array of 6 character string
  let characters = [];
  let temp = '';
  let count = 0;

  for (let i = 0; i < string.length; i++) {
    count++;
    temp += string[i];

    // Every time 6 characters are piles up, push to characters array and reset temp/count
    if (count === 6) {
      characters.push(temp);
      temp = '';
      count = 0;
    }
  }

  // Iterate characters array to get translation for each of them, and add up to converted
  let converted = '';
  let isUppercase = false;
  let isNumber = false;

  for (let i = 0; i < characters.length; i++) {
    let current = brailleToEnglish[characters[i]];

    // Handle special characters
    if (current[0] === 'uppercase') {
      // Next character should be uppercase
      isUppercase = true;
    } else if (current[0] === 'number') {
      // Following characters should be converted as numbers
      isNumber = true;
    } else if (current[0] === ' ' && isNumber) {
      // If a space appears after number/s, add the space and reset the isNumber flag
      converted += current[0];
      isNumber = false;
    } else {
      // Handle regular characters
      if (isNumber) {
        // If isNumber is true, use index 1 to convert it as number
        converted += current[1];
      } else if (isUppercase) {
        // Convert to uppercase and reset the isUppercase flag
        converted += current[0].toUpperCase();
        isUppercase = false;
      } else {
        converted += current[0];
      }
    }
  }

  return converted;
}

// Translate English to Braille
const translateEnglishToBraille = (string) => {
  let converted = '';
  let isNumber = false;

  for (let i = 0; i < string.length; i++) {
    // If it's number
    if (parseInt(string[i])) {
      // If it is the first one of continuous numbers, add braille string for number, and make isNumber flag true
      if (!isNumber) {
        converted += englishToBraille['number']
        isNumber = true;
      }
      // add the number itself
      converted += englishToBraille[string[i]];
    } else {
      // If it's not number
      // Reset isNumber flag 
      isNumber = false;

      if (string[i] !== string[i].toLowerCase()) {
        // If the character is uppercase, add braille string for uppercase, and add the character with lowercase in the mapping
        converted += englishToBraille['uppercase'] + englishToBraille[string[i].toLowerCase()];
      } else {
        converted += englishToBraille[string[i]];
      }
    }
  }

  return converted;
}


/***** Process *****/

// Get translation depending on input type (0: Braille, 1: English)
let translation;
if (checkInputType() === 0) {
  translation = translateBrailleToEnglish(string);
} else {
  translation = translateEnglishToBraille(string);
};

// Display translation in terminal
console.log(translation);