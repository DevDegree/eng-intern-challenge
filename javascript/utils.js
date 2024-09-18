// Mapping: English to Braille (letters)
const englishToBrailleLetters = {
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

// Mapping: English to Braille (numbers)
const englishToBrailleNumbers = {
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

// Mapping: English to Braille (Special characters)
const englishToBrailleSpecialChars = {
  capital: '.....O',
  number: '.O.OOO',
  ' ': '......',
};

// Invert an object (for mapping Braille to English)
const invertObject = (obj) => {
  const inverted = {};
  for (const [key, value] of Object.entries(obj)) {
    inverted[value] = key;
  }
  return inverted;
};

// Mapping: Braille to English (letters)
const brailleToEnglishLetters = invertObject(englishToBrailleLetters);

// Mapping: Braille to English (numbers)
const brailleToEnglishNumbers = invertObject(englishToBrailleNumbers);

// Mapping: Braille to English (special characters)
const brailleToEnglishSpecialChars = invertObject(englishToBrailleSpecialChars);

// Check if the input is Braille
const isInputBraille = (input) => {
  return /^[O.]+$/.test(input);
};

module.exports = {
  englishToBrailleLetters,
  englishToBrailleNumbers,
  englishToBrailleSpecialChars,
  brailleToEnglishLetters,
  brailleToEnglishNumbers,
  brailleToEnglishSpecialChars,
  isInputBraille,
};
