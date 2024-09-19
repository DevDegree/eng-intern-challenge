const lowercaseToBraille = {
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
  "?": "..O.OO",
  ";": "..O.O.",
  ":": "..OO..",
  "!": "..OOO.",
  "-": "....OO",
  "<": ".OO..O",
  ">": "O..OO.",
  "(": "O.O..O",
  ")": ".O.OO.",
  "'": "..O...",
  " ": "......",
};

const uppercaseToBraille = {
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
};

const numbersToBraille = {
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

const IndicatorsToBraille = {
  capitalFollows: ".....O",
  decimalFollows: ".O...O",
  numberFollows: ".O.OOO",
};

const brailleToLowercase = Object.fromEntries(
  Object.entries(lowercaseToBraille).map(([key, value]) => [value, key])
);

const brailleToUppercase = Object.fromEntries(
  Object.entries(uppercaseToBraille).map(([key, value]) => [value, key])
);

const brailleToNumbers = Object.fromEntries(
  Object.entries(numbersToBraille).map(([key, value]) => [value, key])
);

const inputString = process.argv.slice(2).join(" ");
findLanguage(inputString);

function findLanguage(inputString) {
  const braillePattern = /^[O.]+$/;
  if (braillePattern.test(inputString) && inputString.length % 6 === 0) {
    return translateBraille(inputString);
  } else {
    return translateEnglish(inputString);
  }
}

function translateBraille(brailleString) {
  let englishString = "";
  for (let i = 0; i < brailleString.length; i += 6) {
    let brailleChar = brailleString.slice(i, i + 6);
    if (brailleChar === IndicatorsToBraille.capitalFollows) {
      i += 6;
      brailleChar = brailleString.slice(i, i + 6);
      englishString += brailleToUppercase[brailleChar];
    } else if (brailleChar == IndicatorsToBraille.numberFollows) {
      while (i < brailleString.length) {
        i += 6;
        brailleChar = brailleString.slice(i, i + 6);
        if (
          brailleChar === brailleToLowercase[brailleToLowercase.length - 1] ||
          i + 6 > brailleString.length
        ) {
          break;
        } else if (brailleChar === "..OO.O") {
          englishString += brailleToLowercase[brailleChar];
          break;
        }
        englishString += brailleToNumbers[brailleChar];
      }
    } else {
      englishString += brailleToLowercase[brailleChar];
    }
  }
  console.log(englishString);
  return englishString;
}

function translateEnglish(englishString) {
  let brailleString = "";
  let i = 0;
  while (i < englishString.length) {
    let char = englishString[i];
    if (char >= "A" && char <= "Z") {
      brailleString +=
        IndicatorsToBraille.capitalFollows + uppercaseToBraille[char];
      i++;
    } else if (char >= "0" && char <= "9") {
      brailleString += IndicatorsToBraille.numberFollows;
      while (
        i < englishString.length &&
        englishString[i] >= "0" &&
        englishString[i] <= "9"
      ) {
        brailleString += numbersToBraille[englishString[i]];
        i++;
      }
    } else {
      brailleString += lowercaseToBraille[char];
      i++;
    }
  }
  console.log(brailleString);
  return brailleString;
}
