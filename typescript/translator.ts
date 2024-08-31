/**
 * Braille <> English Translator
 * Works with letters, numbers, and spaces
 */

type BrailleChar = `${"O" | "."}${"O" | "."}${"O" | "."}${"O" | "."}${
  | "O"
  | "."}${"O" | "."}`;

const brailleMap: { [key: string]: BrailleChar } = {
  // Letters
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
  " ": "......", // Space character
};

// Braille Number Map
const brailleNumberMap: { [key: string]: BrailleChar } = {
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

// Braille Special Characters that indicate actions
const CAPITAL_SYMBOL: BrailleChar = ".....O";
const NUMBER_SYMBOL: BrailleChar = ".O.OOO";

// utility function to reverse a map
// we need to reverse the map because we want to be able to look up the english character by the braille character
function reverseMap(map: { [key: string]: string }) {
  return Object.fromEntries(Object.entries(map).map(([k, v]) => [v, k]));
}

const reverseBrailleMap: { [key: string]: string } = reverseMap(brailleMap);
const reverseBrailleNumberMap: { [key: string]: string } =
  reverseMap(brailleNumberMap);

function brailleToEnglish(input: string): string {
  const braille: string[] = input.match(/.{1,6}/g) || []; // Split the input into an array of Braille characters
  let result = "";
  let isCapital = false;
  let isNumber = false;
  for (const char of braille) {
    if (char == NUMBER_SYMBOL) {
      isNumber = true;
    } else if (char == CAPITAL_SYMBOL) {
      isCapital = true;
    } else if (char == brailleMap[" "]) {
      result += " ";
      isNumber = false;
    } else if (isNumber) {
      result += reverseBrailleNumberMap[char];
    } else {
      result += isCapital
        ? reverseBrailleMap[char]?.toUpperCase() || ""
        : reverseBrailleMap[char] || "";
      isCapital = false;
    }
  }
  return result;
}

function englishToBraille(input: string): string {
  const text = input.split("");
  let result = "";
  let isNumber = false;
  for (const char of text) {
    if (/[0-9]/.test(char)) {
      if (!isNumber) {
        result += NUMBER_SYMBOL;
        isNumber = true;
      }
      result += brailleNumberMap[char];
    } else {
      isNumber = false;
      if (/[A-Z]/.test(char)) {
        result += CAPITAL_SYMBOL;
      }
      result += brailleMap[char.toLowerCase()] || "";
    }
  }
  return result;
}

// prints the braille in a better format
function prettyPrintBraille(braille: string): string {
  const chars = braille.match(/.{1,6}/g) || [];
  let result = "";
  for (const char of chars) {
    result += char.slice(0, 2) + "  ";
  }
  result += "\n";
  for (const char of chars) {
    result += char.slice(2, 4) + "  ";
  }
  result += "\n";
  for (const char of chars) {
    result += char.slice(4, 6) + "  ";
  }
  return result;
}

function translate(input: string, pretty: boolean = false): string {
  // Check if the input is Braille or English
  if (input.match(/^[O.]+$/)) {
    return brailleToEnglish(input);
  } else {
    const braille = englishToBraille(input);
    return pretty ? prettyPrintBraille(braille) : braille;
  }
}

const commandLineArgs = process.argv.slice(2);
const prettyFlag = commandLineArgs.includes("--pretty");
const inputString = commandLineArgs
  .filter((arg) => arg !== "--pretty")
  .join(" ");
console.log(translate(inputString, prettyFlag));
