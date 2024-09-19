const alphabet = {
  a: "O.....",
  b: "O.O...",
  c: "OO....",
  d: "OO.O..",
  e: "O..O..",
  f: "OOO...",
  g: "OOOO..",
  h: "O.OO..",
  i: ".OO...",
  j: ".OOO..",
  k: "O...O.",
  l: "O.O.O.",
  m: "OO..O.",
  n: "OO.OO.",
  o: "0..00.",
  p: "OOO.O.",
  q: "OOOOO.",
  r: "O.OOO.",
  s: ".OO.O.",
  t: ".OOOO.",
  u: "O...OO",
  v: "O.O.OO",
  w: ".OOO.O",
  x: "OO..OO",
  y: "OO.OOO",
  z: "O..OOO",
  " ": "......",
  capital: ".....O",
  number: ".O.OOO"
};
const numbers = {
  1: "O.....",
  2: "O.O...",
  3: "OO....",
  4: "OO.O..",
  5: "O..O..",
  6: "OOO...",
  7: "OOOO..",
  8: "O.OO..",
  9: ".OO...",
  0: ".OOO.."
};

// Checks if input is braille by seeing if it contains only O and .
function isBraille(string) {
  return /[O.]+$/.test(string) && string.length % 6 === 0;
}

function brailleTranslator(string) {
  let translated = "";

  // Braille input to English
  if (isBraille(string)) {
    // Build hashes with Braille as the keys
    const brailleAlphabet = Object.fromEntries(Object.entries(alphabet).map(a => a.reverse()));
    const brailleNumbers = Object.fromEntries(Object.entries(numbers).map(a => a.reverse()));

    // Split braille input into braille cells
    const characters = string.match(/[\s\S]{1,6}/g);

    let isCapital = false;
    let isNumber = false;

    // Loop through array of braille cells and translate using hashes
    for (let i = 0; i < characters.length; i++) {
      if (brailleAlphabet[characters[i]] === 'capital') {
        isCapital = true;
      } else if (brailleAlphabet[characters[i]] === 'number') {
        isNumber = true;
      } else {
        if (isCapital) {
          translated += brailleAlphabet[characters[i]].toUpperCase();
          isCapital = false;
        } else if (isNumber) {
          // Translate characters to numbers until space is reached, then set isNumber to false
          if (characters[i] !== brailleAlphabet[' ']) {
            translated += brailleNumbers[characters[i]];
          } else {
            translated += brailleAlphabet[characters[i]];
            isNumber = false;
          }
        } else {
          translated += brailleAlphabet[characters[i]];
        }
      }
    }
  // English input to braille
  } else {
    for (let i = 0; i < string.length; i++) {
      // If character is capital letter
      if (/[A-Z]/.test(string[i])) {
        translated += alphabet["capital"] + alphabet[string[i].toLowerCase()];
      // If character is number
      } else if (/[0-9]/.test(string[i])) {
        // If previous character was already a number don't include "number follows" braille
        if (/[0-9]/.test(string[i - 1])) {
          translated += numbers[string[i]];
        } else {
          translated += alphabet["number"] + numbers[string[i]];
        }
      } else {
        translated += alphabet[string[i]];
      }
    }
  }
  return translated;
}

// Grab and join input from command line
const input = process.argv.slice(2).join(' ');
const output = brailleTranslator(input);
console.log(output);