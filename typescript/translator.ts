import { translateEnglishToBraille } from "./utils/english-to-braille";
import { translateBrailleToEnglish } from "./utils/braille-to-english";
import { errorMessages } from "./utils/error-messages";

const STARTING_INDEX_OF_ARGS = 2;
const BRAILLE_CHARACTER_LENGTH = 6;

function isValidEnglishString(input: string) {
  return /^[a-zA-Z0-9 ]+$/.test(input);
}

function isBrailleString(input: string) {
  return /^[.O]+$/.test(input) && input.length % BRAILLE_CHARACTER_LENGTH === 0;
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
