// Braille-English Mappings
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
  ["......", " "],
]);

const englishToBraille = new Map<string, string>();
const numToBraille = new Map<string, string>();

brailleToNum.forEach((key: string, val: string) => {
  numToBraille.set(key, val);
});

brailleToEnglish.forEach((key: string, val: string) => {
  englishToBraille.set(key, val);
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
  let numMode: boolean = false;
  let engStr: string = "";

  for (let i = 0; i * 6 < brailleStr.length; i++) {
    const bLetter: string = brailleStr.substring(i * 6, (i + 1) * 6);
    let eLetter: string | undefined = numMode
      ? brailleToNum.get(bLetter)
      : brailleToEnglish.get(bLetter);

    if (!eLetter) throw new Error(`Invalid braille entry: ${bLetter}`);

    if (eLetter == "capital") {
      capFlag = true;
      continue;
    }

    if (capFlag) {
      eLetter = eLetter.toUpperCase();
      capFlag = false;
    }

    if (eLetter == "number") {
      numMode = true;
      continue;
    }

    if (eLetter == " ") numMode = false;

    engStr = engStr.concat(eLetter);
  }

  return engStr;
};

/**
 * translates the english alphabet + numbers (with Capitalization) into braille
 *
 * @example
 * // return '.....OO.OO..O..O..O.O.O.O.O.O.O..OO.'
 * englishTranslate('Hello')
 *
 * @returns {string} a translated braille phrase
 */
const englishTranslate = (englishStr: string): string => {
  let brailleStr: string = "";
  let numMode: boolean = false;

  for (let eLetter of englishStr) {
    let bLetter: string | undefined;

    if (
      eLetter.toUpperCase() == eLetter &&
      !Number(eLetter) &&
      eLetter != " " &&
      !numMode
    ) {
      brailleStr = brailleStr.concat(englishToBraille.get("capital") ?? "");
      eLetter = eLetter.toLowerCase();
    }

    if (Number(eLetter) && !numMode) {
      brailleStr = brailleStr.concat(englishToBraille.get("number") ?? "");
      numMode = true;
    }

    if (eLetter == " ") {
      numMode = false;
    }

    bLetter = numMode
      ? numToBraille.get(eLetter)
      : englishToBraille.get(eLetter);

    if (!bLetter) throw new Error(`Invalid character entry: ${eLetter}`);

    brailleStr = brailleStr.concat(bLetter);
  }

  return brailleStr;
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

/**
 * main function to determine braille or english and convert it into its other language.
 *
 * @return {string} Translation of a braille or english phrase
 */
const runTranslation = (clArgs: string): string => {
  if (!clArgs) {
    throw new Error(
      "Please provide command line arguments (ie. npm run dev Hello World)",
    );
  }

  // try and catch to handle edge cases that can be braille and english (ie. OOOOOO)
  if (isValidBraille(clArgs)) {
    try {
      return brailleTranslate(clArgs);
    } catch (_) {
      return englishTranslate(clArgs);
    }
  }

  return englishTranslate(clArgs);
};

const out = runTranslation(process.argv.slice(2).join(" "));
console.log(out);
