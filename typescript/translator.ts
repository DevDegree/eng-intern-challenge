//Author: Jose Barboza
//Shopify Internship Challenge Winter 2024
//Date: 09/01/2024

// Mapping Braille patterns to alphabet characters
const brailleAlphabet: { [key: string]: string } = {
  'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
  'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
  'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
  'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
  'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
  'O..OOO': 'z', '......': ' ', ' ': ' ', '.....O': 'capital', '.O.OOO': 'number'
};

// Mapping Braille patterns to digits
const brailleDigits: { [key: string]: string } = {
  'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
  'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
};

// Reverse mappings from English to Braille
const englishAlphabet: { [key: string]: string } = {
  ...Object.entries(brailleAlphabet).reduce((acc, [k, v]) => {
    if (v !== 'capital' && v !== 'number') acc[v] = k; // Exclude 'capital' and 'number' mappings
    return acc;
  }, {} as { [key: string]: string }),
  ...Object.entries(brailleDigits).reduce((acc, [k, v]) => {
    acc[v] = k; // Map digits to Braille patterns
    return acc;
  }, {} as { [key: string]: string })
};

// Determine if the input string is Braille or English alphabet
function isBrailleOrAlphabet(input: string): 'braille' | 'alphabet' | 'unknown' {
  if (/^[O.\s]+$/.test(input)) {
    return 'braille'; // Input is Braille
  } else if (/^[a-zA-Z0-9\s]+$/.test(input)) {
    return 'alphabet'; // Input is English alphabet
  } else {
    return 'unknown'; // Input format is unrecognized
  }
}

// Translate Braille input to English alphabet
function translateBrailleToAlphabet(braille: string): string {
  const cleanedBraille = braille.replace(/\s+/g, ''); // Remove all spaces from Braille input
  // Match each Braille cell (6 characters) in the cleaned input
  const brailleWords = cleanedBraille.match(/.{1,6}/g) || [];

  let result = '';
  let isCapital = false; // Flag to handle capital letters
  let isNumberMode = false; // Flag to handle numbers

  brailleWords.forEach(brailleWord => {
    if (brailleWord === '.O.OOO') {
      isNumberMode = true; // Switch to number mode
    } else if (brailleWord === '.....O') {
      isCapital = true; // Switch to capital mode
    } else if (brailleWord === '......') {
      result += ' '; // Add space for Braille space pattern
      isNumberMode = false; // Exit number mode after space
    } else {
      let letter = isNumberMode ? brailleDigits[brailleWord] : brailleAlphabet[brailleWord];

      if (letter !== undefined) {
        if (isCapital) {
          result += letter.toUpperCase(); // Convert to uppercase if in capital mode
          isCapital = false; // Reset capital mode
        } else {
          result += letter; // Add the letter to result
        }
      } else {
        console.error(`Unrecognized pattern: ${brailleWord}`); // Log error for unrecognized patterns
        result += '?'; // Placeholder for unrecognized patterns
      }

      if (isNumberMode && brailleDigits[brailleWord] === undefined) {
        isNumberMode = false; // Exit number mode if the pattern is not a digit
      }
    }
  });

  return result.trim(); // Return the final translated result
}

// Translate English alphabet input to Braille
function translateAlphabetToBraille(alphabet: string): string {
  let result = '';
  let isNumberMode = false; // Flag to handle number mode

  alphabet.split('').forEach(char => {
    if (/\d/.test(char)) {
      if (!isNumberMode) {
        result += '.O.OOO';  // Prefix for number mode
        isNumberMode = true;
      }
      result += englishAlphabet[char]; // Add Braille pattern for the digit
    } else {
      if (isNumberMode) {
        isNumberMode = false; // Exit number mode for non-digit characters
      }
      if (char === ' ') {
        result += '......'; // Braille space for space character
      } else if (char.toUpperCase() === char && char.toLowerCase() !== char) {
        result += '.....O' + englishAlphabet[char.toLowerCase()]; // Capital letter handling
      } else {
        result += englishAlphabet[char.toLowerCase()]; // Add Braille pattern for the letter
      }
    }
  });

  return result.trim(); // Return the final Braille result
}

// Determine input type and perform the appropriate translation
function translate(input: string): string {
  const inputType = isBrailleOrAlphabet(input);

  switch (inputType) {
    case 'braille':
      return translateBrailleToAlphabet(input); // Translate from Braille to English
    case 'alphabet':
      return translateAlphabetToBraille(input); // Translate from English to Braille
    default:
      return 'Unrecognized input format'; // Handle unrecognized input
  }
}

// Read input from command line arguments, translate it, and print the result
const input = process.argv.slice(2).join(' ');
const output = translate(input);

console.log(output);