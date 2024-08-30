// Adrian Milea
// Braille to English / English to Braille Translator

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

// Create the English to Braille map
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
    } else if (char === " ") {
      braille += brailleMap[" "];
    } else {
      isNumber = false;
      braille += brailleMap[char.toLowerCase()] || "......"; // !!!Handle unexpected characters
    }
  }

  return braille;
}

// Translate Braille to English Function
function translateToEnglish(braille) {
  let english = "";
  let isCapital = false;
  let isNumber = false;

  for (let i = 0; i < braille.length; i += 6) {
    let symbol = braille.slice(i, i + 6);

    if (symbol === brailleMap["capital"]) {
      isCapital = true;
      continue;
    } else if (symbol === brailleMap["number"]) {
      isNumber = true;
      continue;
    }

    let char = englishMap[symbol];

    if (isCapital) {
      char = char.toUpperCase();
      isCapital = false;
    }

    if (isNumber && char && /[a-z]/.test(char)) {
      char = Object.keys(brailleMap).find(
        (key) => brailleMap[key] === symbol && /\d/.test(key)
      );
    }

    english += char || "?"; // !!!Handle unknown Braille symbols
  }

  return english;
}

// The MAIN FUNCTION for detecting the input type
function main(input) {
  let result;
  if (isBraille(input)) {
    result = translateToEnglish(input);
  } else {
    result = translateToBraille(input);
  }
  console.log(result);
}

// Accept the command-line argument and call the MAIN FUNCTION
const input = process.argv.slice(2).join(" "); // !!!Join arguments with spaces
if (input) {
  main(input);
} else {
  console.log("No input provided");
}

// End of script
