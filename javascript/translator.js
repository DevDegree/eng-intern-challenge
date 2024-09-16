// MAPPING OBJECTS

// Braille to English mapping
const brailleToEnglishMapping = {
  'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i',
  '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r',
  '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z', 'O.....': '1',
  'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0',
  '......': ' ',
};

// English to Braille mapping
const englishToBrailleMapping = {
  'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...',
  'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
  's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', '1': 'O.....', 
  '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', 
  ' ': '......',
};

// Special Braille indicators
const capitalIndicator = '.....O';
const numberIndicator = '.O.OOO';

// TRANSLATION FUNCTIONS

// Check if input is Braille by ensuring it contains only 'O', '.', and ' '
function isItBraille(input) {
  for (let i = 0; i < input.length; i++) {
    if (input[i] !== 'O' && input[i] !== '.' && input[i] !== ' ') {
      return false;
    }
  }
  return true;
}

// Translate English text to Braille
function translateToBraille(text) {
  let translatedBraille = '';
  let isCurrentlyNumber = false;

  for (let i = 0; i < text.length; i++) {
    const currentChar = text[i];

    // Add capital indicator for uppercase letters
    if (currentChar >= 'A' && currentChar <= 'Z') {
      translatedBraille += capitalIndicator;
      translatedBraille += englishToBrailleMapping[currentChar.toLowerCase()];
    } 
    // Add number indicator for the first number in a sequence
    else if (currentChar >= '0' && currentChar <= '9') {
      if (!isCurrentlyNumber) {
        translatedBraille += numberIndicator;
        isCurrentlyNumber = true;
      }
      translatedBraille += englishToBrailleMapping[currentChar];
    } 
    // Handle lowercase letters and spaces
    else {
      if (isCurrentlyNumber && !(currentChar >= '0' && currentChar <= '9')) {
        isCurrentlyNumber = false;
      }
      translatedBraille += englishToBrailleMapping[currentChar] || '';
    }
  }

  return translatedBraille;
}

// Translate Braille text to English
function translateToEnglish(braille) {
  let translatedEnglish = '';
  let nextIsCapital = false;
  let nextIsNumber = false;
  let brailleBuffer = '';

  for (let i = 0; i < braille.length; i++) {
    const brailleChar = braille[i];
    brailleBuffer += brailleChar;

    // Process Braille symbol after 6 characters
    if (brailleBuffer.length === 6) {
      // Handle capital and number indicators
      if (brailleBuffer === capitalIndicator) {
        nextIsCapital = true;
      } else if (brailleBuffer === numberIndicator) {
        nextIsNumber = true;
      } else {
        // Translate the Braille symbol to English
        let englishChar = brailleToEnglishMapping[brailleBuffer];

        if (nextIsCapital) {
          englishChar = englishChar.toUpperCase();
          nextIsCapital = false;
        }

        translatedEnglish += englishChar || '';
      }

      brailleBuffer = ''; // Clear buffer for the next Braille symbol
    }
  }

  return translatedEnglish;
}

// Determine input type and translate accordingly
function translator() {
  const input = process.argv.slice(2).join(' ');

  if (isItBraille(input)) {
    console.log(translateToEnglish(input));
  } else {
    console.log(translateToBraille(input));
  }
}

translator();

// Export the functions and constants to make them available for other files
module.exports = {
  isItBraille,
  translateToBraille,
  translateToEnglish,
  translator,
  brailleToEnglishMapping,
  englishToBrailleMapping,
  capitalIndicator,
  numberIndicator
};
  
  