// Braille codes for alpha
const BRAILLE_ALPHA = {
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
};

const BRAILLE_SPACE = "......";
const BRAILLE_NUMBER_FOLLOW = ".O.OOO";
const BRAILLE_CAPITAL_FOLLOW = ".....O";
// Unicode value of letter a
const CHARCODE = "a".charCodeAt(0);

function translateBrailleToEng(brailleString) {
  if (brailleString.length % 6 != 0) {
    console.log("Invalid braille string.");
    return "";
  }
  let result = "";
  let isCapitalized = false;
  let isNumberSeries = false;
  // Process Braille code in a group of 6 characters
  for (let i = 0; i < brailleString.length; i += 6) {
    let symbol = brailleString.substring(i, i + 6);
    if (symbol == BRAILLE_SPACE) {
      result += " ";
      isCapitalized = isNumberSeries = false;
    } else if (symbol == BRAILLE_NUMBER_FOLLOW) {
      // Initialize a flag for next symbols to be translated to digits
      isNumberSeries = true;
    } else if (symbol == BRAILLE_CAPITAL_FOLLOW) {
      // Initialize a flag for next symbol to be capitalized
      isCapitalized = true;
    } else if (isNumberSeries) {
      let alpha = BRAILLE_ALPHA[symbol];
      // Braille number has the same symbol as from a-j, so get the character based on the matched symbol
      // Adding mod 10 so number 0 is wrapped around at the end
      result += (alpha.charCodeAt(0) - CHARCODE + 1) % 10;
    } else {
      let alpha;
      alpha = BRAILLE_ALPHA[symbol];
      if (isCapitalized) {
        result += alpha.toUpperCase();
        isCapitalized = false;
      } else {
        result += alpha;
      }
    }
  }
  return result;
}

function translateEngToBraille(engString) {
  let result = "";
  let isNumberSeries = false;
  for (let i = 0; i < engString.length; i += 1) {
    let c = engString.charAt(i);
    if (c == " ") {
      result += BRAILLE_SPACE;
      // End the number series if it was started before
      isNumberSeries = false;
      continue;
    }
    if (c >= "0" && c <= "9") {
      if (!isNumberSeries) {
        result += BRAILLE_NUMBER_FOLLOW;
      }
      let digit = parseInt(c);
      // Similar to before, since number has the same braille code as from a-j, we use the same code of letter for the number respectively
      // For example, "2" has the same code as "b"
      // To match "2" and "b", add an amount of 2 to the first letter of alpha "a"
      result +=
        BRAILLE_ALPHA[
          digit == 0
            ? String.fromCharCode(digit + CHARCODE + 9)
            : String.fromCharCode(digit + CHARCODE - 1)
        ];
      isNumberSeries = true;
    } else {
      // If the letter is uppercase
      if (c >= "A" && c <= "Z") {
        result += BRAILLE_CAPITAL_FOLLOW;
      }
      result += BRAILLE_ALPHA[c.toLowerCase()];
    }
  }
  return result;
}

function isBrailleCode(input) {
  // If the string is braille, all the characters are either O or .
  let count = 0;
  let length = input.length;
  for (let i = 0; i < length; i++) {
    if (input.charAt(i) == "O" || input.charAt(i) == ".") {
      count += 1;
    }
  }
  return count == length;
}

let args = process.argv;
// String input starts from the second argument
let input = process.argv.slice(2).join(" ");
let result = "";
if (isBrailleCode(input)) {
  result += translateBrailleToEng(input);
} else {
  result += translateEngToBraille(input);
}
console.log(result);
