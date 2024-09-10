import {
  EMPTY_INPUT,
  INVALID_INPUT,
  STRING_REQUIRED,
  VALID_BRAILLE,
  VALID_ENGLISH,
} from "../../constants/appConstants.js";
import { isValidBraille } from "./isValidBraille.js";
import { isValidEnglish } from "./isValidEnglish.js";

export const validateInput = (inputString) => {
  if (typeof inputString !== "string") {
    return STRING_REQUIRED;
  }

  const trimmedInput = inputString.trim();

  if (trimmedInput === "") {
    return EMPTY_INPUT;
  }

  // Check both Braille and English validations
  if (isValidEnglish(trimmedInput)) {
    return VALID_ENGLISH;
  }
  if (isValidBraille(trimmedInput)) {
    return VALID_BRAILLE;
  }
  return INVALID_INPUT;
};
