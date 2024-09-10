const STARTING_INDEX_OF_ARGS = 2;
const BRAILLE_CHARACTER_LENGTH = 6;
const BRAILLE_TO_ENGLISH: { [brailleCharacter: string]: string } = {
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
  "......": " ",
  ".....O": "capital",
  ".O.OOO": "number",
};

const ENGLISH_TO_BRAILLE = generateEnglishToBraille();
const INDEX_TO_BRAILLE = generateIndexToBraille();

function generateEnglishToBraille() {
  const brailleToEnglish: { [englishCharacter: string]: string } = {};

  for (const key in BRAILLE_TO_ENGLISH) {
    const value = BRAILLE_TO_ENGLISH[key];
    brailleToEnglish[value] = key;
  }

  return brailleToEnglish;
}

function generateIndexToBraille() {
  const charsWithNumberTranslation = "jabcdefghi";
  const brailleToNumber = [];

  for (let idx = 0; idx < charsWithNumberTranslation.length; idx += 1) {
    const currentChar = charsWithNumberTranslation[idx];
    brailleToNumber.push(ENGLISH_TO_BRAILLE[currentChar]);
  }

  return brailleToNumber;
}

function isValidEnglish(input: string) {
  return /^[a-zA-Z0-9 ]+$/.test(input);
}

function isValidBraille(input: string) {
  return /^[.O]+$/.test(input) && input.length % BRAILLE_CHARACTER_LENGTH === 0;
}

function isUppercaseCharacter(character: string) {
  return /^[A-Z]$/.test(character);
}

function isNumericCharacter(character: string) {
  return /^[0-9]$/.test(character);
}

function translateEnglishToBraille(englishText: string) {
  let translation = "";
  let numberMode = false;

  for (let idx = 0; idx < englishText.length; idx += 1) {
    const character = englishText[idx];

    if (isUppercaseCharacter(character)) {
      translation += ENGLISH_TO_BRAILLE["capital"];
      translation += ENGLISH_TO_BRAILLE[character.toLowerCase()];
      continue;
    }

    if (isNumericCharacter(character)) {
      if (!numberMode) {
        numberMode = true;
        translation += ENGLISH_TO_BRAILLE["number"];
      }
      translation += INDEX_TO_BRAILLE[Number(character)];
      continue;
    }

    if (character === " ") {
      numberMode = false;
    }

    translation += ENGLISH_TO_BRAILLE[character];
  }

  return translation;
}

const commandLineInput = process.argv.slice(STARTING_INDEX_OF_ARGS);
const formattedInput = commandLineInput.join(" ");

if (isValidEnglish(formattedInput)) {
  const brailleResult = translateEnglishToBraille(formattedInput);
  console.log(brailleResult);
  console.log(
    ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.." +
      "......" +
      ".O.OOOOO.O..O.O..." ===
      brailleResult
  );
} else if (isValidBraille(formattedInput)) {
  console.log("Braille:", formattedInput);
} else {
  console.log("Error, invalid input");
}
/*
node version: 18.20.4

input: string
  - in "English", Alphanumeric, upper/lower, spaces
  - in "Braille": . and O (not zero)
    . white (flat)
    O black (raised)
  - No other special characters will be input

Output: string
  - Only output the translation, NOTHING ELSE

Rules:
  - When a braille "Capital follows" (.....O), only the next symbol is capitalized
  - when a braille "Number follows" (O.O.OO), all following symbols are numbers until a space (......)
  - Each braille character consists of 6 characters

Questions:
  - Will inputs always be English OR Braille, or can it be a mix of both? Assuming it will always be one or the other
  - Will the input always be a valid character? (e.g. English: only alphanumeric + space, Braille: always . and O, length is divisible by 6?)
  - What happens when no arguments are provided? Assuming argument will always be provided
  - What happens if the input is very large? 
  - README.md was not present
  - Trailing spaces will be trimmed
  - Multiple spaces in between characters will be treated as one space

Notes:
  - Made a trade-off to increase space taken by mapping out both english to braille and braille to english characters in objects
  - Resulted in faster retrieval, but takes up more space

  - determine whether input is braille or english
    - if english, translate each letter into braille
    - if braille,
      - divide the string into each character into an array of strings that are 6 chars
      - translate each braille character to english character
    - return translation
  - */
