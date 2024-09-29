// Mapping of English letters, numbers, and special symbols to Braille
const brailleMapping = {
  // Letters (lowercase)
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
  // Numbers
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
  // Special symbols
  " ": "......", // Space
  "#": ".O.OOO", // Number indicator
  "^": ".....O", // Capitalization indicator
};

// Create a reverse mapping for Braille to English translation
const reverseBrailleMapping = {};
for (let char in brailleMapping) {
  reverseBrailleMapping[brailleMapping[char]] = char;
}

// Function to check if the input is Braille (i.e., made up of 'O' and '.')
function isBraille(input) {
  return /^[O\.]+$/.test(input.replace(/\s+/g, "")); // Ignores spaces while checking
}

// Function to translate English text to Braille
function englishToBraille(text) {
  let brailleOutput = "";
  let numberMode = false; // Flag to check if we are in number mode

  // Iterate through each character in the input text
  for (let char of text) {
    if (/\d/.test(char)) {
      // If character is a digit, switch to number mode
      if (!numberMode) {
        brailleOutput += brailleMapping["#"]; // Add number indicator in Braille
        numberMode = true;
      }
      brailleOutput += brailleMapping[char]; // Add Braille representation of the number
    } else {
      // If the number mode was on, reset it after a non-number character
      if (numberMode && char !== " ") {
        numberMode = false;
      }
      if (char === " ") {
        brailleOutput += brailleMapping[" "]; // Add space in Braille
        numberMode = false; // Reset number mode after a space
      } else {
        if (char === char.toUpperCase()) {
          brailleOutput += brailleMapping["^"]; // Add capitalization indicator in Braille
        }
        brailleOutput += brailleMapping[char.toLowerCase()]; // Convert lowercase letters to Braille
      }
    }
  }
  return brailleOutput; // Return the translated Braille string
}

// Function to translate Braille to English text
function brailleToEnglish(braille) {
  let englishOutput = "";
  let numberMode = false; // Flag to check if we are in number mode
  let capitalizeNext = false; // Flag to capitalize the next letter
  const brailleChars = braille.match(/.{1,6}/g); // Split Braille into chunks of 6 characters

  // Iterate through each Braille chunk (each chunk represents one symbol)
  for (let brailleChar of brailleChars) {
    if (brailleChar === brailleMapping["#"]) {
      numberMode = true; // Turn on number mode when encountering number indicator
    } else if (brailleChar === brailleMapping["^"]) {
      capitalizeNext = true; // Capitalize the next letter when encountering capitalization indicator
    } else if (brailleChar === brailleMapping[" "]) {
      englishOutput += " "; // Add a space
      numberMode = false; // Exit number mode after a space
    } else {
      let translatedChar = reverseBrailleMapping[brailleChar]; // Translate Braille chunk to corresponding English character
      if (numberMode) {
        // Convert letters 'a-j' to numbers '1-0' in number mode
        if (translatedChar >= "a" && translatedChar <= "j") {
          englishOutput += String.fromCharCode(
            translatedChar.charCodeAt(0) - "a".charCodeAt(0) + "1".charCodeAt(0)
          );
        }
        if (translatedChar === " ") {
          numberMode = false; // Exit number mode if space is encountered
        }
      } else {
        // Handle capitalization if needed
        if (capitalizeNext) {
          englishOutput += translatedChar.toUpperCase(); // Capitalize the next letter
          capitalizeNext = false;
        } else {
          englishOutput += translatedChar; // Add lowercase letter
        }
      }
    }
  }
  return englishOutput; // Return the translated English string
}

// Main translator function to determine whether the input is Braille or English and translate accordingly
function translator(input) {
  if (isBraille(input)) {
    return brailleToEnglish(input); // Translate Braille to English if input is Braille
  } else {
    return englishToBraille(input); // Translate English to Braille otherwise
  }
}

// Run the translation based on command-line arguments
const input = process.argv.slice(2).join(" "); // Join all arguments into one input string
console.log(translator(input)); // Output the result of the translation
