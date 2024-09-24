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
  " ": "......",
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

const reverseBrailleMap = Object.fromEntries(
  Object.entries(brailleMap).map(([key, value]) => [value, key])
);
const capitalPrefix = ".....O";
const numberPrefix = ".O.OOO";

function isBraille(input) {
  return /^[O\.]+$/.test(input);
}

function translateToBraille(text) {
  let output = "";
  let isNumberMode = false;

  for (let char of text) {
    if (/[A-Z]/.test(char)) {
      output += capitalPrefix; // Add capital prefix
      char = char.toLowerCase();
    }

    if (/[0-9]/.test(char)) {
      if (!isNumberMode) {
        output += numberPrefix; // Enter number mode
        isNumberMode = true;
      }
      char = String.fromCharCode(char.charCodeAt(0) + 48); // Convert to Braille equivalent
    }

    if (char === " ") {
      isNumberMode = false; // Exit number mode on space
    }

    output += brailleMap[char] || "";
  }

  return output;
}

function translateToEnglish(braille) {
  let output = "";
  let isCapital = false;
  let isNumber = false;

  for (let i = 0; i < braille.length; i += 6) {
    const symbol = braille.slice(i, i + 6);

    if (symbol === capitalPrefix) {
      isCapital = true;
      continue;
    }

    if (symbol === numberPrefix) {
      isNumber = true;
      continue;
    }

    let char = reverseBrailleMap[symbol] || "";

    if (isCapital) {
      char = char.toUpperCase();
      isCapital = false; // Reset capital flag after one use
    }

    if (isNumber) {
      char = (char.charCodeAt(0) - 48).toString(); // Convert back from Braille number mode
      if (char === "10") char = "0"; // Special handling for 0
    }

    if (char === " ") isNumber = false; // Exit number mode on space

    output += char;
  }

  return output;
}

const input = process.argv.slice(2).join(" ").trim();
console.log(
  isBraille(input) ? translateToEnglish(input) : translateToBraille(input)
);
