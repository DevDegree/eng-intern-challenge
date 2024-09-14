const englishToBraille = {
  a: "O.....",
  b: "O.O...",
  c: "OO....",
  d: "OO.O..",
  e: "O..O..",
  f: "OOO...",
  g: "OOOO..",
  h: "O.OO..",
  i: ".O.O..",
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

const whatFollows = {
  capitalFollows: ".....O",
  decimalFollows: ".O...O",
  numberFollows: ".O.OOO",
};

const symbolsToBraille = {
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

const brailleForEnglish = Object.fromEntries(
  Object.entries(englishToBraille).map(([key, value]) => [value, key])
);

const brailleForNumbers = Object.fromEntries(
  Object.entries(numbersToBraille).map(([key, value]) => [value, key])
);

const brailleForSymbols = Object.fromEntries(
  Object.entries(symbolsToBraille).map(([key, value]) => [value, key])
);

function translator(string) {
  const isBraille = string
    .split("")
    .every((char) => char === "O" || char === ".");

  let isNumber = false;
  let isCapital = false;

  let result = "";

  if (!isBraille) {
    for (let i = 0; i < string.length; i++) {
      if (string[i] === " ") {
        result += symbolsToBraille[string[i]];
        isNumber = false;
      } else if (string[i] >= "A" && string[i] <= "Z") {
        result += whatFollows["capitalFollows"];
        result += englishToBraille[string[i].toLowerCase()];
        isNumber = false;
      } else if (string[i] >= "a" && string[i] <= "z") {
        result += englishToBraille[string[i]];
        isNumber = false;
      } else if (string[i] >= "0" && string[i] <= "9") {
        if (!isNumber) {
          result += whatFollows["numberFollows"];
          isNumber = true;
        }
        result += numbersToBraille[string[i]];
      } else {
        result += symbolsToBraille[string[i]];
      }
    }
  } else {
    let brailleArray = [];
    for (let i = 0; i < string.length; i += 6) {
      brailleArray.push(string.slice(i, i + 6));
    }

    for (let i = 0; i < brailleArray.length; i++) {
      if (brailleArray[i] === symbolsToBraille[" "]) {
        result += " ";
        isNumber = false;
      } else if (brailleArray[i] === whatFollows["capitalFollows"]) {
        isCapital = true;
      } else if (brailleArray[i] === whatFollows["numberFollows"]) {
        isNumber = true;
      } else if (brailleForSymbols[brailleArray[i]]) {
        result += brailleForSymbols[brailleArray[i]];
      } else if (isNumber) {
        result += brailleForNumbers[brailleArray[i]];
        isNumber = false;
      } else if (isCapital) {
        result += brailleForEnglish[brailleArray[i]].toUpperCase();
        isCapital = false;
      } else {
        result += brailleForEnglish[brailleArray[i]];
      }
    }
  }

  return result;
}

console.log(translator("Abc 123 xYz"));
