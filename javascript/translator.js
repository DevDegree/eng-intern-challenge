// Map each english letter to braille
const ENGLISH_TO_BRAILLE = {
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
  capital: ".....O",
  number: ".O.OOO",
  " ": "......",
};

const BRAILLE_TO_ENGLISH = {
  "O.....": "a",
  "O.O...": "b",
  "OO....": "c",
  "OO.O..": "d",
  "O..O..": "e",
  "OOO...": "f",
  "OOOO..": "g",
  "O.OO..": "h",
  ".OO...": "i",
  ".OOO..": "j",
  "O...O.": "k",
  "O.O.O.": "l",
  "OO..O.": "m",
  "OO.OO.": "n",
  "O..OO.": "o",
  "OOO.O.": "p",
  "OOOOO.": "q",
  "O.OOO.": "r",
  ".OO.O.": "s",
  ".OOOO.": "t",
  "O...OO": "u",
  "O.O.OO": "v",
  ".OOO.O": "w",
  "OO..OO": "x",
  "OO.OOO": "y",
  "O..OOO": "z",
  ".....O": "capital",
  ".O.OOO": "number",
  "......": " ",
};

const BRAILLE_TO_NUM = {
  "O.....": "1",
  "O.O...": "2",
  "OO....": "3",
  "OO.O..": "4",
  "O..O..": "5",
  "OOO...": "6",
  "OOOO..": "7",
  "O.OO..": "8",
  ".OO...": "9",
  ".OOO..": "0",
};

function isBraille(input) {
  // In order to be braile, can only consist of . or 0
  for (let char of input) {
    if (char != "." && char != "O") {
      // Means its English letters
      return false;
    }
  }
  return true;
}

function handleEnglishToBraille(input) {
  let output = "";
  let numberFollows = false;
  for (let i = 0; i < input.length; i++) {
    const word = input[i];
    for (let char of word) {
      if (/[A-Z]/.test(char)) {
        output +=
          ENGLISH_TO_BRAILLE["capital"] +
          ENGLISH_TO_BRAILLE[char.toLowerCase()];
      } else if (/[0-9]/.test(char)) {
        // its a number
        if (!numberFollows) {
          // first number we see, so add the number brailled
          output += ENGLISH_TO_BRAILLE["number"];
          numberFollows = true;
        }
        output += ENGLISH_TO_BRAILLE[char];
      } else {
        // its a lower case letter
        output += ENGLISH_TO_BRAILLE[char];
      }
    }
    // end of a word, add a space if its not the last word
    if (i != input.length - 1) {
      output += ENGLISH_TO_BRAILLE[" "];
    }
  }
  return output;
}

function handleBrailleToEnglish(input) {
  // will be one long string, split up by 6 characters

  let capitalNextChar = false;
  let numberNextChars = false;
  let output = "";
  while (input.length > 0) {
    // each char is 6 characters
    const char = input.substr(0, 6);
    // update the input length
    input = input.substr(6);
    // Get the corresponding english letter the char is
    const englishChar = BRAILLE_TO_ENGLISH[char];
    // Check if its a capital or number follows
    if (englishChar == "capital") {
      // Only the next symbol should be capitalized
      capitalNextChar = true;
      continue;
    } else if (englishChar == "number") {
      numberNextChars = true;
      continue;
    }

    // English characters
    if (numberNextChars) {
      // Is a number
      output += BRAILLE_TO_NUM[char];
    } else {
      // Is an english char
      if (capitalNextChar) {
        // upper case of the char
        output += englishChar.toUpperCase();
        capitalNextChar = false;
      } else {
        // lower case
        output += englishChar;
      }
    }
  }
  return output;
}

function main() {
  // Read the input from the command line
  const input = process.argv.slice(2);

  // Check that input is valid, and at least 1 item in it
  if (input.length > 0) {
    // Check whether its english or braile
    if (isBraille(input[0])) {
      // Braille -> english
      console.log(handleBrailleToEnglish(input[0]));
    } else {
      // Is english string -> braille
      console.log(handleEnglishToBraille(input));
    }
  }
}

main();
