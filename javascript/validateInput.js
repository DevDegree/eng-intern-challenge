import { isValidBraille } from "./isValidBraille.js";
import { isValidEnglish } from "./isValidEnglish.js";

export const validateInput = (inputString) => {
  if (typeof inputString !== "string") {
    return "Input must be a string.";
  }

  const trimmedInput = inputString.trim();

  if (trimmedInput === "") {
    return "Input cannot be empty.";
  }

  // Check both Braille and English validations
  if (isValidEnglish(trimmedInput)) {
    return "Valid English";
  }
  if (isValidBraille(trimmedInput)) {
    return "Valid Braille";
  }
  return "Please provide a valid input string.";
};
