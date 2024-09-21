import { isEnglish } from "./utils/charHelpers.js";
import {
  translateEnglishToBraille,
  translateBrailleToEnglish,
} from "./utils/translators.js";

const input = process.argv.slice(2).join(" ");

if (isEnglish(input)) {
  console.log(translateEnglishToBraille(input));
} else {
  console.log(translateBrailleToEnglish(input));
}
