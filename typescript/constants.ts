export type BrailleKey =
  | "OO...."
  | "OO.O.."
  | "O..O.."
  | "OOO..."
  | "OOOO.."
  | "O.OO.."
  | ".OO..."
  | ".O..OO"
  | "O....."
  | "O.O..."
  | "OO.O.."
  | "O..O.."
  | "OOO..."
  | "OOOO.."
  | "O.OO.."
  | ".OO..."
  | ".OOO.."
  | "O...O."
  | "O.O.O."
  | "OO..O."
  | "OO.OO."
  | "O..OO."
  | "OOO.O."
  | "OOOOO."
  | "O.OOO."
  | ".OO.O."
  | ".OOOO."
  | "O...OO"
  | "O.O.OO"
  | ".OOO.O"
  | "OO..OO"
  | "OO.OOO"
  | "O..OOO"
  | ".....O"
  | ".O...O"
  | ".O.OOO"
  | "..OO.O"
  | "..O..."
  | "..O.OO"
  | "OO...O"
  | "..OO.."
  | "..O.O."
  | "....OO"
  | ".O..O."
  | ".OO..O"
  | "O.O..O"
  | ".O.OO."
  | "......";

export const brailleNumberMapping: Partial<Record<BrailleKey, string>> = {
  "O.....": "1",
  "O.O...": "2",
  "OO....": "3",
  "OO.O..": "4",
  "O..O..": "5",
  "OOO...": "6",
  "OOOO..": "7",
  "O.OO..": "8",
  ".OO...": "9",
  ".O..OO": "0",
  "......": " ",
};

export const brailleAlphabetMapping: Partial<Record<BrailleKey, string>> = {
  "O.....": "a",
  "O.O...": "b",
  "OO....": "c",
  "OO.O..": "d",
  "O..O..": "e",
  "OOO...": "f",
  "OOOO..": "g",
  "O.OO..": "h",
  ".OO...": "i",
  ".OOO..": "j",
  "O...O.": "k",
  "O.O.O.": "l",
  "OO..O.": "m",
  "OO.OO.": "n",
  "O..OO.": "o",
  "OOO.O.": "p",
  "OOOOO.": "q",
  "O.OOO.": "r",
  ".OO.O.": "s",
  ".OOOO.": "t",
  "O...OO": "u",
  "O.O.OO": "v",
  ".OOO.O": "w",
  "OO..OO": "x",
  "OO.OOO": "y",
  "O..OOO": "z",
  ".....O": "cf",
  ".O...O": "df",
  ".O.OOO": "nf",
  "..OO.O": ".",
  "..O...": ",",
  "..O.OO": "?",
  "OO...O": "!",
  "..OO..": ":",
  "..O.O.": ";",
  "....OO": "-",
  ".O..O.": "/",
  ".OO..O": "<",
  // "O..OO.": ">", // Hard edge case to account for eg. 'o>' -> O..OO.O..OO. which is hard to decode without more context or preceding delimiter
  "O.O..O": "(",
  ".O.OO.": ")",
  "......": " ",
};

export type EnglishKey =
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
  | "cf"
  | "df"
  | "nf"
  | "."
  | ","
  | "?"
  | "!"
  | ":"
  | ";"
  | "-"
  | "/"
  | "<"
  //  ">":  "O..OO.":, // Hard edge case to account for eg. 'o>' -> O..OO.O..OO. which is hard to decode without more context or preceding delimitr
  | "("
  | ")"
  | " "
  | "1"
  | "2"
  | "3"
  | "4"
  | "5"
  | "6"
  | "7"
  | "8"
  | "9"
  | "0";

export const englishNumberMapping: Partial<Record<EnglishKey, string>> = {
  "1": "O.....",
  "2": "O.O...",
  "3": "OO....",
  "4": "OO.O..",
  "5": "O..O..",
  "6": "OOO...",
  "7": "OOOO..",
  "8": "O.OO..",
  "9": ".OO...",
  "0": ".O..OO",
};

export const englishAlphabetMapping: Partial<Record<EnglishKey, string>> = {
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
  cf: ".....O",
  df: ".O...O",
  nf: ".O.OOO",
  ".": "..OO.O",
  ",": "..O...",
  "?": "..O.OO",
  "!": "OO...O",
  ":": "..OO..",
  ";": "..O.O.",
  "-": "....OO",
  "/": ".O..O.",
  "<": ".OO..O",
  //  ">":  "O..OO.":, // Hard edge case to account for eg. 'o>' -> O..OO.O..OO. which is hard to decode without more context or preceding delimitr
  "(": "O.O..O",
  ")": ".O.OO.",
  " ": "......",
};
