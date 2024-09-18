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
  A: "......O.....",
  B: "......O.O...",
  C: "......OO....",
  D: "......OO.O..",
  E: "......O..O..",
  F: "......OOO...",
  G: "......OOOO..",
  H: "......O.OO..",
  I: ".......OO...",
  J: ".......OOO..",
  K: "......O...O.",
  L: "......O.O.O.",
  M: "......OO..O.",
  N: "......OO.OO.",
  O: "......O..OO.",
  P: "......OOO.O.",
  Q: "......OOOOO.",
  R: "......O.OOO.",
  S: ".......OO.O.",
  T: ".......OOOO.",
  U: "......O...OO",
  V: "......O.O.OO",
  W: ".......OOO.O",
  X: "......OO..OO",
  Y: "......OO.OOO",
  Z: "......O..OOO",
  "1": ".....O.O.....",
  "2": ".....O.O.O...",
  "3": ".....OOO....",
  "4": ".....OO.O..",
  "5": ".....O..O..",
  "6": ".....OOO...",
  "7": ".....OOOO..",
  "8": ".....O.OO..",
  "9": "......OO...",
  "0": ".......OOO..",
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

// Finally, we just need to implement the translation functions for Eng to Braille, and vice versa

// Function to convert Braille to English
function convertBrailleToEnglish(input: string): string {
  let result = "";
  // Braille characters are 6 characters long
  const brailleLength = 6;
  // Loop through input in our 6 character chunks
  for (let i = 0; i < input.length; i += brailleLength) {
    const brailleChunk = input.substr(i, brailleLength);
    // Look up the English character in the reverse dictionary
    result += brailleToEnglish[brailleChunk] || "unknown";
  }

  return result;
}

// Function to convert English to Braille
function convertEnglishToBraille(input: string): string {
  let result = "";

  // Loop through each character of the English input string
  for (const char of input) {
    // Look up the Braille pattern for each character
    result += englishToBraille[char] || "......"; // Use '......' for unknown characters
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
