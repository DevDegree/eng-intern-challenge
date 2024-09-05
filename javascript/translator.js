// Please note that the account "TheBester14" is also mine such as written in my resume. I connected this account to facilitate the operations
// related to pushing the code and creating the PR

// Read command-line arguments
const inputArgs = process.argv.slice(2).join(" ");

// Mapping for English to Braille
const englishToBraille = {
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
  capitalizedFollows: ".....O",
  numberFollows: ".O.OOO",
  ".": "..OO.O",
  ",": "..O...",
  "?": "..O.OO",
  "!": "..OOO.",
  ":": "..OO..",
  ";": "..O.O.",
  "-": "....OO",
  "/": ".O..O.",
  "(": "O.O..O",
  ")": ".O.OO.",
  " ": "......",
};

// Reverse mapping for Braille to English
const brailleToEnglish = {};
for (let char in englishToBraille) {
  brailleToEnglish[englishToBraille[char]] = char;
}

function translateToBraille(text) {
  let brailleOutput = "";
  let isNumberMode = false; // To track if we are in number mode

  for (let i = 0; i < text.length; i++) {
    const char = text[i]; // We will analyse each char part by part

    // Check for uppercase letters and add capital follows symbol
    if (char === char.toUpperCase() && char !== char.toLowerCase()) {
      brailleOutput += englishToBraille["capitalizedFollows"];
    }

    // Check if character is a digit (0-9)
    if (/\d/.test(char)) {
      // Add "number follows" symbol before the first number
      if (!isNumberMode) {
        brailleOutput += englishToBraille["numberFollows"];
        isNumberMode = true;
      }
    } else {
      // If character is not a number, reset number mode
      isNumberMode = false;
    }

    brailleOutput += englishToBraille[char.toLowerCase()] || "......"; // Default to empty Braille if character is not found
  }
  return brailleOutput;
}

function translateToEnglish(braille) {
  let englishOutput = "";
  let isCapitalized = false;
  let isNumberMode = false; // To track if we are in number mode
  let i = 0;

  // Mapping of Braille letters to numbers when in number mode
  const brailleToNumber = {
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

  // Process each Braille as a set of 6 characters
  while (i < braille.length) {
    const brailleChar = braille.slice(i, i + 6);

    // Check for capitalized letters
    if (brailleChar === englishToBraille["capitalizedFollows"]) {
      isCapitalized = true;
      i += 6;
      continue;
    }

    // Check for number follows symbol
    if (brailleChar === englishToBraille["numberFollows"]) {
      isNumberMode = true;
      i += 6;
      continue;
    }

    let translatedChar;

    // If we are in number mode, use the number mapping
    if (isNumberMode) {
      if (brailleChar === "......") {
        // Reset number mode on space or non-number
        isNumberMode = false;
        translatedChar = " ";
      } else {
        translatedChar = brailleToNumber[brailleChar] || " ";
      }
    } else {
      translatedChar = brailleToEnglish[brailleChar] || " ";
      if (isCapitalized) {
        translatedChar = translatedChar.toUpperCase();
        isCapitalized = false; // Reset capitalization after one character
      }
    }

    englishOutput += translatedChar;
    i += 6;
  }
  return englishOutput;
}

// Function to translate text to Braille and vice versa
function main() {
  if (!inputArgs) {
    console.log("No input provided.");
    return;
  }

  // Translate the input from English to Braille
  const brailleResult = translateToBraille(inputArgs);
  console.log(brailleResult);
}

main(); // Call the main function to start the translation
