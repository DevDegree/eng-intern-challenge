// Braille <> English
const brailleAlpha = {
  // lowercase alphabets
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
  o: "O..OO.",
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
  1: "O.....",
  2: "O.O...",
  3: "OO....",
  4: "OO.O..",
  5: "O..O..",
  6: "OOO...",
  7: "OOOO..",
  8: "O.OO..",
  9: ".OO...",
  0: ".OOO..",
  ".": "..00.0",
  ",": "..0...",
  // Punctuation marks
  ".": "..00.0",
  ",": "..0...",
  "?": "..0.00",
  "!": "..000.",
  ":": "..00..",
  ";": "..0.0.",
  "-": "....00",
  "/": ".0..0.",
  "<": ".00..0",
  ">": "0..00.",
  "(": "0.0..0",
  ")": ".0.00.",
  " ": "......", // space
};

// Instructional symbols
const capFollows = ".....0";
const decimalFollows = ".0...0";
const numberFollows = ".0.000";

// English <> Braille
// const englishAlpha =

// Main section

// Translate English to Braille
function translateToBraille(text) {
  let resultBraille = "";
  let isNumber = false; // prepare for number translation

  for (let index = 0; index < text.length; index++) {
    const char = text[index];

    // Check if the character is an uppercase letter
    if (/[A-Z]/.test(char)) {
      // add the cap follows indicator to the result
      resultBraille += brailleAlpha[char.toLowerCase()];
      isNumber = false;
    }

    // Convert lowercase letters
    else if (/[a-z]/.test(char)) {
      // Handle lowercase letters
      braille += brailleAlpha[char];
      isNumber = false;
    }

    // Check if the charater is a number
    else if (/\d/.test(char)) {
      if (isNumber === false) {
        // add the indicator
        resultBraille += numberFollows;
        isNumber = true;
      }
      resultBraille += brailleAlpha[char];
    }

    // Convert decimals - differentiate from period
    else if (char === ".") {
      const prevChar = text[index - 1];
      const nextChar = text[index + 1];

      // decimal point appears between two digits
      if (/\d/.test(prevChar) && /\d/.test(nextChar)) {
        resultBraille += decimalFollows; // add indicator
      } else {
        // period (punctuation mark)
        resultBraille += brailleAlpha[char];
      }
      isNumber = false;
    } 
    
    // Convert other characters in the alphabet
    else if (brailleAlpha[char]) {
      // Handle punctuation marks and other characters
      resultBraille += brailleAlpha[char]; 
      isNumber = false; 
    }

    // Other unexpected characters
    else {
console.error(`Unexpected character: '${char}'`);
isNumber = false;
    }
    return resultBraille;
}
}

