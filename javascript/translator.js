const BRAILLE_CAPITAL_INDICATOR = ".....O";
const BRAILLE_NUMBER_INDICATOR = ".O.OOO";
const BRAILLE_DECIMAL_FOLLOWS = ".O...O";
const SPACE_BRAILLE = "......";

const eng_to_braille_map = {
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
  ".": "..OO.O",
  ",": "..O...",
  "?": "..O.OO",
  "!": "..OOO.",
  ":": "..OO..",
  ";": "..O.O.",
  "-": "....OO",
  "/": ".O..O.",
  "<": ".OO..O",
  ">": "O..OO.O",
  "(": "O.O..O",
  ")": ".O.OO.",
  " ": SPACE_BRAILLE,
};

const num_to_braille_map = {
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

const braille_to_eng_map = {
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
  "O..OO.O": ">",
  "O.O..O": "(",
  ".O.OO.": ")",
  "......": " ",
};

const braille_to_num_map = {
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

function convertToBraille(text) {
  const brailleOutput = [];
  let isNumber = false;

  for (const char of text) {
    if (char === " ") {
      brailleOutput.push(SPACE_BRAILLE);
      isNumber = false;
    } else if (/\d/.test(char)) {
      if (!isNumber) {
        brailleOutput.push(BRAILLE_NUMBER_INDICATOR);
        isNumber = true;
      }
      brailleOutput.push(num_to_braille_map[char]);
    } else if (char === ".") {
      brailleOutput.push(BRAILLE_DECIMAL_FOLLOWS);
      isNumber = false;
    } else if (
      char.toUpperCase() === char &&
      char.toLowerCase() in eng_to_braille_map
    ) {
      brailleOutput.push(BRAILLE_CAPITAL_INDICATOR);
      brailleOutput.push(eng_to_braille_map[char.toLowerCase()]);
      isNumber = false;
    } else {
      brailleOutput.push(
        eng_to_braille_map[char.toLowerCase()] || SPACE_BRAILLE
      );
      isNumber = false;
    }
  }

  return brailleOutput.join("");
}

function convertToEnglish(braille) {
  const englishOutput = [];
  let isNumber = false;
  let isCapital = false;

  const brailleChars = braille.match(/.{6}/g) || [];

  for (const char of brailleChars) {
    if (char === BRAILLE_NUMBER_INDICATOR) {
      isNumber = true;
    } else if (char === BRAILLE_CAPITAL_INDICATOR) {
      isCapital = true;
    } else if (char === BRAILLE_DECIMAL_FOLLOWS) {
      englishOutput.push(".");
      isNumber = false;
    } else if (char === SPACE_BRAILLE) {
      englishOutput.push(" ");
      isNumber = false;
      isCapital = false;
    } else {
      let newChar;
      if (isNumber) {
        newChar = braille_to_num_map[char] || "?";
      } else {
        newChar = braille_to_eng_map[char] || "?";
        if (isCapital) {
          newChar = newChar.toUpperCase();
          isCapital = false;
        }
      }
      englishOutput.push(newChar);
    }
  }

  return englishOutput.join("");
}

function main() {
  const args = process.argv.slice(2);
  if (args.length === 0) {
    console.log("Please enter a string to be converted!");
    process.exit(1);
  }

  const input = args.join(" ");
  const isBrailleInput = /^[.O]+$/.test(input);

  if (isBrailleInput) {
    console.log(convertToEnglish(input));
  } else {
    console.log(convertToBraille(input));
  }
}

if (require.main === module) {
  main();
}

module.exports = { main, convertToBraille, convertToEnglish };
