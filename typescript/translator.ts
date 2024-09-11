import {
  BRAILLE_TO_ENGLISH,
  BRAILLE_TO_NUMBER,
  NUMBER_TO_BRAILLE,
  ENGLISH_TO_BRAILLE,
} from "./utils/legends";

import { errorMessages } from "./utils/error-messages";

const STARTING_INDEX_OF_ARGS = 2;
const BRAILLE_CHARACTER_LENGTH = 6;

function isValidEnglishString(input: string) {
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

function translateEnglishToBraille(englishString: string) {
  let translation = "";
  let numberMode = false;

  for (let idx = 0; idx < englishString.length; idx += 1) {
    const character = englishString[idx];

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

function splitBrailleStringByCharacter(brailleString: string) {
  const result = [];

  for (
    let idx = 0;
    idx < brailleString.length;
    idx += BRAILLE_CHARACTER_LENGTH
  ) {
    const brailleChar = brailleString.slice(
      idx,
      idx + BRAILLE_CHARACTER_LENGTH
    );
    result.push(brailleChar);
  }

  return result;
}

function translateBrailleToEnglish(brailleString: string) {
  const brailleCharacters = splitBrailleStringByCharacter(brailleString);
  let numberMode = false;
  let uppercaseMode = false;
  let result = "";

  for (let idx = 0; idx < brailleCharacters.length; idx += 1) {
    const currentCharInBraille = brailleCharacters[idx];
    const currentCharacterInEnglish = BRAILLE_TO_ENGLISH[currentCharInBraille];

    if (!currentCharacterInEnglish)
      throw new Error(errorMessages.BRAILLE_INVALID_CHARACTER);

    if (currentCharacterInEnglish === "capitalPrefix") {
      const previousCharInEnglish =
        BRAILLE_TO_ENGLISH[brailleCharacters[idx - 1]];

      if (previousCharInEnglish === currentCharacterInEnglish)
        throw new Error(errorMessages.BRAILLE_MULTIPLE_CAPITALS_PREFIXES);

      uppercaseMode = true;
      continue;
    }

    if (currentCharacterInEnglish === "numberPrefix") {
      const previousCharInEnglish =
        BRAILLE_TO_ENGLISH[brailleCharacters[idx - 1]];

      if (previousCharInEnglish === currentCharacterInEnglish)
        throw new Error(errorMessages.BRAILLE_MULTIPLE_NUMBER_PREFIXES);

      numberMode = true;
      continue;
    }

    if (currentCharacterInEnglish === " ") {
      numberMode = false;
      result += currentCharacterInEnglish;
      continue;
    }

    if (numberMode) {
      const currentNumberInEnglish = BRAILLE_TO_NUMBER[currentCharInBraille];
      result += currentNumberInEnglish;
      continue;
    }

    if (uppercaseMode) {
      result += currentCharacterInEnglish.toUpperCase();
      uppercaseMode = false;
      continue;
    }

    result += currentCharacterInEnglish;
  }

  return result;
}

function main() {
  try {
    const commandLineInput = process.argv.slice(STARTING_INDEX_OF_ARGS);
    if (commandLineInput.length === 0)
      throw new Error(errorMessages.NO_ARGUMENTS_PROVIDED);

    const formattedInput = commandLineInput.join(" ");

    let result;
    if (isValidEnglishString(formattedInput)) {
      result = translateEnglishToBraille(formattedInput);
    } else if (isBrailleString(formattedInput)) {
      result = translateBrailleToEnglish(formattedInput);
    } else {
      throw new Error(errorMessages.INVALID_ARGUMENT);
    }

    console.log(result);
  } catch (error) {
    if (error instanceof Error) {
      console.log(error.message);
    } else {
      console.log(errorMessages.UNKNOWN_ERROR);
    }
  }
}

main();
