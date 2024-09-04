// Mapping from English characters to Braille representations
const englishToBraille = {
  'a': 'O.....', 'b': 'OO....', 'c': 'O.O...', 'd': 'O.OO..', 'e': 'O..O..', 'f': 'OO.O..', 'g': 'OOOO..', 'h': 'O..OO.',
  'i': '.O.O..', 'j': '.OOO..', 'k': 'O...O.', 'l': 'OO..O.', 'm': 'O.OO.O', 'n': 'O.OOOO', 'o': 'O..OO.', 'p': 'OO.OO.',
  'q': 'OOOOO.', 'r': 'O..OOO', 's': '.O.OO.', 't': '.OOOOO', 'u': 'O...OO', 'v': 'OO..OO', 'w': '.OOOO.', 'x': 'O.O.OO',
  'y': 'O.OOOO', 'z': 'O..OOO', ' ': '......', // Space
  '0': '.OOOOO', '1': 'O.....', '2': 'OO....', '3': 'O.O...', '4': 'O.OO..', '5': 'O..O..', '6': 'OO.O..', '7': 'OOOO..',
  '8': 'O..OO.', '9': '.O.O..'
};

// Create a reverse mapping for Braille to English
const brailleToEnglish = {};
for (const [char, braille] of Object.entries(englishToBraille)) {
  brailleToEnglish[braille] = char;
}

// Special Braille signs for capital letters and numbers
const capitalSign = '.....O';
const numberSign = '.O.OOO';

// Check if the input is English (letters, numbers, spaces)
function isEnglish(input) {
  return /^[a-zA-Z0-9\s]+$/.test(input);
}

// Check if the input is Braille (using 'O' and '.')
function isBraille(input) {
  return /^[O\.]+$/.test(input);
}

// Convert English text to Braille
function translateEnglishToBraille(input) {
  let result = '';
  let isNumber = false;

  for (let char of input) {
    if (char === ' ') {
      result += englishToBraille[' '];
    } else if (/\d/.test(char)) {
      if (!isNumber) {
        result += numberSign;
        isNumber = true;
      }
      result += englishToBraille[char];
    } else if (/[A-Z]/.test(char)) {
      result += capitalSign; 
      result += englishToBraille[char.toLowerCase()];
      isNumber = false;
    } else if (/[a-z]/.test(char)) {
      result += englishToBraille[char];
      isNumber = false;
    }
  }

  return result;
}

// Convert Braille text to English
function translateBrailleToEnglish(input) {
  let result = '';
  let isNumber = false;

  for (let i = 0; i < input.length; i += 6) {
    let brailleChar = input.slice(i, i + 6);

    if (brailleChar === numberSign) {
      isNumber = true; // Switch to number mode
      continue;
    }

    if (brailleChar === capitalSign) {
      // Handle capital letters (convert next character to uppercase)
      let nextChar = brailleToEnglish[input.slice(i + 6, i + 12)];
      result += nextChar ? nextChar.toUpperCase() : '?';
      i += 6; // Skip the next character
    } else {
      let englishChar = brailleToEnglish[brailleChar];
      result += isNumber && englishChar !== ' ' ? englishChar : englishChar || '?'; // Use '?' for unknown Braille characters
      isNumber = false;
    }
  }

  return result;
}

// Get the input from command-line arguments
const inputString = process.argv.slice(2).join(" ");

// Process the input based on its type
if (isEnglish(inputString)) {
  console.log(translateEnglishToBraille(inputString));
} else if (isBraille(inputString)) {
  console.log(translateBrailleToEnglish(inputString));
} else {
  console.log("Invalid input. Please provide a valid English or Braille string.");
}
