import { validateInput } from "./utils/validation/validateInput.js";
import { translateToBraille } from "./utils/translateToBraille.js";
import { translateToEnglish } from "./utils/translateToEnglish.js";
import { VALID_BRAILLE, VALID_ENGLISH } from "./constants/appConstants.js";

const translator = (inputString) => {
  const validateResult = validateInput(inputString);
  if (validateResult === VALID_ENGLISH) {
    return translateToBraille(inputString);
  }
  if (validateResult === VALID_BRAILLE) {
    return translateToEnglish(inputString);
  }
  return validateResult;
};

const input = process.argv.slice(2).join(" ");
console.log(translator(input));
