import { argv } from "node:process";

function flip(
  record: Record<string, string>,
): Record<string, string> {
  return Object.entries<string>(record).reduce((object, [key, value]) => ({
    ...object,
    [value]: key,
  }), {} as Record<string, string>);
}

const MODIFIER_CAPITAL = ".....O";
const MODIFIER_NUMBER = ".O.OOO";
const SPACE = "......";

const BRAILLE_MODIFIERS_MAP: Record<string, "capital" | "number" | undefined> =
  {
    [MODIFIER_CAPITAL]: "capital",
    [MODIFIER_NUMBER]: "number",
  };

const BRAILLE_LETTER_MAP: Record<string, string> = {
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
  [SPACE]: " ",
};

const ENGLISH_LETTER_MAP = flip(BRAILLE_LETTER_MAP);

const BRAILLE_NUMBER_MAP: Record<string, string> = {
  "O.....": "1",
  "O.O...": "2",
  "OO....": "3",
  "OO.O..": "4",
  "O..O..": "5",
  "OOO...": "6",
  "OOOO..": "7",
  "O.OO..": "8",
  ".OO...": "9",
  ".OOO..": "0",
};

const ENGLISH_NUMBER_MAP = flip(BRAILLE_NUMBER_MAP);

const [, , ...words] = argv;
const sentence = words.join(" ");

if (isBraille(sentence)) {
  console.log(brailleToEnglish(sentence));
} else {
  console.log(englishToBraile(sentence));
}

function isBraille(sentence: string) {
  return sentence.match(/^[O.]+$/);
}

function brailleToEnglish(braille: string) {
  let result = "";
  let state: "capital" | "number" | null;

  for (let i = 0; i < braille.length; i += 6) {
    const letter = braille.slice(i, i + 6);

    const modifier = BRAILLE_MODIFIERS_MAP[letter];
    if (modifier) {
      state = modifier;
      continue;
    }

    if (letter === SPACE) {
      state = null;
    }

    if (state === "number") {
      result += BRAILLE_NUMBER_MAP[letter];
      continue;
    }

    if (state === "capital") {
      result += BRAILLE_LETTER_MAP[letter].toUpperCase();
      state = null;
      continue;
    }

    if (state === null) {
      result += BRAILLE_LETTER_MAP[letter];
    }
  }

  return result;
}

function englishToBraile(sentence: string) {
  let result = "";
  let state: "number" | null = null;

  for (let i = 0; i < sentence.length; i++) {
    const char = sentence[i];

    const isUppercase = char.codePointAt(0) >= 65 && char.codePointAt(0) <= 90; // A-Z
    const isNumber = char.codePointAt(0) >= 48 && char.codePointAt(0) <= 57; // 0-9

    if (char === " ") {
      result += SPACE;
      state = null;
      continue;
    }

    if (isNumber) {
      if (state !== "number") {
        result += MODIFIER_NUMBER;
      }

      state = "number";
      result += ENGLISH_NUMBER_MAP[char];
      continue;
    }

    if (isUppercase) {
      result += MODIFIER_CAPITAL;
    }

    result += ENGLISH_LETTER_MAP[char.toLowerCase()];
  }

  return result;
}
