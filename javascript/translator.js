const process = require('process');

const englishToBraille = {
  'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
  'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
  'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
  'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
  'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
  ' ': '......',  // Space
  'capital': '.....O',  // Capital indicator
  'number': '.O.OOO'    // Number indicator
};

const brailleToEnglish = {
  'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
  'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
  'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
  'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
  'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z',
  '......': ' ',  // Space
  '.....O': 'capital',  // Capital indicator
  '.O.OOO': 'number'    // Number indicator
};

const numberToBraille = {
  '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
  '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
};

const brailleToNumber = {
  'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
  'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
};

// Function to check if the input is Braille or English
function isBraille(input) {
  const braillePattern = /^[O.]+$/; // Braille will only contain 'O' and '.'
  return braillePattern.test(input);
}

// Main function to handle the input
function main() {
  // Get arguments from the command line
  const args = process.argv.slice(2); // Skip the first two elements (node and script path)

  if (args.length === 0) {
    console.error('Please provide a string to translate.');
    return;
  }

  const input = args.join(' '); // Combine all arguments into a single string

  // Determine if the input is Braille or English
  if (isBraille(input)) {
    console.log('Input is Braille');
  } else {
    console.log('Input is English');
  }
}

main();
