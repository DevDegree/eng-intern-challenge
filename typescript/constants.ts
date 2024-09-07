export const ENGLISH_TO_BRAILLE: { [key: string]: string } = {
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
  " ": "......",
  capital: ".....O",
  number: ".O.OOO"
};

export const ENGLISH_TO_NUMBERS: { [key: string]: string } = {
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
}

export const BRAILLE_TO_ENGLISH: { [key: string]: string } = Object.fromEntries(
  Object.entries(ENGLISH_TO_BRAILLE).map(([key, value]) => [value, key]),
);

export const BRAILLE_TO_NUMBERS: { [key: string]: string } = Object.fromEntries(
  Object.entries(ENGLISH_TO_NUMBERS).map(([key, value]) => [value, key]),
);

export const ENGLISH_SPACE: string = " ";
export const BRAILLE_SPACE: string = ENGLISH_TO_BRAILLE[ENGLISH_SPACE];
export const BRAILLE_NUMBER: string = ENGLISH_TO_BRAILLE["number"];
export const BRAILLE_CAPITAL: string = ENGLISH_TO_BRAILLE["capital"];
export const BRAILLE_PREFIXES = [BRAILLE_NUMBER, BRAILLE_CAPITAL];