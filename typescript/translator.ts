// We need to Convert Braille to English and English to Braille

// Pseudo Code
// Step 1 check for braille or english by checking if the input has only braille characters
// and classify the input as braille or english
// Step 2 convert the input to the other language using a dictionary to lookup the braille to english
// key value pairs // english to braille key value pairs using a reverse lookup
// Step 3 ensure lowercase, uppercase, numbers and digits are handled correctly
// following convention for braille
// Step 4 return the converted input

// Implementation

// Function to check if the input is Braille
function isBraille(input: string): boolean {
  // Loop through each character in the input string
  for (let char of input) {
    // If any character is not 'O' or '.', return false
    if (char !== "O" && char !== ".") {
      return false;
    }
  }
  // If all characters are 'O' or '.', return true
  return true;
}

// Create dictionary to convert English to Braille
const englishToBraille: { [key: string]: string } = {
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
  " ": ".....O",
  H: "......O.OO..",
  I: ".......OO...",
  ".": "..O...",
};

// Capitalization and number indicators in Braille
const brailleCapitalIndicator = "......";
const brailleNumberIndicator = ".O.OO.";

// Number mappings in Braille
const numbersToBraille: { [key: string]: string } = {
  "1": "O.....",
  "2": "O.O...",
  "3": "OO....",
  "4": "OO.O..",
  "5": "O..O..",
  "6": "OOO...",
  "7": "OOOO..",
  "8": "O.OO..",
  "9": ".OO...",
  "0": ".OOO..",
};

// reverse dictionary method to lookup Braille using English and our dictionary
function createReverseDictionary(original: { [key: string]: string }): {
  [key: string]: string;
} {
  // Create an empty object for reversed mappings, with a reversed Key Value setup
  const reversed: { [key: string]: string } = {};

  // Loop over each key-value pair in the original dictionary and set the value as key, and vice versa
  for (let key in original) {
    const value = original[key];
    reversed[value] = key;
  }

  return reversed;
}

// use our reverse method for our dictionary to get Braille to English mappings
const brailleToEnglish = createReverseDictionary(englishToBraille);
const brailleToNumbers = createReverseDictionary(numbersToBraille);

// Function to convert Braille to English
function convertBrailleToEnglish(input: string): string {
  let result = "";
  // Bool to indicate capitalization
  let isCapitalized = false;
  // Bool to indicate number sequence
  let isNumber = false;

  // Braille characters are 6 characters long
  const brailleLength = 6;

  // Loop through input in our 6 character chunks
  for (let i = 0; i < input.length; i += brailleLength) {
    const brailleChunk = input.substr(i, brailleLength);

    // Check for capitalization indicator
    if (brailleChunk === brailleCapitalIndicator) {
      isCapitalized = true;
    }

    // Check for number indicator
    if (brailleChunk === brailleNumberIndicator) {
      isNumber = true;
    }

    // Determine the character
    let englishChar;
    if (isNumber) {
      // If in number mode, use the numbersToBraille reverse dictionary
      englishChar = brailleToNumbers[brailleChunk] || "";
      if (!englishChar) {
        // Invalid number character, exit number mode
        isNumber = false;
      }
    } else {
      // Look up the English character in the reverse dictionary
      englishChar = brailleToEnglish[brailleChunk] || "";
      // Apply capitalization if needed
      if (isCapitalized && englishChar) {
        englishChar = englishChar.toUpperCase();
        isCapitalized = false;
      }
    }

    // Append character to the result if it's not empty
    if (englishChar) {
      result += englishChar;
    }

    // Reset isNumber flag after a space to stop number mode
    if (englishChar === " ") {
      isNumber = false;
    }
  }

  return result;
}

// Function to convert English to Braille
function convertEnglishToBraille(input: string): string {
  let result = "";
  // Tracks if we're currently in number mode
  let inNumberMode = false;

  // Loop through each character of the English input string
  for (const char of input) {
    // Handle capitalization
    if (char >= "A" && char <= "Z") {
      // Add the capitalization indicator
      result += brailleCapitalIndicator;
      // Convert to lowercase and then to Braille
      const lowerChar = char.toLowerCase();
      result += englishToBraille[lowerChar] || "......";
    }
    // Handle numbers
    else if (char >= "0" && char <= "9") {
      // Add the number indicator before each number sequence if not already in number mode
      if (!inNumberMode) {
        result += brailleNumberIndicator;
        inNumberMode = true;
      }
      result += numbersToBraille[char] || "......";
    }
    // Handle spaces and reset number mode
    else if (char === " ") {
      result += englishToBraille[char];
      inNumberMode = false;
    }
    // Handle punctuation like period
    else if (char === ".") {
      result += englishToBraille[char] || "......";
    }
    // Normal lowercase letters and other characters
    else {
      result += englishToBraille[char] || "......";
      inNumberMode = false;
    }
  }

  return result;
}

// Comannd Line Arguments: node translator.ts "Hello World"
const [, , ...args] = process.argv;
const input = args.join(" ");
if (isBraille(input)) {
  // Convert Braille to English
  console.log(convertBrailleToEnglish(input));
} else {
  // Convert English to Braille
  console.log(convertEnglishToBraille(input));
}
