const process = require('process');

//braille dictionaries
const englishLetterToBraille = {
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
};

const specialCharacterToBraille = {
  space: '......',
  capital: '.....O',
  number: '.O.OOO',
};

const numberToBraille = {
  1: 'O.....',
  2: 'O.O...',
  3: 'OO....',
  4: 'OO.O..',
  5: 'O..O..',
  6: 'OOO...',
  7: 'OOOO..',
  8: 'O.OO..',
  9: '.OO...',
  0: '.OOO..',
};

//consolidate all valid braille characters
const allValidBrailleChars = [
  ...Object.values(englishLetterToBraille),
  ...Object.values(specialCharacterToBraille),
  ...Object.values(numberToBraille),
];

//checks to see if there is a number in the passed input
function isNumber(input) {
  return /[0-9]/g.test(input);
}
//checks to see if there is a capital letter in the passed input
function isCapitalLetter(input) {
  return /[A-Z]/.test(input);
}

//function to check whether the received input is in braille or English
function isInputBraille(input) {
  if (input.length % 6 != 0) return false;

  for (let i = 0; i < input.length; i += 6) {
    char = input.substring(i, i + 6);
    if (!allValidBrailleChars.includes(char)) {
      return false;
    }
  }
  return true;
}

function translate(input) {
  return isInputBraille(input)
    ? translateToEnglish(input)
    : translateToBraille(input);
}

//function to reverse dictionaries for braille to English translation
function reverseBrailleDictionary(dictionary) {
  return Object.fromEntries(
    Object.entries(dictionary).map(([key, value]) => [value, key])
  );
}

//function to translate braille to English
function translateToEnglish(input) {
  let numberFollows = false;
  let capitalLetterFollows = false;
  let translation = '';

  //for loop seperates the braille into 6 character long substrings
  for (let i = 0; i < input.length; i += 6) {
    char = input.substring(i, i + 6);
    if (char == specialCharacterToBraille['space']) {
      translation += ' ';
      numberFollows = false;
    } else if (char == specialCharacterToBraille['number']) {
      numberFollows = true;
    } else if (char == specialCharacterToBraille['capital']) {
      capitalLetterFollows = true;
    } else {
      if (capitalLetterFollows) {
        translation += reverseBrailleDictionary(englishLetterToBraille)[
          char
        ].toUpperCase();
        capitalLetterFollows = false;
      } else if (numberFollows) {
        translation += reverseBrailleDictionary(numberToBraille)[char];
      } else {
        translation += reverseBrailleDictionary(englishLetterToBraille)[char];
      }
    }
  }
  return translation;
}

//function to translate english input into braille
function translateToBraille(input) {
  let translation = '';
  let numberSeen = false;
  for (let char of input) {
    if (char === ' ') {
      translation += specialCharacterToBraille['space'];
      numberSeen = false;
    } else if (isNumber(char)) {
      if (!numberSeen) {
        numberSeen = true;
        translation +=
          specialCharacterToBraille['number'] + numberToBraille[char];
      } else {
        translation += numberToBraille[char];
      }
    } else if (isCapitalLetter(char)) {
      translation +=
        specialCharacterToBraille['capital'] +
        englishLetterToBraille[char.toLowerCase()];
    } else {
      translation += englishLetterToBraille[char];
    }
  }
  return translation;
}

// Capture input from command line
const input = process.argv.slice(2).join(' ');
console.log(translate(input));
