// Script to translate Braille to English and vice-versa

const capFollows = ".....O";
const numFollows = ".O.OOO";
const brailleAlphabets = {
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
const brailleNumbers = {
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
const brailleSymbols = {
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

const translateEnglishToBraille = (str) => {
  let output = "";
  let prevIsNum = false;

  for (const ch of str) {
    if (ch.match(/[A-Z]/)) {
      output += capFollows + brailleAlphabets[ch.toLowerCase()];
      prevIsNum = false;
    } else if (ch.match(/[a-z]/)) {
      output += brailleAlphabets[ch];
      prevIsNum = false;
    } else if (ch.match(/[0-9]/)) {
      if (!prevIsNum) {
        output += numFollows;
      }

      output += brailleNumbers[ch];
      prevIsNum = true;
    } else if (ch.match(/[.,?!:;<>\/\(\)\- ]/)) {
      output += brailleSymbols[ch];
      prevIsNum = false;
    }
  }

  return output;
};

const translateBrailleToEnglish = (str) => {
  let output = "";
  let nextIsCap = false;
  let nextAllNums = false;

  for (let i = 0; i < str.length; i += 6) {
    let ch = str.slice(i, i + 6);

    if (ch === numFollows) {
      nextAllNums = true;
      nextIsCap = false;
    } else if (ch === capFollows) {
      nextIsCap = true;
    } else if (ch === "......") {
      nextAllNums = false;
      nextIsCap = false;
      output += " ";
    } else {
      if (nextAllNums) {
        const key = Object.keys(brailleNumbers).find(
          (key) => brailleNumbers[key] === ch
        );
        output += key;
      } else {
        const key = Object.keys(brailleAlphabets).find(
          (key) => brailleAlphabets[key] === ch
        );

        if (nextIsCap) {
          output += key.toUpperCase();
        } else {
          output += key;
        }

        nextIsCap = false;
      }
    }
  }

  return output;
};

// To determine is the given string is English or Braille
let isEnglish = false;
const givenString = process.argv.slice(2).join(" ");

for (ch of givenString) {
  if (!["O", "."].includes(ch)) {
    isEnglish = true;
    break;
  }
}

const outputStr = isEnglish
  ? translateEnglishToBraille(givenString)
  : translateBrailleToEnglish(givenString);

console.log(outputStr);
