#!/usr/bin/env node

// Braille mappings for letters, numbers, and special indicators
const brailleMap = {
  'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
  'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
  'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
  'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
  'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
  'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
  'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......',
  '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
  '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
  '9': '.OO...', '0': '.OOO..',
  '#': '.O.OOO', // Braille number indicator
  'capital': '.....O' // Braille capitalization indicator
};

const reverseBrailleMap = Object.fromEntries(
  Object.entries(brailleMap).map(([key, value]) => [value, key])
);

// Determine if the input string is Braille
function isBraille(input) {
  return /^[O\.]+(\s[O\.]+)*$/.test(input);
}

// Translate from Braille to English
function translateBrailleToEnglish(braille) {
  const words = braille.split(' ');
  let output = '';
  let isCapital = false;

  for (let i = 0; i < words.length; i++) {
    const symbol = words[i];

    if (symbol === brailleMap['capital']) {
      isCapital = true;
      continue;
    }

    if (reverseBrailleMap[symbol]) {
      let letter = reverseBrailleMap[symbol];
      if (isCapital) {
        letter = letter.toUpperCase();
        isCapital = false;  // Reset capitalization after use
      }
      output += letter;
    } else if (symbol === brailleMap[' ']) {
      output += ' ';
    } else {
      console.error(`Unrecognized symbol: ${symbol}`);
    }
  }

  return output;
}

// Translate from English to Braille
function translateEnglishToBraille(english) {
  return english.split('').map(char => {
    if (/[A-Z]/.test(char)) {
      return `${brailleMap.capital} ${brailleMap[char.toLowerCase()]}`;
    } else if (/\d/.test(char)) {
      return `${brailleMap['#']} ${brailleMap[char]}`;
    } else {
      return brailleMap[char] || '';
    }
  }).join(' ');
}

// Main translation function
function translate(input) {
  if (isBraille(input)) {
    return translateBrailleToEnglish(input);
  } else {
    return translateEnglishToBraille(input.toLowerCase());
  }
}

// Run the translation based on command-line input
const input = process.argv[2];
if (input) {
  console.log(translate(input));
} else {
  console.log('Please provide a string to translate.');
}
