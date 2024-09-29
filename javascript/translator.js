// English to Braille dictionary
const ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    'A': '.....OO.....', 'B': '.....OO.O...', 'C': '.....OOO....', 'D': '.....OOO.O..', 
    'E': '.....O..O..', 'F': '.....OOO...', // and so on for the rest of capital letters
    ' ': '......',  // Braille for space
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
    // add other characters like capital letters and numbers
  };

  // Adding capital letters for English to Braille conversion
for (let char of 'abcdefghijklmnopqrstuvwxyz') {
    ENGLISH_TO_BRAILLE[char.toUpperCase()] = '.....O' + ENGLISH_TO_BRAILLE[char];
}
  
  // Braille to English dictionary
  const BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z',
    '......': ' ', // Braille for space
    '.....OO.....': 'A', // Capital A
    '.....OO.O...': 'B', // Capital B, and so on for the rest of capital letters
    // add numbers as well
  };

  // Adding capital letters for Braille to English conversion
for (let char of 'abcdefghijklmnopqrstuvwxyz') {
    BRAILLE_TO_ENGLISH['.....O' + ENGLISH_TO_BRAILLE[char]] = char.toUpperCase();
}

  // Function to convert English to Braille
function englishToBraille(englishText) {
    let brailleText = '';
    for (let char of englishText) {
      if (char.match(/[A-Z]/)) {
        // If it's an uppercase letter, first add the capitalization symbol
        brailleText += '.....O';
        char = char.toLowerCase();
      }
      brailleText += ENGLISH_TO_BRAILLE[char] || ''; // Add Braille equivalent
    }
    return brailleText;
  }

  // Function to convert Braille to English
function brailleToEnglish(brailleText) {
    let englishText = '';
    let isCapital = false; // Flag to check if the next letter is capitalized
  
    // Split the Braille string into chunks of 6 dots each
    for (let i = 0; i < brailleText.length; i += 6) {
      let brailleChar = brailleText.slice(i, i + 6);
      
      if (brailleChar === '.....O') {
        // If we encounter the capitalization symbol
        isCapital = true;
        continue; // Skip to the next character
      }
  
      let englishChar = BRAILLE_TO_ENGLISH[brailleChar] || '';
      if (isCapital) {
        englishChar = englishChar.toUpperCase();
        isCapital = false;
      }
      englishText += englishChar;
    }
    return englishText;
  }

  // Function to detect input type and call the appropriate translation function
function translate(input) {
    if (/^[O.]+$/.test(input)) {
      return brailleToEnglish(input); // If the input contains only O's and .'s, it's Braille
    } else {
      return englishToBraille(input); // Otherwise, assume it's English
    }
  }

  // Capture input from the command line
if (require.main === module) {
    const input = process.argv.slice(2).join(' '); // Join all arguments into one string
    const output = translate(input); // Call the translate function
    console.log(output); // Output the result
  }
  