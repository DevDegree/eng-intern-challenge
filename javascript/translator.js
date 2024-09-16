// CONSTANTS 
const ENGLISH_LETTER_TO_BRAILLE = {
  // Letters
  'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
  'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
  'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
  'y': 'OO.OOO', 'z': 'O..OOO', 
};

const NUMBER_TO_BRAILLE = {
  // Numbers
  '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..',
  '8': 'O.OO..', '9': '.OO...', '0': '.O....', 
}

const BRAILLE_TO_ENGLISH_LETTER = Object.fromEntries(
  Object.entries(ENGLISH_LETTER_TO_BRAILLE).map(([key, value]) => [value, key])
);

const BRAILLE_TO_NUMBER = Object.fromEntries(
  Object.entries(NUMBER_TO_BRAILLE).map(([key, value]) => [value, key])
);

// HELPER FUNCTIONS

/**
 * Check if it is Braille.
 * @param {String} input String
 * @returns true if it only composed of `.` and `O`, 
 *          and if the length of the input is divisible by 6 to match braile alphabet.
 */
function isBraille(input) {
  return /^[O.]+$/.test(input) && input.length % 6 == 0;
}

/**
 * Check if it is a capitalized letter
 * @param {String} char single character
 * @returns true it if character is part of the capitalized letter [A-Z].
 */
function isCapitalized(char) {
  return /^[A-Z]$/.test(char);
}

/**
 * Check if it is a number
 * @param {String} char single character
 * @returns true if character is a number [0-9].
 */
function isNumber(char) {
  return /^\d$/.test(char);
}

/**
 * Translate English to Braille
 * @param {String} text in English
 * @returns and print the Braille translation of an English text.
 */
function englishToBraille(text) {
  let result = "";
  let isNum = false;

  for(const char of text) {
    const lowerChar = char.toLowerCase();

    if(!lowerChar in ENGLISH_LETTER_TO_BRAILLE | !lowerChar in NUMBER_TO_BRAILLE) {
      return `ERROR: ${char} is not an alphanumerical character!`;
    }

    // Handle `number follow`
    if(isNumber(char)) {
      if(!isNum) {
        result += ".O.OOO";
      }
      result += NUMBER_TO_BRAILLE[char];
      isNum = true;
    }      
    // Handle `capital follow`
    else if(isCapitalized(char)) {
      result += ".....O";
      result += ENGLISH_LETTER_TO_BRAILLE[lowerChar];
    }
    // Handle spaces
    else if(char.match(` `)) {
      result += "......";
      isNum = false;
    }
    else {
      result += ENGLISH_LETTER_TO_BRAILLE[char];
    }
    
  }
  return result;
}

/**
 * Translate Braille to English
 * @param {String} text in Braille
 * @returns and print the English translation of an English text.
 */
function brailleToEnglish(text) {
  const brailleChunk = text.match(/.{1,6}/g);
  let result = "";
  let isNum = false;
  let isCapital = false;

  for(const chunk of brailleChunk) {
    // Handle `capitale follow`
    if(chunk === ".....O") {
      isCapital = true;
      continue;
    }
    // Handle `numbers follow`
    else if(chunk === ".O.OOO") {
      isNum = true;
      continue;
    }
    else if(chunk === "......") {
      isNum = false;
      continue;
    }
    else {
      if(!chunk in BRAILLE_TO_ENGLISH_LETTER | !chunk in BRAILLE_TO_NUMBER){
        return `ERROR: ${chunk} is not a valid Braille character`
      }
      else{
        if(isCapital) {
          result += BRAILLE_TO_ENGLISH_LETTER[chunk].toUpperCase();
          isCapital = false;
        }
        else if(isNum) {
          result += BRAILLE_TO_NUMBER[chunk];
        }
        else {
          result += BRAILLE_TO_ENGLISH_LETTER[chunk];
        }
      }    
    }
  }
  return result;
}

// MAIN FUNCTION

/**
 * Translate from English to Braille or vice-versa
 * @param {String} text to be translated, can be English or Braille
 * @returns the translated text in the other language.
 */
function translate(text) {
  if(isBraille(text)){
    console.log(brailleToEnglish(text));
  }
  else {
    console.log(englishToBraille(text));
  }
}

// TERMINAL FUNCTION CALL

// Assume function call is `node translator.js`
const inputText = process.argv.slice(2);

if (!inputText) {
  console.error("Please provide text to translate.");
  process.exit(1);  
}

translate(inputText.join(` `));
