import { exit } from "process";
import brailleTranslator from "./brailleTranslator";
import englishTranslator from "./englishTranslator";
import { isBraille } from "./booleans";

// Remember to join input with a space
let args = process.argv.splice(2);

if (args.length < 1 || (args.length == 1 && args[0] == "")) {
  exit(0);
}

function translate(input: string[]) {
  let output = "";
  if (input.length == 1 && isBraille(input[0])) {
    output = brailleTranslator(input[0]);
  } else {
    output = englishTranslator(input.join(" "));
  }
  console.log(output);
  exit(0);
}

translate(args);
