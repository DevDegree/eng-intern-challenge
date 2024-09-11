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
  ".....O": "capitalPrefix",
  ".O.OOO": "numberPrefix",
};

const ENGLISH_TO_BRAILLE = generateEnglishToBrailleLegend();
const NUMBER_TO_BRAILLE = generateNumberToBrailleLegend();
const BRAILLE_TO_NUMBER = generateBrailleToNumberLegend();

function generateEnglishToBrailleLegend() {
  const brailleToEnglish: { [englishCharacter: string]: string } = {};

  for (const key in BRAILLE_TO_ENGLISH) {
    const value = BRAILLE_TO_ENGLISH[key];
    brailleToEnglish[value] = key;
  }

  return brailleToEnglish;
}

function generateNumberToBrailleLegend() {
  const brailleNumberChars = "jabcdefghi";
  const numberToBraille = [];

  for (let idx = 0; idx < brailleNumberChars.length; idx += 1) {
    const currentChar = brailleNumberChars[idx];
    numberToBraille.push(ENGLISH_TO_BRAILLE[currentChar]);
  }

  return numberToBraille;
}

function generateBrailleToNumberLegend() {
  const brailleToNumber: { [number: string]: string } = {};

  NUMBER_TO_BRAILLE.forEach((letter, index) => {
    brailleToNumber[letter] = String(index);
  });

  return brailleToNumber;
}

function isValidEnglish(input: string) {
  return /^[a-zA-Z0-9 ]+$/.test(input);
}

function isBrailleString(input: string) {
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
      translation += ENGLISH_TO_BRAILLE["capitalPrefix"];
      translation += ENGLISH_TO_BRAILLE[character.toLowerCase()];
      continue;
    }

    if (isNumericCharacter(character)) {
      if (!numberMode) {
        numberMode = true;
        translation += ENGLISH_TO_BRAILLE["numberPrefix"];
      }

      translation += NUMBER_TO_BRAILLE[Number(character)];
      continue;
    }

    if (character === " ") numberMode = false;

    translation += ENGLISH_TO_BRAILLE[character];
  }

  return translation;
}

function splitBrailleStringByLetter(brailleText: string) {
  const result = [];

  for (let idx = 0; idx < brailleText.length; idx += BRAILLE_CHARACTER_LENGTH) {
    const brailleChar = brailleText.slice(idx, idx + BRAILLE_CHARACTER_LENGTH);
    result.push(brailleChar);
  }

  return result;
}

function translateBrailleToEnglish(brailleText: string) {
  const splitBrailleLetters = splitBrailleStringByLetter(brailleText);
  let numberMode = false;
  let uppercaseMode = false;
  let result = "";

  for (let idx = 0; idx < splitBrailleLetters.length; idx += 1) {
    const currentCharInBraille = splitBrailleLetters[idx];
    const currentLetterInEnglish = BRAILLE_TO_ENGLISH[currentCharInBraille];

    if (currentLetterInEnglish === "capitalPrefix") {
      uppercaseMode = true;
      continue;
    }

    if (currentLetterInEnglish === "numberPrefix") {
      numberMode = true;
      continue;
    }

    if (currentLetterInEnglish === " ") {
      numberMode = false;
      result += currentLetterInEnglish;
      continue;
    }

    if (numberMode) {
      const currentNumberInEnglish = BRAILLE_TO_NUMBER[currentCharInBraille];
      result += currentNumberInEnglish;
      continue;
    }

    if (uppercaseMode) {
      result += currentLetterInEnglish.toUpperCase();
      uppercaseMode = false;
      continue;
    }

    result += currentLetterInEnglish;
  }

  return result;
}

const commandLineInput = process.argv.slice(STARTING_INDEX_OF_ARGS);
const formattedInput = commandLineInput.join(" ");

let result;

if (isValidEnglish(formattedInput)) {
  result = translateEnglishToBraille(formattedInput);
} else if (isBrailleString(formattedInput)) {
  result = translateBrailleToEnglish(formattedInput);
} else {
  console.log("Error, invalid input");
}

console.log(result);
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
  - When a braille "Capital follows" (.....O), only the next symbol is c:w
  apitalized
  - when a braille "Number follows" (O.O.OO), all following symbols are numbers until a space (......)
  - Each braille character consists of 6 characters

Questions:
  - Will inputs always be English OR Braille, or can it be a mix of both? Assuming it will always be one or the other
  - Will the input always be a valid character? (e.g. English: only alphanumeric + space, Braille: always . and O, length is divisible by 6?)
  - What happens when no arguments are provided? Assuming argument will always be provided
  - What happens if the input is very large? 

Assumptions:
  - 
  - README.md was not present
  - Trailing spaces will be trimmed
  - Multiple spaces in between characters will be treated as one space
  - Can there be duplicate sequential signifier characters in Braille? (e.g. double capital prefix, double number prefix)

Notes:
  - Made a trade-off to increase space taken by mapping out both english to braille and braille to english characters in objects
  - Resulted in faster retrieval, but takes up more space

  - determine whether input is braille or english
    - if english, translate each letter into braille
    - if braille,
      - divide the string into each character into an array of strings that are 6 chars
      - translate each braille character to english character
    - return translation

  TODO:
  [ ] braille to english translation
  [ ] separate legends into another module
  - */
