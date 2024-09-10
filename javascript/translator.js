const process = require("process");

// Maps lowercase english alphabet to braille
const ENGLISH_TO_BRAILLE = {
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

// Maps numbers to braille
const NUMBER_TO_BRAILLE = {
  0: ".OOO..",
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

// Maps symbols to braille
const SYMBOL_TO_BRAILLE = {
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
};

// Other constants
const CAPITAL = ".....O";
const DECIMAL = ".O...O";
const NUMBER = ".O.OOO";
const SPACE = "......";

// Reverse mapping from Braille to English for characters, numbers, and symbols
const BRAILLE_TO_ENGLISH = Object.fromEntries(
  Object.entries(ENGLISH_TO_BRAILLE).map(([key, value]) => [value, key])
);
const BRAILLE_TO_NUMBER = Object.fromEntries(
  Object.entries(NUMBER_TO_BRAILLE).map(([key, value]) => [value, key])
);
const BRAILLE_TO_SYMBOL = Object.fromEntries(
  Object.entries(SYMBOL_TO_BRAILLE).map(([key, value]) => [value, key])
);

// Determines if the input string is Braille based on matching character patterns
function isBraille(input) {
  return /^[O.]+$/.test(input);
}

// Determine if english character is a number
function isCharNumber(char) {
  return /\d/.test(char);
}

// Determine if english character is upper case letter
function isCharCapital(char) {
  return /^[A-Z]$/.test(char);
}

// Determine if english character is lower case letter
function isCharLower(char) {
  return /^[a-z]$/.test(char);
}

// Accepts english input and outputs braille translation
function english_to_braille(input) {
  let output = "";
  let i = 0;

  while (i < input.length) {
    const char = input[i]; // Current character

    // If character is a number
    if (isCharNumber(char)) {
      output += NUMBER; // Add number follows braille symbol to output string
      // Add numbers as braille symboles until a non-number character or end of input is reached
      while (isCharNumber(input[i]) && i < input.length) {
        output += NUMBER_TO_BRAILLE[input[i]];
        i++;
      }
      continue; // Skip increment at the end of the loop as we already handle it here
    } else if (char === " ") {
      output += SPACE;
    }
    // Convert english symbol to braille if found in dictionary
    else if (SYMBOL_TO_BRAILLE[char]) {
      output += SYMBOL_TO_BRAILLE[char];
    }
    // Add capital follows symbol and convert english character to braille
    else if (isCharCapital(char)) {
      output += CAPITAL;
      output += ENGLISH_TO_BRAILLE[char.toLowerCase()];
    }
    // Convert english character to braille and add to output
    else if (isCharLower(char)) {
      output += ENGLISH_TO_BRAILLE[char];
    }
    // Display error if a character is unsupported
    else {
      console.log("Error: unsupported character detected." + { char });
    }
    i++;
  }
  return output;
}

// Accepts braille input and outputs english translation
function braille_to_english(input) {
  let output = "";
  let i = 0;

  while (i < input.length) {
    let currentChar = input.slice(i, i + 6); // One braille pattern is 6 characters long

    // If capital follows pattern detected
    if (currentChar === CAPITAL) {
      i += 6; // Move past the capital follows pattern
      if (i < input.length) {
        let nextChar = input.slice(i, i + 6); // Next character is the english character
        if (BRAILLE_TO_ENGLISH[nextChar]) {
          output += BRAILLE_TO_ENGLISH[nextChar].toUpperCase(); // Translate braille symbol to english character
        }
      }
    }
    // If number follows pattern detected
    else if (currentChar === NUMBER) {
      i += 6; // Move past number follows pattern

      // Translate numbers until space or end of input detected
      while (i < input.length && input.slice(i, i + 6) !== SPACE) {
        let number = input.slice(i, i + 6);
        if (BRAILLE_TO_NUMBER[number]) {
          output += BRAILLE_TO_NUMBER[number];
          i += 6;
        } else if (number === DECIMAL) {
          output += ".";
          i += 6;
        } else {
          break;
        }
      }
    } else if (currentChar === SPACE) {
      output += " ";
    } else if (BRAILLE_TO_ENGLISH[currentChar]) {
      output += BRAILLE_TO_ENGLISH[currentChar]; // Translate braille to english character
    } else if (BRAILLE_TO_SYMBOL[currentChar]) {
      output += BRAILLE_TO_SYMBOL[currentChar]; // Translate braille to english symbol
    } else {
      return "Error: unsupported character detected." + { currentChar };
    }
    i += 6;
  }
  return output;
}

// Main function to execute program
function main() {
  // [0] is 'node', [1] is 'translator.js', so real input start from index 2
  const args = process.argv.slice(2); // Slices off the first two arguments
  const input = args.join(" "); // Joins all arguments into a single string for processing

  let output = "";

  // Determine if the input is in Braille or English and process accordingly
  if (isBraille(input) && input.length % 6 === 0) {
    output = braille_to_english(input);
  } else if (isBraille(input)) {
    output = "Braille patterns should be multiples of 6 long.";
  } else {
    output = english_to_braille(input);
  }

  console.log(output); // Display the translated output or error in the terminal
}

main();
