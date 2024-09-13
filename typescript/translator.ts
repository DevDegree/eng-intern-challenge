/// <reference types="node" />

const brailleAlphabet: { [key: string]: string } = {
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
  ' ': '......',
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
  '.': '.O.O.O',
  ',': '.O....',
  ';': '.O.O..',
  ':': '.OO...',
  '!': '.O.OO.',
  '?': '.O..O.',
  "'": '.....O',
  '-': '..OO..',
  '(': '.O..OO',
  ')': '.O..OO',
};

const numberPrefix = '.O.OOO';
const capitalPrefix = '.....O';

function translateToBraille(input: string): string {
  let result = '';
  let isNumber = false;

  for (const char of input) {
    if (/[0-9]/.test(char)) {
      if (!isNumber) {
        result += numberPrefix;
        isNumber = true;
      }
      result += brailleAlphabet[char];
    } else {
      if (isNumber) {
        isNumber = false;
      }
      if (/[A-Z]/.test(char)) {
        result += capitalPrefix;
      }
      result += brailleAlphabet[char.toLowerCase()] || '';
    }
  }

  return result;
}

function translateToEnglish(input: string): string {
  let result = '';
  const reverseBraille = Object.fromEntries(Object.entries(brailleAlphabet).map(([k, v]) => [v, k]));
  let isCapital = false;
  let isNumber = false;

  for (let i = 0; i < input.length; i += 6) {
    const char = input.slice(i, i + 6);

    if (char === capitalPrefix) {
      isCapital = true;
      continue;
    }

    if (char === numberPrefix) {
      isNumber = true;
      continue;
    }

    if (reverseBraille[char]) {
      let translatedChar = reverseBraille[char];
      if (isNumber) {
        if (translatedChar >= 'a' && translatedChar <= 'j') {
          translatedChar = String.fromCharCode(translatedChar.charCodeAt(0) - 97 + 49);
        } else {
          isNumber = false;
        }
      } else if (isCapital) {
        translatedChar = translatedChar.toUpperCase();
        isCapital = false;
      }
      result += translatedChar;
    }
  }

  return result;
}

function translate(input: string): string {
  return input.includes('.') || input.includes('O') ? translateToEnglish(input) : translateToBraille(input);
}

// Get input from command line arguments
const input = process.argv.slice(2).join(' ');

if (input) {
  console.log(translate(input));
} else {
  console.error('Please provide a string to translate.');
}

export { translate };
