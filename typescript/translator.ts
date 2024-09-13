// Mapping for Braille and English
const brailleToEnglishMap: { [key: string]: string } = {
  "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
  "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
  "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
  "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
  "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
  "O..OOO": "z", ".....O": " ", ".O.OOO": "cap", ".OOOOO": "num"
};

const englishToBrailleMap: { [key: string]: string } = {
  "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
  "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
  "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
  "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
  "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
  "z": "O..OOO", " ": ".....O"
};

const numbersToBraille: { [key: string]: string } = {
  "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
  "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
};

const brailleToNumbers: { [key: string]: string } = {
  "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
  "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
};

// Check if input is Braille or English
function isBraille(input: string): boolean {
  return /^[O.]+$/.test(input);
}

// Translate Braille to English
function brailleToEnglish(braille: string): string {
  const chunks = braille.match(/.{1,6}/g); // Split Braille into 6-character chunks
  let isCapitalized = false;
  let isNumber = false;
  let result = "";

  if (!chunks) return result;

  for (const chunk of chunks) {
    if (chunk === ".O.OOO") { // Capitalization marker
      isCapitalized = true;
      continue;
    }

    if (chunk === ".OOOOO") { // Number marker
      isNumber = true;
      continue;
    }

    let char = isNumber ? brailleToNumbers[chunk] : brailleToEnglishMap[chunk];

    if (!char) {
      char = "?"; // Unrecognized Braille pattern
    }

    if (char === " ") {
      result += " "; // Add space
    } else {
      result += isCapitalized ? char.toUpperCase() : char;
      isCapitalized = false; // Reset capitalization after use
    }

    isNumber = false; // Reset number mode after each character
  }

  return result;
}

// Translate English to Braille
function englishToBraille(english: string): string {
  let result = "";
  let isNumberMode = false;

  for (const char of english) {
    if (/[A-Z]/.test(char)) {
      result += ".O.OOO"; // Capitalization marker
      result += englishToBrailleMap[char.toLowerCase()];
    } else if (/[0-9]/.test(char)) {
      if (!isNumberMode) {
        result += ".OOOOO"; // Number marker
        isNumberMode = true;
      }
      result += numbersToBraille[char];
    } else if (char === " ") {
      result += ".....O"; // Space in Braille
      isNumberMode = false; // Reset number mode after space
    } else {
      result += englishToBrailleMap[char];
      isNumberMode = false; // Reset number mode after a non-number character
    }
  }

  return result;
}

// Main function
function main() {
  const input = process.argv[2]; // Read input argument from command line

  if (!input) {
    console.error("No input provided.");
    return;
  }

  const result = isBraille(input) ? brailleToEnglish(input) : englishToBraille(input);
  console.log(result);
}

main();
