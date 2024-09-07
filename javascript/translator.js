// Braille alphabet mapping: This object maps each English letter, number, and space to its corresponding Braille representation.
// Each Braille character is represented as a 6-dot matrix, with 'O' indicating a raised dot and '.' indicating an unraised dot.
// The Braille characters for letters and numbers follow a standardized pattern as defined below.

const brailleLetters = {
  'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O.O.O.', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
  'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O.O..O', 'p': 'OOO.O.',
  'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
  'y': 'OO.OOO', 'z': 'O.OOOO', ' ': '......', '0': '.O.OO.', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
  '5': 'O.O.O.', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
};

// Translates a Braille string into English by matching each 6-character Braille cell with its corresponding letter
const translateToEnglish = (brailleString) => {
  const brailleCells = brailleString.match(/.{6}/g);
  return brailleCells.map(cell => Object.keys(brailleLetters).find(key => brailleLetters[key] === cell) || '?').join('');
};

// Translates an English string into Braille by mapping each character to its corresponding Braille symbol
const translateToBraille = (englishString) => {
  return englishString.toLowerCase().split('').map(char => brailleLetters[char] || '?').join('');
};


// Translates input by detecting whether it is in Braille or English, then converts it to the opposite format
const translate = (input) => {
  // Determine if input is Braille or English
  if (/^[O.]+$/.test(input)) {
      // Input is Braille
      return translateToEnglish(input);
  } else {
      // Input is English
      return translateToBraille(input);
  }
};

// Capture arguments from the command-line, join them into a single string, and pass to the translate function
const args = process.argv.slice(2);
const input = args.join(' ');
console.log(translate(input));

