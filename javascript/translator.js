import { translateToBraille } from "./translateToBraille.js";

const translator = (inputString) => {
  return translateToBraille(inputString);
};

const input = process.argv.slice(2).join(" ");
if (input) {
  console.log(translator(input));
} else {
  console.log("Please provide a valid input string.");
}
