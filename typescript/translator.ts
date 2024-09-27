import {
  getKeyByValue,
  isNumber,
  isUpperCase,
  isValidBraille,
  splitBraille,
} from "./utils";

export const brailleAlphabetMap: Record<string, string> = {
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
  number: ".O.OOO",
  capital: ".....O",
  decimal: ".O...O",
  ".": "..OO.O",
  ",": "..O...",
  "?": "..O.OO",
  "!": "..OOO.",
  ":": "..OO..",
  ";": "..O.O.",
  "-": "....OO",
  "<": ".OO..O",
  ">": "O..O.O",
  "(": "O.O..O",
  ")": ".O.OO.",
  " ": "......",
};

export const brailleNumberMap: Record<string, string> = {
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

function translateEnglishToBraille(input: string) {
  let res = "";
  let numberFollows = false;

  for (let char of input) {
    if (isUpperCase(char)) {
      res += brailleAlphabetMap["capital"];
      char = char.toLowerCase();
    }

    if (isNumber(char) && !numberFollows) {
      res += brailleAlphabetMap["number"];
      numberFollows = true;
    }

    if (char === " ") numberFollows = false;

    res += numberFollows ? brailleNumberMap[char] : brailleAlphabetMap[char];
  }

  return res;
}

function translateBrailleToEnglish(input: string) {
  const SPACE = "......";
  let numberFollows = false;
  let capitalFollows = false;
  let res = "";
  const brailleArray = splitBraille(input);

  for (let braille of brailleArray) {
    let char =
      numberFollows && braille !== SPACE
        ? getKeyByValue(brailleNumberMap, braille)
        : getKeyByValue(brailleAlphabetMap, braille);

    if (char === "capital") {
      capitalFollows = true;
      continue;
    }

    if (char === "number") {
      numberFollows = true;
      continue;
    }

    if (char === " ") {
      numberFollows = false;
      res += " ";
      continue;
    }

    if (capitalFollows && char) {
      char = char.toUpperCase();
      capitalFollows = false;
    }

    res += char;
  }

  return res;
}

export function translateInput(input: string) {
  return isValidBraille(input)
    ? translateBrailleToEnglish(input)
    : translateEnglishToBraille(input);
}

function main() {
  const parseInput = process.argv.slice(2).join(" ").trim();
  const res = translateInput(parseInput);
  return res;
}

console.log(main());
