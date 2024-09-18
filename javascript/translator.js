/**
 * This script translates between English text and Braille patterns. It determines
 * if the input is in Braille or English and performs the corresponding translation.
 *
 * Features:
 * - English to Braille translation
 * - Braille to English translation
 * - Handling of numbers, capitalization, and spaces
 *
 * Example:
 * $ node translator.js "Abc 123"
 * Output: .....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO
 */

// Braille mappings
const brailleAlphabet = {
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

// Braille patterns for numbers 0-9
const brailleNumbers = {
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

// Braille patterns for special characters
const specialBraille = {
  capital: ".....O",
  number: ".O.OOO",
  space: "......",
};

// Create reverse mappings for Braille to English
const englishAlphabet = Object.fromEntries(
  Object.entries(brailleAlphabet).map(([char, braille]) => [braille, char])
);

const englishNumbers = Object.fromEntries(
  Object.entries(brailleNumbers).map(([num, braille]) => [braille, num])
);

// Determine if input is Braille
const isBraille = (input) => /^[O.]+$/.test(input.replace(/\s+/g, ""));

// Translate English to Braille
const translateEnglishToBraille = (text) => {
  let brailleText = "";
  let numberMode = false;

  for (const char of text) {
    if (char === " ") {
      brailleText += specialBraille.space;
      numberMode = false;
    } else if (char >= "A" && char <= "Z") {
      brailleText += specialBraille.capital;
      brailleText += brailleAlphabet[char.toLowerCase()] || "......";
      numberMode = false;
    } else if (char >= "0" && char <= "9") {
      if (!numberMode) {
        brailleText += specialBraille.number;
        numberMode = true;
      }
      brailleText += brailleNumbers[char];
    } else if (char >= "a" && char <= "z") {
      brailleText += brailleAlphabet[char] || "......";
      numberMode = false;
    } else {
      brailleText += specialBraille.space;
      numberMode = false;
    }
  }

  return brailleText;
};

// Translate Braille to English text
const translateBrailleToEnglish = (brailleText) => {
  let englishText = "";
  let isCapital = false;
  let numberMode = false;

  const brailleChars = brailleText.replace(/\s+/g, "").match(/.{1,6}/g) || [];

  for (const brailleChar of brailleChars) {
    if (brailleChar === specialBraille.space) {
      englishText += " ";
      numberMode = false;
    } else if (brailleChar === specialBraille.capital) {
      isCapital = true;
    } else if (brailleChar === specialBraille.number) {
      numberMode = true;
    } else {
      let char = numberMode
        ? englishNumbers[brailleChar] || ""
        : englishAlphabet[brailleChar] || "";
      if (isCapital && char) {
        char = char.toUpperCase();
        isCapital = false;
      }
      englishText += char;
    }
  }

  return englishText;
};

// Main translation function
const brailleTranslator = (input) => {
  return isBraille(input)
    ? translateBrailleToEnglish(input)
    : translateEnglishToBraille(input);
};

// Get input from command-line arguments
const input = process.argv.slice(2).join(" ");
const output = brailleTranslator(input);
console.log(output);
