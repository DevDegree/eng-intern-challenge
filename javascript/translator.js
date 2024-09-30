const [, , ...input] = process.argv;
const CAPITAL_FOLLOWS = '.....O';
const NUMBER_FOLLOWS = '.O.OOO';
const NUMBER_END = '......';

const brailleToCharacters = {
  'O.....': 'a',
  'O.O...': 'b',
  'OO....': 'c',
  'OO.O..': 'd',
  'O..O..': 'e',
  'OOO...': 'f',
  'OOOO..': 'g',
  'O.OO..': 'h',
  '.OO...': 'i',
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
  '.OOO.O': 'w',
  'OO..OO': 'x',
  'OO.OOO': 'y',
  'O..OOO': 'z',
  '......': ' ',
};

const brailleToNumbers = {
  'O.....': '1',
  'O.O...': '2',
  'OO....': '3',
  'OO.O..': '4',
  'O..O..': '5',
  'OOO...': '6',
  'OOOO..': '7',
  'O.OO..': '8',
  '.OO...': '9',
  '.OOO..': '0',
};

const charactersToBraille = {};
for (const [braille, char] of Object.entries(brailleToCharacters)) {
  charactersToBraille[char] = braille;
}

const numbersToBraille = {};
for (const [braille, num] of Object.entries(brailleToNumbers)) {
  numbersToBraille[num] = braille;
}

/**
 * Checks if a provided character is a capital letter
 * @param {*} char the character to be checked
 * @returns true if the character is a capital letter, false if not
 */
const isUpperCase = (char) => {
  return char.charCodeAt(0) >= 65 && char.charCodeAt(0) <= 90;
};

/**
 * Checks if a provided character is a number
 * @param {*} char the character to be checked
 * @returns true if the character is a number, false if not
 */
const isNumber = (char) => {
  return char.charCodeAt(0) >= 48 && char.charCodeAt(0) <= 57;
};

/**
 * Translates a string of Braille (represented by a series of 'O' and '.') into English and prints the result onto console
 * @param {*} input the provided Braille string
 */
const translateBraille = (input) => {
  var english = '';
  var capFlag = false;
  var numFlag = false;
  const length = input.length / 6;
  if (input.length % 6 != 0) {
    console.log('not valid braille');
  }
  for (let i = 0; i < length; i++) {
    let cell = input.substring(i * 6, (i + 1) * 6);
    if (cell == CAPITAL_FOLLOWS) {
      capFlag = true;
    } else if (cell == NUMBER_FOLLOWS) {
      numFlag = true;
    } else if (numFlag && cell == NUMBER_END) {
      numFlag = false;
      english += brailleToCharacters[cell];
    } else if (capFlag) {
      english += brailleToCharacters[cell].toUpperCase();
      capFlag = false;
    } else if (numFlag) {
      english += brailleToNumbers[cell];
    } else {
      english += brailleToCharacters[cell];
    }
  }
  console.log(english);
};

/**
 * Translates a string of English into Braille and prints the result onto console
 * @param {*} input the provided English string
 */
const translateEnglish = (input) => {
  var braille = '';
  var numFlag = false;
  for (let i = 0; i < input.length; i++) {
    let char = input.charAt(i);
    if (numFlag && !isNumber(char)) {
      numFlag = false;
    }
    if (isUpperCase(char)) {
      braille += CAPITAL_FOLLOWS;
      braille += charactersToBraille[char.toLowerCase()];
    } else if (isNumber(char) && !numFlag) {
      numFlag = true;
      braille += NUMBER_FOLLOWS;
      braille += numbersToBraille[char];
    } else if (isNumber(char) && numFlag) {
      braille += numbersToBraille[char];
    } else {
      braille += charactersToBraille[char];
    }
  }
  console.log(braille);
};

/**
 * Checks if the command line argument provided is English or Braille text, and calls the respective translation method
 * @param {*} input the provided string to be checked
 */
const checkMode = (input) => {
  if (input.length == 0) {
    console.log('');
  } else if (input.substring(0, 6).indexOf('.') != -1) {
    translateBraille(input);
  } else {
    translateEnglish(input);
  }
};

checkMode(input.join(' '));
