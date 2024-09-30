const arguments = process.argv.slice(2).join(" ");

const englishDictionary = {
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
  space: "......",
  follows: {
    capital: ".....O",
    number: ".O.OOO",
  },
};

const brailleDictionary = {
  alphabet: {
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
  },
  number: {
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
  },
};

function translator(input) {
  const isBraille = /^[O.]+$/.test(input);
  let result = "";

  if (isBraille) {
    const brailleChar = 6;
    let isNumber = false;
    let isCapital = false;
    for (let i = 0; i < input.length; i += brailleChar) {
      let subset = input.substring(i, i + brailleChar);
      if (subset === englishDictionary.follows.capital) {
        isCapital = true;
      } else if (subset === englishDictionary.space) {
        isNumber = false;
        result += " ";
      } else if (subset === englishDictionary.follows.number) {
        isNumber = true;
      } else if (isNumber) {
        result += brailleDictionary.number[subset];
      } else if (isCapital) {
        result += brailleDictionary.alphabet[subset].toUpperCase();
        isCapital = false;
      } else {
        result += brailleDictionary.alphabet[subset];
      }
    }
  } else {
    let numberFollowsAdded = false;
    for (let i = 0; i < input.length; i++) {
      const isUpperCase = /^[A-Z]*$/.test(input[i]);
      const isNumber = /^\d+$/.test(input[i]);
      const isSpace = input[i] === " ";
      if (isUpperCase) {
        result += englishDictionary.follows.capital;
        result += englishDictionary[input[i].toLowerCase()];
      } else if (isSpace) {
        result += englishDictionary.space;
        numberFollowsAdded = false;
      } else if (isNumber) {
        if (numberFollowsAdded === false) {
          result += englishDictionary.follows.number;
          numberFollowsAdded = true;
        }
        result += englishDictionary[input[i]];
      } else {
        result += englishDictionary[input[i]];
      }
    }
  }
  return result;
}

console.log(translator(arguments));
