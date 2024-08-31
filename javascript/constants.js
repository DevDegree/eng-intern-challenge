const BRAILLE_SPACE = "......";
const BRAILLE_CAPITAL = ".....O";
const BRAILLE_NUMBER = ".O.OOO";
const BRAILLE_CHAR_LENGTH = 6;

const alphabetToBraille = {
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
  s: ".OO..O",
  t: ".OOOO.",
  u: "O...OO",
  v: "O.O.OO",
  w: ".OOO.O",
  x: "OO..OO",
  y: "OO.OOO",
  z: "O..OOO",
  // numbers:
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
  " ": BRAILLE_SPACE,
};

const brailleToAlphabet = {
  "O.....": {
    alphabet: "a",
    number: "1",
  },
  "O.O...": {
    alphabet: "b",
    number: "2",
  },
  "OO....": {
    alphabet: "c",
    number: "3",
  },
  "OO.O..": {
    alphabet: "d",
    number: "4",
  },
  "O..O..": {
    alphabet: "e",
    number: "5",
  },
  "OOO...": {
    alphabet: "f",
    number: "6",
  },
  "OOOO..": {
    alphabet: "g",
    number: "7",
  },
  "O.OO..": {
    alphabet: "h",
    number: "8",
  },
  ".OO...": {
    alphabet: "i",
    number: "9",
  },
  ".OOO..": {
    alphabet: "j",
    number: "0",
  },
  "O...O.": "k",
  "O.O.O.": "l",
  "OO..O.": "m",
  "OO.OO.": "n",
  "O..OO.": "o",
  "OOO.O.": "p",
  "OOOOO.": "q",
  "O.OOO.": "r",
  ".OO..O": "s",
  ".OOOO.": "t",
  "O...OO": "u",
  "O.O.OO": "v",
  ".OOO.O": "w",
  "OO..OO": "x",
  "OO.OOO": "y",
  "O..OOO": "z",
  "......": " ",
  // special instructions
  ".....O": "capitalize",
  ".O...O": "decimal",
  ".O.OOO": "number",
};

module.exports = {
  alphabetToBraille,
  brailleToAlphabet,
  BRAILLE_SPACE,
  BRAILLE_CAPITAL,
  BRAILLE_NUMBER,
  BRAILLE_CHAR_LENGTH,
};
