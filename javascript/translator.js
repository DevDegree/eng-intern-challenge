// Braille mappings
const BRAILLE = {
  'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
  'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
  'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
  'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
  'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
  'z': 'O..OOO', ' ': '......',
  '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
  '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
  'capital': '.....O', 'decimal': '.O...O', 'number': '.O.OOO',
  '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
  ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
  '(': 'O.O..O', ')': '.O..'
};

// Reverse mapping for Braille to text conversion
const REVERSE_BRAILLE = Object.fromEntries(Object.entries(BRAILLE).map(([k, v]) => [v, k]));

// Converts text to Braille.
function textToBraille(text) {
  let result = '';
  let inNumber = false;

  for (const char of text) {
      if (/\d/.test(char)) {
          if (!inNumber) {
              result += BRAILLE['number'];
              inNumber = true;
          }
          result += BRAILLE[char];
      } else if (/[a-zA-Z]/.test(char)) {
          if (char === char.toUpperCase() && char !== char.toLowerCase()) {
              result += BRAILLE['capital'];
          }
          result += BRAILLE[char.toLowerCase()];
          inNumber = false;
      } else if (char === ' ') {
          result += BRAILLE[' '];
          inNumber = false;
      } else {
          result += BRAILLE[char] || '';
          inNumber = false;
      }
  }

  return result;
}

// Converts Braille to text
function brailleToText(braille) {
  const chunks = braille.match(/.{6}/g) || [];
  let result = '';
  let isCapital = false;
  let isNumber = false;

  for (const chunk of chunks) {
      if (chunk === BRAILLE['capital']) {
          isCapital = true;
      } else if (chunk === BRAILLE['number']) {
          isNumber = true;
      } else {
          let char = REVERSE_BRAILLE[chunk] || '?';
          if (isNumber) {
              if (char >= 'a' && char <= 'j') {
                  char = String.fromCharCode(char.charCodeAt(0) - 'a'.charCodeAt(0) + '1'.charCodeAt(0));
              }
              isNumber = false;
          }
          if (isCapital) {
              char = char.toUpperCase();
              isCapital = false;
          }
          result += char;
      }
  }

  return result;
}

// Main function to handle command-line input for text-to-Braille or Braille-to-text conversion
function main() {
  const inputText = process.argv.slice(2).join(' ');

  if (/^[.O]+$/.test(inputText)) {
      console.log(brailleToText(inputText));
  } else {
      console.log(textToBraille(inputText));
  }
}

if (require.main === module) {
  main();
}
