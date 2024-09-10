import { ALPHA_NUMERIC_SPACE_REGEX } from "../../constants/appConstants.js";

export const isValidEnglish = (input) => {
  // Regular expression to match only lowercase letters, uppercase letters, numbers, and spaces
  const validEnglishPattern = ALPHA_NUMERIC_SPACE_REGEX;

  return validEnglishPattern.test(input);
};
