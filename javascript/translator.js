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

const brailleToEnglishMap = Object.entries(brailleMap).reduce(
  (acc, [key, value]) => {
    acc[value] = key;
    return acc;
  },
  {}
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
      char = char.toLowerCase(); // Convert to lowercase for mapping
    }

    if (/[0-9]/.test(char) && !isNumberMode) {
      output += numberPrefix; // Enter number mode
      isNumberMode = true; // Set number mode flag
    }

    if (char === " " && isNumberMode) {
      isNumberMode = false; // Exit number mode on space
    }

    output += brailleMap[char] || ""; // Convert character to Braille
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
      i -= 6; // Move back to account for prefix
      continue;
    }

    if (symbol === numberPrefix) {
      isNumber = true;
      i -= 6; // Move back to account for prefix
      continue;
    }

    let translatedChar = brailleToEnglishMap[symbol] || "";
    if (isCapital) {
      translatedChar = translatedChar.toUpperCase();
      isCapital = false; // Reset capital flag
    }

    if (isNumber) {
      // Translate number mode to number, 'a' to '1', 'b' to '2', etc.
      translatedChar = (
        translatedChar.charCodeAt(0) -
        "a".charCodeAt(0) +
        1
      ).toString();
      if (translatedChar === "10") translatedChar = "0"; // Special case for '0'
    }

    if (translatedChar === " ") {
      isNumber = false; // Reset number mode on space
    }

    output += translatedChar;
  }

  return output;
}

// Parse input arguments
const input = process.argv.slice(2).join(" ").trim();

if (isBraille(input)) {
  console.log(translateToEnglish(input));
} else {
  console.log(translateToBraille(input));
}
