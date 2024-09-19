import translateToEnglish from "./translators/brailleToEnglish";
import translateToBraille from "./translators/englishToBraille";
import { isBrailleChars } from "./utils";

class Translator {
  static translate(input: string): string {
    if (isBrailleChars(input)) {
      return translateToEnglish(input);
    } else {
      return translateToBraille(input);
    }
  }
}

// Gather Input
const args: string[] = process.argv.slice(2); // Skip "node" and "script path")
const input = args.join(" ");

// Translate
const result = Translator.translate(input);
if (result === "") {
  throw new Error("Result is Empty! Did you forget to give an input? A single space is not valid input.");
}

console.log(result);
