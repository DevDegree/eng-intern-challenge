const BDictionary = {
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
  " ": "......",
  0: ".OOO..",
  1: "O.....",
  2: "O.O...",
  3: "OO....",
  4: "OO.O..",
  5: "O..O..",
  6: "OOO...",
  7: "OOOO..",
  8: "O.OO..",
  9: ".OO...",
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
};

const EDictionary = {
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
};

const NDictionary = {
  ".OOO..": "0",
  "O.....": "1",
  "O.O...": "2",
  "OO....": "3",
  "OO.O..": "4",
  "O..O..": "5",
  "OOO...": "6",
  "OOOO..": "7",
  "O.OO..": "8",
  ".OO...": "9",
};
const typeChecker = {
  capital: ".....O",
  decimal: ".O...O",
  number: ".O.OOO",
};

const translateToBraille = (str) => {
  let translatedString = "";
  let isNumber = false;

  for (let char of str) {
    if (char === " ") {
      isNumber = false;
      translatedString += BDictionary[char];
    } else if (char >= 0 && char <= 9) {
      if (!isNumber) {
        translatedString += typeChecker["number"];
        isNumber = true;
      }

      translatedString += BDictionary[char];
    } else if (char === char.toUpperCase()) {
      translatedString +=
        typeChecker["capital"] + BDictionary[char.toLowerCase()];
    } else {
      translatedString += BDictionary[char.toLowerCase()];
    }
  }

  return translatedString;
};

const translateToEnglish = (str) => {
  let translatedString = "";
  let isCapital = false;
  let isNumber = false;

  let chars = str.match(/.{1,6}/g);

  for (let char of chars) {
    if (char == "......") {
      isNumber = false;
      translatedString += " ";
    } else if (char === typeChecker["capital"]) {
      isCapital = true;
    } else if (char === typeChecker["number"]) {
      isNumber = true;
    } else if (EDictionary[char] || NDictionary[char]) {
      if (isNumber) {
        translatedString += NDictionary[char];
      } else if (isCapital) {
        translatedString += EDictionary[char].toUpperCase();
        isCapital = false;
      } else {
        translatedString += EDictionary[char];
      }
    }
  }
  return translatedString;
};

const translateInput = (inputString) => {
  if (/^[.O\s]+$/.test(inputString)) {
    console.log(translateToEnglish(inputString));
  } else {
    console.log(translateToBraille(inputString));
  }
};

const argument = process.argv.slice(2);
if (argument.length > 0) {
  const inputString = argument.join(" ");
  translateInput(inputString);
} else {
  console.log("Please provide a string to translate");
}
