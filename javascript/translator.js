
// Dictionary for Braille Alphabets and Numbers

const BRAILLE_ALPHABET = {
  'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
  'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
  'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
  'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
  'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
  'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
  'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......',
  'capital': '.....O',
  'number': '.O.OOO'
};

const BRAILLE_NUMBERS = {
  '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
  '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
  '9': '.OO...', '0': '.OOO..'
};


/**
 * Converts English text to Braille.
 * @param {string} text - The English text to convert.
 * @return {string} The Braille representation of the input text.
 */
function englishToBraille(text) {
  let result = '';
  let numberMode = false; // flag to determine if in number mode

  for (let i = 0; i < text.length; i++) {
    const char = text[i].toLowerCase();
    if (/[a-z]/.test(char)) { // Letter
      if (text[i] === text[i].toUpperCase()) { // uppercase
        result += BRAILLE_ALPHABET['capital'];
      }
      result += BRAILLE_ALPHABET[char];
      numberMode = false;
    } else if (/[0-9]/.test(char)) { // Number
      if (!numberMode) {
        result += BRAILLE_ALPHABET['number'];
        numberMode = true;
      }
      result += BRAILLE_NUMBERS[char];
    } else if (char === ' ') { // Space
      result += BRAILLE_ALPHABET[' '];
      numberMode = false;
    }
  }

  return result;
}

/**
 * Converts Braille to English text.
 * @param {string} braille - The Braille text to convert.
 * @return {string} The English representation of the input Braille.
 */
function brailleToEnglish(braille) {
  let result = '';
  const brailleChars = braille.match(/.{6}/g) || []; // split string into groups of 6
  let capitalNext = false;
  let numberMode = false;

  for (const char of brailleChars) {
    if (char === BRAILLE_ALPHABET['capital']) { // enters capital mode
      capitalNext = true;
    } else if (char === BRAILLE_ALPHABET['number']) { // enters number mode
      numberMode = true;
    } else if (char === BRAILLE_ALPHABET[' ']) { // handles spaces
      result += ' ';
      numberMode = false;
    } else {
      if (numberMode) { // convert to digit
        result += Object.keys(BRAILLE_NUMBERS).find(key =>
            BRAILLE_NUMBERS[key] === char);
      } else { // convert to english letter
        let letter = Object.keys(BRAILLE_ALPHABET).find(key =>
            BRAILLE_ALPHABET[key] === char);
        result += capitalNext ? letter.toUpperCase() : letter;
        capitalNext = false;
      }
    }
  }

  return result;
}

/**
 * Determines the input type and calls the appropriate function
 * @param {string} input - The string to be translated
 * @return {string} The translated string
 */
function translate(input) {
  if (/^[O.]+$/.test(input)) { // Determine if it is Braille
    return brailleToEnglish(input);
  } else {
    return englishToBraille(input);
  }
}

if (process.argv.length < 3) { // Error checking
  console.log("String is not provided. Run again with node translator.js <string>");
} else {
  // Joining all command line arguments into a single string
  const input = process.argv.slice(2).join(' ');
  console.log(translate(input));
}
