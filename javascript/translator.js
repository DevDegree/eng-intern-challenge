const brailleToEnglish = {
  "O.....": { letter: "a", number: 1 },
  "O.O...": { letter: "b", number: 2 },
  "OO....": { letter: "c", number: 3 },
  "OO.O..": { letter: "d", number: 4 },
  "O..O..": { letter: "e", number: 5 },
  "OOO...": { letter: "f", number: 6 },
  "OOOO..": { letter: "g", number: 7 },
  "O.OO..": { letter: "h", number: 8 },
  ".OO...": { letter: "i", number: 9 },
  ".OOO..": { letter: "j", number: 10 },
  "O...O.": { letter: "k" },
  "O.O.O.": { letter: "l" },
  "OO..O.": { letter: "m" },
  "OO.OO.": { letter: "n" },
  "O..OO.": { letter: "o", number: ">" },
  "OOO.O.": { letter: "p" },
  "OOOOO.": { letter: "q" },
  "O.OOO.": { letter: "r" },
  ".OO.O.": { letter: "s" },
  ".OOOO.": { letter: "t" },
  "O...OO": { letter: "u" },
  "O.O.OO": { letter: "v" },
  ".OOO.O": { letter: "w" },
  "OO..OO": { letter: "x" },
  "OO.OOO": { letter: "y" },
  "O..OOO": { letter: "z" },
  "..OO.O": { letter: "." },
  "..O.OO": { letter: "?" },
  "..OOO.": { letter: "!" },
  "..OO..": { letter: ":" },
  "..O.O.": { letter: ";" },
  "....OO": { letter: "-" },
  ".O..O.": { letter: "/" },
  ".OO..O": { letter: "<" },
  "O.O..O": { letter: "(" },
  ".O.OO.": { letter: ")" },
  "......": { letter: " " },
};

const englishToBraille = {
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
  ".": "..OO.O",
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

const capital = ".....O";
const number = ".O.OOO";
const decimal = ".O...O";
let isNumber = false;

const input = process.argv.slice(2).join(" ");
const isBraille = (str) => /^[O.]+$/.test(str);

function translateBrailleToEnglish(braille) {
  let englishText = "";
  let isNumber = false;
  let i = 0;

  while (i < braille.length) {
    let symbol = braille.slice(i, i + 6);

    if (symbol === capital) {
      i += 6;
      let nextSymbol = braille.slice(i, i + 6);
      englishText += brailleToEnglish[nextSymbol].letter.toUpperCase();
    } else if (symbol === number) {
      isNumber = true;
    } else if (symbol === "......") {
      isNumber = false;
      englishText += brailleToEnglish[symbol].letter;
    } else {
      if (isNumber) {
        englishText += brailleToEnglish[symbol].number;
      } else {
        englishText += brailleToEnglish[symbol].letter;
      }
    }
    i += 6;
  }
  return englishText;
}

function translateEnglishToBraille(english) {
  let brailleText = "";
  let i = 0;
  let numberMode = false;
  let length = english.length;

  while (i < length) {
    let text = english[i];

    if (text === text.toUpperCase() && text !== text.toLowerCase()) {
      brailleText += capital;
      text = text.toLowerCase();
      brailleText += englishToBraille[text];
    } else if (!isNaN(text) && text !== " ") {
      if (!numberMode) {
        brailleText += number;
        numberMode = true;
      }
      brailleText += englishToBraille[text];
    } else if (text === " ") {
      numberMode = false;
      brailleText += englishToBraille[text];
    } else {
      brailleText += englishToBraille[text];
    }
    i++;
  }
  return brailleText;
}

if (isBraille(input.toString)) {
  console.log(translateBrailleToEnglish(input));
} else {
  console.log(translateEnglishToBraille(input));
}
