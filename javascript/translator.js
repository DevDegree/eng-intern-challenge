// Object for English to Braille alphabets
const ENGLISH_BRAILLE_CHAR = {
  'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..", 'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
  'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.", 'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
  'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO", 'z': "O..OOO", 'capital': ".....O"
};

// Object for English to Braille numbers and special characters
const ENGLISH_BRAILLE_NUM = {
  '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO..",
  'decimal': ".O...O", 'number': ".O.OOO", '.': "..OO.O", ',': "..O...", '?': "..O.OO", '!': "..OOO.", ':': "..OO..", ';': "..O.O.", '-': "....OO", '/': ".O..O.",
  '<': ".OO..O", '>': "O..OO.", '(': "O.O..O", ')': ".O.OO.", 'space': "......"
};

// Converting Braille symbols into English alphabets and storing them as objects
const BRAILLE_ENGLISH_CHAR = Object.fromEntries(Object.entries(ENGLISH_BRAILLE_CHAR).map(([key, value]) => [value, key]));

// Converting Braille symbols into English numbers and special characters and storing them as objects
const BRAILLE_ENGLISH_NUM = Object.fromEntries(Object.entries(ENGLISH_BRAILLE_NUM).map(([key, value]) => [value, key]));


// Function to detect if the input string is Braille
function isBraille(input) {
  return input.match(/^[O.]+$/) !== null;
}

// Function to translate from English to Braille
function translateToBraille(input) {
  let brailleOutput = '';
  let isNumberMode = false;

  for (let char of input) {
    if (char === ' ') {
      brailleOutput += ENGLISH_BRAILLE_NUM['space'];
      isNumberMode = false; // The number mode will reset on encountering space character
    } else if (char.match(/[A-Z]/)) {
      brailleOutput += ENGLISH_BRAILLE_CHAR['capital'] + ENGLISH_BRAILLE_CHAR[char.toLowerCase()];
      isNumberMode = false; // The number mode will reset on encountering Capital letter
    } else if (char.match(/[0-9]/)) {
      if (!isNumberMode) {
        brailleOutput += ENGLISH_BRAILLE_NUM['number'];
        isNumberMode = true;
      }
      brailleOutput += ENGLISH_BRAILLE_NUM[char];
    } else if (ENGLISH_BRAILLE_CHAR[char]) {
      brailleOutput += ENGLISH_BRAILLE_CHAR[char];
      isNumberMode = false; // The number mode will reset on encountering letter
    } else if (ENGLISH_BRAILLE_NUM[char]) {
      brailleOutput += ENGLISH_BRAILLE_NUM[char];
      isNumberMode = false; // The number mode will reset on encountering special character
    }
  }
  return brailleOutput;
}

// Function to translate from Braille to English
function translateToEnglish(input) {
  let englishOutput = '';
  let i = 0;
  let isNumberMode = false;
  let isCapitalMode = false;

  while (i < input.length) {
    let symbol = input.substring(i, i + 6);

    if (symbol === ENGLISH_BRAILLE_CHAR['capital']) {
      isCapitalMode = true;
      i += 6;
      continue;
    } else if (symbol === ENGLISH_BRAILLE_NUM['number']) {
      isNumberMode = true;
      i += 6;
      continue;
    } else if (symbol === ENGLISH_BRAILLE_NUM['space']) {
      englishOutput += ' ';
      isNumberMode = false; // The number mode will reset on encountering space symbol
      isCapitalMode = false; // The capital mode will reset on encountering space symbol
    } else {
      let char = '';
      if (isNumberMode && BRAILLE_ENGLISH_NUM[symbol]) {
        char = BRAILLE_ENGLISH_NUM[symbol];
      } else if (BRAILLE_ENGLISH_CHAR[symbol]) {
        char = BRAILLE_ENGLISH_CHAR[symbol];
      } else if (BRAILLE_ENGLISH_NUM[symbol]) {
        char = BRAILLE_ENGLISH_NUM[symbol];
      }

      if (isCapitalMode) {
        char = char.toUpperCase();
        isCapitalMode = false; // This ensures capitalization is only for single character
      }
      englishOutput += char;
    }
    i += 6;
  }
  return englishOutput;
}

// Main function to determine the direction of translation - English to Braille or Braille to English
function translate(input) {
  if (isBraille(input)) {
    return translateToEnglish(input);
  } else {
    return translateToBraille(input);
  }
}

// Getting input from terminal and displaying the result
const inputText = process.argv.slice(2).join(" ");
const result = translate(inputText);
console.log(result);