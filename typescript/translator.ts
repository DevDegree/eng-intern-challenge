const BRAILLE_TO_ENGLISH_MAP: { [key: string]: string } = {
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
  ".....O": "CAPITAL",
  ".O.OOO": "NUM",
  "......": " ",
};

const BRAILLE_TO_NUMBER_MAP: { [key: string]: string } = {
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

const ENGLISH_TO_BRAILLE_MAP: { [key: string]: string } = {
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
  "1": "O.....",
  "2": "O.O...",
  "3": "OO....",
  "4": "OO.O..",
  "5": "O..O..",
  "6": "OOO...",
  "7": "OOOO..",
  "8": "O.OO..",
  "9": ".OO...",
  "0": ".OOO..",
  CAPITAL: ".....O",
  NUM: ".O.OOO",
  " ": "......",
};

// check if the input only contains O or .
const isBraille = (input: string): boolean => {
  return /^[O.]+$/.test(input);
};

const translateBrailleToEnglish = (input: string): string => {
  let result = "";
  let isCapital = false;
  let isNumber = false;

  for (let i = 0; i < input.length; i += 6) {
    const brailleChar = input.substring(i, i + 6);
    let translatedChar;

    // check if it's a number
    if (isNumber) {
      translatedChar = BRAILLE_TO_NUMBER_MAP[brailleChar];
      if (!translatedChar) {
        isNumber = false; // switch out of number mode if it's not a number
        translatedChar = BRAILLE_TO_ENGLISH_MAP[brailleChar];
      }
    } else {
      translatedChar = BRAILLE_TO_ENGLISH_MAP[brailleChar];
    }

    if (translatedChar === "CAPITAL") {
      isCapital = true;
      continue;
    }

    if (translatedChar === "NUM") {
      isNumber = true;
      continue;
    }

    if (translatedChar) {
      if (isCapital && !isNumber) {
        result += translatedChar.toUpperCase();
        isCapital = false;
      } else {
        result += translatedChar;
      }
    }

    if (translatedChar === " ") {
      isNumber = false;
    }
  }

  return result;
};

const translateEnglishToBraille = (input: string): string => {
  let result = "";
  let isNumber = false;

  for (const char of input) {
    if (/[A-Z]/.test(char)) {
      // if it's a capital letter, add the capital letter indicator
      result += ENGLISH_TO_BRAILLE_MAP["CAPITAL"];
      result += ENGLISH_TO_BRAILLE_MAP[char.toLowerCase()];
      isNumber = false;
    } else if (/[0-9]/.test(char)) {
      // if it's a number, add the number indicator
      if (!isNumber) {
        result += ENGLISH_TO_BRAILLE_MAP["NUM"];
        isNumber = true;
      }
      result += ENGLISH_TO_BRAILLE_MAP[char];
    } else {
      result += ENGLISH_TO_BRAILLE_MAP[char];
      isNumber = false;
    }
  }

  return result;
};

// process input
const input = process.argv.slice(2).join(" ");

if (isBraille(input)) {
  console.log(translateBrailleToEnglish(input));
} else {
  console.log(translateEnglishToBraille(input));
}
