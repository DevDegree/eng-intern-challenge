import { validateInput } from "./validateInput.js";
import { translateToBraille } from "./translateToBraille.js";
import { translateToEnglish } from "./translateToEnglish.js";

const translator = (inputString) => {
  const validateResult = validateInput(inputString);
  if (validateResult === "Valid English") {
    return translateToBraille(inputString);
  }
  if (validateResult === "Valid Braille") {
    return translateToEnglish(inputString);
  }
  return validateResult;
};

const input = process.argv.slice(2).join(" ");
console.log(translator(input));
