import { Braille, Utility } from "./types";

export const numbers: Record<string, Braille> = {
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

export const letters: Record<string, Braille> = {
  "a": "O.....",
  "b": "O.O...",
  "c": "OO....",
  "d": "OO.O..",
  "e": "O..O..",
  "f": "OOO...",
  "g": "OOOO..",
  "h": "O.OO..",
  "i": ".OO...",
  "j": ".OOO..",
  "k": "O...O.",
  "l": "O.O.O.",
  "m": "OO..O.",
  "n": "OO.OO.",
  "o": "O..OO.",
  "p": "OOO.O.",
  "q": "OOOOO.",
  "r": "O.OOO.",
  "s": ".OO.O.",
  "t": ".OOOO.",
  "u": "O...OO",
  "v": "O.O.OO",
  "x": "OO..OO",
  "y": "OO.OOO",
  "z": "O..OOO",
  "w": ".OOO.O",
};

export const utilityMap: Record<Utility, Braille> = {
  capitalize: ".....O",
  number: ".O.OOO",
  space: "......",
};

export const brailleNumbers = swapKeys<Braille>(numbers);
export const brailleLetters = swapKeys<Braille>(letters);

function swapKeys<U extends number | string>(obj) {
  let newObj: Record<U, string> = {} as Record<U, string>;
  for (let [key, value] of Object.entries<U>(obj)) {
    newObj[value] = key;
  }
  return newObj;
}
