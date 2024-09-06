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

const givenString = process.argv.slice(2).join(" ");

let isEnglish = false;
let outputStr = "";

// To determine is the given string is English or Braille
for (ch of givenString) {
  if (!["O", "."].includes(ch)) {
    isEnglish = true;
    break;
  }
}

if (isEnglish) {
  //English to Braille
  let prevIsNum = false;

  for (ch of givenString) {
    if (ch.match(/[A-Z]/)) {
      outputStr += capFollows + brailleAlphabets[ch.toLowerCase()];
      prevIsNum = false;
    } else if (ch.match(/[a-z]/)) {
      outputStr += brailleAlphabets[ch];
      prevIsNum = false;
    } else if (ch.match(/[0-9]/)) {
      if (!prevIsNum) {
        outputStr += numFollows;
      }

      outputStr += brailleNumbers[ch];
      prevIsNum = true;
    } else if (ch.match(/[.,?!:;<>\/\(\)\- ]/)) {
      outputStr += brailleSymbols[ch];
      prevIsNum = false;
    }
  }
} else {
  //Braille to English
  let nextIsCap = false;
  let nextAllNums = false;

  for (let i = 0; i < givenString.length; i += 6) {
    let ch = givenString.slice(i, i + 6);

    if (ch === numFollows) {
      nextAllNums = true;
      nextIsCap = false;
    } else if (ch === capFollows) {
      nextIsCap = true;
    } else if (ch === "......") {
      nextAllNums = false;
      nextIsCap = false;
      outputStr += " ";
    } else {
      if (nextAllNums) {
        let key = Object.keys(brailleNumbers).find(
          (key) => brailleNumbers[key] === ch
        );

        outputStr += key;
      } else {
        let key = Object.keys(brailleAlphabets).find(
          (key) => brailleAlphabets[key] === ch
        );

        if (nextIsCap) {
          outputStr += key.toUpperCase();
        } else {
          outputStr += key;
        }

        nextIsCap = false;
      }
    }
  }
}

console.log(outputStr);
