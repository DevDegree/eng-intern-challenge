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
  Capital: ".....O",
  Decimal: ".O...O",
  Number: ".O.OOO",
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

const splitBraillesArr = [];
const translatedArr = [];

function translateToBraille(input) {
  if (input.includes("O") || input.includes(".")) {
    // If input is in Braille
    // Implement Braille to text translation
    // Split into 6-character strings and add to splitBrailleArr
    // Loop over the splitBrailleArr and find matching key in brailleMap
    // Push translated values into translatedArr
    // If the braille value is for "Number", enable number mode
    // If the braille value is for empty space, disable number mode
    // Translate based on the current mode (number or alphabet)
  } else {
    // If input is a string of alphabets
    // Implement text to Braille translation
    // Split string into Alphabet Array
    // Loop over Alphabet Array and find matching braille value in brailleMap
    // If character is a number, enable number mode
    // If character is an empty space, disable number mode
    // If character is an uppercase, push "Capital" symbol into Translation Array
  }
}
