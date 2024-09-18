export const brailleInputRegex = /^([OO.]{6})+$/;

export const brailleToNumberMap = new Map<string, string>([
  ["O.....", "1"],
  ["O.O...", "2"],
  ["OO....", "3"],
  ["OO.O..", "4"],
  ["O..O..", "5"],
  ["OOO...", "6"],
  ["OOOO..", "7"],
  ["O.OO..", "8"],
  [".OO...", "9"],
  [".OOO..", "0"]
]);

export const brailleToEnglishMap = new Map<string, string>([
  ["O.....", "a"],
  ["O.O...", "b"],
  ["OO....", "c"],
  ["OO.O..", "d"],
  ["O..O..", "e"],
  ["OOO...", "f"],
  ["OOOO..", "g"],
  ["O.OO..", "h"],
  [".OO...", "i"],
  [".OOO..", "j"],
  ["O...O.", "k"],
  ["O.O.O.", "l"],
  ["OO..O.", "m"],
  ["OO.OO.", "n"],
  ["O..OO.", "o"],
  ["OOO.O.", "p"],
  ["OOOOO.", "q"],
  ["O.OOO.", "r"],
  [".OO.O.", "s"],
  [".OOOO.", "t"],
  ["O...OO", "u"],
  ["O.O.OO", "v"],
  [".OOO.O", "w"],
  ["OO..OO", "x"],
  ["OO.OOO", "y"],
  ["O..OOO", "z"],
  ["......", " "],
  [".....O", "capital"],
  [".O.OOO", "number"]
]);

export const englishToBrailleMap = new Map(Array.from(brailleToEnglishMap.entries()).map(([braille, english]) => [english, braille]));

export const numbersToBrailleMap = new Map(Array.from(brailleToNumberMap.entries()).map(([braille, numbers]) => [numbers, braille]));

export const isNumeric = (value: string): boolean => {
  return !isNaN(parseFloat(value)) && isFinite(Number(value));
};
