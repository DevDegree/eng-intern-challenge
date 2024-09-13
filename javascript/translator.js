const TRANSLATION_MAP = {
  "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
  "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
  "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
  "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
  "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
  "z": "O..OOO", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
  "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...",
  "0": ".OOO..", "capital follows": ".....O", "decimal follows": ".O...O",
  "number follows": ".O.OOO", " ": "......"
};

// Reverse translation map for decoding
const REVERSE_TRANSLATION_MAP = Object.fromEntries(
  Object.entries(TRANSLATION_MAP).flatMap(([key, value]) => {
    if (/[0-9]/.test(key)) {
      return [[`num_${value}`, key]];  // Add number prefix for numbers
    } else {
      return [[`char_${value}`, key]]; // Add char prefix for letters
    }
  })
);

// Constants for special strings
const CAPITAL_FOLLOWS = TRANSLATION_MAP["capital follows"];
const NUMBER_FOLLOWS = TRANSLATION_MAP["number follows"];
const SPACE = TRANSLATION_MAP[" "];

// Helper function to split a string into chunks of size 6
function splitIntoChunks(string, size = 6) {
  const chunks = [];
  for (let i = 0; i < string.length; i += size) {
    chunks.push(string.substring(i, i + size));
  }
  return chunks;
}

function encodeString(string) {
  let output = "";
  let currentlyNumber = false;

  for (const char of string) {
    if (char === " ") {
      output += SPACE;
      currentlyNumber = false; // Reset number state
    } else if (/\d/.test(char)) { // Check if it's a number
      if (!currentlyNumber) {
        output += NUMBER_FOLLOWS;
        currentlyNumber = true;
      }
      output += TRANSLATION_MAP[char];
    } else if (char === char.toUpperCase()) { // Handle capital letters
      output += CAPITAL_FOLLOWS + TRANSLATION_MAP[char.toLowerCase()];
    } else {
      output += TRANSLATION_MAP[char]; // Handle lowercase letters
    }
  }

  return output;
}

function decodeString(string) {
  const splitString = splitIntoChunks(string);
  let output = '';
  let capitalNextLetter = false;
  let currentlyNumber = false;

  for (const char of splitString) {
    if (char === CAPITAL_FOLLOWS) {
      capitalNextLetter = true;
    } else if (char === NUMBER_FOLLOWS) {
      currentlyNumber = true; // Sets sumber state
    } else if (char === SPACE) {
      output += ' ';
      currentlyNumber = false; // Reset number state
    } else if (capitalNextLetter) {
      output += REVERSE_TRANSLATION_MAP[`char_${char}`].toUpperCase();
      capitalNextLetter = false;
    } else if (currentlyNumber) {
      output += REVERSE_TRANSLATION_MAP[`num_${char}`];
    } else {
      output += REVERSE_TRANSLATION_MAP[`char_${char}`];
    }
  }

  return output;
}

function translate(input) {
  const isEncoded = /^[O. ]*$/.test(input);
  return isEncoded ? decodeString(input) : encodeString(input);
}

// Capture commandline arguments
const args = process.argv.slice(2).join(" ");
console.log(translate(args));