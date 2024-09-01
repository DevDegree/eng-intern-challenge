// Braille mappings for English letters (a-z), numbers (0-9), capital letter indicator, and number indicator
const brailleAlphabet = {
  a: "O.....", b: "O.O...", c: "OO....", d: "OO.O..", e: "O..O..",
  f: "OOO...", g: "OOOO..", h: "O.OO..", i: ".OO...", j: ".OOO..",
  k: "O...O.", l: "O.O.O.", m: "OO..O.", n: "OO.OO.", o: "O..OO.",
  p: "OOO.O.", q: "OOOOO.", r: "O.OOO.", s: ".OO.O.", t: ".OOOO.",
  u: "O...OO", v: "O.O.OO", w: ".OOO.O", x: "OO..OO", y: "OO.OOO",
  z: "O..OOO",
  "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
  "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
  " ": "......",  // Braille for space
  "#": ".O.OOO",  // Braille indicator for numbers
  "^": ".....O"   // Braille indicator for capitalization
};

// Reverse mapping from Braille to English letters and numbers
const englishAlphabet = Object.fromEntries(Object.entries(brailleAlphabet).map(([key, value]) => [value, key]));

/**
 * Function to translate a given string to its Braille equivalent.
 * @param {string} input - The English text to be translated to Braille.
 * @returns {string} - The Braille translation of the input text.
 */
function translateToBraille(input) {
  let result = "";
  let isNumberMode = false;  // Flag to track if number mode is activated

  for (let i = 0; i < input.length; i++) {
    const char = input[i];

    // Check for capital letters
    if (char >= "A" && char <= "Z") {
      result += brailleAlphabet["^"];  // Add capitalization indicator
      result += brailleAlphabet[char.toLowerCase()];
    }
    // Check for numbers
    else if (char >= "0" && char <= "9") {
      if (!isNumberMode) {
        result += brailleAlphabet["#"];  // Add number indicator if not already in number mode
        isNumberMode = true;
      }
      result += brailleAlphabet[char];
    }
    // Reset number mode after space
    else if (char === " ") {
      result += brailleAlphabet[char];  // Add Braille for space
      isNumberMode = false;  // Reset number mode after a space
    }
    // For lowercase letters
    else {
      result += brailleAlphabet[char];
    }
  }

  return result;
}

/**
 * Function to translate a Braille string to its English equivalent.
 * @param {string} input - The Braille text to be translated to English.
 * @returns {string} - The English translation of the input Braille text.
 */
function translateToEnglish(input) {
  let result = "";
  let i = 0;
  let isNumberMode = false;  // Flag to track if number mode is activated

  while (i < input.length) {
    const brailleChar = input.slice(i, i + 6);  // Each Braille character is 6 symbols long

    // Check if it's a capitalization indicator
    if (brailleChar === brailleAlphabet["^"]) {
      const nextChar = input.slice(i + 6, i + 12);  // Look ahead to the next Braille character
      result += englishAlphabet[nextChar].toUpperCase();
      i += 12;  // Skip to the next character
    }
    // Check if it's a number indicator
    else if (brailleChar === brailleAlphabet["#"]) {
      isNumberMode = true;  // Activate number mode
      i += 6;  // Skip to the next character
    }
    // Check if it's a space
    else if (brailleChar === brailleAlphabet[" "]) {
      result += " ";  // Add space to the result
      i += 6;  // Skip to the next character
      isNumberMode = false;  // Reset number mode after a space
    }
    // For letters and numbers
    else {
      if (isNumberMode) {
        result += englishAlphabet[brailleChar];  // Append as a number
      } else {
        result += englishAlphabet[brailleChar];  // Append as a letter
      }
      i += 6;  // Move to the next Braille character
    }
  }

  return result;
}

/**
 * Main function to determine the type of input (English or Braille)
 * and translate it accordingly.
 * @param {string} input - The input string to be translated.
 * @returns {string} - The translated output.
 */
function brailleTranslator(input) {
  // Check if input is Braille (only contains 'O' and '.')
  if (/^[O.]+$/.test(input.replace(/\s/g, ""))) {
    // Input is Braille
    return translateToEnglish(input);
  } else {
    // Input is English
    return translateToBraille(input);
  }
}

// Example usage: Node.js command-line argument handling
if (require.main === module) {
  // Take input from command line arguments
  const input = process.argv.slice(2).join(" ");  // Combine all arguments into a single input string
  const result = brailleTranslator(input);  // Translate the input
  console.log(result);  // Output the result
}
