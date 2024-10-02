// Braille dictionaries
// For upper case letters
const brailleUpperAlpha = {
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

// For lower case letters
const brailleAlpha = {
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

// For numbers
const brailleNumbers = {
  1: "O.....", // same as a
  2: "O.O...", // same as b
  3: "OO....", // same as c
  4: "OO.O..", // same as d
  5: "O..O..", // same as e
  6: "OOO...", // same as f
  7: "OOOO..", // same as g
  8: "O.OO..", // same as h
  9: ".OO...", // same as i
  0: ".OOO..", // same as j
};

// For Punctuation marks - including space
const braillePunctuation = {
  ".": "..OO.O",
  ",": "..O...",
  "?": "..O.OO",
  "!": "..OOO.",
  ":": "..OO..",
  ";": "..O.O.",
  "-": "....OO",
  "/": ".O..O.",
  "<": ".OO..O",
  ">": "O..OO.", // same as letter O
  "(": "O.O..O",
  ")": ".O.OO.",
  " ": "......", // space
};

// Instructional indicators
const capFollows = ".....O";
const decimalFollows = ".O...O";
const numberFollows = ".O.OOO";

// Translate English to Braille
function translateToBraille(text) {
  const result = [];
  let prevChar = "";

  for (let char of text) {
    let brailleChar = "";

    // Check if the character is an uppercase letter
    if (char === char.toUpperCase() && /[A-Z]/.test(char)) {
      brailleChar += capFollows; 
      brailleChar += brailleUpperAlpha[char] || "?";
    }
    // Convert lower case
    else if (/[a-z]/.test(char)) {
      brailleChar += brailleAlpha[char] || "?";
    }
    // Convert number & add indicator
    else if (/[0-9]/.test(char)) {
      brailleChar += numberFollows; 
      brailleChar += brailleNumbers[char] || "?";
    }
    // Convert decimal & add indicator
    else if (char === ".") {
      if (prevChar.match(/[0-9]/)) {
        brailleChar += decimalFollows; 
      } else {
        brailleChar += braillePunctuation["."]; // Add punctuation
      }
    }
    // Convert Punctuation
    else if (braillePunctuation[char]) {
      brailleChar += braillePunctuation[char];
    }
    // Placeholder for unknown character
    else {
      brailleChar += "?";
    }
    result.push(brailleChar);
    prevChar = char; // Update previous character
  }
  return result.join("");
}

// Translate Braille to English
function translateToEnglish(text) {
  const result = [];
  const brailleChars = text.match(/.{1,6}/g); // Split into 6-character segments

  let isCapital = false;
  let isNumberContext = false;

  for (let i = 0; i < brailleChars.length; i++) {
    let brailleChar = brailleChars[i];
    let englishChar = "";

    // Check for capitalization
    if (brailleChar === capFollows) {
      isCapital = true;
      continue; // skip the cap indicator
    } 
    
    // Check for number context
    if (brailleChar === numberFollows) {
      isNumberContext = true;
      continue; // Skip the number indicator
    }


    // Check for number 
    if (isNumberContext) {
      // reverse mapping
      for (let [key, value] of Object.entries(brailleNumbers)) {
        if (brailleChar === value) {
          englishChar = key; // Match the character with the braille
          break;
        }
      }
      // Placeholder for unknown character / non-existing characters
      if (!englishChar) {
        englishChar = "?";
      }
    } else {
      // Convert Uppercase letters 
      if (isCapital) {
        for (let [key, value] of Object.entries(brailleUpperAlpha)) {
          if (brailleChar === value) {
            englishChar = key; 
            break;
          }
        }
        isCapital = false; // Reset after processing the capital letter
      } 
      // Convert lowercase letter
      else {
        for (let [key, value] of Object.entries(brailleAlpha)) {
          if (brailleChar === value) {
            englishChar = key; 
            break;
          }
        }
      }

      // Check for punctuation
      if (!englishChar) {
        for (let [key, value] of Object.entries(braillePunctuation)) {
          if (brailleChar === value) {
            englishChar = key; 
            break;
          }
        }
      }
    }

    result.push(englishChar);
  }

  return result.join("").trim(); // Join all characters and trim whitespace
}

// Test
// Braille to English
// const engText = "Hello world";
// const brailleResult = translateToBraille(engText);
// console.log("Braille Result:", brailleResult);

// // English to Braille
// const brailleText = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO....";
// const englishResult = translateToEnglish(brailleText);
// console.log("English Result:", englishResult);
