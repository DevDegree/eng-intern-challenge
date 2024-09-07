// Braille alphabet mapping: This object maps each English letter, number, and space to its corresponding Braille representation.
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
  if (!brailleCells) return ''; // Return empty string if no valid Braille cells

  return brailleCells.map(cell => {
    const englishChar = Object.keys(brailleLetters).find(key => brailleLetters[key] === cell);
    return englishChar || '?'; // Return '?' if Braille cell is not found
  }).join('');
};

// Translates an English string into Braille by mapping each character to its corresponding Braille symbol
const translateToBraille = (englishString) => {
  let inNumberMode = false;
  return englishString.split('').map(char => {
    if (char === ' ') {
      inNumberMode = false; // Reset number mode after space
      return brailleLetters[' '];
    }
    if (/[A-Z]/.test(char)) {
      inNumberMode = false; // Reset number mode for letters
      return '.....O' + brailleLetters[char.toLowerCase()];
    }
    if (/[0-9]/.test(char)) {
      if (!inNumberMode) {
        inNumberMode = true;
        return '.O.OOO' + brailleLetters[char];
      }
      return brailleLetters[char];
    }
    inNumberMode = false;
    return brailleLetters[char] || '?'; // Return '?' if character is not in mapping
  }).join('');
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


