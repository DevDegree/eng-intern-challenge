// Mappings between English characters and their Braille representations

const brailleMap = {
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
  capital: ".....O",
  number: ".O.OOO",
  " ": "......",
  0: ".OOOO.",
  1: "O.....",
  2: "O.O...",
  3: "OO....",
  4: "OO.O..",
  5: "O..O..",
  6: "OOO...",
  7: "OOOO..",
  8: "O.OO..",
  9: ".OO...",
};

const englishMap = Object.fromEntries(
  Object.entries(brailleMap).map(([k, v]) => [v, k])
);

// The function for detecting whether the input string is in Braille or English
function isBraille(input) {
  return /^[O.]+$/.test(input);
}

// Translate English to Braille Function
function translateToBraille(text) {
  let braille = "";
  let isNumber = false;

  for (let char of text) {
    if (/[A-Z]/.test(char)) {
      braille += brailleMap["capital"] + brailleMap[char.toLowerCase()];
    } else if (/[0-9]/.test(char)) {
      if (!isNumber) {
        braille += brailleMap["number"];
        isNumber = true;
      }
      braille += brailleMap[char];
    } else {
      isNumber = false;
      braille += brailleMap[char];
    }
  }

  return braille;
}
