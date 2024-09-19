// This is the source of truth for english character conversions to Braille

import { EnglishToBrailleMap } from "../types";

export const englishToBraillLetterMap: EnglishToBrailleMap = {
  a: ["O", ".", ".", ".", ".", "."],
  b: ["O", ".", "O", ".", ".", "."],
  c: ["O", "O", ".", ".", ".", "."],
  d: ["O", "O", ".", "O", ".", "."],
  e: ["O", ".", ".", "O", ".", "."],
  f: ["O", "O", "O", ".", ".", "."],
  g: ["O", "O", "O", "O", ".", "."],
  h: ["O", ".", "O", "O", ".", "."],
  i: [".", "O", "O", ".", ".", "."],
  j: [".", "O", "O", "O", ".", "."],
  k: ["O", ".", ".", ".", "O", "."],
  l: ["O", ".", "O", ".", "O", "."],
  m: ["O", "O", ".", ".", "O", "."],
  n: ["O", "O", ".", "O", "O", "."],
  o: ["O", ".", ".", "O", "O", "."],
  p: ["O", "O", "O", ".", "O", "."],
  q: ["O", "O", "O", "O", "O", "."],
  r: ["O", ".", "O", "O", "O", "."],
  s: [".", "O", "O", ".", "O", "."],
  t: [".", "O", "O", "O", "O", "."],
  u: ["O", ".", ".", ".", "O", "O"],
  v: ["O", ".", "O", ".", "O", "O"],
  w: [".", "O", "O", "O", ".", "O"],
  x: ["O", "O", ".", ".", "O", "O"],
  y: ["O", "O", ".", "O", "O", "O"],
  z: ["O", ".", ".", "O", "O", "O"],
  " ": [".", ".", ".", ".", ".", "."], // Empty Braille cell for space
};

export const englishToBrailleNumberMap: EnglishToBrailleMap = {
  "0": [".", "O", "O", "O", ".", "."],
  "1": ["O", ".", ".", ".", ".", "."],
  "2": ["O", ".", "O", ".", ".", "."],
  "3": ["O", "O", ".", ".", ".", "."],
  "4": ["O", "O", ".", "O", ".", "."],
  "5": ["O", ".", ".", "O", ".", "."],
  "6": ["O", "O", "O", ".", ".", "."],
  "7": ["O", "O", "O", "O", ".", "."],
  "8": ["O", ".", "O", "O", ".", "."],
  "9": [".", "O", "O", ".", ".", "."],
};

export const englishToBrailleCharacterizationMap: EnglishToBrailleMap = {
  capital: [".", ".", ".", ".", ".", "O"], // Capital follows symbol
  number: [".", "O", ".", "O", "O", "O"], // Number follows symbol
};
