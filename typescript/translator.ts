// Mappings from Braille to English letters
const brailleToEng = new Map<string, string>([
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

// Mappings from Braille to English numbers
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

// Reverse mapping - braille to english
const englishToBraille = new Map([...brailleToEng].map(([k, v]) => [v, k]));
const numToBraille = new Map([...brailleToNum].map(([k, v]) => [v, k]));

// Translates braille to english
const brailleToEngTranslate = (braille: string): string => {
  let result = "";
  let capitalize = false;
  let numberMode = false;

  for (let i = 0; i < braille.length; i += 6) {
    const brailleChar = braille.slice(i, i + 6);
    let char = numberMode
      ? brailleToNum.get(brailleChar)
      : brailleToEng.get(brailleChar);

    if (!char) throw new Error(`Invalid Braille character: ${brailleChar}`);

    if (char === "capital") {
      capitalize = true;
      continue;
    }

    if (char === "number") {
      numberMode = true;
      continue;
    }

    if (capitalize) {
      char = char.toUpperCase();
      capitalize = false;
    }

    result += char;
    if (char === " ") numberMode = false;
  }
  return result;
};

// Translation to Braille
const englishToBrailleTranslate = (text: string): string => {
  let result = "";
  let numberMode = false;

  for (const char of text) {
    let brailleChar;

    if (/[A-Z]/.test(char)) {
      result += englishToBraille.get("capital");
      brailleChar = englishToBraille.get(char.toLowerCase());
    } else if (/[0-9]/.test(char)) {
      if (!numberMode) {
        result += englishToBraille.get("number");
        numberMode = true;
      }
      brailleChar = numToBraille.get(char);
    } else {
      brailleChar = englishToBraille.get(char);
      if (char === " ") numberMode = false; // Reset number mode on space
    }

    if (!brailleChar) throw new Error(`Invalid English character: ${char}`);
    result += brailleChar;
  }
  return result;
};

// Checks if string is valid Braille string (only contains 'O' and '.' and is a multiple of 6)
const isValidBraille = (str: string): boolean =>
  /^[O.]+$/.test(str) && str.length % 6 === 0;

// Runs translation based on determined English or Braille input
const runTranslation = (input: string): string => {
  if (isValidBraille(input)) {
    return brailleToEngTranslate(input);
  } else {
    return englishToBrailleTranslate(input);
  }
};

// Take input
const args = process.argv.slice(2).join(" ");
if (!args) {
  throw new Error("No input detected, please try again");
}
