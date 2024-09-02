/* File contains all the english char to Braille mappings */

// FORWARD MAPPING
// hashmap for the alphabets
const alphToBraille = new Map<string, string>([
  ["a", "O....."],
  ["b", "O.O..."],
  ["c", "OO...."],
  ["d", "OO.O.."],
  ["e", "O..O.."],
  ["f", "OOO..."],
  ["g", "OOOO.."],
  ["h", "O.OO.."],
  ["i", ".OO..."],
  ["j", ".OOO.."],
  ["k", "O...O."],
  ["l", "O.O.O."],
  ["m", "00..0."],
  ["n", "OO.OO."],
  ["o", "O..OO."],
  ["p", "OOO.O."],
  ["q", "OOOOO."],
  ["r", "O.OOO."],
  ["s", ".OO.O."],
  ["t", ".OOOO."],
  ["u", "O...OO"],
  ["v", "O.O.OO"],
  ["x", "OO..OO"],
  ["y", "OO.OOO"],
  ["z", "O..OOO"],
  ["w", ".OOO.O"],
  //   [".", "..OO.O"],
]);

// hashmap for the numbers
const digitToBraille = new Map<string, string>([
  ["1", "O....."],
  ["2", "O.O..."],
  ["3", "OO...."],
  ["4", "OO.O.."],
  ["5", "O..O.."],
  ["6", "OOO..."],
  ["7", "OOOO.."],
  ["8", "O.OO.."],
  ["9", ".OO..."],
  ["0", ".OOO.."],
  [".", ".O...O"], // decimal follows
  ["<", ".OO..O"],
  [">", "O..OO."],
]);

// hashmap for the numbers
const punctToBraille = new Map<string, string>([
  [".", "..OO.O"], //period or dot
  [",", "..O..."],
  ["?", "..O.OO"],
  ["!", "..OOO."],
  [":", "..OO.."],
  [";", "..O.O."],
  ["-", "....OO"],
  ["/", ".O..O."],
  ["(", "O.O..O"],
  [")", ".O.OO."],
  [" ", "......"],
  //   ["<", ".OO..O"],
  //   [">", "O..OO."],
]);

// REVERSE MAPPING
const brailleToAlph: Map<string, string> = new Map(
  [...alphToBraille.entries()].map(([key, value]) => [value, key]),
);

const brailleToDigit: Map<string, string> = new Map(
  [...digitToBraille.entries()].map(([key, value]) => [value, key]),
);

const brailleToPunct: Map<string, string> = new Map(
  [...punctToBraille.entries()].map(([key, value]) => [value, key]),
);

export {
  alphToBraille,
  digitToBraille,
  punctToBraille,
  brailleToAlph,
  brailleToDigit,
  brailleToPunct,
};
