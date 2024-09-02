// Translator by Marzuk Mashrafe (created 02-09-2024)
// Has a runtime of O(n) which is the best possible runtime.

const BRAILLE_REGEX = /^[O.]*$/; // RegEx to detect Braille input
const INTEGER_REGEX = /[0-9]/; // RegEx to detect Int Char

const CAPITAL_FOLLOWS = '.....O';
const DECIMAL_FOLLOWS = '.O...O';
const NUMBER_FOLLOWS = '.O.OOO';
const SPACE = '......';

//----------------------------Translate to Braille----------------------------//

const englishToBraille = {
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

  // Capitalization hard-coded for simpler logic
  'A': '.....OO.....', 
  'B': '.....OO.O...', 
  'C': '.....OOO....', 
  'D': '.....OOO.O..', 
  'E': '.....OO..O..',
  'F': '.....OOOO...', 
  'G': '.....OOOOO..', 
  'H': '.....OO.OO..', 
  'I': '.....O.OO...', 
  'J': '.....O.OOO..',
  'K': '.....OO...O.', 
  'L': '.....OO.O.O.', 
  'M': '.....OOO..O.', 
  'N': '.....OOO.OO.', 
  'O': '.....OO..OO.',
  'P': '.....OOOO.O.', 
  'Q': '.....OOOOOO.', 
  'R': '.....OO.OOO.', 
  'S': '.....O.OO.O.', 
  'T': '.....O.OOOO.',
  'U': '.....OO...OO', 
  'V': '.....OO.O.OO', 
  'W': '.....O.OOO.O', 
  'X': '.....OOO..OO', 
  'Y': '.....OOO.OOO',
  'Z': '.....OO..OOO', 
  
  '1': 'O.....', 
  '2': 'O.O...', 
  '3': 'OO....', 
  '4': 'OO.O..', 
  '5': 'O..O..',
  '6': 'OOO...', 
  '7': 'OOOO..', 
  '8': 'O.OO..', 
  '9': '.OO...', 
  '0': '.OOO..'
};

/**
 * Translates given English input into Braille in O(n) runtime.
 * 
 * @param {string} braille : English sentence (in string form)
 * @returns {string} Braille translation as a string
 */
function TranslateToBraille(english) {
  const len = english.length; // length of input
  let inNumberMode = false; // Keeps track of whether the previous char was a number

  let translation = "";
  // Translate English->Braille one char at a time -> O(n) runtime
  for (let i = 0; i < len; i++) {
    const char = english.charAt(i);
    if (INTEGER_REGEX.test(char)) { // Char is a 0-9 number
      if (!inNumberMode) {
        inNumberMode = true;
        translation += NUMBER_FOLLOWS;
      }
      translation += englishToBraille[char];
    } else if (char === " ") { // Char is a space
      inNumberMode = false;
      translation += SPACE;
    } else { // Char is an English letter
      translation += englishToBraille[char];
    }
  }

  // Output
  return translation;
}

//----------------------------------------------------------------------------//



//----------------------------Translate to English----------------------------//

// Object mapping Braille Cells to English alphabet
const brailleToLetters = {
  'O.....': 'a', 
  'O.O...': 'b', 
  'OO....': 'c', 
  'OO.O..': 'd', 
  'O..O..': 'e',
  'OOO...': 'f', 
  'OOOO..': 'g', 
  'O.OO..': 'h', 
  '.OO...': 'i', 
  '.OOO..': 'j',
  'O...O.': 'k', 
  'O.O.O.': 'l', 
  'OO..O.': 'm', 
  'OO.OO.': 'n', 
  'O..OO.': 'o',
  'OOO.O.': 'p', 
  'OOOOO.': 'q', 
  'O.OOO.': 'r', 
  '.OO.O.': 's', 
  '.OOOO.': 't',
  'O...OO': 'u', 
  'O.O.OO': 'v', 
  '.OOO.O': 'w', 
  'OO..OO': 'x', 
  'OO.OOO': 'y',
  'O..OOO': 'z'
};

// Object mapping Braille Cells to Numbers
const brailleToNumbers = {
  'O.....': '1', 
  'O.O...': '2', 
  'OO....': '3', 
  'OO.O..': '4', 
  'O..O..': '5',
  'OOO...': '6', 
  'OOOO..': '7', 
  'O.OO..': '8', 
  '.OO...': '9', 
  '.OOO..': '0'
};

/**
 * Translates given Braille input into English in O(n) runtime.
 * 
 * @param {string} braille : Braille representation as a series of O (the letter O) or . (a period)
 * @returns {string} English translation as a string
 */
function TranslateToEnglish(braille) {
  // Braille input length must be a multiple of 6 -> O(1)
  if (braille.length % 6 !== 0) return "";

  // Create an array of Braille cells -> O(n)
  const brailleCells = braille.match(/.{1,6}/g);

  // Variable storing the translations
  let translation = "";

  let upcomingCapital = false;
  let upcomingNumbers = false;
  // Translate Braille->English one cell at a time -> O(n)
  brailleCells.forEach(brailleCell => {
    if (brailleCell === CAPITAL_FOLLOWS) { // upcoming capital letter flag set
      upcomingCapital = true;
    } else if (brailleCell === NUMBER_FOLLOWS) { // upcoming numbers flag set
      upcomingNumbers = true;
    } else if (brailleCell === SPACE) { // space is encountered
      upcomingNumbers = false;
      upcomingCapital = false;
      translation += " ";
    } else if (brailleCell === DECIMAL_FOLLOWS) { // decimal (not in technical requirement but was in the picture)
      translation += ".";
    } else {
      let char; // temporary char for translation
      if (upcomingNumbers) {
        char = brailleToNumbers[brailleCell];
      } else {
        char = brailleToLetters[brailleCell];
        if (upcomingCapital) {
          char = char.toUpperCase();
          upcomingCapital = false;
        }
      }
      translation += char;
    }
  });

  // Output
  return translation;
}

//----------------------------------------------------------------------------//


//----------------------------------- Main -----------------------------------//

// Number of words provided in the terminal/CLI
const numberOfWords = (process.argv.length - 2);

if (numberOfWords < 1) { // Empty String is printed in case of no input
  console.log("");
} else { // If one or more strings are provided in the input

  // Extract the input from command-line arguments as one string
  const input = process.argv.slice(2).join(" ");

  // Check if the given input is in Braille 
  // (assuming Braille is given as a single word string - this wasn't clear
  //  in the challenge)
  const isBraille = BRAILLE_REGEX.test(input);

  // Translate using helper functions
  let translation;
  if (isBraille) {
    translation = TranslateToEnglish(input); // Braille -> English
  } else {
    translation = TranslateToBraille(input); // English -> Braille
  }

  // Main Output
  console.log(translation);
}

//----------------------------------------------------------------------------//
//------------------------------------ EOF -----------------------------------//