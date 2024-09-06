type BraillePattern = `${"O" | "."}${"O" | "."}${"O" | "."}${"O" | "."}${
  | "O"
  | "."}${"O" | "."}`;
type BrailleArray = BraillePattern[];
type EnglishLetterKey =
  | "a"
  | "b"
  | "c"
  | "d"
  | "e"
  | "f"
  | "g"
  | "h"
  | "i"
  | "j"
  | "k"
  | "l"
  | "m"
  | "n"
  | "o"
  | "p"
  | "q"
  | "r"
  | "s"
  | "t"
  | "u"
  | "v"
  | "w"
  | "x"
  | "y"
  | "z"
  | " ";
type NumberKey = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9";
type EnglishToBrailleMap = { [key in EnglishLetterKey]: BraillePattern };
type NumberToBrailleMap = { [key in NumberKey]: BraillePattern };

const capitalIndicator: BraillePattern = ".....O";
const numberIndicator: BraillePattern = ".O.OOO";
const blank: EnglishLetterKey = " ";

const englishToBrailleMap: EnglishToBrailleMap = {
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
  [blank]: "......",
};

const numberToBrailleMap: NumberToBrailleMap = {
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

const brailleToEnglishMap = Object.fromEntries(
  Object.entries(englishToBrailleMap).map(([char, braille]) => [braille, char])
) as Record<BraillePattern, EnglishLetterKey>;

const brailleToNumberMap = Object.fromEntries(
  Object.entries(numberToBrailleMap).map(([num, braille]) => [braille, num])
) as Record<BraillePattern, NumberKey>;

function stringToBrailleArray(input: string): BrailleArray {
  const brailleArray: BrailleArray = [];

  for (let i = 0; i < input.length; i += 6) {
    const braillePattern = input.slice(i, i + 6) as BraillePattern;
    brailleArray.push(braillePattern);
  }

  return brailleArray;
}

function brailleArrayToString(brailleArray: BrailleArray): string {
  return brailleArray.join("");
}

function englishToBraille(input: string): string {
  const result: BrailleArray = [];
  let numberMode = false;

  for (const char of input) {
    if (char === blank) {
      result.push(englishToBrailleMap[blank]);
      numberMode = false;
    } else if ("A" <= char && char <= "Z") {
      result.push(capitalIndicator);
      result.push(englishToBrailleMap[char.toLowerCase() as EnglishLetterKey]);
      numberMode = false;
    } else if (char >= "0" && char <= "9") {
      if (!numberMode) {
        result.push(numberIndicator);
        numberMode = true;
      }
      result.push(numberToBrailleMap[char as NumberKey]);
    } else {
      result.push(englishToBrailleMap[char as EnglishLetterKey]);
      numberMode = false;
    }
  }

  return brailleArrayToString(result);
}

function brailleToEnglish(input: string): string {
  const brailleArrays = stringToBrailleArray(input);
  let result = "";
  let capitalizeNext = false;
  let numberMode = false;

  for (const braille of brailleArrays) {
    if (braille === "......") {
      result += blank;
      numberMode = false;
    } else if (braille === capitalIndicator) {
      capitalizeNext = true;
    } else if (braille === numberIndicator) {
      numberMode = true;
    } else {
      if (numberMode) {
        result += brailleToNumberMap[braille];
      } else {
        let englishLetter = brailleToEnglishMap[braille];

        if (capitalizeNext) {
          englishLetter = englishLetter.toUpperCase() as EnglishLetterKey;
          capitalizeNext = false;
        }

        result += englishLetter;
      }
    }
  }

  return result;
}

function translate(input: string): string {
  const isBraille = /^[O.]+$/.test(input) && input.length % 6 === 0;

  if (isBraille) {
    return brailleToEnglish(input);
  } else {
    return englishToBraille(input);
  }
}

const input = process.argv.slice(2).join(" ");
console.log(translate(input));
