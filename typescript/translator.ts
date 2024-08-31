const brailleToEnglish = new Map<string, string>([
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
  [".....O", "capital"],
  [".O.OOO", "number"],
  ["......", " "],
]);

const brailleToNum = new Map<string, string>([
  ["O.....", "1"],
  ["O.O...", "2"],
  ["OO....", "3"],
  ["OO.O..", "4"],
  ["O..O..", "5"],
  ["OOO...", "6"],
  ["OOOO..", "7"],
  ["O.OO..", "8"],
  [".OO...", "9"],
  [".OOO..", "0"],
]);

const englishToBraille = new Map<string, string>();
const numToBraille = new Map<string, string>();

brailleToNum.forEach((key: string, val: string) => {
  numToBraille.set(val, key);
});

brailleToEnglish.forEach((key: string, val: string) => {
  englishToBraille.set(val, key);
});

/**
 * translates braille into the english alphabet + numbers (with Capitalization)
 *
 * @example
 * // returns 'Hello'
 * brailleTranslate('.....OO.OO..O..O..O.O.O.O.O.O.O..OO.')
 *
 * @returns {string} a translated english phrase
 */
const brailleTranslate = (brailleStr: string): string => {
  let capFlag: boolean = false;
  let engStr: string = "";

  let aLetter: string | undefined = "";
  let bLetter: string = "";

  for (let i = 0; i * 6 < brailleStr.length; i++) {
    bLetter = brailleStr.substring(i * 6, (i + 1) * 6);
    aLetter = brailleToEnglish.get(bLetter);

    if (!aLetter) {
      throw new Error(`Invalid braille entry: ${bLetter}`);
    }

    if (aLetter == "capital") {
      capFlag = true;
      continue;
    }

    if (capFlag) {
      aLetter = aLetter.toUpperCase();
      capFlag = false;
    }

    engStr = engStr.concat(aLetter);
  }

  return engStr;
};

/**
 * check if a string is or isn't valid Braille such that it only contains O or .
 *
 * @example
 * // returns false
 * isValidBraille("..O...O...A.")
 *
 * @returns {boolean} Returns whether or not it is a braille string
 */
const isValidBraille = (str: string): boolean => {
  const allowedSet: string[] = ["O", "."];

  if (str.length % 6 != 0) return false;

  for (const letter of str) {
    if (!allowedSet.includes(letter)) {
      return false;
    }
  }
  return true;
};

const clArgs = process.argv.slice(2).join(" ");

// // if true -> translate to braille
// // if false -> translate to english
// console.log(isValidBraille(clArgs));

console.log(brailleTranslate(clArgs));
