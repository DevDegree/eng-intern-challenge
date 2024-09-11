const ENGLISH_LETTERS_SYMBOLS = {
  A: "O.....",
  B: "O.O...",
  C: "OO....",
  D: "OO.O..",
  E: "O..O..",
  F: "OOO...",
  G: "OOOO..",
  H: "O.OO..",
  I: ".OO...",
  J: ".OOO..",
  K: "O...O.",
  L: "O.O.O.",
  M: "OO..O.",
  N: "OO.OO.",
  O: "O..OO.",
  P: "OOO.O.",
  Q: "OOOOO.",
  R: "O.OOO.",
  S: ".OO.O.",
  T: ".OOOO.",
  U: "O...OO",
  V: "O.O.OO",
  W: ".OOO.O",
  X: "OO..OO",
  Y: "OO.OOO",
  Z: "O..OOO",
  ".": "..OO.O",
  ",": "..O...",
  "?": "..O.OO",
  "!": "..OOO.",
  ":": "..OO..",
  ";": "..O.O.",
  "-": "....OO",
  "/": ".O..O.",
  "<": ".OO..O",
  ">": "O..OO.",
  "(": "O.O..O",
  ")": ".O.OO.",
  " ": "......",
};

const ENGLISH_NUMBERS = {
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
};

const BRAILLE_LETTERS_SYMBOLS = {
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
  "..OO.O": ".",
  "..O...": ",",
  "..O.OO": "?",
  "..OOO.": "!",
  "..OO..": ":",
  "..O.O.": ";",
  "....OO": "-",
  ".O..O.": "/",
  ".OO..O": "<",
  "O..OO.": ">",
  "O.O..O": "(",
  ".O.OO.": ")",
  "......": " ",
};

const BRAILLE_NUMBERS = {
  "O.....": 1,
  "O.O...": 2,
  "OO....": 3,
  "OO.O..": 4,
  "O..O..": 5,
  "OOO...": 6,
  "OOOO..": 7,
  "O.OO..": 8,
  ".OO...": 9,
  ".OOO..": 0,
};

const CAP = ".....O";
const DEC = ".O...O";
const NUM = ".O.OOO";
const SPACE = "......";

const words = process.argv.slice(2);

const string = words.join(" ");

let convertedString = "";

if (isBraille()) {
  convertToEnglish();
} else {
  convertToBraille();
}

console.log(convertedString);

// -----------FUNCTIONS-----------
function convertToBraille() {
  let numFlag = false;

  string.split("").forEach((char) => {
    if (/^\d$/.test(char)) {
      if (!numFlag) {
        numFlag = true;
        convertedString += NUM;
      }
      convertedString += ENGLISH_NUMBERS[Number(char)];
      return;
    }
    if (char === " ") {
      numFlag = false;
      convertedString += ENGLISH_LETTERS_SYMBOLS[char];
      return;
    }
    if (char === ".") {
      convertedString += DEC;
      convertedString += ENGLISH_LETTERS_SYMBOLS[char];
      return;
    }
    if (char === char.toUpperCase() && char !== char.toLowerCase()) {
      convertedString += CAP;
    }
    convertedString += ENGLISH_LETTERS_SYMBOLS[char.toUpperCase()];
  });
}

function convertToEnglish() {
  const brailleCharacters = getBrailleCharacters();
  let capFlag = false;
  let numFlag = false;

  brailleCharacters.forEach((brailleCharacter) => {
    if (brailleCharacter == CAP) {
      capFlag = true;
      return;
    }
    if (brailleCharacter == NUM) {
      numFlag = true;
      return;
    }
    if (brailleCharacter == DEC) {
        return;
    }
    if (capFlag) {
      convertedString +=
        BRAILLE_LETTERS_SYMBOLS[brailleCharacter].toUpperCase();
      capFlag = false;
      return;
    }
    if (numFlag) {
      if (brailleCharacter == SPACE) {
        numFlag = false;
        convertedString += BRAILLE_LETTERS_SYMBOLS[brailleCharacter];
        return;
      }
      convertedString += BRAILLE_NUMBERS[brailleCharacter];
      return;
    }
    convertedString += BRAILLE_LETTERS_SYMBOLS[brailleCharacter];
  });
}

// -----------HELPERS-----------

function isBraille() {
  let isBraille = true;

  if (string.length % 6 !== 0) return false;

  for (let i = 0; i < string.length; i++) {
    if (string.charCodeAt(i) != 46 && string.charCodeAt(i) != 79) {
      return false;
    }
  }

  return isBraille;
}

function getBrailleCharacters() {
  let brailleCharacters = [];

  for (let i = 0; i < string.length - 5; i = i + 6) {
    const d = string.substring(i, i + 6);
    brailleCharacters.push(string.substring(i, i + 6));
  }

  return brailleCharacters;
}
