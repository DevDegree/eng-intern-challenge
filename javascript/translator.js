const brailleLetters = {
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
};

const brailleDigits = {
  // Braille digits use the same patterns as letters a-j
  "O.....": "1",
  "O.O...": "2",
  "OO....": "3",
  "OO.O..": "4",
  "O..O..": "5",
  "OOO...": "6",
  "OOOO..": "7",
  "O.OO..": "8",
  ".OO...": "9",
  ".OOO..": "0",
};

const brailleSpecial = {
  ".....O": "+", // Capital sign
  "......": " ", // Space
  ".O.OOO": "~", // Number sign
};

const englishToBrailleLetters = {
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

const englishToBrailleDigits = {
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

const englishToBrailleSpecial = {
  "+": ".....O", // Capital sign
  " ": "......", // Space
  "~": ".O.OOO", // Number sign
};

// Function to detect the language of the input
function detectLanguage(input) {
  let isBraille = true;

  // Loop through each character in the input
  for (let i = 0; i < input.length; i++) {
    const char = input[i];
    // If a character is not "O", ".", it's not Braille
    if (char !== "O" && char !== ".") {
      isBraille = false;
      break;
    }
  }

  return isBraille ? "braille" : "english";
}

// Function to translate Braille to English
function brailleToEnglishTranslator(braille) {
  let result = "";
  let capital = false;
  let numberMode = false;

  for (let i = 0; i < braille.length; ) {
    // Handle spaces
    if (braille.slice(i, i + 6) === brailleSpecial[" "]) {
      result += " ";
      i += 6;
      numberMode = false;
      capital = false;
      continue;
    }

    let brailleChar = braille.slice(i, i + 6);
    i += 6;

    let englishChar = "";

    if (brailleChar === brailleSpecial["+"]) {
      capital = true;
      continue;
    }
    if (brailleChar === brailleSpecial["~"]) {
      numberMode = true;
      continue;
    }

    if (numberMode) {
      englishChar = brailleDigits[brailleChar];
      if (!englishChar) {
        // If not a digit, exit number mode
        numberMode = false;
        // Try interpreting as a letter
        englishChar = brailleLetters[brailleChar] || "";
      }
    } else {
      englishChar = brailleLetters[brailleChar] || "";
    }

    if (capital) {
      englishChar = englishChar.toUpperCase();
      capital = false;
    }

    result += englishChar;
  }

  return result;
}

// Function to translate English to Braille
function englishToBrailleTranslator(english) {
  let result = "";
  let numberMode = false;

  for (let i = 0; i < english.length; i++) {
    let ch = english[i];

    if (ch === " ") {
      result += englishToBrailleSpecial[" "];
      numberMode = false;
    } else if (ch >= "0" && ch <= "9") {
      if (!numberMode) {
        // Add number sign
        result += englishToBrailleSpecial["~"];
        numberMode = true;
      }
      const brailleChar = englishToBrailleDigits[ch];
      if (brailleChar) {
        result += brailleChar;
      }
    } else if (ch >= "A" && ch <= "Z") {
      // Exit number mode
      if (numberMode) {
        numberMode = false;
      }
      // Add capital sign
      result += englishToBrailleSpecial["+"];

      const brailleChar = englishToBrailleLetters[ch.toLowerCase()];
      if (brailleChar) {
        result += brailleChar;
      }
    } else if (ch >= "a" && ch <= "z") {
      if (numberMode) {
        numberMode = false;
      }
      const brailleChar = englishToBrailleLetters[ch];
      if (brailleChar) {
        result += brailleChar;
      }
    } else {
      // Other characters can be ignored or handled separately
      numberMode = false;
    }
  }

  return result;
}

// Main function
function translate(input) {
  const language = detectLanguage(input);
  if (language === "braille") {
    return brailleToEnglishTranslator(input);
  } else {
    return englishToBrailleTranslator(input);
  }
}

// Get input from command line arguments
const input = process.argv.slice(2).join(" ");
const result = translate(input);
console.log(result);
