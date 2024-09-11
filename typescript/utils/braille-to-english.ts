import { BRAILLE_TO_ENGLISH, BRAILLE_TO_NUMBER } from "./legends";
import { errorMessages } from "./error-messages";

const BRAILLE_CHARACTER_LENGTH = 6;

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

export function translateBrailleToEnglish(brailleString: string) {
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
